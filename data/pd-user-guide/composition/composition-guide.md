# Guide / Dataset Composition

Provenant Data supports the construction of datasets via composition using
simple operators.

* [add](/docs/commands/pd_workspace_add.html) / union
* [intersect](/docs/commands/pd_workspace_intersect.html)
* [remove](/docs/commands/pd_workspace_remove.html) / difference

These operators are applied to one or more datasets, and result in a new
datasets. The operators behave much like basic operators you're familiar with
from set theory.

Dataset operations in PD are highly scalable, and don't depend directly on the
number of records involved. Operations performed on a larger datasets (millions
of records or more) are roughly the same complexity as the same operations
performed on small (ten or fewer records) datasets, and take roughly the same
amount of time.

### Add

Adding two or more datasets together results in a dataset that contains all the
records contained within the original datasets. Duplicate records (records
contained in more than one input dataset) are represented once in the new
dataset.

Dataset A

```json
{"a":1}
```

Dataset B

```json
{"b":2}
```


Dataset C

```json
{"c":3}
```

If we add these three datasets together, the resulting dataset will contain all
three records:

Dataset A + B + C

```json
{"a":1}
{"b":2}
{"c":3}
```

### Intersect

Finding the intersection between two or more datasets results in a dataset that
contains only the records in common between the input datasets.

Dataset A

```json
{"a":1}
{"c":3}
```

Dataset B

```json
{"b":2}
{"c":3}
```

Dataset A ∩ B

```json
{"c":3}
```

If there are no records in common, the resulting dataset is empty.

### Remove

Removing a dataset from another dataset is likewise intuitive: The records in
the second operand (subtrahend) are removed from the first (minuend). Unlike
`add` and `intersect`, `remove` is not commutative.

Dataset A

```json
{"a":1}
{"b":2}
{"c":3}
```

Dataset B

```json
{"a":1}
```

Dataset A - B

```json
{"b":2}
{"c":3}
```

### The Dataset Composition CLI Commands

The dataset composition CLI commands are subcommands of `pd workspace`, but
because to make them easier to work with, they may be access without reference
to the workspace command (IE as `pd add ...`, `pd intersect ...`, and `pd
remove ...`). The resulting dataset from any of these operations is stored in
your workspace active dataset.

Each of these commands can take files, commit IDs or ingest IDs as datasets
operands. More than one type may be provided; EG you may `pd add` a file to an
existing commit:

```shell
pd add --files ~/path/to/files/example.json \
  --commit 01G4E6NQ5JEHTT7DJQXBHXSTG0
```

And more than one dataset of each type may be provided:

```shell
pd add --files ~/path/to/files/example.json \
   --files ~/path/to/files/example2.json    \
   --commit 01G4E6NQ5JEHTT7DJQXBHXSTG0      \
   --commit 01G4GSD4MXDA41N52HGXKD664Z
```

### See Also

See the CLI reference for more information on using
[add](/docs/commands/pd_workspace_add.html),
[intersect](/docs/commands/pd_workspace_intersect.html), and
[remove](/docs/commands/pd_workspace_remove.html)
