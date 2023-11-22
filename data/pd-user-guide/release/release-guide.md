# Guide / Release

A "Release" is directly analogous to a software release, but in this case,
instead of preparing and packaging software for use, we are preparing and
packaging datasets.

Each release belongs to a [product](/docs/guide/product), and has a version number
in the style of [Semantic Versioning](https://semver.org). A release contains a
reference to a [commit](/docs/guide/commit) that contains the data intended for the
release.

In the CLI, all these steps are taken in subcommands of the `pd product` command.

### Creating a Release

Assuming we already have a product named "my_new_product", let's create a
release. We first need to identify the commit we want to use...

```shell
$ pd branch show main|head -20
Repository:    MyRepository
Display Name:  main
Name:          main
Branch ID:     01G6S5VPJG1QVK53NKVAX77MHV
Version:       01G7QQM8XBTPSFBJ7JJC8KA6HE
Created:       2022-06-29T19:08:24.144PDT
Last Updated:  2022-07-11T15:56:08.107PDT
Parent Branch: None
Parent Commit: None

Commits:
    ID                         Version                    Created                    Branch ID                  Message               Records
0   01G6S5VPJG1QVK53NKVCP26XHE 01G6S5VPJG1QVK53NKVQE0RP92 2022-06-29T19:08:24.144PDT 01G6S5VPJG1QVK53NKVAX77MHV main - initial commit 0
1   01G6S5WJ4J6JHPSPK537G7PE63 01G6S5WJ4KVYVGCM9ZT0FAJZ09 2022-06-29T19:08:52.37PDT  01G6S5VPJG1QVK53NKVAX77MHV commita               1
2   01G6S5WJV6J9BE0ERZCHT7S183 01G6S5WJV7QEN8V778FJ5CM3K3 2022-06-29T19:08:53.094PDT 01G6S5VPJG1QVK53NKVAX77MHV commmitb              2
3   01G6S5WK96TB0KZW1JS30YZ4WN 01G6S5WK97H4DVHEV2D6DHJK6H 2022-06-29T19:08:53.542PDT 01G6S5VPJG1QVK53NKVAX77MHV commit csv            3
4   01G6S5WKKQY4YPTWA7JAWPBTJX 01G6S5WKKRABE0RTCA1VBTTVV7 2022-06-29T19:08:53.879PDT 01G6S5VPJG1QVK53NKVAX77MHV commit csv            3
5   01G6S5WM9FM3R47PM149YTYHZ6 01G6S5WM9G8PSXAS05AC74EYBR 2022-06-29T19:08:54.575PDT 01G6S5VPJG1QVK53NKVAX77MHV commit with metadata  11
6   01G6S5WMMWWN8VSRP7BRYTQP79 01G6S5WMMX1XJXBM3C2VBA3DZ9 2022-06-29T19:08:54.94PDT  01G6S5VPJG1QVK53NKVAX77MHV clobber               1
7   01G6S5X8XNT8H5D3Y9XASCSGCC 01G6S5X8XP5C80ZV3EGEVT7FPV 2022-06-29T19:09:15.701PDT 01G6S5VPJG1QVK53NKVAX77MHV into main             1
...
```
...and then we create the release itself:

```shell
$ pd product release --name my_new_product --commit 01G6S5WM9FM3R47PM149YTYHZ6 -v 1.0.0
released product my_new_product ver 1.0.0

$ pd product show my_new_product
Repository:   MyRepository
Name:         my_new_product
Product ID:   01G7FGM8DR6AFVTA96C1FMPD6V
Version:      01G7MXENJG64E7V1X8R41NKV88
Created:      2022-07-08T11:19:52.12PDT
Last Updated: 2022-07-10T13:40:12.624PDT
License:      mit
License ID:   01G7FJP5FKPBPB3P612WPJW41M
Releases:
              SemVer ID                         Version                    Created                    Updated
0             1.0.0  01G7FHNPBWYMFS7QH00F0EMQ6P 01G7FJ2WW89TM97RSP6HS6FRRE 2022-07-08T11:38:07.74PDT  2022-07-08T11:45:20.392PDT

Tags: none
```

Now we can see that we have a single release ("1.0.0") in our product
"my_new_product". We can retrieve the content of that release easily:

```shell
$ pd product retrieve my_new_product 1.0.0
{"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0}
{"field_1":"OfatLGC","field_2":["some","array","values",519],"field_3":"uHHaSytmJq","id":1}
{"field_1":"field1_val1","field_2":"field2_val1","field_3":"333","id":"0"}
{"field_1":"MKdEyms","field_2":["some","array","values",912],"field_3":"nhlkZUSAxR","id":2}
{"field_1":"tMJfvAH","field_2":["some","array","values",743],"field_3":"CKURhbpNTG","id":3}
{"field_1":"WQWKOJr","field_2":["some","array","values",543],"field_3":"JKeERhtsTp","id":4}
{"field_1":"kCdshuD","field_2":["some","array","values",620],"field_3":"NSrIqczwQP","id":5}
{"field_1":"LcQWJkZ","field_2":["some","array","values",734],"field_3":"jSOuqJCzFm","id":6}
{"field_1":"FGDMYic","field_2":["some","array","values",745],"field_3":"kqmBWcvdAp_10JSON","id":7}
{"field_1":"yePxvmV","field_2":["some","array","values",925],"field_3":"zgdAAhcgiN_10JSON","id":8}
{"field_1":"ZqRUUTX","field_2":["some","array","values",98],"field_3":"acUWcMGTfh_10JSON","id":9}
```

If we've given one or more user groups to our product, those users will be
notified the next time they use PD that a release for this product has been
made.

### Deprecating a Release

There may be many reasons for formally removing a release for access: new data
has superseded that in the previous release, the prior data is no longer
accurate or applicable, or perhaps our product lifecycle uses removal of old
versions to encourage subscribers to "upgrade". Whatever the reason, PD offers
a way to mark a release as deprecated, and, as when creating a release,
notifying subscribers.

```shell
$ pd product deprecate my_new_product 1.0.0 -m 'example deprecation'
my_new_product 1.0.0, ID 01G7FHNPBWYMFS7QH00F0EMQ6P deprecated
```

And if we attempt to retrieve it:

```shell
$ pd product retrieve my_new_product 1.0.0
release deprecated
```
