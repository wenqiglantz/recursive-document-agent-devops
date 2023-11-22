# Concepts / Dataset

In Provenant Data, we use the term **dataset** to refer to a collection of records. Broadly, it refers to any collection of records, but specifically we use *dataset* to refer to a collection of data known to the repo and accessed via a lightweight reference. Datasets are usually contained in a PD Entity like a "commit" or a "branch" with the entity's ID specified.

Datasets contain one or more records. The number of records within a dataset is bound only by the ability to physically store the records. Datasets may be composed out of other datasets. For example, if you wish to add a single record to a dataset that already contains 9999 records, you perform a union of the two datasets (the single-record dataset, and the 9999-record dataset). The result is a new, 10,000-record dataset, identified by a unique Event ID in which the union action was performed.

What's important here is that it's the underlying references themselves that are composable. Within PD, performing a union of two datasets, each containing one record, is roughly the same complexity as performing a union on two datasets each of which contain a million records.

### Dataset Composition

Composition of datasets is based on the simple concept of set operations:
**union**, **intersection** and **difference**.

- A union is the addition of two or more datasets (with the duplicates removed). 
- The difference between datasets A and B is the removal of all contents of dataset B from dataset A.
- An intersection is the dataset of records in common between two or more datasets.

These operators offer a simple, and when combined with the scalability of the dataset references, powerful way to construct datasets within PD. A detailed explication and description of how these operators are used with pd commands may be found in the guide on [Dataset Composition](/docs/guide/composition).

### Data Deduplication

Where a source code manager (SCM) such as *git* is content-addressable and file-oriented, Provenant Data is content-addressable and record-oriented. The first time a record is introduced to a repository, it is canonicalized, and a reference to the record is created. Any further ingests of this record are captured by the existing reference.

This makes it convenient to capture datasets at many different points during the data product lifecycle, capturing the different contexts and uses as metadata. Each time, the only new data that is stored is the data that's valuable at that point: the metadata.

