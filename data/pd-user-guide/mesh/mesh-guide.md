A "Data Mesh" is a federation of repositories that allows friction-free access
to the resources of the member repositories for users of any member
repository. To a user, the only difference between an interaction with their
repository, and an interaction with the mesh, is an additional flag that says
"please execute this everywhere". Results are rolled-up and returned to the
user. There is no additional configuration, authentication or red tape
involved.

### Peers

To establish a Data Mesh, two repositories must be introduced to one another as peers.

```shell
$ pd peer create peer_user@another_repo.example.org
Enter Password:
peer created
```

`peer create` creates a uni-directional relationship between the primary repo and
the target (the peer). Users of the primary repo may now query the mesh, and will
be able to receive responses from the peer (`another_repo` in the example
above). The reverse is not true. Users of the peer do not (yet) have Mesh
access to the primary repo. For the peer relationship needs to be reciprocated,
before it can be a full mesh:

```shell
(on "another_repo.example.org")
$ pd peer create peer_user@primary_repo.example.org
Enter Password:
peer created
```

When creating peers a username and password are required. These are for a user
_on the peer_. All users on the primary repo will access the peer as the user
specified in the `pd peer create` command. It is recommended that for each peer
relationship, a user specific to that purpose be created on each repository.

See the CLI reference for more information on using [pd
peer](/docs/commands/pd_peer.html)

### Peers Serve as Proxies

Peers serve, essentially, as proxies to the rest of the Mesh. Observe the
diagram below, which has three repositories, Alpha, Bravo and Charlie, with
mutual peer relationships between Alpha and Bravo, and between Bravo and
Charlie, but _not_ between Alpha and Charlie.

```
 Alpha◄────►Bravo◄────►Charlie
```

Users of repository Alpha still have access to the data on Charlie, even though
they do not have a direct peer relationship. In this case repository Bravo
serves as "transit", transparently proxying requests to Charlie on behalf of
Alpha.

It is important to note that, though Bravo is acting as an intermediary,
Charlie still has access to the query origin in each request. This assures that
the owner of repository Charlie can craft policies that will address any access
restrictions or logging that they need with precision.

This model of "transit" extends to any  size or configuration mesh. Even in
mesh configurations that may have multiple natural loops...

```
     ┌────────►One◄────────┐
     │          ▲          │
     │          │          │
     ▼          ▼          ▼
 Primary◄─────►Two◄──────►Four
     ▲          ▲          ▲
     │          │          │
     │          ▼          │
     └────────►Three◄──────┘
```

...query loops and excessive querying is avoided through a simple in-band
protocol.

### Data Transfer within a Mesh

In many instances, there is little need to transfer data between repositories
on a Mesh, as that data should be available to the entire mesh no matter where
it resides.

However, when data must be copied, this is supported through `pd peer push` and
`pd peer pull`. Branches, Commits, Products and Releases may be pushed and pulled. 
However, there is a subtlety: The primary objects to be transfered are the
_dataset_ underlying these constructs, and the commit or commits that
references the dataset. The branch itself (or product or release) is not transferred, but
a new branch is established on the target, stating its origin as coming from a
push or a pull, and the datasets involved are plugged into that branch as a
commit or as a series of commits.

Due to the way datasets and commits are organized in the repository, moving
them in this manner allows for continual provenance, and supports cryptographic
commit verification even after transver.

See the CLI reference for more information on using the [pd peer
push](/docs/commands/pd_peer_push.html) and [pd peer pull](/docs/commands/pd_peer_pull.html)
commands.

### Policy Mediation of Mesh Access

The [Policy Engine](/docs/guide/policy) provides the mechanism to fine tune the
rules for access and interaction to repositories within a mesh. Each query, as
it traverses the mesh, retains the originating user and repository. These may
be used to create unequal access patterns on an otherwise open mesh.

Every API call that comes in across a mesh is the same API call as if it were
submitted directly to the repository. There is little to no additional
complexity in querying a mesh, nor in controlling access to your repository
when it is on a mesh. Simply write policies that codify your rules and
conditions, and the Policy Engine will enforce them.

### Mesh-Enabled Functionality

Not all functionality of a PD repository makes sense to be executed against a
mesh. An ingest for example should be limited to the repository to which the
user is connected. There are a number of capabilities that are mesh-enabled by
default:

#### Audit

Auditing files from the command line, and recalling a specific Audit Report ID
will work against a mesh. When submitting files for audit, each node will
generate its own audit report (and audit report ID), and the results will be
delivered to the caller keyed by repository name. That is, if you execute an
audit against a mesh of three nodes, you'll get three audit reports. 

#### License

Listing all licenses, showing a specific named license or showing all versions
of a specific named license works against a mesh.

#### Peers

Listing all peers within the mesh, or showing specific peers within the mesh
(and showing versions of that peer definition) is supported.

#### Branch

Listing all branches within the mesh, or a finding/showing a specific named
branch works within a mesh.

#### Repository information

Repo information from each of the repositories participating in a mesh may be
retrieved.

#### Product

Listing all products, showing a specific product and showing versions of a
specific product within a mesh all work. If there are two or more products in a
mesh with the same name, a "product show" will return both. 

#### Retrieve

Retrieval of commits and product releases are supported, with a couple of caveats:

First, Commits are unique to a repo. So retrieving a commit ID can therefore
only return from a single repository.

Second, From the CLI a bare "pd retrieve" against a mesh may not work as
expected, as this retrieves the current session's active dataset. Sessions are
specific to repo instances, and the user only has a session on the repository
to which they are connected, so retrieval of a session's content from a
repository on which you do not have a session makes little sense.

#### Commit

Showing a commit, including a preview of the records, is enabled on a mesh. 

#### Tags

Showing a tag and receiving results from each node on the mesh is possible.
Some objects that may be tagged may not be retrieved via a mesh, for example,
Users. So even if a user on a peer is tagged with the tag in question, that
result will not be returned to the caller.

### CLI Access

To interact with a mesh, commands that are mesh-capable have a `--mesh` flag.
If this flag is present, the command will be distributed to all nodes on the
mesh, and modulo policy, the results will be collected, collated and returned.
