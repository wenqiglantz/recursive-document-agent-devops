# Guide / Schemas

Schemas allow Provenant Data administrators to restrict ingested data to
conform with a set of restrictions expressed as [JSON
Schema](https://json-schema.org).

Schemas are similar to [plugins](/docs/guide/plugins) in that they are written and
uploaded by the user, triggered by policies, and have access to the record data
as it flows across the system (in this case, at ingest).

To get familiar with them, let's create a simple schema and apply. This schema
will enforce just a few very simple conditions on the data. 

```json
{
  "title": "Schema Validation Example",
  "description": "An Example Schema Validation",
  "type": "object",
  "properties": {
    "id": {
      "description": "A unique identifier",
      "type": "integer"
    },
    "field_1": {
      "description": "The first field",
      "type": "string"
    }
  },
  "required": [
    "id",
    "field_1"
  ]
}
```

In the JSON Schema above we can see that the field named "id" must be an
integer, the field named "field_1" must be a string, and that both are
required.

To put a schema in place we need to: 

1. Write a schema
2. Create the schema within PD, uploading the schema file
3. Apply it using a policy

To create the schema:

```shell
$ pd schema create simple_schema ./path/to/schema.json
schema created
```

And now we need a policy applied to ingest that references the schema:

```rego
package provenant.ingest
default allow = true

schema[name] {
    allow
	name = "simple_schema"
}
```

This simple policy states that all authenticated users are allowed to ingest, and that
every ingest must be checked against our schema named 'simple_schema'.


We update the policy:

```
pd policy update provenant.ingest ./data/schematest_everyone.rego
```

Our schema and policy are now in place and ready to validate our ingested data.
Here's some sample data we can ingest.


```json
{"id": 11, "field_1": "prlFNzk", "field_2": ["some", "array", "values"], "field_3": "RZnbDCGfmO"}
{"id": "Not an integer", "field_1": "prlFNzk", "field_2": ["some", "array", "values"], "field_3": "RZnbDCGfmO"}
{"id": 1, "field_2": ["some", "array", "values"], "field_3": "Field 1 is missing"}
```

Without a schema in place, the above data can be ingested without any restriction. With the schema in place we will see some errors

```shell
$ pd branch ingest main --message 'some problems here' ./path/to/sample_data.json
Ingest ID:        01G7QRTDPATJM0FQSBFEP9V55D
Version:          01G7QRTDPV1HEHT2DWZ836KEY9
Created:          2022-07-11T16:16:58.186PDT
Last Updated:     2022-07-11T16:16:58.203PDT
Ingested Records: 1
New Records:      0
Validation Error: validation error(s) [/id: "Not an integer" type should be integer, got string]. Content: {"id": "Not an integer", "field_1": "prlFNzk", "field_2": ["some", "array", "values"], "field_3": "RZnbDCGfmO"}
Validation Error: validation error(s) [/: {"field_2":["some","... "field_1" value is required]. Content: {"id": 1, "field_2": ["some", "array", "values"], "field_3": "Field 1 is missing"}
Tags:             none

Commit ID:        01G7QRTDQ33XV7B9FGMSGGSH3Z
Version:          01G7QRTDQ4Y67M7BMZMR87VF28
Created:          2022-07-11T16:16:58.211PDT
Last Updated:     2022-07-11T16:16:58.212PDT
Branch:           main
Message:          xyz
Dataset Size:     1
Origin Repos:     1
                  01G7QFA0FQ8PNFTHD0Q941RC6S (this repo)
Tags:             none
```

We can see that only one record (the one that conforms) was ingested. The other
two were rejected, and the reasons are given. Record 2's 'id' field is not an
integer, but a string, and was rejected. And record 3 is missing a required
field ('field_1') altogether. 
