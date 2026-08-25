# getRdbStoreSync

## Modules to Import

```TypeScript
import { relationalStore } from '@kit.ArkData';
```

## getRdbStoreSync

```TypeScript
function getRdbStoreSync(context: Context, config: StoreConfig): RdbStore
```

Obtains a RDB store. You can set parameters of the RDB store as required. This is a synchronous method that blocks the thread until the RDB store is obtained.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| config | [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbStore](arkts-arkdata-relationalstore-rdbstore-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800010](../errorcode-data-rdb.md#14800010-invalid-database-path) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14801001](../errorcode-data-rdb.md#14801001-stage-model-required) |
| [14801002](../errorcode-data-rdb.md#14801002-invalid-datagroupid-in-storeconfig) |
| [14800017](../errorcode-data-rdb.md#14800017-key-configuration-changed) |
| [14800020](../errorcode-data-rdb.md#14800020-key-damaged-or-lost) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |
