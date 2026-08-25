# @ohos.security.asset

关键资产存储服务提供了用户短敏感数据的安全存储及管理能力。其中，短敏感数据可以是密码类（账号/密码）、Token类（应用凭据）、其他关键明文（如银行卡号）等长度较短的用户敏感数据。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**系统能力：** SystemCapability.Security.Asset

## 导入模块

```TypeScript
import { asset } from '@kit.AssetStoreKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [add](arkts-assetstore-asset-add-f.md) |
| [addSync](arkts-assetstore-asset-addsync-f.md) |
| [batchAdd](arkts-assetstore-asset-batchadd-f.md) |
| [batchRemove](arkts-assetstore-asset-batchremove-f.md) |
| [batchUpdate](arkts-assetstore-asset-batchupdate-f.md) |
| [postQuery](arkts-assetstore-asset-postquery-f.md) |
| [postQuerySync](arkts-assetstore-asset-postquerysync-f.md) |
| [preQuery](arkts-assetstore-asset-prequery-f.md) |
| [preQuerySync](arkts-assetstore-asset-prequerysync-f.md) |
| [query](arkts-assetstore-asset-query-f.md) |
| [querySync](arkts-assetstore-asset-querysync-f.md) |
| [querySyncResult](arkts-assetstore-asset-querysyncresult-f.md) |
| [remove](arkts-assetstore-asset-remove-f.md) |
| [removeSync](arkts-assetstore-asset-removesync-f.md) |
| [update](arkts-assetstore-asset-update-f.md) |
| [updateSync](arkts-assetstore-asset-updatesync-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addAsUser](arkts-assetstore-asset-addasuser-f-sys.md) |
| [postQueryAsUser](arkts-assetstore-asset-postqueryasuser-f-sys.md) |
| [preQueryAsUser](arkts-assetstore-asset-prequeryasuser-f-sys.md) |
| [queryAsUser](arkts-assetstore-asset-queryasuser-f-sys.md) |
| [removeAsUser](arkts-assetstore-asset-removeasuser-f-sys.md) |
| [updateAsUser](arkts-assetstore-asset-updateasuser-f-sys.md) |
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
