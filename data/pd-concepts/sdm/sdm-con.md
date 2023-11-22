# Concepts / Source Data Management

### Summary

The Provenant Data platform is built around a series of fundamental concepts and techniques we call distributed  **Source Data Managment** (SDM). Many of SDM concepts are analogous to those of distributed Source Code Managment (SCM) with which most software developers are already familiar. Like many SCM tools, PD organizes source data using the _repository_, _branch_, _commit_, _tag_ and other foundational aspects that make working with versioned datasets more comfortable and familiar.

### Repositories

The broadest fundamental object in the PD platform is a [Repository](/docs/concepts/repo). A repository is an instance of the platform which contains and stores the data, assets, history (lineage and provenance) for a given purpose.  The PD repository contains the other objects and assets recognized by PD as having functional or operational roles in the SDM.

A repository (often known as a 'repo') is made up of commits and branches.

### Commits

[Commits](/docs/guide/commits) are the primary vehicle for referencing a dataset. A commit is a "checkpoint" that contains a reference, or references, to the data contained within. Commits are attached to the branch in which they occurred, and are identified by their unique 26-character ID.

Each commit also carries with it a cryptographic hash which permanently establishes its place  in the lineage of the data. This cryptographic data may be used to verify the contents of a commit, following the crypto-trail back to the root of the repository.

When considering the concept of a commit, think of it as nearly synonymous with the dataset it contains.

Commits may be _composed_; that is, they may be added together, subtracted from one another, the intersection may be computed etc, and the resulting dataset may be stored in another, distinct commit.

The most important things to remember are
1.  Commits are immutable
2.  Commit ids will be different every time - even if the data contained in commit is otherwise indistinguishable
3.  A PD Commit always retains references its parent id(s)

### Branches

A PD [Branch](/docs/guide/branches) is similar in concept to a branch in SCM tools and it is defined as an ordered collection of commits. PD creates a branch designation with a distinct, unique ID which always maintains a reference to the commit ID from where it starts. In the parlance of PD, it is a container that holds commits, and relates the commits to each other in an immutable chain of provenance.

Branches are lightweight and inexpensive in PD; create as many as you need!
Because they only contain references to data, they have almost no impact on the size or malleability of the repository.

In contrast to PD's _data_-management approach,  _code_-management practices standardize around a small number of long-lived code branches, with ephemeral feature- or task-specific branches popping in and out of existence as needed. Most of these code changes in a SCM, after validation, are merged back into a limited number of "more stable" branches.

For Source _Data_ Management, specifically for PD, a different approach is encouraged. Branches in PD are so inexpensive, and the context provided by the chain-of-commits within a branch so valuable, that branches are retained permanently. "Deleting" a branch in PD hides it from view, and removes it as a possible target for data ingests and commits. But the branch, and all of its lineage and provenance remains.

In PD, the tree does not require, nor does it benefit from, continual pruning.

### Ingests

[Ingests](/docs/guide/ingest) are similar to commits in that they are a single, stable reference to the data contained in the ingest. An ingest is created each time data is added to the repository. Whereas commits are the primary vehicle for referencing a dataset, ingests are a secondary way to reference a specific dataset that was generated at the time the data was introduced to the repository.

Like commits, ingests may be _composed_, by which we mean that new datasets may be created by combining ingests with one another, and with commits, or other dataset-containing PD objects.

### Tags

[Tags](/docs/guide/tags) are labels that can be applied to nearly any Provenant Data entity. They have broader scope than their analogous counterparts in popular SCM tools. And nearly anywhere you can reference an object that contains one or more datasets (like a commit, an ingest or a branch), you can reference a tag instead, and operate in aggregate on the contained datasets.

### Workspaces

SCM tools largely use your filesystem as their workspace. Code is free to mutate on your filesystem without impacting the code repository until it is staged and/or committed. In PD, manipulation of datasets requires a different approach. Datasets may be too large or unwieldy to manipulate on your laptop's filesystem, or the data pipeline's automated process may simply be a mismatch for the "staging-area-on-your-filesystem" approach.

In PD, data in-flight is saved to a [workspace](/docs/guide/workspace) (also sometimes called a session). A workspace is a history of changes made to datasets, and the results of those changes. Workspaces may be suspended, and resumed, created and renamed. They are saved within the repository, so there is never any danger of losing work in process.

The central component of a workspace is the "Active Dataset" which is the dataset in-flight. When you ingest data, it lands not only in an Ingest object, but in the Active Dataset of your current workspace. When adding two commits together, the result lands in your Active Dataset. And when making a commit, it is the active dataset that is committed to the repository.

Workspaces are fully versioned and navigable; you may return to any point in your workspace history without losing any data. It's infinite undo for dataset composition.
