# ResultSet

Provides APIs to access the result set obtained by querying the RDB store. This result set is the collection of results returned with the **query()** method called.

The **ResultSet** instance is not refreshed in real time. After using the result set, if the data in the database is changed (by being added, deleted, or modified), you need to query the result set again to obtain the latest data.

For the following APIs, you should use either [query] [query](arkts-arkdata-relationalstore-rdbstore-i.md#query), [querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querysqlwithoutrowcount), [remoteQuery] [remoteQuery](arkts-arkdata-relationalstore-rdbstore-i.md#remotequery) , or [queryLockedRow](arkts-arkdata-relationalstore-rdbstore-i.md#querylockedrow) to obtain the **ResultSet** instance first, and then use this instance to call the corresponding method.

**Since:** 23

<!--Device-relationalStore-interface ResultSet--><!--Device-relationalStore-interface ResultSet-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from '@kit.ArkData';
```

## close

```TypeScript
close(): void
```

Closes this **resultSet** to release memory. If the **resultSet** is not closed, FD or memory leaks may occur.

**Since:** 23

<!--Device-ResultSet-close(): void--><!--Device-ResultSet-close(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).close().then(() => {
    console.info(`close succeeded`);
  }).catch((err: BusinessError) => {
    console.error(`close failed, code is ${err.code},message is ${err.message}`);
  });
}
```

```TypeScript
if (resultSet != undefined) {
  (resultSet as relationalStore.ResultSet).close();
}
```

```TypeScript
async function closeExample(store : relationalStore.RdbStore) {
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
    if (resultSet != undefined) {
      resultSet.close();
    }
  } catch (err) {
    console.error(`failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

## getAsset

```TypeScript
getAsset(columnIndex: int): Asset
```

Obtains the value from the specified column in the current row, and returns the value in the [Asset](arkts-arkdata-relationalstore-asset-i.md) format. If the type of the value in the column is **Asset**, the value of the Asset type is returned. If the value in the column is null, **null** is returned. If the value in the column is of other types, 14800000 is returned.

**Since:** 23

<!--Device-ResultSet-getAsset(columnIndex: int): Asset--><!--Device-ResultSet-getAsset(columnIndex: int): Asset-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | int | Yes | Index of the target column, starting from 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Asset | Value obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) | Column index is out of bounds. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error.<br>**Applicable version:** 12 and later |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds.<br>**Applicable version:** 12 and later |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed.<br>**Applicable version:** 12 and later |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
if (resultSet != undefined) {
  const doc = (resultSet as relationalStore.ResultSet).getAsset((resultSet as relationalStore.ResultSet).getColumnIndex("DOC"));
}
```

```TypeScript
async function getAssetExample(store : relationalStore.RdbStore) {
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
    if (resultSet != undefined) {
      resultSet.goToNextRow();
      const doc = resultSet.getAsset(resultSet.getColumnIndex("DOC"));
    }
  } catch (err) {
    console.error(`failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

## getAssets

```TypeScript
getAssets(columnIndex: int): Assets
```

Obtains the value from the specified column in the current row, and returns the value in the [Assets](arkts-arkdata-relationalstore-assets-t.md) format. If the type of the value in the column is **Assets**, the value of the Assets type is returned. If the value in the column is null, **null** is returned. If the value in the column is of other types, 14800000 is returned.

**Since:** 23

<!--Device-ResultSet-getAssets(columnIndex: int): Assets--><!--Device-ResultSet-getAssets(columnIndex: int): Assets-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | int | Yes | Index of the target column, starting from 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Assets | Value obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) | Column index is out of bounds. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error.<br>**Applicable version:** 12 and later |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds.<br>**Applicable version:** 12 and later |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed.<br>**Applicable version:** 12 and later |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
if (resultSet != undefined) {
  const docs = (resultSet as relationalStore.ResultSet).getAssets((resultSet as relationalStore.ResultSet).getColumnIndex("DOCS"));
}
```

```TypeScript
async function getAssetsExample(store : relationalStore.RdbStore) {
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
    if (resultSet != undefined) {
      resultSet.goToNextRow();
      const name = resultSet.getAssets(resultSet.getColumnIndex("DOCS"));
    }
  } catch (err) {
    console.error(`failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

## getBlob

```TypeScript
getBlob(columnIndex: int): Uint8Array
```

Obtains the value from the specified column in the current row, and returns it in a byte array.

If the type of the value in the specified column is INTEGER, DOUBLE, TEXT, or BLOB, the value will be converted into a byte array and returned. If the column is null/empty, an empty byte array will be returned. If the value is of any other type, 14800000 will be returned.

**Since:** 23

<!--Device-ResultSet-getBlob(columnIndex: int): Uint8Array--><!--Device-ResultSet-getBlob(columnIndex: int): Uint8Array-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | int | Yes | Index of the target column, starting from 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | Value obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) | Column index is out of bounds. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error.<br>**Applicable version:** 12 and later |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds.<br>**Applicable version:** 12 and later |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed.<br>**Applicable version:** 12 and later |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
if (resultSet != undefined) {
  const codes = (resultSet as relationalStore.ResultSet).getBlob((resultSet as relationalStore.ResultSet).getColumnIndex("CODES"));
}
```

```TypeScript
async function getBlobExample(store : relationalStore.RdbStore) {
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
    if (resultSet != undefined) {
      resultSet.goToNextRow();
      const name = resultSet.getBlob(resultSet.getColumnIndex("CODES"));
    }
  } catch (err) {
    console.error(`failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

## getColumnIndex

```TypeScript
getColumnIndex(columnName: string): int
```

Obtains the column index based on the column name.

**Since:** 23

<!--Device-ResultSet-getColumnIndex(columnName: string): int--><!--Device-ResultSet-getColumnIndex(columnName: string): int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnName | string | Yes | Column name. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Column index obtained. If the result set contains duplicate column names, the return value is not as expected. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) | Column index is out of bounds. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error.<br>**Applicable version:** 12 and later |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed.<br>**Applicable version:** 12 and later |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) | The SQL must be a query statement.<br>**Applicable version:** 12 and later |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
if (resultSet != undefined) {
  const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
  const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
  const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
  const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
}
```

```TypeScript
async function getColumnIndexExample(store : relationalStore.RdbStore){
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
    if (resultSet != undefined) {
      const idIndex = resultSet.getColumnIndex("ID");
      const nameIndex = resultSet.getColumnIndex("NAME");
      const ageIndex = resultSet.getColumnIndex("AGE");
      const salaryIndex = resultSet.getColumnIndex("SALARY");
    }
  } catch (err) {
    console.error(`failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

## getColumnName

```TypeScript
getColumnName(columnIndex: int): string
```

Obtains the column name based on the column index.

**Since:** 23

<!--Device-ResultSet-getColumnName(columnIndex: int): string--><!--Device-ResultSet-getColumnName(columnIndex: int): string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | int | Yes | Column index. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Column name obtained. If the result set contains duplicate column names, the return value is not as expected. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) | Column index is out of bounds. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error.<br>**Applicable version:** 12 and later |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed.<br>**Applicable version:** 12 and later |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) | The SQL must be a query statement.<br>**Applicable version:** 12 and later |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
if (resultSet != undefined) {
  const id = (resultSet as relationalStore.ResultSet).getColumnName(0);
  const name = (resultSet as relationalStore.ResultSet).getColumnName(1);
  const age = (resultSet as relationalStore.ResultSet).getColumnName(2);
}
```

```TypeScript
async function getColumnNameExample(store : relationalStore.RdbStore){
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
    if (resultSet != undefined) {
      const id = resultSet.getColumnName(0);
      const name = resultSet.getColumnName(1);
      const age = resultSet.getColumnName(2);
      const salary = resultSet.getColumnName(3);
    }
  } catch (err) {
    console.error(`failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

## getColumnNames

```TypeScript
getColumnNames(): Array<string>
```

Obtains the names of all columns in the result set.

The column names are returned in a string array. The sequence of strings in the array is the same as that of columns in the result set.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResultSet-getColumnNames(): Array<string>--><!--Device-ResultSet-getColumnNames(): Array<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | Names of all columns in the result set obtained. Duplicate column names can be obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted. |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed. |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) | The SQL must be a query statement. |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error. |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory. |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred. |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file. |

**Examples**

```TypeScript
try {
  // Query EMPLOYEE1 and EMPLOYEE2 and obtain the duplicate column names. store is the obtained RdbStore instance.
  let resultSet: relationalStore.ResultSet = await store.querySql("SELECT e1.NAME, e2.NAME, e1.AGE, e2.AGE FROM EMPLOYEE1 e1 LEFT JOIN EMPLOYEE2 e2 ON e1.SALARY=e2.SALARY");
  if (resultSet != undefined) {
    const names = resultSet.getColumnNames();
  }
} catch (err) {
  console.error(`Failed to get column names: code:${err.code}, message:${err.message}`);
}
```

```TypeScript
async function getColumnNamesExample(store : relationalStore.RdbStore){
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    // Query EMPLOYEE1 and EMPLOYEE2 and obtain the duplicate column names. store is the obtained RdbStore instance.
    resultSet = await store.querySqlWithoutRowCount("SELECT e1.NAME, e2.NAME, e1.AGE, e2.AGE FROM EMPLOYEE1 e1 LEFT JOIN EMPLOYEE2 e2 ON e1.SALARY=e2.SALARY");
    if (resultSet != undefined) {
      const names = resultSet.getColumnNames();
    }
  } catch (err) {
    console.error(`Failed to get column names: code:${err.code}, message:${err.message}`);
  }
}
```

## getColumnType

```TypeScript
getColumnType(columnIdentifier: int | string): Promise<ColumnType>
```

Obtains the column type based on the specified column index or column name. This API uses a promise to return the result.

**Since:** 23

<!--Device-ResultSet-getColumnType(columnIdentifier: int | string): Promise<ColumnType>--><!--Device-ResultSet-getColumnType(columnIdentifier: int | string): Promise<ColumnType>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIdentifier | int \| string | Yes | Index or name of column in a result set. The index must be a non- negative integer and cannot exceed the length of **columnNames**. The column name must be a name in **columnNames**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ColumnType](arkts-arkdata-relationalstore-columntype-e.md)&gt; | Promise used to return the column type obtained. If the result set contains duplicate column names, the return value is not as expected. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error. |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted. |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds. |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) | Column index is out of bounds. |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed. |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) | The SQL must be a query statement. |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error. |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort. |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied. |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked. |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked. |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory. |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database. |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred. |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full. |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file. |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit. |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation. |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch. |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly. |

**Examples**

```TypeScript
if (resultSet != undefined) {
  let idType = await (resultSet as relationalStore.ResultSet).getColumnType("ID") as relationalStore.ColumnType;
  let nameType = await (resultSet as relationalStore.ResultSet).getColumnType("NAME") as relationalStore.ColumnType;
  let ageType = await (resultSet as relationalStore.ResultSet).getColumnType("AGE") as relationalStore.ColumnType;
  let salaryType = await (resultSet as relationalStore.ResultSet).getColumnType("SALARY") as relationalStore.ColumnType;
  let codesType = await (resultSet as relationalStore.ResultSet).getColumnType("CODES") as relationalStore.ColumnType;
  let identityType = await (resultSet as relationalStore.ResultSet).getColumnType(5) as relationalStore.ColumnType;
  let assetDataType = await (resultSet as relationalStore.ResultSet).getColumnType(6) as relationalStore.ColumnType;
  let assetsDataType = await (resultSet as relationalStore.ResultSet).getColumnType(7) as relationalStore.ColumnType;
  let floatArrayType = await (resultSet as relationalStore.ResultSet).getColumnType(8) as relationalStore.ColumnType;
}
```

```TypeScript
async function getColumnTypeExample(store : relationalStore.RdbStore){
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
    if (resultSet != undefined) {
      resultSet.goToNextRow();
      //Method 1: Obtain the column type by column name.
      let idType = await resultSet.getColumnType("ID");
      let nameType = await resultSet.getColumnType("NAME");
      let ageType = await resultSet.getColumnType("AGE");
      let salaryType = await resultSet.getColumnType("SALARY");
      let codesType = await resultSet.getColumnType("CODES");
      //Method 2: Obtain the column type by column index.
      let identityType = await resultSet.getColumnType(5);
      let assetDataType = await resultSet.getColumnType(6);
      let assetsDataType = await resultSet.getColumnType(7);
      let floatArrayType = await resultSet.getColumnType(8);
    }
  } catch (err) {
    console.error(`failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

## getColumnTypeSync

```TypeScript
getColumnTypeSync(columnIdentifier: int | string): ColumnType
```

Obtains the column type based on the specified column index or column name. This API returns the result synchronously.

**Since:** 23

<!--Device-ResultSet-getColumnTypeSync(columnIdentifier: int | string): ColumnType--><!--Device-ResultSet-getColumnTypeSync(columnIdentifier: int | string): ColumnType-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIdentifier | int \| string | Yes | Index or name of column in a result set. The index must be a non- negative integer and cannot exceed the length of **columnNames**. The column name must be a name in **columnNames**. |

**Return value:**

| Type | Description |
| --- | --- |
| [ColumnType](arkts-arkdata-relationalstore-columntype-e.md) | Column type obtained. If the result set contains duplicate column names, the return value is not as expected. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error. |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted. |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds. |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) | Column index is out of bounds. |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed. |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) | The SQL must be a query statement. |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error. |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort. |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied. |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked. |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked. |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory. |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database. |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred. |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full. |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file. |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit. |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation. |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch. |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly. |

**Examples**

```TypeScript
if (resultSet != undefined) {
  let idType = (resultSet as relationalStore.ResultSet).getColumnTypeSync("ID") as relationalStore.ColumnType;
  let nameType = (resultSet as relationalStore.ResultSet).getColumnTypeSync("NAME") as relationalStore.ColumnType;
  let ageType = (resultSet as relationalStore.ResultSet).getColumnTypeSync("AGE") as relationalStore.ColumnType;
  let salaryType = (resultSet as relationalStore.ResultSet).getColumnTypeSync("SALARY") as relationalStore.ColumnType;
  let codesType = (resultSet as relationalStore.ResultSet).getColumnTypeSync("CODES") as relationalStore.ColumnType;
  let identityType = (resultSet as relationalStore.ResultSet).getColumnTypeSync(5) as relationalStore.ColumnType;
  let assetDataType = (resultSet as relationalStore.ResultSet).getColumnTypeSync(6) as relationalStore.ColumnType;
  let assetsDataType = (resultSet as relationalStore.ResultSet).getColumnTypeSync(7) as relationalStore.ColumnType;
  let floatArrayType = (resultSet as relationalStore.ResultSet).getColumnTypeSync(8) as relationalStore.ColumnType;
}
```

```TypeScript
async function getColumnTypeSyncExample(store : relationalStore.RdbStore){
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
    if (resultSet != undefined) {
      resultSet.goToNextRow();
      //Method 1: Obtain the column type by column name.
      let idType = resultSet.getColumnTypeSync("ID");
      let nameType = resultSet.getColumnTypeSync("NAME");
      let ageType = resultSet.getColumnTypeSync("AGE");
      let salaryType = resultSet.getColumnTypeSync("SALARY");
      let codesType = resultSet.getColumnTypeSync("CODES");
      //Method 2: Obtain the column type by column index.
      let identityType = resultSet.getColumnTypeSync(5);
      let assetDataType = resultSet.getColumnTypeSync(6);
      let assetsDataType = resultSet.getColumnTypeSync(7);
      let floatArrayType = resultSet.getColumnTypeSync(8);
    }
  } catch (err) {
    console.error(`failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

## getCurrentRowData

```TypeScript
getCurrentRowData(): RowData
```

Obtains the values of all columns in this row.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResultSet-getCurrentRowData(): RowData--><!--Device-ResultSet-getCurrentRowData(): RowData-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| [RowData](arkts-arkdata-relationalstore-rowdata-t.md) | Values of all columns in this row obtained. The values of columns with the same name can be obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted. |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds. |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed. |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) | The SQL must be a query statement. |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error. |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory. |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred. |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file. |

**Examples**

```TypeScript
try {
  // Query EMPLOYEE1 and EMPLOYEE2 and obtain the values of the current row that contain duplicate column names. store is the obtained RdbStore instance.
  let resultSet: relationalStore.ResultSet = await store.querySql("SELECT e1.NAME, e2.NAME, e1.AGE, e2.AGE FROM EMPLOYEE1 e1 LEFT JOIN EMPLOYEE2 e2 ON e1.SALARY=e2.SALARY");
  if (resultSet != undefined) {
    resultSet.goToFirstRow();
    const rowData = resultSet.getCurrentRowData();
  }
} catch (err) {
  console.error(`Failed to get row data: code:${err.code}, message:${err.message}`);
}
```

```TypeScript
async function getCurrentRowDataExample(store : relationalStore.RdbStore) {
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    // Query EMPLOYEE1 and EMPLOYEE2 and obtain the values of the current row that contain duplicate column names. store is the obtained RdbStore instance.
    resultSet = await store.querySqlWithoutRowCount("SELECT e1.NAME, e2.NAME, e1.AGE, e2.AGE FROM EMPLOYEE1 e1 LEFT JOIN EMPLOYEE2 e2 ON e1.SALARY=e2.SALARY");
    if (resultSet != undefined) {
      resultSet.goToNextRow();
      const rowData = resultSet.getCurrentRowData();
      console.info(`rowData: ${JSON.stringify(rowData)}`);
    }
  } catch (err) {
    console.error(`Failed to get row data: code:${err.code}, message:${err.message}`);
  }
}
```

## getDouble

```TypeScript
getDouble(columnIndex: int): double
```

Obtains the value from the specified column in the current row, and returns a value of Double type.

If the type of the value in the specified column is INTEGER, DOUBLE, TEXT, or BLOB, a value of Double type will be returned. If the column is null/empty, **0.0** will be returned. If the value is of any other type, 14800000 will be returned.

**Since:** 23

<!--Device-ResultSet-getDouble(columnIndex: int): double--><!--Device-ResultSet-getDouble(columnIndex: int): double-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | int | Yes | Index of the target column, starting from 0. |

**Return value:**

| Type | Description |
| --- | --- |
| double | Value obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) | Column index is out of bounds. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error.<br>**Applicable version:** 12 and later |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds.<br>**Applicable version:** 12 and later |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed.<br>**Applicable version:** 12 and later |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
if (resultSet !== undefined) {
  while (resultSet.goToNextRow()) {
    const colIndex = resultSet.getColumnIndex("SALARY");
    if (colIndex > -1) {
      const salary = resultSet.getDouble(colIndex);
      console.info(`Get double success, salary is ${salary}`);
    }
  }
}
```

```TypeScript
async function getDoubleExample(store : relationalStore.RdbStore) {
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
    if (resultSet != undefined) {
      resultSet.goToNextRow();
      const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
    }
  } catch (err) {
    console.error(`failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

## getLong

```TypeScript
getLong(columnIndex: int): long
```

Obtains the value from the specified column in the current row, and returns a value of Long type.

If the type of the value in the specified column is INTEGER, DOUBLE, TEXT, or BLOB, a value of Long type will be returned. If the column is null/empty, **0** will be returned. If the value is of any other type, 14800000 will be returned. If the data type in the specified column is INTEGER and the value is greater than **Number.MAX_SAFE_INTEGER** or less than **Number.MIN_SAFE_INTEGER**, you are advised to use the [getString](#getstring) API to obtain the value without losing precision. If the data type in the specified column is DOUBLE, you are advised to use the [getDouble](#getdouble) API to obtain the value without losing precision.

**Since:** 23

<!--Device-ResultSet-getLong(columnIndex: int): long--><!--Device-ResultSet-getLong(columnIndex: int): long-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | int | Yes | Index of the target column, starting from 0. |

**Return value:**

| Type | Description |
| --- | --- |
| long | Value obtained. <br>The value range supported by this API is **Number.MIN_SAFE_INTEGER** to **Number.MAX_SAFE_INTEGER**. If the value is out of this range, use [getDouble]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) | Column index is out of bounds. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error.<br>**Applicable version:** 12 and later |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds.<br>**Applicable version:** 12 and later |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed.<br>**Applicable version:** 12 and later |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
if (resultSet !== undefined) {
  while (resultSet.goToNextRow()) {
    const colIndex = resultSet.getColumnIndex("AGE");
    if (colIndex > -1) {
      const age = resultSet.getLong(colIndex);
      console.info(`Get long success, age is ${age}`);
    }
  }
}
```

```TypeScript
async function getLongExample(store : relationalStore.RdbStore) {
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
    if (resultSet != undefined) {
      resultSet.goToNextRow();
      const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
    }
  } catch (err) {
    console.error(`failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

## getRow

```TypeScript
getRow(): ValuesBucket
```

Obtains this row.

**Since:** 23

<!--Device-ResultSet-getRow(): ValuesBucket--><!--Device-ResultSet-getRow(): ValuesBucket-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| ValuesBucket | Value of the specified row. If the result set contains duplicate column names, the return value is not as expected. You are advised to use the [getCurrentRowData]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error. |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds.<br>**Applicable version:** 12 and later |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) | Column index is out of bounds.<br>**Applicable version:** 12 and later |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed.<br>**Applicable version:** 12 and later |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
if (resultSet != undefined) {
  const row = (resultSet as relationalStore.ResultSet).getRow();
}
```

```TypeScript
async function getRowExample(store : relationalStore.RdbStore) {
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
    if (resultSet != undefined) {
      resultSet.goToNextRow();
      const rowData = resultSet.getRow();
      console.info(`rowData: ${JSON.stringify(rowData)}`);
    }
  } catch (err) {
    console.error(`failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

## getRows

```TypeScript
getRows(maxCount: int, position?: int): Promise<Array<ValuesBucket>>
```

Obtains a specified amount of data from the result set. This API uses a promise to return the result. Do not call this API concurrently with other APIs of [ResultSet](arkts-data-relationalstore.md). Otherwise , unexpected data may be obtained.

**Since:** 23

<!--Device-ResultSet-getRows(maxCount: int, position?: int): Promise<Array<ValuesBucket>>--><!--Device-ResultSet-getRows(maxCount: int, position?: int): Promise<Array<ValuesBucket>>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| maxCount | int | Yes | Number of rows to obtain. The value is a positive integer. If the value is not a positive integer, error 401 will be thrown. |
| position | int | No | Start position for obtaining data from the result set. The value is a non-negative integer. If this parameter is not specified, data is obtained from the current row of the result set (by default, it is the first row of the result set when data is obtained for the first time). If the value is not a non-negative integer, error code 401 will be thrown. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;ValuesBucket&gt;&gt; | Promise used to return **maxCount** rows of data obtained. If the number of remaining records is less than **maxCount**, the remaining records are returned. Returning an empty array indicates that the end of the result set is reached. If the result set contains duplicate column names, the return values are not as expected. You are advised to use the [getRowsData]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error. |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted. |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds. |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) | Column index is out of bounds. |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed. |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error. |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort. |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied. |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked. |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked. |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory. |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred. |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full. |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit. |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation. |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch. |

**Examples**

```TypeScript
// Obtain 100 rows of data.
async function processRows(resultSet: relationalStore.ResultSet) {
  // Example 1: Specify only maxCount.
  if (resultSet != undefined) {
    let rows: Array<relationalStore.ValuesBucket>;
    let maxCount: number = 50;
    // Obtain data from the current row of the result set. By default, the first fetch starts from the first row of the current result set. Subsequent fetches start from the row following the last row retrieved.
    // getRows automatically moves the current row of the result set to the row following the last row retrieved by the previous getRows call. You do not need to use APIs such as goToFirstRow and goToNextRow.
    while ((rows = await (resultSet as relationalStore.ResultSet).getRows(maxCount)).length != 0) {
      console.info(JSON.stringify(rows[0]));
    }
  }

  // Example 2: Specify maxCount and position.
  if (resultSet != undefined) {
    let rows: Array<relationalStore.ValuesBucket>;
    let maxCount: number = 50;
    let position: number = 50;
    while ((rows = await (resultSet as relationalStore.ResultSet).getRows(maxCount, position)).length != 0) {
      console.info(JSON.stringify(rows[0]));
      position += rows.length;
    }
  }
}
```

```TypeScript
async function getRowsExample(store : relationalStore.RdbStore) {
  // Obtain 100 rows of data.
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
    // Example 1: Specify only maxCount.
    if (resultSet != undefined) {
      let rows: Array<relationalStore.ValuesBucket>;
      let maxCount: number = 50;
      // Obtain data from the current row of the result set. By default, the first fetch starts from the first row of the current result set. Subsequent fetches start from the row following the last row retrieved.
      // getRows automatically moves the current row of the result set to the next row after the end position of the last retrieval by getRows. You do not need to use the goToNextRow API to move the row.
      while ((rows = await resultSet.getRows(maxCount)).length != 0) {
        console.info(JSON.stringify(rows[0]));
      }
    }
  
    // Example 2: Specify maxCount and position.
    if (resultSet != undefined) {
      let rows: Array<relationalStore.ValuesBucket>;
      let maxCount: number = 50;
      let position: number = 50;
      while ((rows = await resultSet.getRows(maxCount, position)).length != 0) {
        console.info(JSON.stringify(rows[0]));
        position += rows.length;
      }
    }
  } catch (err) {
    console.error(`failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

## getRowsData

```TypeScript
getRowsData(maxCount: int, position?: int): Promise<RowsData>
```

Obtains data of a specified number of rows from the specified position. This API uses a promise to return the result. Do not call this API concurrently with other APIs of [ResultSet](arkts-data-relationalstore.md). Otherwise, unexpected data may be obtained.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResultSet-getRowsData(maxCount: int, position?: int): Promise<RowsData>--><!--Device-ResultSet-getRowsData(maxCount: int, position?: int): Promise<RowsData>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| maxCount | int | Yes | Number of rows to obtain. The value is a positive integer. If the value is not a positive integer, error 14800001 will be thrown. |
| position | int | No | Start position for obtaining data from the result set. The value is a non-negative integer. If this parameter is not specified, data is obtained from the current row of the result set (by default, it is the first row of the result set when data is obtained for the first time). If the value is not a non-negative integer, error code 14800001 will be thrown. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[RowsData](arkts-arkdata-relationalstore-rowsdata-t.md)&gt; | Promise used to return **maxCount** rows of data obtained. If the number of remaining records is less than **maxCount**, the remaining records are returned. Returning an empty array indicates that the end of the result set is reached. The values of columns with the same name can be obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted. |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds. |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed. |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) | The SQL must be a query statement. |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error. |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory. |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred. |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file. |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit. |

**Examples**

```TypeScript
try {
  // Query EMPLOYEE1 and EMPLOYEE2 and obtain the values of multiple rows that contain duplicate column names. store is the obtained RdbStore instance.
  let resultSet: relationalStore.ResultSet = await store.querySql("SELECT e1.NAME, e2.NAME, e1.AGE, e2.AGE FROM EMPLOYEE1 e1 LEFT JOIN EMPLOYEE2 e2 ON e1.SALARY=e2.SALARY");
  // Obtain 50 rows of data.
  // Example 1: Specify only maxCount.
  if (resultSet != undefined) {
    let rowsData: relationalStore.RowsData;
    // Obtain data from the current row of the result set. By default, the first fetch starts from the first row of the current result set. Subsequent fetches start from the row following the last row retrieved.
    // getRowsData automatically moves the current row of the result set to the next row after the end position of the last retrieval by getRowsData. You do not need to use APIs such as goToFirstRow and goToNextRow.
    let maxCount: number = 50;
    let rowCount: number = 0;
    while ((rowsData = await resultSet.getRowsData(maxCount)).length != 0) {
      rowsData.forEach((rowData, index) => {
        // Query result of the row specified by rowCount + index + 1
        console.info(`${rowCount + index + 1}: ${rowData}`);
      });
      rowCount += rowsData.length;
    }
  }

  // Example 2: Specify maxCount and position.
  if (resultSet != undefined) {
    let rowsData: relationalStore.RowsData;
    let maxCount: number = 50;
    let position: number = 50;
    while ((rowsData = await resultSet.getRowsData(maxCount, position)).length != 0) {
      rowsData.forEach((rowData, index) => {
        // Query result of the row specified by position + index + 1
        console.info(`${position + index + 1}: ${rowData}`);
      });
      position += rowsData.length;
    }
  }
} catch (err) {
  console.error(`Failed to get rows data: code:${err.code}, message:${err.message}`);
}
```

```TypeScript
async function getRowsDataExample(store : relationalStore.RdbStore) {
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    // Query EMPLOYEE1 and EMPLOYEE2 and obtain the values of multiple rows that contain duplicate column names. store is the obtained RdbStore instance.
    resultSet = await store.querySqlWithoutRowCount("SELECT e1.NAME, e2.NAME, e1.AGE, e2.AGE FROM EMPLOYEE1 e1 LEFT JOIN EMPLOYEE2 e2 ON e1.SALARY=e2.SALARY");
    // Obtain 50 rows of data.
    // Example 1: Specify only maxCount.
    if (resultSet != undefined) {
      let rowsData: relationalStore.RowsData;
      // Obtain data from the current row of the result set. By default, the first fetch starts from the first row of the current result set. Subsequent fetches start from the row following the last row retrieved.
      // getRowsData automatically moves the current row of the result set to the next row after the end position of the last retrieval by getRowsData. You do not need to use the goToNextRow API to move the row.
      let maxCount: number = 50;
      let rowCount: number = 0;
      while ((rowsData = await resultSet.getRowsData(maxCount)).length != 0) {
        rowsData.forEach((rowData, index) => {
          // Query result of the row specified by rowCount + index + 1
          console.info(`${rowCount + index + 1}: ${rowData}`);
        });
        rowCount += rowsData.length;
      }
    }
  
    // Example 2: Specify maxCount and position.
    if (resultSet != undefined) {
      let rowsData: relationalStore.RowsData;
      let maxCount: number = 50;
      let position: number = 50;
      while ((rowsData = await resultSet.getRowsData(maxCount, position)).length != 0) {
        rowsData.forEach((rowData, index) => {
          // Query result of the row specified by position + index + 1
          console.info(`${position + index + 1}: ${rowData}`);
        });
        position += rowsData.length;
      }
    }
  } catch (err) {
    console.error(`Failed to get rows data: code:${err.code}, message:${err.message}`);
  }
}
```

## getSendableRow

```TypeScript
getSendableRow(): sendableRelationalStore.ValuesBucket
```

Obtains the sendable data from the current row. The sendable data can be passed across threads.

**Since:** 12

<!--Device-ResultSet-getSendableRow(): sendableRelationalStore.ValuesBucket--><!--Device-ResultSet-getSendableRow(): sendableRelationalStore.ValuesBucket-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| sendableRelationalStore.ValuesBucket | Sendable data obtained for cross-thread transfer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error. |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted. |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds. |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) | Column index is out of bounds. |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed. |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error. |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort. |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied. |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked. |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked. |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory. |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database. |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred. |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full. |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file. |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit. |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation. |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch. |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly. |

**Examples**

For details about the definition of this.context in the sample code, see the application [context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) of the stage model.

```TypeScript
import { window } from '@kit.ArkUI';
import { UIAbility } from '@kit.AbilityKit';
import { relationalStore } from '@kit.ArkData';
import { taskpool } from '@kit.ArkTS';
import { common } from '@kit.AbilityKit';
import { sendableRelationalStore } from '@kit.ArkData';

@Concurrent
async function getDataByName(name: string, context: common.UIAbilityContext) {
  const STORE_CONFIG: relationalStore.StoreConfig = {
    name: "RdbTest.db",
    securityLevel: relationalStore.SecurityLevel.S3
  };
  const store = await relationalStore.getRdbStore(context, STORE_CONFIG);
  const predicates = new relationalStore.RdbPredicates("EMPLOYEE");
  predicates.equalTo("NAME", name);
  const resultSet = store.querySync(predicates);

  if (resultSet.rowCount > 0) {
    resultSet.goToFirstRow();
    const sendableValuesBucket = resultSet.getSendableRow();
    return sendableValuesBucket;
  } else {
    return null;
  }
}

export default class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage) {
    const task = new taskpool.Task(getDataByName, 'Lisa', this.context);
    const sendableValuesBucket = await taskpool.execute(task) as sendableRelationalStore.ValuesBucket;

    if (sendableValuesBucket) {
      const columnCount = sendableValuesBucket.size;
      const age = sendableValuesBucket.get('age');
      const name = sendableValuesBucket.get('name');
      console.info(`Query data in taskpool succeeded, name is "${name}", age is "${age}"`);
    }
  }
}
```

## getString

```TypeScript
getString(columnIndex: int): string
```

Obtains the value from the specified column in the current row, and returns it in the form of a string.

If the type of the value in the specified column is INTEGER, DOUBLE, TEXT, or BLOB, a string will be returned. If the value type is INTEGER and the column is null/empty, an empty string **""** will be returned. If the value is of any other type, 14800000 will be returned. If the value in the current column is of the DOUBLE type, the precision may be lost. You are advised to use [getDouble](#getdouble) to obtain the value.

**Since:** 23

<!--Device-ResultSet-getString(columnIndex: int): string--><!--Device-ResultSet-getString(columnIndex: int): string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | int | Yes | Index of the target column, starting from 0. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Value obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) | Column index is out of bounds. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error.<br>**Applicable version:** 12 and later |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds.<br>**Applicable version:** 12 and later |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed.<br>**Applicable version:** 12 and later |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
if (resultSet != undefined) {
  const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
}
```

```TypeScript
async function getStringExample(store : relationalStore.RdbStore) {
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
    if (resultSet != undefined) {
      resultSet.goToNextRow();
      const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
    }
  } catch (err) {
    console.error(`failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

## getValue

```TypeScript
getValue(columnIndex: int): ValueType
```

Obtains the value from the specified column in the current row. If the value type is any of **ValueType**, the value of the corresponding type will be returned. Otherwise, 14800000 will be returned. If the value type is INTEGER and the value is greater than **Number.MAX_SAFE_INTEGER** or less than **Number.MIN_SAFE_INTEGER**, you are advised to use the [getString](#getstring) API to obtain the value without losing precision.

**Since:** 23

<!--Device-ResultSet-getValue(columnIndex: int): ValueType--><!--Device-ResultSet-getValue(columnIndex: int): ValueType-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | int | Yes | Index of the target column, starting from 0. |

**Return value:**

| Type | Description |
| --- | --- |
| ValueType | Allowed data field types. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error. |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted. |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds. |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) | Column index is out of bounds. |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed. |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error. |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort. |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied. |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked. |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked. |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory. |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database. |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred. |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full. |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file. |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit. |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation. |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch. |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly. |

**Examples**

```TypeScript
if (resultSet !== undefined) {
  while (resultSet.goToNextRow()) {
    const colIndex = resultSet.getColumnIndex("NAME");
    if (colIndex > -1) {
      const name = resultSet.getValue(colIndex);
      console.info(`Get value success, name is ${name}`);
    }
  }
}
```

```TypeScript
async function getValueExample(store : relationalStore.RdbStore) {
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
    if (resultSet != undefined) {
      resultSet.goToNextRow();
      const name = resultSet.getValue(resultSet.getColumnIndex("NAME"));
    }
  } catch (err) {
    console.error(`failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

## goTo

```TypeScript
goTo(offset: int): boolean
```

Moves the result set pointer based on the offset specified.

**Since:** 23

<!--Device-ResultSet-goTo(offset: int): boolean--><!--Device-ResultSet-goTo(offset: int): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | int | Yes | Offset relative to the position of the current result set pointer. A positive value means to move the pointer backward, and a negative value means to move the pointer forward. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error.<br>**Applicable version:** 12 and later |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed.<br>**Applicable version:** 12 and later |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) | The SQL must be a query statement.<br>**Applicable version:** 12 and later |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
if (resultSet != undefined) {
  (resultSet as relationalStore.ResultSet).goTo(1);
}
```

## goToFirstRow

```TypeScript
goToFirstRow(): boolean
```

Moves to the first row of the result set.

**Since:** 23

<!--Device-ResultSet-goToFirstRow(): boolean--><!--Device-ResultSet-goToFirstRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error.<br>**Applicable version:** 12 and later |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed.<br>**Applicable version:** 12 and later |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) | The SQL must be a query statement.<br>**Applicable version:** 12 and later |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
if (resultSet != undefined) {
  (resultSet as relationalStore.ResultSet).goToFirstRow();
}
```

## goToLastRow

```TypeScript
goToLastRow(): boolean
```

Moves to the last row of the result set.

**Since:** 23

<!--Device-ResultSet-goToLastRow(): boolean--><!--Device-ResultSet-goToLastRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error.<br>**Applicable version:** 12 and later |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed.<br>**Applicable version:** 12 and later |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) | The SQL must be a query statement.<br>**Applicable version:** 12 and later |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
if (resultSet != undefined) {
  (resultSet as relationalStore.ResultSet).goToLastRow();
}
```

## goToNextRow

```TypeScript
goToNextRow(): boolean
```

Moves to the next row in the result set.

**Since:** 23

<!--Device-ResultSet-goToNextRow(): boolean--><!--Device-ResultSet-goToNextRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error.<br>**Applicable version:** 12 and later |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed.<br>**Applicable version:** 12 and later |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) | The SQL must be a query statement.<br>**Applicable version:** 12 and later |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
if (resultSet != undefined) {
  (resultSet as relationalStore.ResultSet).goToNextRow();
}
```

```TypeScript
async function goToNextRowExample(store : relationalStore.RdbStore) {
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
    if (resultSet != undefined) {
      resultSet.goToNextRow();
    }
  } catch (err) {
    console.error(`failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

## goToPreviousRow

```TypeScript
goToPreviousRow(): boolean
```

Moves to the previous row in the result set.

**Since:** 23

<!--Device-ResultSet-goToPreviousRow(): boolean--><!--Device-ResultSet-goToPreviousRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error.<br>**Applicable version:** 12 and later |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed.<br>**Applicable version:** 12 and later |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) | The SQL must be a query statement.<br>**Applicable version:** 12 and later |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
if (resultSet != undefined) {
  (resultSet as relationalStore.ResultSet).goToPreviousRow();
}
```

## goToRow

```TypeScript
goToRow(position: int): boolean
```

Moves to the specified row in the result set.

**Since:** 23

<!--Device-ResultSet-goToRow(position: int): boolean--><!--Device-ResultSet-goToRow(position: int): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | int | Yes | Destination position to move to. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error.<br>**Applicable version:** 12 and later |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed.<br>**Applicable version:** 12 and later |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) | The SQL must be a query statement.<br>**Applicable version:** 12 and later |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
if (resultSet != undefined) {
  (resultSet as relationalStore.ResultSet).goToRow(5);
}
```

## isColumnNull

```TypeScript
isColumnNull(columnIndex: int): boolean
```

Checks whether the value in the specified column is null.

**Since:** 23

<!--Device-ResultSet-isColumnNull(columnIndex: int): boolean--><!--Device-ResultSet-isColumnNull(columnIndex: int): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | int | Yes | Index of the target column, starting from 0. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the value is null; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) | Column index is out of bounds. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) | Inner error.<br>**Applicable version:** 12 and later |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) | ResultSet is empty or pointer index is out of bounds.<br>**Applicable version:** 12 and later |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) | The target instance is already closed.<br>**Applicable version:** 12 and later |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-read-only-database) | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
if (resultSet !== undefined) {
  while (resultSet.goToNextRow()) {
    const colIndex = resultSet.getColumnIndex("CODES");
    if (colIndex > -1) {
      const isColumnNull = resultSet.isColumnNull(colIndex);
      console.info(`Column is null: ${isColumnNull}`);
    }
  }
}
```

```TypeScript
async function isColumnNullExample(store : relationalStore.RdbStore) {
  try {
    let resultSet: relationalStore.LiteResultSet | undefined;
    resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
    if (resultSet != undefined) {
      resultSet.goToNextRow();
      const name = resultSet.isColumnNull(resultSet.getColumnIndex("NAME"));
    }
  } catch (err) {
    console.error(`failed, code is ${err.code}, message is ${err.message}`);
  }
}
```

## columnCount

```TypeScript
columnCount: int
```

Number of columns in the result set.

**Type:** int

**Since:** 23

<!--Device-ResultSet-columnCount: int--><!--Device-ResultSet-columnCount: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## columnNames

```TypeScript
columnNames: Array<string>
```

Names of all columns in the result set. If the result set contains duplicate column names, the return values are not as expected. You are advised to use the [getColumnNames](#getcolumnnames) API to obtain the column names.

**Type:** Array&lt;string&gt;

**Since:** 23

<!--Device-ResultSet-columnNames: Array<string>--><!--Device-ResultSet-columnNames: Array<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isAtFirstRow

```TypeScript
isAtFirstRow: boolean
```

Whether the result set pointer is in the first row (the row index is **0**). The value **true** means the result set pointer is in the first row.

**Type:** boolean

**Since:** 23

<!--Device-ResultSet-isAtFirstRow: boolean--><!--Device-ResultSet-isAtFirstRow: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isAtLastRow

```TypeScript
isAtLastRow: boolean
```

Whether the result set pointer is in the last row. The value **true** means the pointer is in the last row.

**Type:** boolean

**Since:** 23

<!--Device-ResultSet-isAtLastRow: boolean--><!--Device-ResultSet-isAtLastRow: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isClosed

```TypeScript
isClosed: boolean
```

Whether the result set is closed. The value **true** means the result set is closed.

**Type:** boolean

**Since:** 23

<!--Device-ResultSet-isClosed: boolean--><!--Device-ResultSet-isClosed: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isEnded

```TypeScript
isEnded: boolean
```

Whether the result set pointer is after the last row. The value **true** means the pointer is after the last row.

**Type:** boolean

**Since:** 23

<!--Device-ResultSet-isEnded: boolean--><!--Device-ResultSet-isEnded: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isStarted

```TypeScript
isStarted: boolean
```

Whether the result set pointer is moved. The value **true** means the pointer is moved.

**Type:** boolean

**Since:** 23

<!--Device-ResultSet-isStarted: boolean--><!--Device-ResultSet-isStarted: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## rowCount

```TypeScript
rowCount: int
```

Number of rows in the result set.

**Type:** int

**Since:** 23

<!--Device-ResultSet-rowCount: int--><!--Device-ResultSet-rowCount: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## rowIndex

```TypeScript
rowIndex: int
```

Index of the current row in the result set.

Default value: **-1**. The index position starts from **0**.

**Type:** int

**Since:** 23

<!--Device-ResultSet-rowIndex: int--><!--Device-ResultSet-rowIndex: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

