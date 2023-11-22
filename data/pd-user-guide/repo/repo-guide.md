# Guide / Repository

A Provenant Data Repository is an instance of the Provenant Data platform. It
can run locally on your filesystem, or it can be accessed as a services.

### Running a Local Instance

The PD CLI binary contains everything you need to create and run a PD
repository. See the [CLI quick start](/docs/quickstart/qs_cli) to download the CLI
and get started using it.

#### Initializing a Repository

In order to create a new, local repository, use `pd repo init`. See the [manual
entry](/docs/commands/pd_repo_init.html) for details on using the command.

Initializing a repository does a number of things. 

1. It creates a `.pd` directory in the location specified by the `pd repo init`
   command, 
2. Within that directory, it creates a simple default configuration file (named
   `config`).
3. Also within that directory, it creates a database to hold the repository
   data (named `pd.db`).
4. Creates a default administrator account (named `default`) for initial access.

The repository is now available for login. See the [CLI quick
start](/docs/quickstart/qs_cli.html), or the [login manual](/docs/commands/pd_login.html) for more
information.

Every repository has a name, and a repository ID. The repository ID is a
universally unique identifier that becomes embedded in data (and metadata)
associated with this repository. To see your repository ID, use the `pd repo
id` [command](/docs/commands/pd_repo_id.html).

#### Running as a Service

Initializing and accessing the repository as outlined above is constrained to
local access. If you need to remotely access the repository, you will need to
run it as a service. Running the PD repo as a service starts a gRPC interface.

See the `pd repo serve` [command](/docs/commands/pd_repo_serve.html) for details on
starting the services. 

### Accessing a Provenant Data Repository Service

Access to a locally-hosted PD repository through the CLI is straightforward. 
The [CLI quick start](/docs/quickstart/qs_cli) offers guidance on this. 

#### gRPC API

Running the PD repository as a service exposes the PD gRPC API. This API allows
programmatic access to the repository using any language that supports gRPC.
See the [API reference](/docs/api/) for guidance on using the API.

#### REST API

The PD repository service may optionally expose a REST API that offers the same
capabilities as the gRPC API (except, of course, as REST). See the `--gw` option to
the `pd repo serve` [command for details](/docs/commands/pd_repo_serve.html).

### Using Docker

See the [Docker quick start](/docs/quickstart/qs_docker) for instructions on using
the PD Docker image.

### See Also

See the CLI reference for more information on using [pd repo](/docs/commands/pd_repo.html).
