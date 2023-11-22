# Guide / Tags

Tags are a convenient method for grouping disparate PD entities, or to give
nameless objects (like commits) a memorable handle.

Tags can be applied to many PD entities:

* branches
* commits
* groups
* ingests
* licenses
* policies
* plugins
* products
* releases
* sessions
* users

A tag can be applied to more than one object, and there are few restrictions on
the name of a tag. In the future, tags that are applied to a single object may
be used in place of that object for most commands. For example instead of `pd
commit retrieve some_commit_id` you should be able to `pd retrieve tag_name`.

### Add a Tag to an Entity

To add a tag to an entity, use the `pd tag add <tagname>` command. If the tag
does not already exist, it will be automatically created.

```shell
$ pd tag add my_tag --branch main
Tag my_tag set for 1 objects

$ pd tag add my_tag --commit 01G7B8QC2N90T816W01DHQ3FJ1
Tag my_tag set for 1 objects

$ pd tag show my_tag

Repository:   MyRepository
Name:         my_tag
Tag ID:       01G7BAXKPDY1MKN6PC32XDFE50
Version:      01G7QP3CSJ0TW4WKEPKAWPXD8A
Created:      2022-07-06T20:23:09.389PDT
Last Updated: 2022-07-11T15:29:26.45PDT
Branches:     1
              Name         ID                         Version                    Created                    Updated                    Commits Tags
0             main         01G6S5VPJG1QVK53NKVAX77MHV 01G7QQM8XBTPSFBJ7JJC8KA6HE 2022-06-29T19:08:24.144PDT 2022-07-11T15:56:08.107PDT 568     1
Commits:      1
              ID                         Version                    Created                    Branch ID                  Message                           Records
0             01G7B8QC2N90T816W01DHQ3FJ1 01G7BAYPQYHZS5QR645BNKVTT4 2022-07-06T19:44:47.829PDT 01G6S5VPJG1QVK53NKVAX77MHV the same fourteen example records 500
Groups:       none
Ingests:      none
Licenses:     none
Policies:     none
Plugins:      none
Products:     none
Releases:     none
Workspaces:   none
Users:        none
```

Multiple applications can be done in a single command by providing
comma-separated values and multiple flags. See [the command line
reference](/docs/commands/pd_tag_add.html) for details.

### Listing Existing Tags

Listing tags is must like listing any other object within PD:

```shell
$ pd tag list
  Name         ID                         Version                    Created                    Updated
0 my_tag       01G7BAXKPDY1MKN6PC32XDFE50 01G7QP3CSJ0TW4WKEPKAWPXD8A 2022-07-06T20:23:09.389PDT 2022-07-11T15:29:26.45PDT
1 my_other_tag 01G7K132CRSDVAC069QRV8QH6R 01G7K132CS2NFGETXBPGGC57NY 2022-07-09T20:05:17.976PDT 2022-07-09T20:05:17.977PDT
```

### Removing a Tag From an Object

Removing a tag from an object is identical to adding a tag, except instead of
using the argument "add", we use the argument "remove": 

```shell
$ pd tag remove test --branch main --commit 01FTY4N6TPJ7JK256GFJBDVP2D
```

See [the command line reference](/docs/commands/pd_tag_remove.html) for more details on
the usage of this command.
