# getQuerySqlInfo

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## getQuerySqlInfo

```TypeScript
function getQuerySqlInfo(predicates: RdbPredicates, columns?: Array<string>):SqlInfo
```

Obtains the SQL statement used to query data. This API returns the result synchronously.

**Since:** 20

<!--Device-relationalStore-function getQuerySqlInfo(predicates: RdbPredicates, columns?: Array<string>):SqlInfo--><!--Device-relationalStore-function getQuerySqlInfo(predicates: RdbPredicates, columns?: Array<string>):SqlInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | Yes |
| columns | Array&lt;string&gt; | No |

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
const predicates = new relationalStore.RdbPredicates("users");
predicates.notEqualTo("age", 18);
predicates.equalTo("name", "zhangsan");
const sqlInfo: relationalStore.SqlInfo = relationalStore.getQuerySqlInfo(predicates);
```
