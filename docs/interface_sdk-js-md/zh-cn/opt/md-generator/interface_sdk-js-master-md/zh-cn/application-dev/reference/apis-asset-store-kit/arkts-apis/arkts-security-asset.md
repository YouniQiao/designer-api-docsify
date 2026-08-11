# @ohos.security.asset

关键资产存储服务提供了用户短敏感数据的安全存储及管理能力。其中，短敏感数据可以是密码类（账号/密码）、Token类（应用凭据）、其他关键明文（如银行卡号）等长度较短的用户敏感数据。

**起始版本：** 11

<!--Device-unnamed-declare namespace asset--><!--Device-unnamed-declare namespace asset-End-->

**系统能力：** SystemCapability.Security.Asset

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
| --- |
| [addAsUser](arkts-assetstore-asset-addasuser-f-sys.md#addasuser) |
| [postQueryAsUser](arkts-assetstore-asset-postqueryasuser-f-sys.md#postqueryasuser) |
| [preQueryAsUser](arkts-assetstore-asset-prequeryasuser-f-sys.md#prequeryasuser) |
| [queryAsUser](arkts-assetstore-asset-queryasuser-f-sys.md#queryasuser) |
| [removeAsUser](arkts-assetstore-asset-removeasuser-f-sys.md#removeasuser) |
| [updateAsUser](arkts-assetstore-asset-updateasuser-f-sys.md#updateasuser) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [BatchErrInfo](arkts-assetstore-asset-batcherrinfo-i.md) |
| [BatchResult](arkts-assetstore-asset-batchresult-i.md) |
| [SyncResult](arkts-assetstore-asset-syncresult-i.md) |

### 枚举

| 名称 |
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
### 枚举（系统接口）

| 名称 |
| --- |
| [AuthType](arkts-assetstore-asset-authtype-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [AssetMap](arkts-assetstore-asset-assetmap-t.md) |
| [Value](arkts-assetstore-asset-value-t.md) |
