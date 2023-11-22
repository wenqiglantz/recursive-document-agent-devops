# Guide / Branches 

A branch is an object within the Provenant Data platform roughly analogous to
the branches you might find in a Source Code Management (SCM) tool. They exist
primarily to hold commits, and metadata required to cryptographically verify
the contents and lineage of those commits.

Branches are lightweight and inexpensive datastructures composed mainly of
references to other objects. A repository can confortably manage hundreds or
even thousands of branches. Where in an SCM like git, most development
processes lead to short-lived branches that inevitably merge into the main
branch (or are abandoned), branches in PD are permanent and unobtrusive.
Deleting a branch makes it invisible, and unavialble for operations like
holding a commit, or being pushed or pulled, but he branch itself remains
within the repository.

### Listing Branches

To see all the branches avialable in the repository, use `pd branch list`:

```shell
$ pd branch list
Repository: MyRepository
  Name     ID                         Version                    Created                    Updated                    Commits Tags
0 main     01G6S5VPJG1QVK53NKVAX77MHV 01G7QNRGH3TBG9RR3MFFS1JY7F 2022-06-29T19:08:24.144PDT 2022-07-11T15:23:29.827PDT 565     1
1 alpha    01G6S5WN46QNH0JY1BEG0NZBYA 01G6S5WN47PKCJ1BY7WVDXNXFT 2022-06-29T19:08:55.43PDT  2022-06-29T19:08:55.431PDT 0       0
2 bravo    01G6S5WN6N7M62DV3JBYKWT97T 01G6VCJ8C9EBS95NE3P54ZD5HZ 2022-06-29T19:08:55.509PDT 2022-06-30T15:44:03.593PDT 0       0
3 charlie  01G6S5XAA18Q89PA3RW52QYBTT 01G6VCJPNR9YJMFK79SFAH8MB6 2022-06-29T19:09:17.121PDT 2022-06-30T15:44:18.232PDT 4       0
```

That will show you all available branches, excluding deleted branches. To see
deleted branches:

```shell
$ pd branch list --deleted
Repository: MyRepository
  Name              ID                         Version                    Created                    Updated                    Commits Tags
0 main              01G6S5VPJG1QVK53NKVAX77MHV 01G7QNRGH3TBG9RR3MFFS1JY7F 2022-06-29T19:08:24.144PDT 2022-07-11T15:23:29.827PDT 565     1
1 alpha             01G6S5WN46QNH0JY1BEG0NZBYA 01G6S5WN47PKCJ1BY7WVDXNXFT 2022-06-29T19:08:55.43PDT  2022-06-29T19:08:55.431PDT 0       0
2 bravo             01G6S5WN6N7M62DV3JBYKWT97T 01G6VCJ8C9EBS95NE3P54ZD5HZ 2022-06-29T19:08:55.509PDT 2022-06-30T15:44:03.593PDT 0       0
3 charlie           01G6S5XAA18Q89PA3RW52QYBTT 01G6VCJPNR9YJMFK79SFAH8MB6 2022-06-29T19:09:17.121PDT 2022-06-30T15:44:18.232PDT 4       0
4 goodbye (deleted) 01G6S5XCBS30R8VZBRTCVKJEEX 01G6VCJQMXD0FA266M7W37JBCB 2022-06-29T19:08:55.43PDT  2022-06-29T19:08:55.431PDT 0       0
```

### Show Branch Details

To see the branch in detail, use `pd branch show <branch_name>`:

```shell
$ pd branch show main|head -20
Repository:    MyRepository
Display Name:  main
Name:          main
Branch ID:     01G6S5VPJG1QVK53NKVAX77MHV
Version:       01G7QNRGH3TBG9RR3MFFS1JY7F
Created:       2022-06-29T19:08:24.144PDT
Last Updated:  2022-07-11T15:23:29.827PDT
Parent Branch: None
Parent Commit: None

Commits:
    ID                         Version                    Created                    Branch ID                  Message                               Records
0   01G6S5VPJG1QVK53NKVCP26XHE 01G6S5VPJG1QVK53NKVQE0RP92 2022-06-29T19:08:24.144PDT 01G6S5VPJG1QVK53NKVAX77MHV main - initial commit                 0
1   01G6S5WJ4J6JHPSPK537G7PE63 01G6S5WJ4KVYVGCM9ZT0FAJZ09 2022-06-29T19:08:52.37PDT  01G6S5VPJG1QVK53NKVAX77MHV commita                               1
2   01G6S5WJV6J9BE0ERZCHT7S183 01G6S5WJV7QEN8V778FJ5CM3K3 2022-06-29T19:08:53.094PDT 01G6S5VPJG1QVK53NKVAX77MHV commmitb                              2
3   01G6S5WK96TB0KZW1JS30YZ4WN 01G6S5WK97H4DVHEV2D6DHJK6H 2022-06-29T19:08:53.542PDT 01G6S5VPJG1QVK53NKVAX77MHV commit csv                            3
4   01G6S5WKKQY4YPTWA7JAWPBTJX 01G6S5WKKRABE0RTCA1VBTTVV7 2022-06-29T19:08:53.879PDT 01G6S5VPJG1QVK53NKVAX77MHV commit csv                            3
5   01G6S5WM9FM3R47PM149YTYHZ6 01G6S5WM9G8PSXAS05AC74EYBR 2022-06-29T19:08:54.575PDT 01G6S5VPJG1QVK53NKVAX77MHV commit with metadata                  11
6   01G6S5WMMWWN8VSRP7BRYTQP79 01G6S5WMMX1XJXBM3C2VBA3DZ9 2022-06-29T19:08:54.94PDT  01G6S5VPJG1QVK53NKVAX77MHV clobber                               1
7   01G6S5X8XNT8H5D3Y9XASCSGCC 01G6S5X8XP5C80ZV3EGEVT7FPV 2022-06-29T19:09:15.701PDT 01G6S5VPJG1QVK53NKVAX77MHV into main                             1
...
```

You'll notice in the output here something unique to the branch `main`: the
Parent Branch ID and Parent Commit ID are set to "None". `Main` is the only
branch that does not "split off" from another branch (it is also the only
un-deletable branch).

If you look at another branch...

```shell
$ pd branch show bravo
Repository:    MyRepository
Display Name:  main
Name:          main
Branch ID:     01G6S5VPJG1QVK53NKVAX77MHV
Version:       01G7QNRGH3TBG9RR3MFFS1JY7F
Created:       2022-06-29T19:08:24.144PDT
Last Updated:  2022-07-11T15:23:29.827PDT
Parent Branch: 01G6S5VPJG1QVK53NKVAX77MHV
Parent Commit: 01G6S5WMMWWN8VSRP7BRYTQP79
Commits:       None
Tags:          none
```
... you will see the that the Parent Branch ID points the branch from which
this branch was created (in this case `main`) as well as the commit.

Branches are versioned and append only, and they all contain a reference to the
branch and commit from which they were created. This becomes especially
important when talking about commit verification, as it is these reference that
the verification process follows back to the root of the repository.

### Deleting and Restoring a Branch

Deletion of a branch, and restoration of a deleted branch works the same as
deletion/restoration for any other metadata entity within Provenant Data:

```shell
$ pd branch delete alpha --comment 'goodbye'
Are you sure you want to delete branch alpha? [y/n] y
Branch alpha deleted
```

Branch `alpha` is now unavailable. It's still in the repository, but it is
marked deleted and unavailable for normal use. To get it back:

```shell
$ pd branch restore alpha -c x
Are you sure you want to restore branch alpha? [y/n] y
Branch alpha restored
```

Branch `alpha` is now available again. 

### Checkout

There is one operation that can be performed on a branch that doesn't change
the branch itself, but instead mutates the state of the workspace/session. `pd
branch checkout <branch_name>` makes `<branch_name>` the active branch in the
user's current workspace:

```shell
$ pd status
Repository:     MyRepository
User:           default
Workspace ID:   01G7QNPJYXTXN019BDV0TVMN78
Worksapce Name: 01G7QNPJYXTXN019BDV0TVMN78
URL:            file://localhost:8000
Branch:         main       # <-- currently on branch main
Last Commit:    01G7QNRGH135H2FNCNAWR6M1X7, commit message one
Dataset Size:   1
Origin Repos:   1
                01G6S5VPGWYAZ4B70ZJ2NNN907 (this repo)

$ pd branch checkout alpha # <-- Check out alpha

$ pd status
Repository:     MyRepository
User:           default
Workspace ID:   01G7QNPJYXTXN019BDV0TVMN78
Worksapce Name: 01G7QNPJYXTXN019BDV0TVMN78
URL:            file://localhost:8000
Branch:         alpha      # <-- now on branch alpha
Last Commit:    01G7QNRGH135H2FNCNAWR6M1X7, commit message one
Dataset Size:   1
Origin Repos:   1
                01G6S5VPGWYAZ4B70ZJ2NNN907 (this repo)
```

Now that brange `alpha` is the checked out branch, it becomes the target for
any commits that are made.

#### Checking Out a Specific Commit

When checking out a branch, we are actually checking out a branch and a commit.
Both the branch and the commit are captured as state in our
[workspace](/docs/guide/workspaces). The checked out branch becomes the default
target for any subsequent commits that we make, and the checked out commit
populates the Active Dataset of our workspace.

If a commit is not specified when checking out, the last commit on the branch
will be used. To use a specific commit, specify it as an argument:

```shell
pd branch checkout main --commit 01G7DDZKH7RCKVGFKC10FN0P39
```

### Ingest

There is an exception to that, however. When adding data to a repository via
`pd add` or composing a dataset using the dataset composition commands, any
commits made in that process will target the currently checked out branch.
However, often time you, and especially when working with automated processes,
you just want to ingest and commit into a specific branch without interactively
checking it out.

For those cases, the `pd branch ingest` command aggregates the actions involved
as a convenience.

```shell
$ pd branch ingest main --files ~/some/test/data.json --message 'automated ingest' --metadata-file ./some/test/metadata1.json
Ingest
Ingest ID:        01G7QPXBWPDRTDA9HCERACTDN3
Version:          01G7QPXCH1MGAJ3NN32XF2Y8P0
Created:          2022-07-11T15:43:37.494PDT
Last Updated:     2022-07-11T15:43:38.145PDT
Ingested Records: 500
New Records:      0
Metadata ID:      01G6S5WKVMJQJRR1HWRB64B54Y
Tags:             none

Commit
Ingest ID:    01G7QPXCKSR78WCYH9BB4CEHF1
Version:      01G7QPXCKVPAHJH1ZEZS7YGNND
Created:      2022-07-11T15:43:38.233PDT
Last Updated: 2022-07-11T15:43:38.235PDT
Branch:       main
Message:      automated ingest
Dataset Size: 500
Origin Repos: 1
              01G6S5VPGWYAZ4B70ZJ2NNN907 (this repo)
Tags:         none
```

`pd ingest` provides a shortcut for one of the most often used actions: ingest
a chunk of data into a specific branch, and commit it there.

