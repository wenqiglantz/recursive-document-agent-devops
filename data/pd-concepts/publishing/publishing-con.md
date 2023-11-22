# Concepts / Publishing

### Summary

The purpose of Provenant Data is to provide a platform to manage the
publication and monetization of datasets. To that end, PD allows the creation
of _Data Products_. Conceptually, a Data Product, like other types of products,
is a solution that addresses specific business needs. This might be the
publication of data products only to systems internal to an enterprise.  Or,
this product may be a commercial offering  designed for specific markets or a
specific customer. PD's data management tools focus on making the composition
of datasets intuitive and efficient, allowing a single wellhead of data to feed
a pipeline that may produce a wide array of Data Products.

The core PD concepts that make this possible are the aforementioned _Products_,
_Releases_ of those Products, and _Licenses_ which may be attached to the
Products. Let's review these in that order.

### Product

Within PD, a **Product** is a lightweight entity that identifies a distinct
data product. It wraps together the data involved, specific releases of that
data collection, and the use license associated with that data, along with a
mechanism for providing entitlement and access.

### Releases

A **Release** of a product is directly analogous to a release of a software
product. There is a version number, a mechanism to deprecate the release, a
license associated with the release (which may be the same license associated
with the Product). In the case of a PD Data Product, there is also, of course,
a reference to the dataset that comprises the release.

Releases also have a messaging capability: a user of, or subscriber to, a
product can be notified when new releases are made, and, critically, when a
release has been deprecated or superseded. Deprecation status is also surfaced
in audit and compliance. In concert, these mechanisms ensure that users of the
Data Product are never using out-of-date nor out-of-compliance data.

### Licenses

In PD, a **License** is simply a document, or reference to a document, that is
associated with one or more products or releases. It has a name, a description,
and content. The association is permanent between a license and the data to
which it applies, and is apparent not only when accessing the product or
release, but also when the underlying datasets are under audit.
