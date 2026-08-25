# toSendableValues

## Modules to Import

```TypeScript
import { sendableRelationalStore } from 'kits/@kit.ArkData';
```

## toSendableValues

```TypeScript
function toSendableValues(values: NonSendableValues): collections.Array<ValueType>
```

Converts the array data that cannot be passed across threads into the data that can be passed across threads.

**Since:** 20

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | [NonSendableValues](arkts-arkdata-sendablerelationalstore-nonsendablevalues-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| collections.Array & lt;ValueType & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
