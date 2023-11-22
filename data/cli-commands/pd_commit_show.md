## pd commit show

display details for commit <commit_id>

### Synopsis

Displays details for commit <commit_id>. If --preview is specified,
shows a preview of the data in the commit. If --versions is specified, show
each version of the commit. --versions and --preview are mutually exclusive.

```
pd commit show <commit_id> [flags]
```

### Options

```
  -h, --help       help for show
      --mesh       Query all nodes in data mesh
  -p, --preview    Preview dataset; do not retieve the entire dataset
      --versions   Show all versions of commit
```

### Options inherited from parent commands

```
      --json          Print output as JSON
      --json-pretty   Pretty print output as JSON
```

### SEE ALSO

* [pd commit](/docs/commands/pd_commit.html)	 - Commands to manipulate commits

###### Auto generated by spf13/cobra on 25-Aug-2022