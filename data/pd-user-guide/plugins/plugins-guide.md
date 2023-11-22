# Guide / Plugins

Plugins are modules of code used to extend and modify the behavior of the
repository. Plugins can conceivably be written in any language that supports
gRPC. They may have access to the Provenant Data API, and, in certain contexts, 
the records flowing into and out of the repository.

### A Simple Plugin

To see how they work, let's create a simple one that ensures that all records retrieved from
the repository have all their keys and records set to lower case. 

We'll write our plugin in go. Here it is in its entirety:

```go
package main

import (
	"strings"

	"github.com/hashicorp/go-plugin"
	"github.com/provenantdata/nostromo/pdplugin"
)

type Processor struct{}

func (p Processor) Process(buf []byte) ([]byte, error) {
	s := strings.ToLower(string(buf))
	return []byte(s), nil
}

func main() {
	plugin.Serve(&plugin.ServeConfig{
		HandshakeConfig: pdplugin.Handshake,
		Plugins: map[string]plugin.Plugin{
			"RetrievalProcessor": &pdplugin.RetrievalProcessorPlugin{Impl: &Processor{}},
		},

		GRPCServer: plugin.DefaultGRPCServer,
	})
}
```

The boilerplate is straightforward. There are two necessary imports which work
in concert with one another to provide the gRPC interface to PD. The `main`
function simply connects the plugin to the gRPC server.

The only interesting content is the `Processor` struct and the single
`Process()` method associated with it. In a RetrievalProcessor, each record of
content will be sent to, and emitted from, the plugin (or list of plugins, in
order). `Process()` therefore takes a `[]byte`, the JSON record sent into the
plugin. It then manipulates it, in this case lower-casing the entire thing, and
emits it in its modified form. If this is the only plugin in the retrieval
chain, the modified record is what is delivered to the person or process
performing the retrieval.

For the PD prototype, the only interfaces that exist for plugins is the
Retrieval interrface. In the future, plugins will have access to dataset
content as it flows into and out of the repository, as well as the API call,
its arguments, and associated metadata. Plugins will be able to interact then
with the PD API (and/or external systems) allowing the plugin author to
customize the repository experience for any use case.

### Putting a Plugin In Place

Plugging a plugin into the respository is a simple process:

1. Write the plugin
2. Build the plugin (if applicable)
3. Create the plugin within the repository
4. Assign a policy that calls the plugin under the right conditions.

We saw above that writing the plugin is fairly straightforward. For step 2, if
the plugin is in a language that requires compilation (like go), you must build
the plugin. For this example, we'll name our built plugin with a `.plugin` extension.

Creating the plugin within the repository is simply a matter of using the
command line to upload the binary:

```shell
$ pd plugin create lowercaser ../build/lc.plugin
plugin created
```

We can now see it in the repository:

```shell
$ pd plugin list
  Name       ID                         Version                    Created                    Updated                    FileHash
0 lowercaser 01G7ARVKK2X41YTESZARDT19RV 01G7ARVKK2X41YTESZATAQKJY6 2022-07-06T15:07:29.378PDT 2022-07-06T15:07:29.378PDT e9c34fa0d962063...

$ pd plugin show lowercaser
Name:         lowercaser
Plugin ID:    01G7ARVKK2X41YTESZARDT19RV
Version:      01G7ARVKK2X41YTESZATAQKJY6
Created:      2022-07-06T15:07:29.378PDT
Last Updated: 2022-07-06T15:07:29.378PDT
File Hash:    e9c34fa0d9620637df16cab680c0cca33c5fd79eb1615ebc9ee94670e01501850bd0c48046045e4095fa4f054df32f3252d9ef2d6230ba3f3aa2c64abe3bf5da
Tags:         none
```

For the final step, we will assign a policy to the `Retrieve` family of API calls
that will pass data to this plugin under all conditions.

The (very simple) policy: 

```rego
package provenant.retrieve
default allow = true

plugin[name] {
    allow
	name = "lowercaser"
}
```

This policy allows retrieval in all conditions for authenticated users, and, in
all cases, also specifies that the "lowercaser" plugin will be used.

Once we update the retrieval policy, this plugin will "intercept" all records
egressing the system and modify them en passant.

```shell
$ pd policy update provenant.retrieve ./example/lowercase_example.rego
policy updated
```

### Runtimes 

While plugins can be implemented in any language that can interface via gRPC,
the system(s) running the PD platform would need to have runtimes to support
those languages. For example, Python plugins would need a compatible Python
runtime on the PD host system in order to execute. 
