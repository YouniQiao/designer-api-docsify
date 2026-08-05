# toSendableValues

## toSendableValues

```TypeScript
function toSendableValues(values: NonSendableValues): collections.Array<ValueType>
```

Converts the array data that cannot be passed across threads into the data that can be passed across threads.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-sendableRelationalStore-function toSendableValues(values: NonSendableValues): collections.Array<ValueType>--><!--Device-sendableRelationalStore-function toSendableValues(values: NonSendableValues): collections.Array<ValueType>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| values | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Array data that cannot be passed across threads. |

**Return value:**

| Type | Description |
| --- | --- |
| collections.Array&lt;ValueType&gt; | Array data that can be passed across threads. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-parameter-check-failed) | Inner error. |

**Example**

```TypeScript
import { relationalStore, sendableRelationalStore } from '@kit.ArkData';
const array: relationalStore.ValueType[] = [];
array.push(1);
array.push(2);
array.push("aaaaaa")
const values = sendableRelationalStore.toSendableValues(array);
```

