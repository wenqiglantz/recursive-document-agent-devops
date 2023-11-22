# Guide / Licensing

Licenses in Provenant Data are simply documents, in any format, that are
attached to products. The association of a license with a dataset is
persistent: under later examination (IE Audit) the license or licenses that
have been applied to the data are evident. 

In addition to explicit licensing of products (and releases), there is a default
license, that will apply to all data in the repository unless another license
is applied in a more specific context (like a product).

### Creating a License

Licenses are simply documents. PD enforces no requirements or structure, and
does not examine the content, or have knowledge of it in any way. PD is more
interested in the _association_ of a license with datasets, than in the terms
of the license specifically.

Below, we'll create a PD License entity that is the MIT license.

```shell
$ pd license create mit -d "mit license" -f ./docs/content/static/example_lic.json
License created, id 01G7FJP5FKPBPB3P612WPJW41M

$ pd license show mit
Repository:   MyRepository
Name:         mit
License ID:   01G7FJP5FKPBPB3P612WPJW41M
Version:      01G7MX8RNC5ME5AGWBYNJ9FWKJ
Created:      2022-07-08T11:55:51.795PDT
Last Updated: 2022-07-10T13:36:59.18PDT
Description:  fix spelling mistake?
File Name:    example_lic.json
```

Here, our license happens to be a json object, but, again, it can be any format
(or it can simply contain a name,  _link_ or reference to the license in
question).

Listing, deleting and restoring a license works the same as with many other PD
entities. If you need to update a license with new content, that is possible as
well:

```shell
$ pd license update mit -d 'fix spelling mistake?' -f ./docs/content/static/example_lic.json
License updated, id 01G7FJP5FKPBPB3P612WPJW41M
```

In this case, where the _content_ of a license may have changed, PD maintains
the history of the license, and for licensed datastes can maintains which _version_ of
a given license was applied.

Retrieving the content of a license is a matter of passing the `-s` option to
`pd license show` in order to save the file to your filesystem:

```shell
pd license show mit -s ./myfile

Repository:   MyRepository
Name:         mit
License ID:   1G7FJP5FKPBPB3P612WPJW41M
Version:      01G7MX8RNC5ME5AGWBYNJ9FWKJ
Created:      2022-07-08T11:55:51.795PDT
Last Updated: 2022-07-10T13:36:59.18PDT
Description:  fix spelling mistake?
File Name:    example_lic.json

Applied to Products:
      Name           ID                         Version                    Created                   Updated                    Description Releases
0     my_new_product 01G7FGM8DR6AFVTA96C1FMPD6V 01G7MXENJG64E7V1X8R41NKV88 2022-07-08T11:19:52.12PDT 2022-07-10T13:40:12.624PDT             2
Tags: none
```

### Applying a License to a Product

```shell
$ pd product license my_new_product mit
license applied to product.

$ pd product show my_new_product
Repository:   MyRepository
Name:         my_new_product
License ID:   01G7FGM8DR6AFVTA96C1FMPD6V
Version:       1G7MXENJG64E7V1X8R41NKV88
Created:      2022-07-08T11:19:52.12PDT
Last Updated: 2022-07-10T13:40:12.624PDT
License:      mit, 01G7FJP5FKPBPB3P612WPJW41M
Releases:
  SemVer ID                         Version                    Created                    Updated
0 1.0.0  01G7FHNPBWYMFS7QH00F0EMQ6P 01G7FJ2WW89TM97RSP6HS6FRRE 2022-07-08T11:38:07.74PDT  2022-07-08T11:45:20.392PDT
1 2.0.0  01G7MXENJE5JMYHG2PJVAX0TMW 01G7MXENJG64E7V1X8QZ58CCHR 2022-07-10T13:40:12.622PDT 2022-07-10T13:40:12.624PDT
```

License are not applied directly to releases: Releases inherit the license of
the product to which they are attached.

### The Default License

Every repository starts with a default license named "default_license":

```shell
$ pd license list
Repository: MyRepository
  Name            ID                         Version                    Created                    Updated                    Filename         Description            Products Releases
0 default_license 01G6S5VPMSAHVSB2WPV5AP65DS 01G6S5VPMSAHVSB2WPVC98G8H4 2022-06-29T19:08:24.217PDT 2022-06-29T19:08:24.217PDT license.txt      Empty default license  0        0
1 mit             01G7FJP5FKPBPB3P612WPJW41M 01G7MX8RNC5ME5AGWBYNJ9FWKJ 2022-07-08T11:55:51.795PDT 2022-07-10T13:36:59.18PDT  example_lic.json fix spelling mistake?  1        0

$ pd license show default_license
Repository:   MyRepository
Name:         default_license
License ID:   01G6S5VPMSAHVSB2WPV5AP65DS
Version:       1G6S5VPMSAHVSB2WPVC98G8H4
Created:      2022-06-29T19:08:24.217PDT
Last Updated: 2022-06-29T19:08:24.217PDT
Description:  Empty default license
File Name:    license.txt
Tags:         none
```

The default license is a way to apply a license to all data within a
repository, whether or not it has been released as a product. It is a safety
net to ensure that no data is unlicensed. By default, the "default_license" is
empty, so it should be updated with a more appropriate data for the repository.
