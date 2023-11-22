---
date: 2022-05-21T11:21:55-07:00
title: "Default Policy Input"
---

Default policy input provided by the platform is evolving. At present it is limited to the following:

* Username of the user making the request
* User groups configured in the repository
* The [ClientSpec](/api/common) provided in the request.

Data is provided as a simple JSON object. An example follows:

```json
{ "user": "default",
  "groups": [
      {
        "Name": "admin",
        "ID": "01G6S5VPJG1QVK53NKVVGKSKWB",
        "Deleted": false,
        "Hash": "9defb65e821292a1040bb124bf8173a3f28e09f5da62ff886bd712f2ff8079f022a364a9fea4fb4e9941e402912a612190b5f42cb7551d8c55dc81dee18e7902",
        "Immortal": false,
        "RID": "01G6S5VPGWYAZ4B70ZJ2NNN907",
        "Tags": [],
        "Type": {
          "Name": "group"
        },
        "Version": "01G6S5VPM14A6WFQ6X0Q391377",
        "VersionComment": "",
        "Description": "",
        "Members": [
          "01G6S5VPM0WZN9CSF8XRHZD09D"
        ]
      },
      {
        "Name": "user",
        "ID": "01G6S5VPJHP1QR70RT7R3VBHY0",
        "Deleted": false,
        "Hash": "20d1aea12d170253839df90e72e2f12ff2d07e49091ee1a1a6bf970511ace15d55361b03fbb2c9b616eb3342da8aebe6ca8399f11a805c55807808760c3beac4",
        "Immortal": false,
        "RID": "01G6S5VPGWYAZ4B70ZJ2NNN907",
        "Tags": [],
        "Type": {
          "Name": "group"
        },
        "Version": "01G6S5X3KGFCZN3JX17V2S8HF9",
        "VersionComment": "",
        "Description": "",
        "Members": [
          "01G6S5X38XHYHPGQDHFKABKZ0E",
          "01G6S5X3FNP80K0S2JDZF6HCXY",
          "01G6S5X3KFNFEA4QRAWCZE6715"
        ]
      },
      {
        "Name": "group_a",
        "ID": "01G6S5X6WJHAC6A385B9TJS1ER",
        "Deleted": false,
        "Hash": "1206a66fe60538263de4126effe6cf0ab20a9f1446781f0ee3103ee350a99a130deb36882d5944b45ba1ea117bb72a7b1b25a3f3a628a0ed0f6d42801b3dee0e",
        "Immortal": false,
        "RID": "01G6S5VPGWYAZ4B70ZJ2NNN907",
        "Tags": [],
        "Type": {
          "Name": "group"
        },
        "Version": "01G6VCJN924980Y2H9413XTVNM",
        "VersionComment": "",
        "Description": "group a",
        "Members": []
      },
      {
        "Name": "group_b",
        "ID": "01G6S5X70E2VR7XEZAM02S4X30",
        "Deleted": false,
        "Hash": "84fc4b346d7405d977b0d4e3a3e88fbeb0aca9dae03a487f44a62702aa1bcb5401a9a920a15c0d021cbfc3756406fe298734aee590cff8b0e3e093b151ca7db5",
        "Immortal": false,
        "RID": "01G6S5VPGWYAZ4B70ZJ2NNN907",
        "Tags": [],
        "Type": {
          "Name": "group"
        },
        "Version": "01G6S5X84ZR5ATE085WKCTSTK2",
        "VersionComment": "",
        "Description": "group b",
        "Members": [
          "01G6S5X3FNP80K0S2JDZF6HCXY"
        ]
      }
    ],
  "clientspec": {
      "QueryID": "01G78P4YT7XT9WWAC18X6QFK94",
      "QueryPeers": false,
      "QueriedNodes": null,
      "HopCount": 0,
      "RepoName": "x",
      "RepoID": "01G6S5VPGWYAZ4B70ZJ2NNN907",
      "APIAction": {
        "Name": "",
        "Aggregate": false,
        "Parent": "",
        "DefaultAdmin": false
      },
      "Path": "/Users/xyz/provenantdata/.pd",
      "SessionID": "01G78P20J03FMZ2T7CWGV8EZHG",
      "Token": "<redacted>",
      "Username": "default",
      "URL": {
        "Scheme": "https",
        "Opaque": "",
        "User": null,
        "Host": "localhost:8000",
        "Path": "",
        "RawPath": "",
        "ForceQuery": false,
        "RawQuery": "",
        "Fragment": "",
        "RawFragment": ""
      },
      "Name": "pd_prototype_cli",
      "Version": "0.0.0",
      "Branch": "",
      "Hash": "",
      "OS": "darwin",
      "Hostname": "xyz.local",
      "UserAgent": "",
      "Address": "",
      "Timestamp": "2022-07-05T19:41:41.19131-07:00",
      "Args": "/var/folders/rf/4qb1fdx10m39z4_gs_0gk6dc0000gn/T/go-build988974764/b001/exe/main status"
    }
  }
}
```
