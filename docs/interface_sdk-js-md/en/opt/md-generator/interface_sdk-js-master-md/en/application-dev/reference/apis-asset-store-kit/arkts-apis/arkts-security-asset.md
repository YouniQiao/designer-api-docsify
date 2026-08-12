# @ohos.security.asset

This module provides the capabilities for life cycle management of sensitive user data (Asset) such as passwords and tokens, including adding, removing, updating, and querying.

**Since:** 11

<!--Device-unnamed-declare namespace asset--><!--Device-unnamed-declare namespace asset-End-->

**System capability:** SystemCapability.Security.Asset

## Modules to Import

```TypeScript
import { asset } from '@kit.AssetStoreKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [add](arkts-assetstore-asset-add-f.md#add) |
| [addSync](arkts-assetstore-asset-addsync-f.md#addsync) |
| [batchAdd](arkts-assetstore-asset-batchadd-f.md#batchadd) |
| [batchRemove](arkts-assetstore-asset-batchremove-f.md#batchremove) |
| [batchUpdate](arkts-assetstore-asset-batchupdate-f.md#batchupdate) |
| [postQuery](arkts-assetstore-asset-postquery-f.md#postquery) |
| [postQuerySync](arkts-assetstore-asset-postquerysync-f.md#postquerysync) |
| [preQuery](arkts-assetstore-asset-prequery-f.md#prequery) |
| [preQuerySync](arkts-assetstore-asset-prequerysync-f.md#prequerysync) |
| [query](arkts-assetstore-asset-query-f.md#query) |
| [querySync](arkts-assetstore-asset-querysync-f.md#querysync) |
| [querySyncResult](arkts-assetstore-asset-querysyncresult-f.md#querysyncresult) |
| [remove](arkts-assetstore-asset-remove-f.md#remove) |
| [removeSync](arkts-assetstore-asset-removesync-f.md#removesync) |
| [update](arkts-assetstore-asset-update-f.md#update) |
| [updateSync](arkts-assetstore-asset-updatesync-f.md#updatesync) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAsUser](arkts-assetstore-asset-addasuser-f-sys.md#addasuser) |
| [postQueryAsUser](arkts-assetstore-asset-postqueryasuser-f-sys.md#postqueryasuser) |
| [preQueryAsUser](arkts-assetstore-asset-prequeryasuser-f-sys.md#prequeryasuser) |
| [queryAsUser](arkts-assetstore-asset-queryasuser-f-sys.md#queryasuser) |
| [removeAsUser](arkts-assetstore-asset-removeasuser-f-sys.md#removeasuser) |
| [updateAsUser](arkts-assetstore-asset-updateasuser-f-sys.md#updateasuser) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BatchErrInfo](arkts-assetstore-asset-batcherrinfo-i.md) |
| [BatchResult](arkts-assetstore-asset-batchresult-i.md) |
| [SyncResult](arkts-assetstore-asset-syncresult-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Accessibility](arkts-assetstore-asset-accessibility-e.md) |
| [AuthType](arkts-assetstore-asset-authtype-e.md) |
| [ConflictResolution](arkts-assetstore-asset-conflictresolution-e.md) |
| [ErrorCode](arkts-assetstore-asset-errorcode-e.md) |
| [OperationType](arkts-assetstore-asset-operationtype-e.md) |
| [ReturnType](arkts-assetstore-asset-returntype-e.md) |
| [SyncType](arkts-assetstore-asset-synctype-e.md) |
| [Tag](arkts-assetstore-asset-tag-e.md) |
| [TagType](arkts-assetstore-asset-tagtype-e.md) |
| [WrapType](arkts-assetstore-asset-wraptype-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuthType](arkts-assetstore-asset-authtype-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AssetMap](arkts-assetstore-asset-assetmap-t.md) |
| [Value](arkts-assetstore-asset-value-t.md) |
