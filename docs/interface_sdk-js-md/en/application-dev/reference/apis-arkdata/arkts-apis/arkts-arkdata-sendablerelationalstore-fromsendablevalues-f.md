# fromSendableValues

## Modules to Import

```TypeScript
import { sendableRelationalStore } from 'kits/@kit.ArkData';
```

## fromSendableValues

```TypeScript
function fromSendableValues(values: collections.Array<ValueType>): NonSendableValues
```

Converts the array data that can be passed across threads into the data that cannot be passed across threads.

**Since:** 20

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | collections.Array & lt;ValueType & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NonSendableValues](arkts-arkdata-sendablerelationalstore-nonsendablevalues-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
