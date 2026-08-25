# fromSendableValuesBucket

## Modules to Import

```TypeScript
import { sendableRelationalStore } from 'kits/@kit.ArkData';
```

## fromSendableValuesBucket

```TypeScript
function fromSendableValuesBucket(valuesBucket: ValuesBucket): NonSendableBucket
```

Converts a KV pair that can be passed across threads into the data that cannot be passed across threads.

**Since:** 12

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [valuesBucket](../../apis-ability-kit/arkts-apis/arkts-ability-dataabilityoperation-dataabilityoperation-i.md) | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NonSendableBucket](arkts-arkdata-sendablerelationalstore-nonsendablebucket-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
