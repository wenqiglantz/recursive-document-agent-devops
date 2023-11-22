# Concepts / Policy Engine 

### Summary

All movement of data into or out of the PD platform, each view, change, update or discovery is mediated by policies. **Policies** are the primary tool for managing access to and use of the data within the platform. Policies give data publishers a powerful, easy-to-comprehend method to ensure that their data is accessed and used in accordance with their expectations and restrictions.

### The Policy Engine

At the heart of the Provenant Data platform is a flexible and comprehensive _Policy Engine_.

The first job of the policy engine is to evaluate each API call to determine if it is allowed or denied. The Policy Engine tests the context of the API call (who, what, where, when and why) against the rules established by the repository owner.

When the context contained within the repository or passed into the policy engine is not sufficient to satisfy the needs of the policy writer, any external system that can produce JSON can be used as additional context to feed into the policy. For example, if a user's access level is dependent upon an external data source, like LDAP, the policy can be configured to reach out to that system and incorporate the data returned in reaching an access decision.

The second job of the policy engine is to conditionally trigger custom [plugins](/concepts/plugins). Plugins are a powerful method to customize the behavior of the repository, and the presentation of data contained within the repository. Plugins are code, written by Provenant Data, the repository owner, or third parties, that can modify data en passant, as it moves into or out of the repository, and can interact with the repository, or with external systems, in whatever way is required by the repository owner. For example, a repository owner may want to redact sensitive data when viewed by a specific set of dataset subscribers, but not by others. Or the repository owner may want to update an internal dashboard each time a new branch is created. Policy-triggered plugins make the Provenant Data platform infinitely customizable.

