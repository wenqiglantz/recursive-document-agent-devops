# Guide / Commits

Within the repository, a commit is the primary reference to a dataset. You make
commits out of datasets, retrieve commits, compose products and releases out of
commits, and verify the contents of your repository by verifying the contents
of commits. A commit is a “checkpoint” that contains a reference, or
references, to the data contained within. Commits are attached to the branch in
which they occured, and are identified by their unique 26-character ID.

Branches, being primarily containers for commits, are the place you see commits most often:

```shell
$ pd branch show main|head -20
Repository:    MyRepository
Display Name:  main
Name:          main
Commit ID:     01G6S5VPJG1QVK53NKVAX77MHV
Version:       01G7QNRGH3TBG9RR3MFFS1JY7F
Created:       2022-06-29T19:08:24.144PDT
Last Updated:  2022-07-11T15:23:29.827PDT
Parent Branch: None
Parent Commit: None

Commits:
    ID                         Version                    Created                    Branch ID                  Message               Records
0   01G6S5VPJG1QVK53NKVCP26XHE 01G6S5VPJG1QVK53NKVQE0RP92 2022-06-29T19:08:24.144PDT 01G6S5VPJG1QVK53NKVAX77MHV main - initial commit 0
1   01G6S5WJ4J6JHPSPK537G7PE63 01G6S5WJ4KVYVGCM9ZT0FAJZ09 2022-06-29T19:08:52.37PDT  01G6S5VPJG1QVK53NKVAX77MHV commita               1
2   01G6S5WJV6J9BE0ERZCHT7S183 01G6S5WJV7QEN8V778FJ5CM3K3 2022-06-29T19:08:53.094PDT 01G6S5VPJG1QVK53NKVAX77MHV commmitb              2
3   01G6S5WK96TB0KZW1JS30YZ4WN 01G6S5WK97H4DVHEV2D6DHJK6H 2022-06-29T19:08:53.542PDT 01G6S5VPJG1QVK53NKVAX77MHV commit csv            3
4   01G6S5WKKQY4YPTWA7JAWPBTJX 01G6S5WKKRABE0RTCA1VBTTVV7 2022-06-29T19:08:53.879PDT 01G6S5VPJG1QVK53NKVAX77MHV commit csv            3
5   01G6S5WM9FM3R47PM149YTYHZ6 01G6S5WM9G8PSXAS05AC74EYBR 2022-06-29T19:08:54.575PDT 01G6S5VPJG1QVK53NKVAX77MHV commit with metadata  11
6   01G6S5WMMWWN8VSRP7BRYTQP79 01G6S5WMMX1XJXBM3C2VBA3DZ9 2022-06-29T19:08:54.94PDT  01G6S5VPJG1QVK53NKVAX77MHV clobber               1
7   01G6S5X8XNT8H5D3Y9XASCSGCC 01G6S5X8XP5C80ZV3EGEVT7FPV 2022-06-29T19:09:15.701PDT 01G6S5VPJG1QVK53NKVAX77MHV into main             1
...
```

Each entry under "Commits" is a Commit ID (paired with its version ID). 

### Inspecting a Commit

Viewing a commit is done with `pd commit show`:

```shell
$ pd commit show 01G6S5WJ4J6JHPSPK537G7PE63
Repository:   MyRepository
Commit ID:    01G6S5WJ4J6JHPSPK537G7PE63
Version:      01G6S5WJ4KVYVGCM9ZT0FAJZ09
Created:      2022-06-29T19:08:52.37PDT
Last Updated: 2022-06-29T19:08:52.371PDT
Branch:       main
Message:      commita
Dataset Size: 1
Origin Repos: 1
              01G6S5VPGWYAZ4B70ZJ2NNN907 (this repo)
Tags:         none
```

The output gives you a handful of useful data. The Branch ID denotes the branch
to which this commit is attached. It also shows you the commit message
registered with the commit at the time it was created, as well as a view into
the origin of some of the data within the commit: data in this commit
originated from one repo (the one we're currently logged into) And contains
data from a single ingest. Real data will likely come from many ingests, and
data transferred between repositories on a mesh will likely originate from
multiple repos.

### Creating a Commit

Creating a new commit is straightforward and painless. There are two main avenues to take:
 
1. Via `branch ingest`. See the [branch ingest](/docs/guide/branches) documentation on how to do that.
2. By commiting data from your workspace's active dataset.

First we'll add some data into our workspace from a file, and then we'll commit it:

```shell
$ pd add --files ~/some/test/data.json
Composition ID:   01G7QQ5X63Q9D24ASWPHQQ66YZ
Total Records:    2

Ingest ID:        01G7QQ5X54SX0CWMF1HFGB4477
Version:          01G7QQ5X5SXKMNVVMYJJSJ0ER0
Created:          2022-07-11T15:48:17.316PDT
Last Updated:     2022-07-11T15:48:17.337PDT
Ingested Records: 2
New Records:      2
Tags:             none


$ pd commit create 'my commit message'
Created commit 01G7B9T1B6E15R85KVC1RT9TFE
```

Commiting requires a commit message to give later viewers some idea of what is
in this commit, or why it exists at all.

### Retrieving the Commit Dataset

In order to get the data out of the commit, we `pd retrieve` it:

```shell
pd commit retrieve 01G7B9T1B6E15R85KVC1RT9TFE
{"field_1":"prlFNzk","field_2":["some","array","values",619],"field_3":"RZnbDCGfmO","id":0}
{"field_1":"prlFXXX","field_2":["some","array","values",620],"field_3":"RZnbDCGfmO","id":1}
```

This dataset is only two records, which is not particularly exciting, but real
datasets may be tens of thousands of records. In those cases, you may want to
preview the data before you retrieve it, so `pd retrieve` has a `--preview`
option.

### Verifying a Commit

Each commit contains a cryptographic hash that captures the content and
metadata of the commit, as well as its relationship to the commit preceding it
in a branch. And that commit, likewise, is cryptographically tied to the one
before it... and so on until the beginning of the branch. The branch is linked
again to the branch and commit from which it was created... this process
proceeds all the way back to the initial commit in the repository.

When you use `pd verify commit <commit_id>`, PD verfies each commit in the
chain until the origin of the reopository. If any cryptographic proof at any
stage has been altered, the commit will fail verification. In this way you can
be assured that the datasets committed in the repository, and the metadata
associated with them, are unaltered.

```shell
$ pd commit verify 01G7B8QC2N90T816W01DHQ3FJ1
Commit verified
```
