## pd tag add

Add <tagname> --flags <names or ids>

### Synopsis

Add <tagname> to the specified objects. If the tag does not exist
it will be created. Flags may be repeated, or may be passed multiple values
separated by comma. Some flags take object names, others take only IDs.

```
pd tag add [flags]
```

### Examples

```
These two are equivalent:
pd add my_tag --branch main,other,feature
pd add my_tag --branch main --branch other --branch feature

Multiple objects may be tagged in a single invocation:
pd add my_tag --branch main,other,feature --commit 01FTXY1D4FQEN7STPBWY2J2T5Q

If a tag fails to apply to one of the objects, an error will be reported for
that object, and application will continue for the remaining objects.

```

### Options

```
      --branch strings    Branch names, separated by commas
      --commit strings    Commit IDs, separated by commas
      --group strings     Group names, separated by commas
  -h, --help              help for add
      --ingest strings    Ingest IDs, separated by commas
      --license strings   License names, separated by commas
      --plugin strings    Plugin names, separated by commas
      --policy strings    Policy names, separated by commas
      --product strings   Product names, separated by commas
      --release strings   Release IDs, separated by commas
      --session strings   Session names or IDs, separated by commas
      --user strings      User names, separated by commas
```

### Options inherited from parent commands

```
      --json          Print output as JSON
      --json-pretty   Pretty print output as JSON
```

### SEE ALSO

* [pd tag](/docs/commands/pd_tag.html)	 - Commands to manipulate tags

###### Auto generated by spf13/cobra on 25-Aug-2022