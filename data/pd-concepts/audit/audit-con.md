# Concepts / Audit

### Summary

The **Audit function** assesses data submitted for a record-by-record examination to determine whether the (extended) repository performing the audit has any prior information pertaining to that record _explicitly_ or for any records which are considered 'similar'.

The Audit function retrieves the detailed history and provenance of the data records that it identifies unambiguously as matching the submitted record, or (if similarity scoring is employed) the history and provenance of records already contained in the repository which meet a 'similarity threshold'.

The user can audit data from external sources (such as content contained in files), or from data already in the repository and is reference in your workspace dataset (like a previous **Commit event** referenced by its Commit ID).

Each Audit invocation (**Audit Event**) results in a report which represents a snapshot from a specific point in time.  The **Audit Event ID** associated with the report references a dataset which can be downloaded or referenced again for some other purpose _without_ actually having to repeat the audit assessment process.

### Constructing the Submission Set

For each record submitted for audit in the **Submission Set**, the Audit function retrieves from the repository the records associated with unique Audit Event IDs created by PD and the **Audit Entries** associated with the Audit Event.   An Audit Event is treated as a 'dataset container' holding the records associated with a uniquely identified API call (such as a data ingest, a data commit, a retrieval event, etc.). Each event may have more than one sub-event, which we call an entry.

For example an ingest event may have been defined as the contents of multiple ingested files, each of which may result in an audit entry in that ingest event.

### Similarity Scoring

If you audit the dataset represented by a Commit Event, you can be certain that all of the data under audit will be found in the repository. Often, however, you will want to audit exogenous data that exists outside the repo.  For example,  you may want to determine if the exogenous data being submitted for audit has been derived from one of your existing data products, possibly in a fashion that violates the license or other terms of use.

PD's Audit function is designed to assess the submitted data and to determine its similarity on a record-by-record basis, even though the submitted record may have been altered, fields and values added, or transformations applied. In submitting the exogenous data for audit, PD will determine 

- if it is related to data already in the repository 
- to _which_ data (which release or commit, for example) it's related, and 
- how closely it resembles the data already in the repository. 

For this, the user can specify a _similarity threshold_ for the audit which ranges from  0.0 to 1.0. A value of 1.0 will only return exact matches (each key and value in a submitted record are an exact match for those of a record in the repository). A threshold value of 0.0 will return the history and provenance of records which are only slightly related to the submitted data (a single value in common, for example).

### Report Generation

Once an **Audit report** is generated, it represents a snapshot from a specific point in time. It can be downloaded or referenced again by using the report's Audit Event ID, and does not need to be regenerated.

Audit reports may produce a great deal of information. Depending on the size and scope of the repository, the heterogeneity of the data in the repository, and the similarity threshold specified in the Audit invocation, Audit reports may be too large for practical use or exploration, or may take a long time to generate.

Best practice is to limit the scope of each audit: the user should limit the number of records under audit and choose the highest threshold that produces a meaningful report.

### Using Audit Results as Input

An Audit invocation returns, potentially, a lot of data about the history and provenance of a dataset. Often too much data. The raw output from an audit is largely meant to be used as input to other processes or commands, or as a dataset to be mined in pursuit of more specific questions.

The **Compliance Report** functionality exists as a simple example of this. When a compliance report is requested (see [pd compliance](/docs/commands/pd_compliance.html)), a full audit of the data is performed, and that audit report's raw data is fed to the compliance policy, which uses it to determine whether or not the dataset is compliant with the terms of the policy.

### Increasing Audit Value

The more PD knows about the life of your data, the more meaningful information can be produced by an audit. An ideal usage of PD is as a checkpointing system within a data pipeline: at each transformation, or each discrete step within the pipeline it makes sense to ingest the dataset into PD, with metadata describing the context. Later, in the same pipeline run or years down the road, detailed context can be retrieved on-demand; the state of your data can be inspected at any point in its history. Data deduplication within PD makes fine-grained, permanent data lineage and provenance a low-difficulty, high impact, low-cost, high-value reality.

