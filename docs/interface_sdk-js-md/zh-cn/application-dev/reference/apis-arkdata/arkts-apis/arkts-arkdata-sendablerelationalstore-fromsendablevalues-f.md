# fromSendableValues

## 导入模块

```TypeScript
import { sendableRelationalStore } from '@kit.ArkData';
```

## fromSendableValues

```TypeScript
function fromSendableValues(values: collections.Array<ValueType>): NonSendableValues
```

将可跨线程传递的数组数据，转换为不可跨线程传递的数组数据。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| values | collections.Array & lt;ValueType & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [NonSendableValues](arkts-arkdata-sendablerelationalstore-nonsendablevalues-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |

**示例**

```TypeScript
import { sendableRelationalStore } from '@kit.ArkData';
import { collections } from '@kit.ArkTS';
const array = new collections.Array<sendableRelationalStore.ValueType>();
array.push("a");
array.push("b");
array.push(1);
array.push(2);
const values = sendableRelationalStore.fromSendableValues(array);
```
