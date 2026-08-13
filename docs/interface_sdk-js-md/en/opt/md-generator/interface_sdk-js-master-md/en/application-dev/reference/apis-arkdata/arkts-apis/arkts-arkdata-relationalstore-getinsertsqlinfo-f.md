# getInsertSqlInfo

## Modules to Import

```TypeScript
import { relationalStore } from '@kit.ArkData';
```

## getInsertSqlInfo

```TypeScript
function getInsertSqlInfo(table: string, values: ValuesBucket, conflict?: ConflictResolution):SqlInfo
```

Obtains the SQL statement used to insert data. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** -1

<!--Device-relationalStore-function getInsertSqlInfo(table: string, values: ValuesBucket, conflict?: ConflictResolution):SqlInfo--><!--Device-relationalStore-function getInsertSqlInfo(table: string, values: ValuesBucket, conflict?: ConflictResolution):SqlInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SqlInfo](arkts-arkdata-relationalstore-sqlinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |

## Examples

```TypeScript
const bucket: relationalStore.ValuesBucket = {
  name: "Logitech",
  age: 18,
  sex: "man",
  desc: "asserter"
};
const sqlInfo: relationalStore.SqlInfo = relationalStore.getInsertSqlInfo(
  "USER",
  bucket,
  relationalStore.ConflictResolution.ON_CONFLICT_NONE
);
```
