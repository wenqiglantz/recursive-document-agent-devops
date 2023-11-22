## pd product deprecate

deprecate a given release of <productname> at <version>

### Synopsis

Marks version <version> of product <productname> as deprecated.
Deprecating a release prevents that release from being retrieved.
<message>, if provided, will be delivered to all users who have access
permissions to the product. If not message is given here, the users will
receive a generic "release deprecated" message

```
pd product deprecate <productname> <version> [flags]
```

### Options

```
  -h, --help             help for deprecate
  -m, --message string   Release deprecation message
```

### Options inherited from parent commands

```
      --json          Print output as JSON
      --json-pretty   Pretty print output as JSON
```

### SEE ALSO

* [pd product](/docs/commands/pd_product.html)	 - Commands to manipulate products

###### Auto generated by spf13/cobra on 25-Aug-2022