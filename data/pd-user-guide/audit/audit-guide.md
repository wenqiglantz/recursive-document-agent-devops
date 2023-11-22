# Guide / Audit

Audit is the process of submitting records to the repostory in order to
retrieve the history and provenance of those records. Records from outside the
repostory may be audited, and partial matches returned. Data
fully contained within the repository (EG a commit) may also be audited to
recover its history and provenance.

### Auditing a File

For the examples here, we'll be ingesting and auditing extremely small sets of
data to make interacting with the output reasonable.

In an empty repository, we'll ingest a single record from a file, and commit it.

Here's the record:

```json
{"id": 0, "field_1": "prlFNzk", "field_2": ["some", "array", "values", 619], "field_3": "RZnbDCGfmO"}
```

Now we ingest and commit it:

```shell
$ pd add ~/path/to/file/example_1.json
Composition ID:   01G7TNAW3NZNDGZ2PEFPRS7YKZ
Total Records:    17

Ingest ID:        01G7TNAW2NY6Z1Z3YV938WM70X
Version:          01G7TNAW3A1D09KDGESJJR93XH
Created:          2022-07-12T19:13:46.197PDT
Last Updated:     2022-07-12T19:13:46.218PDT
Ingested Records: 1
New Records:      0
Tags:             none

$ pd commit create 'commit message one'
Created commit 01G4E6NQ5JEHTT7DJQXBHXSTG0
```

We then perform an audit on that same file. We're guaranteed to find an exact
match in the repository, so we'll leave the threshold at it's default of 1.0.

```shell
$ pd audit create --files ~/path/to/file/example_1.json
Repository:        MyRepository 
Name:              audit_default_20220711145647
Auditreport ID:    01G7QM7KZ1FMFM14YJ75GJ259Q
Version:           01G7QM7NXZACCWCGQZF48VATEF
Created:           2022-07-11T14:56:47.713PDT
Last Updated:      2022-07-11T14:56:49.727PDT
Submitted Records: 1
Events:            3
Entries:           3

Submitted Content {"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0} (5cd8c628f3def770...) matches the following repository contents

	Repository Content {"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0} (5cd8c628f3def770...)
	Score 1.000000
	Entry: ID: 01G4E6NF1MRB3RVCMFGRA1PMRT EventID: 01G4E6NF0M7PQZS7M1G3WZQS4G Timestamp: 2022-05-31 16:19:26.004999 -0700 PDT Type: IngestNewRecordsEntry Num Records 1
	Metaddata: {}
	License: default_license 01G4E6DRTVHPVAW4PBPP4PQWCR/01G4E6DRTVHPVAW4PBPTCS1FFM. Empty default license
	Entry: ID: 01G4E6NF4D2V4SKPP35RDHHQY3 EventID: 01G4E6NF4D2V4SKPP35THZTVT9 Timestamp: 2022-05-31 16:19:26.094485 -0700 PDT Type: Compose Num Records 1
	Metaddata: {}
	Entry: ID: 01G4E6NQ5JEHTT7DJQXJ5WSJ6Z EventID: 01G4E6NQ5JEHTT7DJQXM87QXSY Timestamp: 2022-05-31 16:19:34.324363 -0700 PDT Type: CreateCommit Num Records 1
	Metaddata: {}

Event 01G4E6NF0M7PQZS7M1G3WZQS4G ingest (ID 01G4E6NF0M7PQZS7M1FYZY64E1) refers to content that matches or partially matches submitted content
Event Start: 2022-05-31 16:19:25.972128 -0700 PDT
Event End: 2022-05-31 16:19:26.049314 -0700 PDT
	Metaddata: {
	  "context": {
	    "auditTimestamp": "2022-05-31T16:19:25.972195-07:00",
	    "clientSpec": {
	      "APIAction": {
	        "Aggregate": false,
	        "DefaultAdmin": false,
	        "Name": "beginingest",
	        "Parent": "ingest"
	      },
	      "Args": "pd add ./tests/apitests/testdata/simple/1.json",
	      "Branch": "docs_audit",
	      "Hash": "b6d36e71a99c82cfb8591177a63847abed06c0f0",
	      "HopCount": 1,
	      "Hostname": "Scotts-iMac.local",
	      "Name": "pd_prototype_cli",
	      "OS": "darwin",
	      "Path": "/Users/scotthartzel/github/nostromo/.pd",
	      "QueriedNodes": [
	        "x"
	      ],
	      "QueryID": "01G4E6NF05FWMZYRCWZW2JJTFV",
	      "QueryPeers": false,
	      "RepoID": "01G4E6DRPSWGB4Y0GEX2B5ZXQS",
	      "RepoName": "x",
	      "SessionID": "01G4E6DW7BKNFJBBNVZRYEKM8X",
	      "Timestamp": "2022-05-31T16:19:25.957452-07:00",
	      "URL": {
	        "ForceQuery": false,
	        "Fragment": "",
	        "Host": "",
	        "Opaque": "",
	        "Path": "/Users/scotthartzel/github/nostromo",
	        "RawFragment": "",
	        "RawPath": "",
	        "RawQuery": "",
	        "Scheme": "file",
	        "User": null
	      },
	      "Username": "default",
	      "Version": "0.0.0"
	    }
	  }
	}

	Submitted Content {"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0} (5cd8c628f3def770...)
	Score 1.000000

Event 01G4E6NF4D2V4SKPP35THZTVT9 compose (ID 01G4E6NF4D2V4SKPP35P82KS8Q) refers to content that matches or partially matches submitted content
Event Start: 2022-05-31 16:19:26.093138 -0700 PDT
Event End: 2022-05-31 16:19:26.094788 -0700 PDT
	Metaddata: {
	  "context": {
	    "auditTimestamp": "2022-05-31T16:19:26.09318-07:00",
	    "clientSpec": {
	      "APIAction": {
	        "Aggregate": false,
	        "DefaultAdmin": false,
	        "Name": "compose",
	        "Parent": ""
	      },
	      "Args": "pd add ./tests/apitests/testdata/simple/1.json",
	      "Branch": "docs_audit",
	      "Hash": "b6d36e71a99c82cfb8591177a63847abed06c0f0",
	      "HopCount": 1,
	      "Hostname": "Scotts-iMac.local",
	      "Name": "pd_prototype_cli",
	      "OS": "darwin",
	      "Path": "/Users/scotthartzel/github/nostromo/.pd",
	      "QueriedNodes": [
	        "x"
	      ],
	      "QueryID": "01G4E6NF3B941YMACABRZ5T9N9",
	      "QueryPeers": false,
	      "RepoID": "01G4E6DRPSWGB4Y0GEX2B5ZXQS",
	      "RepoName": "x",
	      "SessionID": "01G4E6DW7BKNFJBBNVZRYEKM8X",
	      "Timestamp": "2022-05-31T16:19:26.059667-07:00",
	      "URL": {
	        "ForceQuery": false,
	        "Fragment": "",
	        "Host": "",
	        "Opaque": "",
	        "Path": "/Users/scotthartzel/github/nostromo",
	        "RawFragment": "",
	        "RawPath": "",
	        "RawQuery": "",
	        "Scheme": "file",
	        "User": null
	      },
	      "Username": "default",
	      "Version": "0.0.0"
	    }
	  },
	  "supplied": {
	    "ids": [
	      {
	        "ID": "01G4E6DW7CKV3Z1KW8DWEA2VCR",
	        "Type": 29
	      },
	      {
	        "ID": "01G4E6NF0M7PQZS7M1FYZY64E1",
	        "Type": 11
	      }
	    ],
	    "op": "Union"
	  }
	}

	Submitted Content {"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0} (5cd8c628f3def770...)
	Score 1.000000

Event 01G4E6NQ5JEHTT7DJQXM87QXSY createcommit (ID 01G4E6NQ5JEHTT7DJQXBHXSTG0) refers to content that matches or partially matches submitted content
Event Start: 2022-05-31 16:19:34.32266 -0700 PDT
Event End: 2022-05-31 16:19:34.324765 -0700 PDT
	Metaddata: {
	  "context": {
	    "auditTimestamp": "2022-05-31T16:19:34.322737-07:00",
	    "clientSpec": {
	      "APIAction": {
	        "Aggregate": false,
	        "DefaultAdmin": false,
	        "Name": "createcommit",
	        "Parent": ""
	      },
	      "Args": "pd commit create commit message one",
	      "Branch": "docs_audit",
	      "Hash": "b6d36e71a99c82cfb8591177a63847abed06c0f0",
	      "HopCount": 1,
	      "Hostname": "Scotts-iMac.local",
	      "Name": "pd_prototype_cli",
	      "OS": "darwin",
	      "Path": "/Users/scotthartzel/github/nostromo/.pd",
	      "QueriedNodes": [
	        "x"
	      ],
	      "QueryID": "01G4E6NQ54B1W2D69RFJ1WS7AP",
	      "QueryPeers": false,
	      "RepoID": "01G4E6DRPSWGB4Y0GEX2B5ZXQS",
	      "RepoName": "x",
	      "SessionID": "01G4E6DW7BKNFJBBNVZRYEKM8X",
	      "Timestamp": "2022-05-31T16:19:34.308481-07:00",
	      "URL": {
	        "ForceQuery": false,
	        "Fragment": "",
	        "Host": "",
	        "Opaque": "",
	        "Path": "/Users/scotthartzel/github/nostromo",
	        "RawFragment": "",
	        "RawPath": "",
	        "RawQuery": "",
	        "Scheme": "file",
	        "User": null
	      },
	      "Username": "default",
	      "Version": "0.0.0"
	    }
	  },
	  "supplied": {
	    "message": "commit message one"
	  }
	}

	Submitted Content {"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0} (5cd8c628f3def770...)
	Score 1.000000
```

There's a good amount of output there, but let's zero in on the most important aspects. 

1. There was one record submitted which exactly matched one record in the
   repository.
2. This record falls under the default license (since this was an empty
   repository, there was no license uploaded).
3. There were three events associated with this record: an Ingest, a compose
   (which is part of the ingest in this case) and a commit.

You can see all of this in the first stanza of the report:

```shell
Submitted Content {"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0} (5cd8c628f3def770...) matches the following repository contents

	Repository Content {"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0} (5cd8c628f3def770...)
	Score 1.000000
	Entry: ID: 01G4E6NF1MRB3RVCMFGRA1PMRT EventID: 01G4E6NF0M7PQZS7M1G3WZQS4G Timestamp: 2022-05-31 16:19:26.004999 -0700 PDT Type: IngestNewRecordsEntry Num Records 1
	Metaddata: {}
	License: default_license 01G4E6DRTVHPVAW4PBPP4PQWCR/01G4E6DRTVHPVAW4PBPTCS1FFM. Empty default license
	Entry: ID: 01G4E6NF4D2V4SKPP35RDHHQY3 EventID: 01G4E6NF4D2V4SKPP35THZTVT9 Timestamp: 2022-05-31 16:19:26.094485 -0700 PDT Type: Compose Num Records 1
	Metaddata: {}
	Entry: ID: 01G4E6NQ5JEHTT7DJQXJ5WSJ6Z EventID: 01G4E6NQ5JEHTT7DJQXM87QXSY Timestamp: 2022-05-31 16:19:34.324363 -0700 PDT Type: CreateCommit Num Records 1
	Metaddata: {}
```

The remainder of the report is details and metadata for each of those events.
If we had ingested and audited 100 records, this stanza would be shown 100
times: once for each record. But the remainder of the report would still have
the details of only three events, the three events those 100 records were
involved in.

Next, we'll audit a single record that partially matches the one record of the
repository.

Here's the record in the repository

```json
{"id": 0, "field_1": "prlFNzk", "field_2": ["some", "array", "values", 619], "field_3": "RZnbDCGfmO"}
```

And here's the record we're going to audit.

```json
{"id": 1000, "field_1": "DIFFERENT", "field_2": ["some", "array", "values", 619], "field_3": "RZnbDCGfmO"}
```

Note the minimal differences. Only the "id" and "field_1" fields are different.

If we try an audit with the default threshold of 1.0 (exact matches only) we
won't receive much of an audit report:

```shell
$ pd audit create --files ~/path/to/file/example_1_NOT_QUITE_RIGHT.json
Repo TestRepo, Audit ID 01G4E7FB00W157G8RZADHBS19J, Name audit_default_20220531163333, finished.
Repository TestRepo
Audit Name: audit_default_20220531163333
Audit ID: 01G4E7FB00W157G8RZADHBS19J
Number of submitted records: 1
Number of events: 0
Number of entries: 0
Submitted Content {"field_1":"DIFFERENT","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":1000} (5ff6aed923d61ec0...): No matches found
```

We asked for exact matches, and received none, as expected (you might have to
scroll to the right to see it `No matches found`). Instead let's specify a
threshold of 0.5:

```shell
$ pd audit create --files ~/path/to/file/example_1_NOT_QUITE_RIGHT.json --threshold 0.5
Repository:        x
Name:              audit_default_20220711145647
Auditreport ID:    01G7QM7KZ1FMFM14YJ75GJ259Q
Version:           01G7QM7NXZACCWCGQZF48VATEF
Created:           2022-07-11T14:56:47.713PDT
Last Updated:      2022-07-11T14:56:49.727PDT
Submitted Records: 1
Events:            3
Entries:           3

Submitted Content {"field_1":"DIFFERENT","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":1000} (5ff6aed923d61ec0...) matches the following repository contents

	Repository Content {"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0} (5cd8c628f3def770...)
	Score 0.600000
	Entry: ID: 01G4E6NF1MRB3RVCMFGRA1PMRT EventID: 01G4E6NF0M7PQZS7M1G3WZQS4G Timestamp: 2022-05-31 16:19:26.004999 -0700 PDT Type: IngestNewRecordsEntry Num Records 1
	Metaddata: {}
	License: default_license 01G4E6DRTVHPVAW4PBPP4PQWCR/01G4E6DRTVHPVAW4PBPTCS1FFM. Empty default license
	Entry: ID: 01G4E6NF4D2V4SKPP35RDHHQY3 EventID: 01G4E6NF4D2V4SKPP35THZTVT9 Timestamp: 2022-05-31 16:19:26.094485 -0700 PDT Type: Compose Num Records 1
	Metaddata: {}
	Entry: ID: 01G4E6NQ5JEHTT7DJQXJ5WSJ6Z EventID: 01G4E6NQ5JEHTT7DJQXM87QXSY Timestamp: 2022-05-31 16:19:34.324363 -0700 PDT Type: CreateCommit Num Records 1
	Metaddata: {}

Event 01G4E6NF0M7PQZS7M1G3WZQS4G ingest (ID 01G4E6NF0M7PQZS7M1FYZY64E1) refers to content that matches or partially matches submitted content
Event Start: 2022-05-31 16:19:25.972128 -0700 PDT
Event End: 2022-05-31 16:19:26.049314 -0700 PDT
	Metaddata: {
	  "context": {
	    "auditTimestamp": "2022-05-31T16:19:25.972195-07:00",
	    "clientSpec": {
	      "APIAction": {
	        "Aggregate": false,
	        "DefaultAdmin": false,
	        "Name": "beginingest",
	        "Parent": "ingest"
	      },
	      "Args": "pd add ./tests/apitests/testdata/simple/1.json",
	      "Branch": "docs_audit",
	      "Hash": "b6d36e71a99c82cfb8591177a63847abed06c0f0",
	      "HopCount": 1,
	      "Hostname": "Scotts-iMac.local",
	      "Name": "pd_prototype_cli",
	      "OS": "darwin",
	      "Path": "/Users/scotthartzel/github/nostromo/.pd",
	      "QueriedNodes": [
	        "x"
	      ],
	      "QueryID": "01G4E6NF05FWMZYRCWZW2JJTFV",
	      "QueryPeers": false,
	      "RepoID": "01G4E6DRPSWGB4Y0GEX2B5ZXQS",
	      "RepoName": "x",
	      "SessionID": "01G4E6DW7BKNFJBBNVZRYEKM8X",
	      "Timestamp": "2022-05-31T16:19:25.957452-07:00",
	      "URL": {
	        "ForceQuery": false,
	        "Fragment": "",
	        "Host": "",
	        "Opaque": "",
	        "Path": "/Users/scotthartzel/github/nostromo",
	        "RawFragment": "",
	        "RawPath": "",
	        "RawQuery": "",
	        "Scheme": "file",
	        "User": null
	      },
	      "Username": "default",
	      "Version": "0.0.0"
	    }
	  }
	}

	Submitted Content {"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0} (5cd8c628f3def770...)
	Score 0.600000

Event 01G4E6NF4D2V4SKPP35THZTVT9 compose (ID 01G4E6NF4D2V4SKPP35P82KS8Q) refers to content that matches or partially matches submitted content
Event Start: 2022-05-31 16:19:26.093138 -0700 PDT
Event End: 2022-05-31 16:19:26.094788 -0700 PDT
	Metaddata: {
	  "context": {
	    "auditTimestamp": "2022-05-31T16:19:26.09318-07:00",
	    "clientSpec": {
	      "APIAction": {
	        "Aggregate": false,
	        "DefaultAdmin": false,
	        "Name": "compose",
	        "Parent": ""
	      },
	      "Args": "pd add ./tests/apitests/testdata/simple/1.json",
	      "Branch": "docs_audit",
	      "Hash": "b6d36e71a99c82cfb8591177a63847abed06c0f0",
	      "HopCount": 1,
	      "Hostname": "Scotts-iMac.local",
	      "Name": "pd_prototype_cli",
	      "OS": "darwin",
	      "Path": "/Users/scotthartzel/github/nostromo/.pd",
	      "QueriedNodes": [
	        "x"
	      ],
	      "QueryID": "01G4E6NF3B941YMACABRZ5T9N9",
	      "QueryPeers": false,
	      "RepoID": "01G4E6DRPSWGB4Y0GEX2B5ZXQS",
	      "RepoName": "x",
	      "SessionID": "01G4E6DW7BKNFJBBNVZRYEKM8X",
	      "Timestamp": "2022-05-31T16:19:26.059667-07:00",
	      "URL": {
	        "ForceQuery": false,
	        "Fragment": "",
	        "Host": "",
	        "Opaque": "",
	        "Path": "/Users/scotthartzel/github/nostromo",
	        "RawFragment": "",
	        "RawPath": "",
	        "RawQuery": "",
	        "Scheme": "file",
	        "User": null
	      },
	      "Username": "default",
	      "Version": "0.0.0"
	    }
	  },
	  "supplied": {
	    "ids": [
	      {
	        "ID": "01G4E6DW7CKV3Z1KW8DWEA2VCR",
	        "Type": 29
	      },
	      {
	        "ID": "01G4E6NF0M7PQZS7M1FYZY64E1",
	        "Type": 11
	      }
	    ],
	    "op": "Union"
	  }
	}

	Submitted Content {"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0} (5cd8c628f3def770...)
	Score 0.600000

Event 01G4E6NQ5JEHTT7DJQXM87QXSY createcommit (ID 01G4E6NQ5JEHTT7DJQXBHXSTG0) refers to content that matches or partially matches submitted content
Event Start: 2022-05-31 16:19:34.32266 -0700 PDT
Event End: 2022-05-31 16:19:34.324765 -0700 PDT
	Metaddata: {
	  "context": {
	    "auditTimestamp": "2022-05-31T16:19:34.322737-07:00",
	    "clientSpec": {
	      "APIAction": {
	        "Aggregate": false,
	        "DefaultAdmin": false,
	        "Name": "createcommit",
	        "Parent": ""
	      },
	      "Args": "pd commit create commit message one",
	      "Branch": "docs_audit",
	      "Hash": "b6d36e71a99c82cfb8591177a63847abed06c0f0",
	      "HopCount": 1,
	      "Hostname": "Scotts-iMac.local",
	      "Name": "pd_prototype_cli",
	      "OS": "darwin",
	      "Path": "/Users/scotthartzel/github/nostromo/.pd",
	      "QueriedNodes": [
	        "x"
	      ],
	      "QueryID": "01G4E6NQ54B1W2D69RFJ1WS7AP",
	      "QueryPeers": false,
	      "RepoID": "01G4E6DRPSWGB4Y0GEX2B5ZXQS",
	      "RepoName": "x",
	      "SessionID": "01G4E6DW7BKNFJBBNVZRYEKM8X",
	      "Timestamp": "2022-05-31T16:19:34.308481-07:00",
	      "URL": {
	        "ForceQuery": false,
	        "Fragment": "",
	        "Host": "",
	        "Opaque": "",
	        "Path": "/Users/scotthartzel/github/nostromo",
	        "RawFragment": "",
	        "RawPath": "",
	        "RawQuery": "",
	        "Scheme": "file",
	        "User": null
	      },
	      "Username": "default",
	      "Version": "0.0.0"
	    }
	  },
	  "supplied": {
	    "message": "commit message one"
	  }
	}

	Submitted Content {"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0} (5cd8c628f3def770...)
	Score 0.600000
```

When you specify a threshold under 1.0, audit will report on partial matches
above that threshold. Here, our submitted content matches (score of 0.6) the
single record that we have in the repository. Audit then reports on all events
for that partially matched record.

This is critical to understand when dealing with thresholds: in a large repo, a
submitted record may partially match hundreds or thousands of records (if your
data has fields that are the same across many records, it may match not
hundreds or thousands, but hundreds of thousands). Audit will report all events
for each of these partially matched records. This is why it is important to
limit the scope of each audit: limit the number of records under audit and
choose the highest threshold that produces a meaningful report.

### Auditing a Dataset

Supplying a dataset for audit works as you would expect: instead of reading the
records for audit from a file, PD reads them from an existing dataset within
the repository.

We can use the commit ID from our ingest of a single record above as the
argument to the audit command:

```shell
$ pd audit create --commit 01G4E6NQ5JEHTT7DJQXBHXSTG0
< output removed >
```

The output is exactly as if we had audited the file containing the record:

```shell
$ pd audit create --files ~/path/to/file/example_1.json
< output removed >
```

The PD CLI supports auditng records from files, commit or from your current
workspace dataset.

### See Also

See the CLI reference for more information on using [pd audit](/docs/commands/pd_audit.html)
