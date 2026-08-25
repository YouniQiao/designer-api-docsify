# fromSendableAsset

## 导入模块

```TypeScript
import { sendableRelationalStore } from 'kits/@kit.ArkData';
```

## fromSendableAsset

```TypeScript
function fromSendableAsset(asset: Asset): NonSendableAsset
```

将可跨线程传递的附件数据，转换为不可跨线程传递的附件数据。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [asset](../../apis-asset-store-kit/arkts-apis/arkts-security-asset.md) | [Asset](arkts-arkdata-sendablerelationalstore-asset-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [NonSendableAsset](arkts-arkdata-sendablerelationalstore-nonsendableasset-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
