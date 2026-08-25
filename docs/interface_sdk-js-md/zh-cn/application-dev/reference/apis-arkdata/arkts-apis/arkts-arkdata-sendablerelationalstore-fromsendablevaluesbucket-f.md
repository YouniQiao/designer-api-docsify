# fromSendableValuesBucket

## 导入模块

```TypeScript
import { sendableRelationalStore } from 'kits/@kit.ArkData';
```

## fromSendableValuesBucket

```TypeScript
function fromSendableValuesBucket(valuesBucket: ValuesBucket): NonSendableBucket
```

将可用于跨线程传递的键值对数据，转换为不能用于跨线程传递的键值对数据。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [valuesBucket](../../apis-ability-kit/arkts-apis/arkts-ability-dataabilityoperation-dataabilityoperation-i.md) | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [NonSendableBucket](arkts-arkdata-sendablerelationalstore-nonsendablebucket-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
