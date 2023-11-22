# Guide / Retrieval

### Retrieving Data from the Repository

In order to retrieve data from the repository, you need to have a reference to
the data you're interested in. This can be a commit ID, an ingest ID, the
current workspace, or a product release. 


#### Commits

`pd commit retrieve` takes a commit id to retrieve, and outputs the dataset:

```shell
$ pd commit retrieve 01G43VH4600SEN93VSHTWG1CZP 
{"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0}
{"field_n":"my value","id":1,"list":[1,2,3,"four"]} 
...
```

#### Products and Releases
To retrieve a release of a product, you specify the product name and the release version:

```shell
$ pd product retrieve 'my product' 0.1.0 
{"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0}
{"field_n":"my value","id":1,"list":[1,2,3,"four"]}
...
```

#### Workspace
You're likely to want to examine your workspace dataset frequently if you're
composing data, so retrieving the contents of your current workspace is even
easier. The long form `pd workspace retrieve` can be shortened to just `pd
retrieve`:

```shell
$ pd retrieve
{"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0}
{"field_n":"my value","id":1,"list":[1,2,3,"four"]}
...
```

In the examples above we've elided most of the output to save space. When
you're working with real datasets, sometimes you just want a taste of the
data... you don't need thousands of records scrolling by. In that case, use the
`--preview` option to retrieve only a handful of records.

```shell
$ pd retrieve --preview
{"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0}
{"field_n":"my value","id":1,"list":[1,2,3,"four"]}
{"field_n":"my value","id":2,"list":[2,2,3,"four"]}
{"field_n":"my value","id":3,"list":[3,2,3,"four"]}
{"field_n":"my value","id":4,"list":[4,2,3,"four"]}
```

### Output Formats

In all the retrieval cases above, we've let the CLI assume that we want NLDJSON
as output. But, if we want, we can choose a JSON array or CSV data with a
header.

```shell
$ pd retrieve --preview --type jsonarray
[{"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0},{"field_n":"my value","id":1,"list":[1,2,3,"four"]},{"field_n":"my value","id":2,"list":[2,2,3,"four"]},{"field_n":"my value","id":3,"list":[3,2,3,"four"]},{"field_n":"my value","id":4,"list":[4,2,3,"four"]}]
```

There are a couple of caveats dealing with CSV data that boil down to this: 

1) don't use it as the output type for any datasets that have nested data structures 
2) don't use it for any datasets that have "heterogenous" structure

In the first case, nested structures will get flattened to a string:

```shell
pd retrieve --preview --type csvwithheader |head -2
field_1,field_2,field_3,id
prlFNzk,[some array values 619],RZnbDCGfmO,0
```

Note here that field_2, and array field, was flattened to a string containing
"[some array values]", which are no long array values.

And in the second case, PD infers the output keys from the first output record.
If the same keys don't exist for every record, you don't get meaningful data:

```shell
pd retrieve --preview --type csvwithheader
field_1,field_2,field_3,id
prlFNzk,[some array values 619],RZnbDCGfmO,0
nil,nil,nil,1
nil,nil,nil,2
nil,nil,nil,3
nil,nil,nil,4
```

Only use CSV if you know your output dataset can be represented faithfully as CSV.

### See Also

See the CLI reference for more information on using [pd
retrieve](/docs/commands/pd_workspace_retrieve.html), [pd commit
retrieve](/docs/commands/pd_commit_retrieve.html), and [pd product
retrieve](/docs/commands/pd_product_retrieve.html).
