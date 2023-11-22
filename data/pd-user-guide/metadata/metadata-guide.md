# Guide / Metadata

## Providing Metadata

You may attach arbitrary JSON data structures to nearly every available API
call. This metadata will then appear along side these API calls and actions
when you perform an audit. You are also be able to search metadata values and
have the objects to which they are associated returned.

In the example below, we use the CLI to both attach a file containing a JSON
object as metadata (`--metadata-file ./metadata1.json`), and to directly supply
metadata as a JSON object on the command line (`--metadata-arg '{"a":"b"}'`).

```shell
$ pd branch ingest main --message 'XYZ' ./simple/14.json --metadata-file ./metadata1.json --metadata-arg '{"a":"b"}'
Ingest ID:        01GGK1WPBVH2YR1532FAZC5A4A
Version:          01GGK1WPCQ6P7B6GTA4ETJXQN0
Created:          2022-10-29T16:40:34.043PDT
Last Updated:     2022-10-29T16:40:34.071PDT
Ingested Records: 14
New Records:      14
Metadata ID:      01GGK1WPBVH2YR1532FE4VRAMB
Tags:             none

Repository:   testrepo
Commit ID:    01GGK1WPD0SAD4E7X41HCYCV58
Version:      01GGK1WPD1CC855VX599KRWRPZ
Created:      2022-10-29T16:40:34.08PDT
Last Updated: 2022-10-29T16:40:34.081PDT
Branch:       main
Message:      YOU
Dataset Size: 14
Origin Repos: 1
              01GGK1W22581VQS4AYZX7MF0FZ (this repo)
Metadata ID:  01GGK1WPD0SAD4E7X41NGKCRT1
Tags:         none
```

We can use the `pd metadata show` command to examine the metadata that was
attached to our ingest:

```shell
$ pd metadata show 01GGK1WPD0SAD4E7X41NGKCRT1
Metadata ID: 01GGK1WPD0SAD4E7X41NGKCRT1
             Type   ID
             commit 01GGK1WPD0SAD4E7X41HCYCV58
Content:     {"Brothers":["Larry","Darryl","Darryl"],"Co-Owner":"Joanna Louden","Owner":"Dick Louden","__PD_ClientInfo":{"Environment":{"Timestamp":"2022-10-29T16:40:34.072841-07:00","Args":"pd branch ingest main --message XYZ ./simple/14.json --metadata-file ./metadata.json --metadata-arg {\"a\":\"b\"}"},"Host":{"OS":"darwin","Hostname":"Scotts-iMac.local","UserAgent":"","Address":""},"Software":{"Name":"pd_prototype_cli","Version":"0.0.0","Branch":"metadata_replacement","Hash":"260e4d3be8efb28e095aaec6c3d41fbda14faa17"}},"a":"b"}
```

Everything under the `__pd_ClientInfo` key is supplied automatically by the
CLI. The rest of the metadata content was supplied by the user.

Right now, from the CLI and the Web UI, metadata may be attached to ingests,
commits and releases. When you search and retrieve based on metadata values,
you retrieve these objects via metadata keys and values supplied at the point
these objects were created.

All other API actions available now will take a metadata object as an argument,
but, unless the API call created an ingest, a commit or a release, the metadata
is only surfaced in audit.

In the near future the utility of the metadata is likely to expand: You may
very well be able search for metadata keys and values and find all API actions
associated with that metadata. This would allow an application developer the
ability to recall objects and actions from the Provenant Data platform with
maximum flexibility.

## Searching for Metadata

We may search for commits, ingests and releases to which we have attached
metadata, by providing a key and a value.

Metadata search at the moment is rudimentary, but serviceable. You need to
provide both a key and a value, and only metadata objects where the key and the
value both match will be returned. The search is case-insensitive.

```shell
$ pd metadata search a b
Found 2 metadata objects
Metadata ID:       01GH4RJFAYD86ZTHY5JTGFQRMX
Version ID:        01GH4RJFAYD86ZTHY5JZGN9M3R
Association Count: 1
                   ID                         Type
                   01GH4RJFAYD86ZTHY5JMBW2E8E ingest
Content:     {"Brothers":["Larry","Darryl","Darryl"],"Co-Owner":"Joanna Louden","Owner":"Dick Louden","__PD_ClientInfo":{"Environment":{"Timestamp":"2022-10-29T16:40:34.072841-07:00","Args":"pd branch ingest main --message XYZ ./simple/14.json --metadata-file ./metadata.json --metadata-arg {\"a\":\"b\"}"},"Host":{"OS":"darwin","Hostname":"Scotts-iMac.local","UserAgent":"","Address":""},"Software":{"Name":"pd_prototype_cli","Version":"0.0.0","Branch":"metadata_replacement","Hash":"260e4d3be8efb28e095aaec6c3d41fbda14faa17"}},"a":"b"}

Metadata ID:       01GH4RJFBWBM3KEHYASK9CQEYA
Version ID:        01GH4RJFBWBM3KEHYASRJK4428
Association Count: 1
                   ID                         Type
                   01GH4RJFBWBM3KEHYASD8BN7V1 commit
Content:     {"Brothers":["Larry","Darryl","Darryl"],"Co-Owner":"Joanna Louden","Owner":"Dick Louden","__PD_ClientInfo":{"Environment":{"Timestamp":"2022-10-29T16:40:34.072841-07:00","Args":"pd branch ingest main --message XYZ ./simple/14.json --metadata-file ./metadata.json --metadata-arg {\"a\":\"b\"}"},"Host":{"OS":"darwin","Hostname":"Scotts-iMac.local","UserAgent":"","Address":""},"Software":{"Name":"pd_prototype_cli","Version":"0.0.0","Branch":"metadata_replacement","Hash":"260e4d3be8efb28e095aaec6c3d41fbda14faa17"}},"a":"b"}
```

In the future, extensive search capabilities will be included in the platform,
not only for searching metadata, but for searching and organizing all of the
content of the repository.
