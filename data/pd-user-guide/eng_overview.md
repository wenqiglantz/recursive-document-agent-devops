# Introduction

When we talk about the architecture and design of PD, we need to talk
specifically about both the prototype and the eventual production deployment,
as are some significant differences. 

# Prototype

## Distribution

The prototype is distributed as both Docker images and as executable binaries.
There are three flavors of Docker images:

* An image that supports Intel/AMD Docker environments
* An image that supports ARM Docker environments
* An Intel/AMD-only image that includes support for Foundation DB (see
  [Production Deployment](#production-deployment) below).

The available binaries mirror the Docker images, except that the first two
flavors support both Linux And Darwin (Mac) operating systems

* Two binaries for Intel/AMD: one for Linux, one for Darwin
* Two binaries for ARM: one for Linux, one for Darwin
* A single Linux- and Intel/AMD-only binary that includes support for
  Foundation DB.

For testing and demonstration purposes Intel/AMD images and binaries should be
strongly preferred. FoundationDB support is not intended for use in a test or
demonstration environment.

## Application

The PD application is a single, "monolithic" executable. The single executable
is used as both the service and as the client.

Services are exposed via a gRPC API. All services are hosted within the single
executable. Functionality is organized as follows:

* Audit Service: Audit and compliance.
* Distribution Service: Dataset Distribution.
* Ingest Service: Ingest of data into a repository.
* Login/Auth Service: Authentication.
* Metadata Service: Data-about-the-datasets: Branches, commits, tags, etc.
* Peer Service: Manages the Data Mesh and relationships within the mesh.
* Policy Service: Interaction with the PD Policy Engine.
* Retrieval Service: Delivery of datasets to users and consumers.
* User Service: User and group management.

See the [API documentation](/docs/api) for details on what each service
provides.

These services roughly align with major subsystems within PD. Two subsystems
deserve special mention:

### The Policy Engine 

The Policy Engine mediates all API calls. That is, each API call has at least
one policy associated with it that may allow or prevent the API call from
succeeding, or may determine that data "crossing" the API should be validated
or modified in some way.

The Policy Engine uses [Open Policy Agent](https://www.openpolicyagent.org/)
(OPA) for flexible, declarative control. 

Please see the [policy concept](/docs/concepts/policy) documentation or the
[policy guide](/docs/guide/policy) for more details on the Policy Engine.

#### Plugins

PD Policies may call customer-supplied plugins. Plugins are programs written by
users or repository administrators that may conditionally be executed depending
on the context and content of an API call. One particularly powerful use of a
plugin is to modify data en passant, that is, dependent upon some condition, to
modify the data within a dataset on ingress or egress. 

Plugins may be written in any language that supports the gRPC interface, but
the repository administrator needs to ensure that the appropriate execution
environment exists to support the plugin. EG, when writing a Python plugin,
Python of the appropriate version, with all required modules would need to
exist within the environment where the plugin is executing.

Please see [plugin concept](/docs/concepts/plugins) documentation or the [plugin
guide](/docs/guide/plugins)

### The Data Mesh  

A Data Mesh is an affiliation or federation of PD Repositories. Access to the
mesh is, from the viewpoint of the user, seamless. They need only choose to use
the mesh, and their interactions with the mesh (IE data returned from
repositories within the mesh) require no further thought or action. Most
services offer some functionality that can interact with a Mesh; The Peer and
Distribution services (and of course the Policy Engine) largely manage
interactions between repositories within a Mesh.

Access to a remote repository (IE a repository to which the user does not have
direct access) is dependent upon the relationship between the repositories on
the mesh and the policies established by the respective repository
owners/administrators. 

Repositories on the mesh need not directly connected to one another:

```shell

RepoA <--> RepoB <--> RepoC

```

In the above, Repos A and B are connected to each other as peers, and Repos B
and C are connected to each other as peers. A user of Repo A may query the mesh
and receive an answer from Repo C, even though they are only indirectly
connected.

Meshes may be established without undue concern for the mesh topology. The Data
Mesh query proxy process has loop avoidance built-in. Mesh-enabled queries are,
by default, delivered to all members of the mesh, who then respond.
Mesh-enabled queries may also be directed to only specific member nodes of the
mesh.

Please see the [data mesh concept](/docs/concepts/mesh) documentation or [data
mesh guide](/docs/guide/mesh) for more details on a Data Mesh.

## Storage

For the prototype a single, embedded storage engine is available. When creating
a repository with the executable, a folder name `.pd` will be created in the
current working directory by default (the directory specified on the command
line). This directory will hold a configuration file, and the database, name
`pd.db`. 

Only a single process may access this database at a given time. 

## User Interface

To access a running repository, you may use the web interface or the CLI. The
CLI currently supports all functionality, while the web interface supports most
but not all of the PD functionality. Specifically missing from the web
interface is support for querying meshes. This will be added shortly.

### Web UI

When you follow either the [CLI quickstart](/docs/quickstart/qs_cli.html) or
the [Docker quickstart](/docs/quickstart/qs_docker.html) the web interface will
be available at [https://localhost:9001](https://localhost:9001). Note that the
certificate shipped with the prototype is self-signed, and you will have to
follow your browser prompts as necessary. 

### CLI

The same binary that was used to start PD as a service functions as your CLI
client. If you are running PD via Docker and wish to connect to PD via the
command line, you will need to download the binary appropriate for your
Operating System and architecture.

CLI help is available via `pd --help`, or [in the CLI
reference](/docs/commands/pd.html)

Login credentials are as stated in the [quickstart
guide](/docks/quickstart/qs_cli.html).

## API 

Virtually all functionality of the PD platform is exposed via the gRPC API. 
Please see the [API documentation](/docs/api) for guidance and examples.

There also exists a REST API which is a direct transliteration of the gRPC API.
The gRPC should be strongly preferred in all cases, and the REST API is
provided on an experimental basis only. See the
[documentation](/docs/api#rest-api) for more details.

# Production Deployment

In a production deployment of PD, where the PD is offered as a service to the
users, there are only a few, but significant changes in deployment and storage. 

## Distribution

Only the Linux variants, and specifically the Intel/AMD versions of the
software will be supported for running the service.

Client or end-user access via the CLI may still be possible with the Darwin and
ARM versions.

## Deployment

The application scales horizontally, so any number of application instances may
be deployed and load balanced. 

Two different deployment methodologies are envisioned: containerized or more
traditional.

In the containerized deployment, the PD application and storage layers both run
as Kubernetes deployments. 

In the more traditional deployment, the PD application is deployed to _n_
virtual (or physical) hosts behind a load balancer. Likewise, the storage layer
is deployed to virtual (or physical) hosts.

It should be noted that the Web UI may be run separately from the rest of the
PD application, so the familiar three-tier architecture is easily supported.

## Storage

The storage layer in a production deployment requires
[FoundationDB](https://www.foundationdb.org/). FoundationDB (FDB) can be both
extremely performant and scalable. Indeed, some of the performance requires
scale: a small FDB installation often lacks both performance and sufficient
redundancy in case of instance failure.

Caching for the storage tier is done as a distributed cache co-resident with
and managed by each application instance. 
