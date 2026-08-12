# ResultSet

Provides APIs to access the result set obtained by querying the RDB store. This result set is the collection of results returned with the **query()** method called.

The **ResultSet** instance is not refreshed in real time. After using the result set, if the data in the database is changed (by being added, deleted, or modified), you need to query the result set again to obtain the latest data.

For the following APIs, you should use either [query](arkts-arkdata-relationalstore-rdbstore-i.md#query),  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querySqlWithoutRowCount),  
[remoteQuery](arkts-arkdata-relationalstore-rdbstore-i.md#remoteQuery), or [queryLockedRow](arkts-arkdata-relationalstore-rdbstore-i.md#queryLockedRow) to obtain the  
**ResultSet** instance first, and then use this instance to call the corresponding method.

**Since:** 9

<!--Device-relationalStore-interface ResultSet--><!--Device-relationalStore-interface ResultSet-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from '@kit.ArkData';
```

## getFloat32Array

```TypeScript
getFloat32Array(columnIndex: number): Float32Array
```

Obtains the value of the specified column in the current row as a float array.The implementation class determines whether to throw an exception if the value of the specified column in the current row is null or the specified column is not of the float array type.

**Since:** 12

<!--Device-ResultSet-getFloat32Array(columnIndex: int): Float32Array--><!--Device-ResultSet-getFloat32Array(columnIndex: int): Float32Array-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Float32Array |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [14800032](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800013](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |
