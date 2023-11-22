# Aggregated API Calls and Policies

Some API calls are organized into aggregates: groupings of API calls that are
usually called together, and may be subject to a single policy. For example,
"Ingest" family of API calls consist of BeginIngest, FinishIngest, IngestFiles,
IngestRecords, ShowIngest, and so forth. Instead of updating a policy for each
of these, there is an aggregate policy `provenant.ingest` which applies on any
of those API calls. 

If a policy is put in place for any of the "leaf" API calls (EG
"FinishIngest"), the policy specific to "FinishIngest" will be used for that
API call, and the general "Ingest" policy will be used for the remainder.

# Admin-restricted API calls

Some API calls, by default, are restricted to members of the `admin` group. Those
are noted here.

# Default Policy List

* provenant.apiaccess: Runs on every API call, after authentication, but before any other policy is invoked. 
* provenant.ingest. Aggregates BeginIngest, FinishIngest, IngestFiles, IngestRecords, ShowIngest.
* provenant.retrieve. Aggregates BeginRetrieve, BeginRetrieveRaw, FinishRetrieve, Retrievechunk.
* provenant.audit. Aggregates AuditDataset, AuditFiles, AuditReport, BeginAUdit, FinishAudit.
* provenant.recorddelete. Aggregates DeleteRecords, ListDeletions, RestoreRecords. Restricted to Admin by default.
* provenant.activatesession
* provenant.addtag
* provenant.addusertogroup. Restricted to Admin by default.
* provenant.allowgroupaccesstoproduct
* provenant.applylicensetoproduct
* provenant.authtoken
* provenant.changepassword
* provenant.changepassworduser. Restricted to Admin by default.
* provenant.checkout
* provenant.commitintobranch
* provenant.compliancereport
* provenant.compose
* provenant.createbranch
* provenant.createcommit
* provenant.creategroup. Restricted to Admin by default.
* provenant.createlicense
* provenant.createplugin. Restricted to Admin by default.
* provenant.createpolicy. Restricted to Admin by default.
* provenant.createproduct
* provenant.createrepo
* provenant.createschema. Restricted to Admin by default.
* provenant.createsession
* provenant.createuser. Restricted to Admin by default.
* provenant.deletebranch
* provenant.deletelicense
* provenant.deletesession
* provenant.deleteuser. Restricted to Admin by default.
* provenant.deprecaterelease
* provenant.disablepolicy. Restricted to Admin by default.
* provenant.disableuser. Restricted to Admin by default.
* provenant.enablepolicy. Restricted to Admin by default.
* provenant.enableuser. Restricted to Admin by default.
* provenant.establishpeer. Restricted to Admin by default.
* provenant.getgroup
* provenant.getgroupversions
* provenant.getplugin
* provenant.getpluginversions
* provenant.getrelease
* provenant.getreleases
* provenant.getrepo
* provenant.getschema
* provenant.getschemaversions
* provenant.initializerepo
* provenant.listbranches
* provenant.listgroups
* provenant.listlicenses
* provenant.listplugins
* provenant.listpolicies
* provenant.listproducts
* provenant.listrepos
* provenant.listschema
* provenant.listsessions
* provenant.listtags
* provenant.listusers
* provenant.login
* provenant.meshrequest
* provenant.metadatasearch
* provenant.peercreate
* provenant.peerdelete
* provenant.peerget
* provenant.peergetversions
* provenant.peerundelete
* provenant.peerlist
* provenant.policyget
* provenant.policylist
* provenant.policyresettodefault. Restricted to Admin by default.
* provenant.policyupdate. Restricted to Admin by default.
* provenant.promotesessionversion
* provenant.pull
* provenant.pulldatasetinfo
* provenant.push
* provenant.refreshtoken
* provenant.releaseproduct
* provenant.removegroupaccesstoproduct
* provenant.removetag
* provenant.removeuserfromgroup. Restricted to Admin by default.
* provenant.renamesession
* provenant.repoid
* provenant.setperrecordplugin. Restricted to Admin by default.
* provenant.setrecordschemavalidator. Restricted to Admin by default.
* provenant.showbranch
* provenant.showbranchversions
* provenant.showcommit
* provenant.showcommitversions
* provenant.showlicense
* provenant.showlicenseatversion
* provenant.showlicenseversions
* provenant.showmetadata
* provenant.showpolicy
* provenant.showpolicyversions
* provenant.showproduct
* provenant.showproductversions
* provenant.showsession
* provenant.showsessionversions
* provenant.showtag
* provenant.showuser
* provenant.showmetadata
* provenant.showuserversions
* provenant.status
* provenant.undeletebranch
* provenant.undeletelicense
* provenant.undeleterecords
* provenant.undeletesession
* provenant.undeleteuser
* provenant.updatelicense
* provenant.updateplugin. Restricted to Admin by default.
* provenant.updateschema. Restricted to Admin by default.
* provenant.usermessages
* provenant.usermessagesmarkread
* provenant.verify


See the [API Reference](/docs/api) for more information on these API calls.

