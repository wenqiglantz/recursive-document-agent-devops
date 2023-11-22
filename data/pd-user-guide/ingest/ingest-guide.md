# Guide / Ingest

Ingest is the process of placing records in the repository. Theses records may
originally be stored in files, or in a database, or may be coming to Provenant
Data in a stream. Ingesting records are stored in a canonicalized form, that
is, stores them in a standard format, that allows them to be referenced
efficiently. Records are deduplicated; if a record is ingested more than once,
it will only be stored a single time. That single, canonical record may be
referenced any number of times by different datasets.

An ingest produces an IngestID. This IngestID uniquely identifies the dataset
contained in the ingest.

### Supported File Formats

Three file formats are currently supported for ingest: Newline-delimited JSON
(NLDJSON or NDJSON), an array of JSON records (JSONArray) and Comma-separated
values with a header row (CSVWithHeader).

Example of NLDJSON:

```json
{"a": "x", "b": 1}
{"a": "y", "b": 2}
{"a": "z", "b": 3}
```

An axample of an array of JSON records:

```json
[{"a": "x", "b": 1},{"a": "y", "b": 2},{"a": "z", "b": 3}]
```

And CSV with header:
```shell
a,b
x,1
y,2
z,3
```

Note that the CSV example is not equivalent to the others. All values in the
CSV will be treated as strings, while numbers in the JSON examples will be
treated as numbers. The CSV has other issues, chief among them is that it is
unable to support nested structures. It is recommended to use one of the other
supported data types if possible. 


### Ingesting a File Using the Command Line

The easiest way to add data to your repository is by using the `pd add` command:

```shell

$ pd add --files ~/path/to/file/example.json
Composition ID:   01G7QQGC1XVTM7KVYHVXXD6589
Total Records:    500

Ingest ID:        01G7QQGBK1A5WYH7JEQXDWAF4A
Version:          01G7QQGC1K8DH4MZ444W5BFVWA
Created:          2022-07-11T15:53:59.777PDT
Last Updated:     2022-07-11T15:54:00.243PDT
Ingested Records: 500
New Records:      0
Tags:             none
```

This command adds the records from the example file to the repository. The
records are, at this point, uncommitted: They exist in the repository, can be
referred to by their ingest id, but are not "saved" to a branch. They exist in
"workspace" where you can compose them with other datasets. When you're ready,
it's best to commit them so they are easer to reference later:

```shell
$ pd commit create "five-hundred example records"
Created commit 01G43R9V2HE2GH8AGPG1MGRP5X
```

This saves these records as a commit into your current branch.

You can also do this via an "ingest" command:

```shell
pd branch ingest main --files ~/path/to/file/example.json --message 'the same five-hundred example records'
Ingest ID:        01G7QQHWENBEYENJ2KZTS9KF09
Version:          01G7QQHWWG38CJSE4S6A1R6S1P
Created:          2022-07-11T15:54:49.813PDT
Last Updated:     2022-07-11T15:54:50.256PDT
Ingested Records: 500
New Records:      0
Tags:             none

Repository:       MyRepository
Commit ID:        01G7QQHWZ9APRTMD27QWDJADSY
Version:          01G7QQHWZB4SSF4R9AC1N9MGJ7
Created:          2022-07-11T15:54:50.345PDT
Last Updated:     2022-07-11T15:54:50.347PDT
Branch:           main
Message:          the same five-hundred example records
Dataset Size:     500
Origin Repos:     1
                  01G6S5VPGWYAZ4B70ZJ2NNN907 (this repo)
Tags:             none
```

This accomplishes the same basic thing (ingesting records into the repository)
but the `pd branch ingest` command is 1) explicit about the branch and 2) makes
a commit for the ingest in one command.

In both examples, if you don't specify the `--type`, the command assumes it is
ingesting NLDJSON. 

#### Deduplication

You may have noticed above that in the second example (`pd branch ingest...`)
the output shows that, while the ingested dataset was 500 records, no _new_
records were created. That's because PD deduplicates records as it encounters
them. Above, we ingested twice, and have two ingests that refer to the same
records, but each record only exists once in storage.

This is important because in a scenario where PD is part of a data pipeline, we
want to encourage frequent ingests of working datasets so that their
development can be tracked. Due to deduplication, ingest of a record that
already exists has no processing or storage, aside from tracking the fact that
a record was part of another ingest.

### Adding Metadata to an Ingest

In order to attach arbitrary metadata to an ingest (and therefore, to each
record within the ingest) you may specify the `--metadata-file` option to
either the `pd add` or `pd branch ingest` commands. The argument to the
`--metadata-file` option is the path to a NLDJSON file that holds your
metadata.

```shell
$ cat ~/path/to/file/example_metadata.json
{
    "Owner": "JSmith"
    "Secrecy": "Top"
}

$ pd add --files ~/path/to/file/example.json --metadata-file ~/path/to/file/example_metadata.json
Ingest ID         01G7QQM8PK59CH68NWGRRMP7ZV
Version:          01G7QQM8TG3GQ7S0S7BQYYNA5J
Created:          2022-07-11T15:56:07.891PDT
Last Updated:     2022-07-11T15:56:08.016PDT
Ingested Records: 1
New Records:      0
Metadata ID:      01G6S5WKVMJQJRR1HWRB64B54Y
Tags:             none

Commit ID:        01G7QQM8X9GTQFY7ZQEFGJ3TPH
Version:           1G7QQM8XAJJKP8276RA7385K5
Created:          2022-07-11T15:56:08.105PDT
Last Updated:     2022-07-11T15:56:08.106PDT
Branch:           main
Message:          metadata example
Dataset Size:     1
Origin Repos:     1
                  01G6S5VPGWYAZ4B70ZJ2NNN907 (this repo)
Tags:             none
```

Now, when data from this ingest is returned as part of an audit, or otherwise
inspected, the Key-Value pairs of the associated metadata will be available.

### See Also

See the CLI reference for more information on using [pd add](/docs/commands/pd_workspace_add.html)
and [pd branch ingest](/docs/commands/pd_branch_ingest.html).
