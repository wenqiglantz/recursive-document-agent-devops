# Guide / Workspaces

A Workspace is a _session_; it holds your work-in-progress, and manages your
command history. When you compose a dataset out of other datasets (commits,
ingests, etc) that data-in-flight needs a place to be recorded and persisted,
and this is the purpose of the workspace. Each time you log into Provenant
Data, if you do not specifically request to resume an existing workspace a new
one is created for you.

Workspace operations can be divided broadly into two categories: 

1) Management of the workspace
2) Manipulation of state, and specifically the dataset contained in the workspace

### Workspace Management

Workspaces behave like most other entities in PD, meaning that you can list
them, show details about them, inspect the versions of a workspace, as well as
delete and restore.

```shell
$ pd workspace show
Name:               01G7Q1QTKH9KY9S2YG9XDCW9AJ
Workspace ID:       01G7Q1QTKH9KY9S2YG9XDCW9AJ
Version:            01G7Q8CY82951PWTNY9HEW4686
Created:            2022-07-11T09:33:35.857PDT
Last Updated:       2022-07-11T11:29:59.17PDT
Branch:             main
Commit ID:          01G7Q8CY7SARCHFWP1C6RK2CA3
Last Accessed From: Scotts-iMac.local
Dataset Size:       514
Origin Repos:       1
                    01G6S5VPGWYAZ4B70ZJ2NNN907 (this repo)

Tags: none
```

`pd workspace show` is shorthand for `pd workspace show
<name_of_current_workspace>`. Because we work with workspaces quite
frequently, there are a few other convenient shorthands. You may, for example,
shorten `pd workspace` to `pd ws` to save just a bit of typing.

```shell
$ pd ws list 
   Name                       ID                         Version                    Created                    Updated                    Records
0  01G6S5VRF6V2FAPNY8RESQJ254 01G6S5VRF6V2FAPNY8RESQJ254 01G6S5VRF77AYZ70P6DAGF6TN9 2022-06-29T19:08:26.086PDT 2022-06-29T19:08:26.087PDT 0
1  01G6S5W79Q2DPBRQ2601K9WB9C 01G6S5W79Q2DPBRQ2601K9WB9C 01G6S5Y4F1CM11CEKZFF7J8S41 2022-06-29T19:08:41.271PDT 2022-06-29T19:09:43.905PDT 2
2  session_one                01G6S5Y5KASBZKY0S2RF7SFBY7 01G7DDGY98MB14W9S7V6HXNF51 2022-06-29T19:09:45.066PDT 2022-07-07T15:47:08.84PDT  0
3  session_two                01G6S5Y68W5XJV44NTQBPNXVXP 01G6VCJZSC3SPCC88J30VK6B2W 2022-06-29T19:09:45.756PDT 2022-06-30T15:44:27.564PDT 0
4  01G6S5Y6FMR5MGB0GFJZN9EQXD 01G6S5Y6FMR5MGB0GFJZN9EQXD 01G6S5Y905ZJHWX20BJDE4S3VK 2022-06-29T19:09:45.972PDT 2022-06-29T19:09:48.549PDT 1
5  01G6S5YA1T35MMRNX7GMJ6WXKQ 01G6S5YA1T35MMRNX7GMJ6WXKQ 01G6S5YG15PZS8V0AXBTH0N719 2022-06-29T19:09:49.626PDT 2022-06-29T19:09:55.749PDT 14
6  01G6S5YVW9C23AV5JPH8KQFM9X 01G6S5YVW9C23AV5JPH8KQFM9X 01G6S69GZF292PR6K0TBD6PM7J 2022-06-29T19:10:07.881PDT 2022-06-29T19:15:57.167PDT 500
7  01G6S75814N9PHDVPGV3QZTAAY 01G6S75814N9PHDVPGV3QZTAAY 01G6S7583GRED9BPZBFKVXZ02R 2022-06-29T19:31:05.508PDT 2022-06-29T19:31:05.584PDT 0
8  01G6S88WJR4WKFTFMC31SYS4NW 01G6S88WJR4WKFTFMC31SYS4NW 01G6S88WN3K2PSE36SHS4ADVVY 2022-06-29T19:50:33.432PDT 2022-06-29T19:50:33.507PDT 0
...
```

The management commands that are unique to workspaces are `rename`, `resume`
and `history`.

#### Rename

You can see from the output above that the name of the session, unless we
change it, is the same as the workspace ID. `pd workspace rename`, as you might
expect, renames the session to something a bit more digestable:

```shell
$ pd workspace show
Name:               01G7QRWZ7GWDWRPQYQ5V0AZ53A
Workspace ID:       01G7QRWZ7GWDWRPQYQ5V0AZ53A
Version:            01G7QRWZA2KYS42C1629QB13GS
Created:            2022-07-11T16:18:21.68PDT
Last Updated:       2022-07-11T16:18:21.762PDT
Branch:             main
Commit ID:          01G7QQM8X9GTQFY7ZQEFGJ3TPH
Last Accessed From: Scotts-iMac.local
Tags:               none

$ pd workspace rename my_favorite_session
Renamed workspace my_favorite_session, ID 01G7QRWZ7GWDWRPQYQ5V0AZ53A

$ pd workspace show
Name:               my_favorite_session
Workspace ID:       01G7QRWZ7GWDWRPQYQ5V0AZ53A
Version:            01G7QRWZA2KYS42C1629QB13GS
Created:            2022-07-11T16:18:21.68PDT
Last Updated:       2022-07-11T16:18:21.762PDT
Branch:             main
Commit ID:          01G7QQM8X9GTQFY7ZQEFGJ3TPH
Last Accessed From: Scotts-iMac.local
Tags:               none
```

#### Resume

Now that you have a named session, if you log out and log back in, you may wish
to resume it. 

```shell
$ pd workspace resume my_favorite_session
Resumed workspace my_favorite_session, ID 01G7DDHBCC0VJ1QKCKE0GWN0EK
```

The state of your workspace 'my_favorite_session' is made active, and you may
continue the work you were engaged in previously.

#### History

As workspaces mutate, each step in that process is saved as an entry in the
Workspace's history. 

```shell
$ pd ws history
Current Session ID 01G7DDHBCC0VJ1QKCKE0GWN0EK
0: 01G7DDHBF31DDXG46WZV6E65JD SessionCreated. No active dataset
1: 01G7DDHP99PDEWTKJBFJ8Y7SQH SessionActivated. No active dataset
2: 01G7DDZ9K9YHJD4TEECQ60R61W DataIngested. 2 records in active dataset
3: 01G7DDZ9KY95BNTWKR0AXFKQY5 DataComposed. 2 records in active dataset
4: 01G7DDZKHHF7K7B774RQX2MBD1 CommitCreated. 2 records in active dataset
```

The history above is the result of the following sequence of actions:

1. Logging in creates entries 0 and 1
2. Using `pd add...` to ingest a file creates entries 2 and 3 (`pd add`-ing a
   file is an ingest for the file, and a composition command to add it to the
   active workspace).
3. `pd commit...` creates entry 4.

The workspace history allows us to return the Active Dataset to any prior
point. For example, the workspace above has 2 records in the active dataset. If
we wish to return to point in the history where there were _no_ records in the
Active Dataset, we simply promote the entry:

```shell
$ pd workspace history

Current Session ID 01G7Q1QTKH9KY9S2YG9XDCW9AJ
0: 01G7Q1QTP1Z6C8E28H2VFQR7NH SessionCreated. No active dataset
1: 01G7Q1TQC1V1CYYDH62C45MTN8 DataIngested. 2 records in active dataset
2: 01G7Q1TQCN7BS6R56BJZG63HAF DataComposed. 2 records in active dataset
3: 01G7Q36S5K91397X7G39HXDS3Z DataIngested. 2 records in active dataset
4: 01G7Q36S68BRTH67SSWW5Z4FJE DataComposed. 2 records in active dataset

$ pd workspace history --promote 0
workspace version 0 promoted

$ pd workspace history

Current Session ID 01G7Q1QTKH9KY9S2YG9XDCW9AJ
0: 01G7Q1QTP1Z6C8E28H2VFQR7NH SessionCreated. No active dataset
1: 01G7Q1TQC1V1CYYDH62C45MTN8 DataIngested. 2 records in active dataset
2: 01G7Q1TQCN7BS6R56BJZG63HAF DataComposed. 2 records in active dataset
3: 01G7Q36S5K91397X7G39HXDS3Z DataIngested. 2 records in active dataset
4: 01G7Q36S68BRTH67SSWW5Z4FJE DataComposed. 2 records in active dataset
5: 01G7Q37VBZ00KV4HVZ33AWKNH6 SessionActivated. No active dataset
```

We can see that there is a new entry appended to the history, one that contains
no records in its active dataset, just as there were no records in the active
dataset at the point we chose to promote (entry 0).

### Active Dataset and State

Workspaces are a mechanism to capture and manage _state_. As such there are
three major aspects of state that are reflected in the output of `pd workspace
show`:

```shell
$ pd workspace show
Name:               01G7Q1QTKH9KY9S2YG9XDCW9AJ
Workspace ID:       01G7Q1QTKH9KY9S2YG9XDCW9AJ
Version:            01G7Q8CY82951PWTNY9HEW4686
Created:            2022-07-11T09:33:35.857PDT
Last Updated:       2022-07-11T11:29:59.17PDT
Branch:             main
Commit ID:          01G7Q8CY7SARCHFWP1C6RK2CA3
Last Accessed From: Scotts-iMac.local
Dataset Size:       514
Origin Repos:       1
                    01G6S5VPGWYAZ4B70ZJ2NNN907 (this repo)

Tags: none
```

1. Branch: This is the name of the currently checked out branch. Any commits
   make in this workspace/session will be made in this branch.
2. Commit ID: this is the ID of the checked out commit. If we check out a
   branch without specifying the Commit ID the last commit on the branch will
   be selected. When we check out a commit, it pre-populates our Workspace's
   Active Dataset with the contents of that commit. It's convenient to think of
   this as the "last saved checkpoint" when working with datasets.
3. The Dataset: This is the dataset-in-flight. When ingesting data, adding
   data, composing a new dataset out of existing commits and ingests, the
   product of those operations exists in the Active Dataset. 

Each time a change is introduced to the Active Dataset a new entry is made in
the workspace's history. Changes are introduced:

1. when [using dataset composition commands](/docs/guide/composition)
2. when manipulating workspace history.
3. when checking out a branch and/or commit

### Workspace Shorthand

We've already seen that `pd workspace...` may be shortened to `pd ws...`.
As manipulation of the workspace is central to PD workflows, in the CLI
tools, commands which are _properly_ subcommands of `pd workspace` (meaning
that the are functions that manipulate the workspace) are aliased to more
genralized versions to help work flow more smoothly.

For example, `pd add` is an alias of `pd workspace add`, as are all compsition
commands. And an unadorned `pd retrieve` retrieves the workspace's Active
Dataset.

### See Also

See the [CLI reference](/docscommands/pd_workspace.html) for more information on using
workspaces.
