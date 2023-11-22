# Guide / Users and Groups

### Users

Users are exactly as you would expect: named users, with a password and some
other minor attributes, that are able to log into the Provenant Data platform,
and work with it.

An administrative user (a user in the group "admin" (covered in more detail
below)) can create users, enable and disable them, and delete and restore them.

#### Enabling and Disabling Users

Management of users is similar to the management of most other PD entities: you
can list them, show details for a specific user, show all versiosn of a user
entity for a specific user, delete them (mark them as deleted) and restore
them. There is one addition operation that can be performed on users that
cannot be performed on other PD entities: enabling and disabling. 

Disabling a user prevents that user from logging in and, therefore, from
interacting with the platform in any way. From the impacted user's perspectieve
it is identical to being delted: The account no longer functions. However, to
other users there are some slight differences. Deleted users don't show in the
listing of all users (unless specifically requested), whilc disabled users do,
by default, show in that listing. Likewise, one cannot see the details (`pd
user show ...`) for a deleted user, while they can for disabled user.

Enabling/Disabling exists primarily to satisfy User Account Management (UAM)
processes that make a distinction between disabling and deleting (IE forbidding
or resticting the occaisions when a user account may be deleted). Even though
in PD user entities are append only, and the versions are immutable, this minor
distinction may prove useful when integrating with a UAM process.

#### User Ownership of Entities

At present, repositories do not track the "ownership" of entities within the
repository. That is, user "A" may make a branch "my_branch", but "my_branch"
carries no metadata that states "A" is the owner, or that limits other users'
access to the branch. The repository is viewed more as a common creative area
where restrictions in behavior and data access should be driven on the one hand
by development culture and convention, and on the other, by codification into
the Policy Engine, customized for each installation.

Entity ownership may be added in the future, but it will still very likely
depend on the Policy Engine, and the implementation of policies by the
repository owner, for restrictions.

See the [CLI documentation](/docs/commands/pd_user.html) for details on creating,
inspecting and modifying users from the command line.

### Groups

Users may be placed into groups, so that they may be managed in aggregate. At
present, this serves two purposes within PD.

1. In order to access a Product, and the releases of the Product, a user must
   be assigned to a group which has been explicitly permitted to access the
   Product.
2. Group membership of the user executing an API call is available to all
   Policy Engine decisions, and provides a simple way to implement Roles-Based
   Access control (RBAC) at the policy layer.

At repository initialization, there are two groups pre-defined.: The `admin`
group, and the `user` group. All users are members of the `user` group. The
only salient difference between the two groups, is that certain API calls are
restricted to members of the `admin` group by the default policies. This very
simple seperation serves as a sane and clear starting point for a more
sophisticated policy implementation, customized to the needs of the
organization.

See the [CLI documentation](/docs/commands/pd_group.html) for details on creating,
inspecting  and modifying groups from the command line.

### The "default" User

Every repository begins with one user, a user named "default". This user is in
the `admin` group, and cannot be deleted. It is recommended to change this
user's password immediately after repository initialization, and to create
other user accounts in the `admin` group for day-to-day administration of the
repository.
