# Guide / Policy

Policies are a way to customize both the behavior of the Provenant Data
platform, and the presentation of datasets within the repository. The PD Policy
Engine allows for policies and business rules regarding the use of datasets to
be decoupled from the implementation of the repository itself, and for policy
to be treated as code.

The PD Policy Engine is based on the [Open Policy
Agent (OPA)](https://www.openpolicyagent.org). Policies are written in
[Rego](https://www.openpolicyagent.org/docs/latest/policy-language/), a
declarative language inspired by Datalog.

1. [Introduction](#introduction-to-pd-policies)
2. [Modifying Policies](#modifying-policies)
3. [Metadata Provided To Policies](#metadata-provided-to-policies)
4. [External Data](#external-data)
5. [Testing Policies](#testing-policies)
6. [Resetting Policies](#resetting)

### Introduction to PD Policies

Each API call has an associated policy. To see [all of the
policies](/docs/guide/policy/policy_list.html) available: 

```shell 
$ pd policy list
    Name                                 ID                         Version                    Created                    Updated
0   provenant.apiaccess                  01G6S5VPM14A6WFQ6X0V9F1YV6 01G6S5VPM14A6WFQ6X12MGS87D 2022-06-29T19:08:24.193PDT 2022-06-29T19:08:24.193PDT
1   provenant.ingest                     01G6S5VPM14A6WFQ6X19NRPDP8 01G7MY1BCJCRS43MAJ1K517M52 2022-06-29T19:08:24.193PDT 2022-07-10T13:50:24.786PDT
2   provenant.retrieve                   01G6S5VPM14A6WFQ6X1J1TC1Z9 01G6S5VPM14A6WFQ6X1PMP43YS 2022-06-29T19:08:24.193PDT 2022-06-29T19:08:24.193PDT
3   provenant.audit                      01G6S5VPM14A6WFQ6X1WJSQA4W 01G6S5VPM14A6WFQ6X214YPSKK 2022-06-29T19:08:24.193PDT 2022-06-29T19:08:24.193PDT
4   provenant.recorddelete               01G6S5VPM24RSBA1BQ9J9Y8A23 01G6S5VPM24RSBA1BQ9QKE05BB 2022-06-29T19:08:24.194PDT 2022-06-29T19:08:24.194PDT
5   provenant.activatesession            01G6S5VPM24RSBA1BQ9WTM9V74 01G6S5VPM24RSBA1BQA10SM5CH 2022-06-29T19:08:24.194PDT 2022-06-29T19:08:24.194PDT
6   provenant.addtag                     01G6S5VPM24RSBA1BQA31MEF0B 01G6S5VPM24RSBA1BQA84VCCM5 2022-06-29T19:08:24.194PDT 2022-06-29T19:08:24.194PDT
7   provenant.addusertogroup             01G6S5VPM24RSBA1BQADQ5PZ7W 01G6S5VPM24RSBA1BQAJMVC5B0 2022-06-29T19:08:24.194PDT 2022-06-29T19:08:24.194PDT
8   provenant.allowgroupaccesstoproduct  01G6S5VPM24RSBA1BQANFV56ZG 01G6S5VPM24RSBA1BQASEJGYGM 2022-06-29T19:08:24.194PDT 2022-06-29T19:08:24.194PDT
...
```

In an unmodified repository, all of the policies in place are permissive. Let's
look at the contents of the "retrieve" policy. The "retrieve" policy is
inspected each time the "retrieve" API method is called (that is, any time a
user wants to retrieve (or preview) a dataset).

```shell
$ pd policy show provenant.retrieve
Name:         provenant.retrieve
Policy ID:    01G6S5VPM14A6WFQ6X1J1TC1Z9
Version:      01G6S5VPM14A6WFQ6X1PMP43YS
Created:      2022-06-29T19:08:24.193PDT
Last Updated: 2022-06-29T19:08:24.193PDT
Tags:         none

Source
========
package provenant.retrieve
default allow = false

allow {
 allowed[_]
}

# Any messages attached to allowed will be available to the user.
allowed[msg] {
 # This policy defaults to allow, since the following is always true
 msg := "Allowed by default policy"
}

# Any messages attached to deny will be available to the user.
deny[msg] {
 not allow
 msg := "Denied by default policy"
}

# The first value in the schema array will be used to load the named schema
# validator and the schema validator will be run against each record. Schema
# validation is available on ingest only. Only the first value is consulted.
# All other values are ignored.
schema[name] {
 name = ""
}

# The first value in the plugin array will be used to load the named plugin and
# the plugin will be run against each record. Record-processing plugins are
# available on ingest and retrieval only. Only the first value is consulted.
# All other values are ignored.
plugin[name] {
 name = ""
}
========
```

This shows you the name, ID and version of the policy, as well as the source.
The source is the interesting part. If you're unfamiliar with
[Rego](https://www.openpolicyagent.org/docs/latest/policy-language/) take a few
minutes to review it.

Let's break down a couple portions of the policy.

```rego
package provenant.retrieve
default allow = false
...
```

The first section simpley identifies this policy by a package name
(conveniently the same as the policy name), and specifies that the default
action for this policy is a deny.

That last part may be a bit misleading as we've already stated that this is, by
default, a permissive policy (IE retrieval is always allowed under this
policy). Specifying `default allow = false` simply means that if no rule is
matched in the policy, the policy will take the default action of deny. This is
a sane default, and should be used in any custom policies.

The next two stanzas are where we set our retrieve policy to allow in all cases:

```rego
allow {
        allowed[_]
}

# Any messages attached to allowed will be available to the user.
allowed[msg] {
        # This policy defaults to allow, since the following is always true
        msg := "Allowed by default policy"
}
```

You can read this as "this API action will be allowed if there is an entry in the
allowed list", which there is as we set it to "Allowed by default policy".

```rego
# Any messages attached to deny will be available to the user.
deny[msg] {
        not allow
        msg := "Denied by default policy"
}
```

And this can be read as "deny with the message "Denied by the default policy if
the 'allow' assertion above is false".

PD Policies can allow data, by satisfying the `allow` assertion, or deny it by
_not_ satisfying the allow assertion.

Furthermore, PD Policies can take two additional actions: enforce a schema, or
trigger a plugin.

```rego
# The first value in the schema array will be used to load the named schema
# validator and the schema validator will be run against each record. Schema
# validation is available on ingest only. Only the first value is consulted.
# All other values are ignored.
schema[name] {
        name = ""
}

# The first value in the plugin array will be used to load the named plugin and
# the plugin will be run against each record. Record-processing plugins are
# available on ingest and retrieval only. Only the first value is consulted.
# All other values are ignored.
plugin[name] {
        name = ""
}
```

To set a policy that evaluates all ingests against a given schema, upload a
schema, and supply that schema's name to the schema assertion. The following is
an extremely simple  policy that will allow all ingests, and evaluate them
against the schema name "my_schema":

```rego
package provenant.ingest
default allow = true

schema[name] {
    allow
	name = "my_schema"
}
```
Likewise, supplying a plugin name to the plugin assertion will run that plugin when
the policy conditions are met. Here's a very simple policy that runs a plugin
named "my_plugin" for each retrieval.

```rego
package provenant.retrieve
default allow = true

plugin[name] {
    allow
	name = "my_plugin"
}
```

### Modifying Policies

Modifying a policy involves overwriting the policy with a new version.

```shell
$ pd policy update provenant.ingest ./path/to/new/file.rego
```

### Metadata Provided to Policies

[Metadata provided as input](/docs/guide/policy/input) to the policy varies according to the API call. By
default, each policy should receive the ClientSpec associated with the API
call, data regarding the user, and data regarding the user's group membership. 

Input data is evolving as the platform evovlves, and will be documented as it
becomes available. 

### External Data

Use of external data allows a policy writer to leverage existing authoritative
sources (for example, an organization's existing LDAP infrastructure) to modify
the behavior of the PD Platform. 

To fetch external data and use it as input to a policy, see the [OPA
documentation](https://www.openpolicyagent.org/docs/latest/policy-reference/#http).

### Developing Policies

Policies are powerful. Polcies are flexible. But for novice OPA/Rego users,
policies can be difficult to perfect. The good news is that treating policies
as code allows us to use many of the same tools and practices that are used in
the the rest of our development environment. To that end, it is advisable to
maintain policies in version control and to test sufficiently.

See the Open Policy Agent [documentation on testing
policies](https://www.openpolicyagent.org/docs/latest/policy-testing/) for
details on implementation.

### Resetting

Sometimes testing is not enough, and something goes wrong. In those times use
`pd policy reset <policyname>` to reset a policy to the default (permissive)
state.

Policies are versioned in the Platform, but rollback to a specific version is not
yet available. 

Be especially cautious with the `provenant.apiaccess` policy. This policy is run
for every api call, prior to any other policies. It is a convenient way to make
policy decisions early in the codepath, especially where they do not depend on
the specific API call requested. For example, one can use this policy to
broadly deny access to the API. Any mistakes made in this policy make make it
difficult to use the platform.
