# Guide / Products

A "Product" is mechanism to group datasets that are to be published (as
[releases](/docs/guide/release)), an access control control or entitlement
mechanism, and a way to associate [licenses](/docs/guide/license) with published
datasets.

Products, releases, and licensing is the three-legged stool of dataset
publishing. They work together to effectively package a dataset for purchase,
or subscription, by customers.

### Creating a Product

A product is effectively a container used to manage datasets-as-releases and
licensing. Creation is similar to other entities within PD:

```shell
$ pd product create my_new_product
product created.

$ pd product show my_new_product
Repository:   MyRepository
Name:         my_new_product
Product ID:   01G7FGM8DR6AFVTA96C1FMPD6V
Version:      01G7MXENJG64E7V1X8R41NKV88
Created:      2022-07-08T11:19:52.12PDT
Last Updated: 2022-07-10T13:40:12.624PDT
License:      mit
License ID:   01G7FJP5FKPBPB3P612WPJW41M
Releases:     none
Tags:         none
```

### Restricting Access

Products provide a simple access control mechanism: only users within groups
specifically allowed access will be able to retrieve the Product's releases and
access the underlying data.

Assuming we've created a group named "subscribers", we'll add that group to the
product:

```shell
$ pd product allow subscribers my_new_product
group added to product.
```

At present, there is no way to delete a product, but you can remove all groups'
access, effectively removing the product from view:

```shell
$ pd product disallow subscribers my_new_product
group removed from product.
```

See the docuementation on [releases](/docs/guide/release) and
[licensing](/docs/guide/license) to add data to your product, and make it available
to your customers.
