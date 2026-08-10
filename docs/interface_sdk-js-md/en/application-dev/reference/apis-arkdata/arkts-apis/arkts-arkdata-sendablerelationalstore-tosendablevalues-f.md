# toSendableValues

## Modules to Import

```TypeScript
import { sendableRelationalStore } from 'kits/@kit.ArkData';
```

## toSendableValues

```TypeScript
function toSendableValues(values: NonSendableValues): collections.Array<ValueType>
```

将不可跨线程传递的数组数据，转换为可跨线程传递的数组数据。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-sendableRelationalStore-function toSendableValues(values: NonSendableValues): collections.Array<ValueType>--><!--Device-sendableRelationalStore-function toSendableValues(values: NonSendableValues): collections.Array<ValueType>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| values | [NonSendableValues](arkts-arkdata-sendablerelationalstore-nonsendablevalues-t.md) | Yes | 不可跨线程传递的数组数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| collections.Array&lt;ValueType&gt; | 可跨线程传递的数组数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800000 | Inner error. |

## Examples

```TypeScript
import { relationalStore, sendableRelationalStore } from '@kit.ArkData';
const array: relationalStore.ValueType[] = [];
array.push(1);
array.push(2);
array.push("aaaaaa")
const values = sendableRelationalStore.toSendableValues(array);
```

