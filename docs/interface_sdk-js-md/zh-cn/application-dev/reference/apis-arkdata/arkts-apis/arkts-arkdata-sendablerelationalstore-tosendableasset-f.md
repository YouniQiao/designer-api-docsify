# toSendableAsset

## 导入模块

```TypeScript
import { sendableRelationalStore } from 'kits/@kit.ArkData';
```

## toSendableAsset

```TypeScript
function toSendableAsset(asset: NonSendableAsset): Asset
```

将不可跨线程传递的附件数据，转换为可跨线程传递的附件数据。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [asset](../../apis-asset-store-kit/arkts-apis/arkts-security-asset.md) | [NonSendableAsset](arkts-arkdata-sendablerelationalstore-nonsendableasset-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Asset](arkts-arkdata-sendablerelationalstore-asset-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
