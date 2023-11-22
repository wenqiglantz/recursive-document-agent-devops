# Concepts / Schemas

### Summary

The Provenant Data platform is designed to deal with data that is schemaless. While this offers the greatest flexibility when arranging or manipulating the datasets within the repository, there are times when some restrictions on the ingested data are necessary. In those cases, the repository owner can create a [schema](/docs/guide/schemas) and apply it with an ingest [policy](/docs/concepts/policy). Each record in an ingest is then checked for compliance against the schema, and may be rejected (or a warning may be issued) if the schema is violated.

Because schemas are triggered by policies they may be applied or required conditionally, and, given the flexibility of the policy engine, those conditions are limited only by the policy designer's access to data on which to make the decision.

Schemas are expressed as [JSON Schema](https://json-schema.org/specification.html), and offer the full capabilities of the specification.
