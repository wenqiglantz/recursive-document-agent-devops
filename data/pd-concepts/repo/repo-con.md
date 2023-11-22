# Concepts / Repository

### Summary

A Provenant Data **Repository** is an instance of the Provenant Data platform,
containing datasets, metadata about those datasets, and policies that modulate
admission of, access to, and experience of those datasets. Let's break that
down:

_A collection of Datasets_. [Datasets](/docs/concepts/dataset), as discussed,
are simply collections of records. The foundation of a PD repository is the
datasets it contains.

_Metadata about those datasets_. A PD repo holds extensive metadata about the
datasets it contains. Products, releases, branches etc. are all
metadata-containers of datasets, immutably maintained within the repository.
Additionally, every interaction with the data in the repository is tracked as
audit metadata.

_Polices_. Policies modulate admission of, access to, and experience of those
datasets. Without policies, a repository is only a collection of content. With
policies, a repository joins content with behavior. PD policies are powerful,
more powerful than simply allowing or denying access. PD Policies can transform
data and metadata, customizing a user's experience, or an administrator's
expectations, of the data.

### Repository Federation

*Repositories* are not constrained to standing alone. Repositories may be
linked to other repositories, and share data (modulated, as always, by policy),
effectively federating the data. Users interact with this federation (called a
[data mesh](/docs/concepts/mesh)) seamlessly; they don't need to know where
their data lives, or manage a different set of credentials for each dataset
they use, or care who manages the data or how. They simply work with the
datasets they need.
