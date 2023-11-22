# Concepts / Mesh

### Summary

In the PD universe, a **Data Mesh** is a federation of repositories...
Repositories that maintain data-sharing relationships between them. For a user,
interacting with the mesh of repositories is transparent: The user's
interaction, query or API call is seamlessly relayed to every node in the mesh,
even nodes that are not directly connected to one another.

Access to the repositories, to API calls on the repositories and to the data
within the repositories is governed by the policies established on that
repository. Each repository owner can tune their policies as appropriate. Each
repository owner maintains complete control of their data, and insight into its
usage.

### Peers, and the Mesh

A peer relationship is a connection between two repositories. If we want to
make `Repo_B` a peer of `Repo_A`, we create a peer entity on `Repo_A` that has
specific login credentials to `Repo_B`.

A subset of API calls may be proxied by the repo to one or more peers. For
example, a retrieve API call may attempt to retrieve not only from the primary
repository (the primary to which the user is authenticated), but also from the
peer or peers.

Peers may have peers of their own, in arbitrary configuration including
reciprocal peerings.

This network of peers proxying API calls to other peers is called a mesh.

Those API calls which are mesh-enabled may be executed recursively against the
mesh. The mesh may be an arbitrary topology.

The user does not need to know the topology, nor the names, locations, or
connection details of the nodes within the mesh. They simply execute a
mesh-enabled API call or CLI command and receive the appropriate output.

Likewise the user doesn't need a personal account on each repository in the
mesh, nor do they need to maintain credentials, connection information, etc. on
those meshed repos.


### Copying Data Within a Mesh

In many instances, there is little need to transfer data between repositories
on a mesh, as that data should be available by means of an API call to the
entire mesh no matter where it resides. Occasionally however, it makes sense
first to compose or construct a dataset within one repository, and then
productize and publish it on another. Alternatively, a publisher will release a
data product on their repository and a subscriber or consumer of that product
will retrieve it to their own repository in order to work with it locally.

In those cases, when the underlying data is transferred, we may do this by
pushing to, or pulling from, a peer. When pushing or pulling, only the records
and metadata that are not already present in the target repository are
transmitted, and, crucially, the metadata related to the _origin_ of the data
within the dataset travels with the data. In this way, data may be copied
between repositories, but the origin and provenance of the data is stable,
secure, and consistent no matter where it is accessed.

### Meshes are Governed by Policy

The [Policy Engine](/docs/concepts/policy) mediates all aspects of the Data Mesh.
Repository owners use policies to define how the other repositories of the Mesh
will interact with their Repository. There is no Data Mesh-wide configuration:
it is a true federation of repositories.

In that way, Repository owners and publisher may retain command over their
data, while the traditional data-silos are broken down, and barriers to
collaboration are removed.

### Mesh-Enabled Functionality

Not all functionality of a PD repository is appropriate for execution against a
mesh. An ingest, for example, should be limited to the repository to which the
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

Retrieval of commits and product releases are supported, with a couple of
caveats:

First, Commits are unique to a repo. So retrieving a commit ID can therefore
only return from a single repository.

Second, from the CLI a bare "pd retrieve" against a mesh may not work as
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
