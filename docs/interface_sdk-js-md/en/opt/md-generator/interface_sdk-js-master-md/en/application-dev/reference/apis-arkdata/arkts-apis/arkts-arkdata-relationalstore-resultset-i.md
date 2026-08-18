# ResultSet

Provides APIs to access the result set obtained by querying the RDB store. This result set is the collection of results returned with the **query()** method called. The **ResultSet** instance is not refreshed in real time. After using the result set, if the data in the database is changed (by being added, deleted, or modified), you need to query the result set again to obtain the latest data. For the following APIs, you should use either [query] [query](arkts-arkdata-relationalstore-rdbstore-i.md#query), [querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querysqlwithoutrowcount), [remoteQuery] [remoteQuery](arkts-arkdata-relationalstore-rdbstore-i.md#remotequery) , or [queryLockedRow](arkts-arkdata-relationalstore-rdbstore-i.md#querylockedrow) to obtain the **ResultSet** instance first, and then use this instance to call the corresponding method.

**Since:** 23

<!--Device-relationalStore-interface ResultSet--><!--Device-relationalStore-interface ResultSet-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
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

| Error Code ID |
| --- |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |

## getAsset

```TypeScript
getAsset(columnIndex: number): Asset
```

Obtains the value from the specified column in the current row, and returns the value in the [Asset](arkts-arkdata-relationalstore-asset-i.md#asset) format. If the type of the value in the column is **Asset**, the value of the Asset type is returned. If the value in the column is null, **null** is returned. If the value in the column is of other types, 14800000 is returned.

**Since:** 23

<!--Device-ResultSet-getAsset(columnIndex: int): Asset--><!--Device-ResultSet-getAsset(columnIndex: int): Asset-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Asset](arkts-arkdata-commontype-asset-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getAssets

```TypeScript
getAssets(columnIndex: number): Assets
```

Obtains the value from the specified column in the current row, and returns the value in the [Assets](arkts-arkdata-relationalstore-assets-t.md#assets) format. If the type of the value in the column is **Assets**, the value of the Assets type is returned. If the value in the column is null, **null** is returned. If the value in the column is of other types, 14800000 is returned.

**Since:** 23

<!--Device-ResultSet-getAssets(columnIndex: int): Assets--><!--Device-ResultSet-getAssets(columnIndex: int): Assets-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Assets](arkts-arkdata-sendablerelationalstore-assets-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getBlob

```TypeScript
getBlob(columnIndex: number): Uint8Array
```

Obtains the value from the specified column in the current row, and returns it in a byte array. If the type of the value in the specified column is INTEGER, DOUBLE, TEXT, or BLOB, the value will be converted into a byte array and returned. If the column is null/empty, an empty byte array will be returned. If the value is of any other type, 14800000 will be returned.

**Since:** 23

<!--Device-ResultSet-getBlob(columnIndex: int): Uint8Array--><!--Device-ResultSet-getBlob(columnIndex: int): Uint8Array-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getColumnIndex

```TypeScript
getColumnIndex(columnName: string): number
```

Obtains the column index based on the column name.

**Since:** 23

<!--Device-ResultSet-getColumnIndex(columnName: string): int--><!--Device-ResultSet-getColumnIndex(columnName: string): int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getColumnName

```TypeScript
getColumnName(columnIndex: number): string
```

Obtains the column name based on the column index.

**Since:** 23

<!--Device-ResultSet-getColumnName(columnIndex: int): string--><!--Device-ResultSet-getColumnName(columnIndex: int): string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getColumnNames

```TypeScript
getColumnNames(): Array<string>
```

Obtains the names of all columns in the result set. The column names are returned in a string array. The sequence of strings in the array is the same as that of columns in the result set.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResultSet-getColumnNames(): Array<string>--><!--Device-ResultSet-getColumnNames(): Array<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getColumnType

```TypeScript
getColumnType(columnIdentifier: number | string): Promise<ColumnType>
```

Obtains the column type based on the specified column index or column name. This API uses a promise to return the result.

**Since:** 23

<!--Device-ResultSet-getColumnType(columnIdentifier: int | string): Promise<ColumnType>--><!--Device-ResultSet-getColumnType(columnIdentifier: int | string): Promise<ColumnType>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIdentifier | number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ColumnType](arkts-arkdata-relationalstore-columntype-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getColumnTypeSync

```TypeScript
getColumnTypeSync(columnIdentifier: number | string): ColumnType
```

Obtains the column type based on the specified column index or column name. This API returns the result synchronously.

**Since:** 23

<!--Device-ResultSet-getColumnTypeSync(columnIdentifier: int | string): ColumnType--><!--Device-ResultSet-getColumnTypeSync(columnIdentifier: int | string): ColumnType-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIdentifier | number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColumnType](arkts-arkdata-relationalstore-columntype-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

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

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RowData](arkts-arkdata-relationalstore-rowdata-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getDouble

```TypeScript
getDouble(columnIndex: number): number
```

Obtains the value from the specified column in the current row, and returns a value of Double type. If the type of the value in the specified column is INTEGER, DOUBLE, TEXT, or BLOB, a value of Double type will be returned. If the column is null/empty, **0.0** will be returned. If the value is of any other type, 14800000 will be returned.

**Since:** 23

<!--Device-ResultSet-getDouble(columnIndex: int): double--><!--Device-ResultSet-getDouble(columnIndex: int): double-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getLong

```TypeScript
getLong(columnIndex: number): number
```

Obtains the value from the specified column in the current row, and returns a value of Long type. If the type of the value in the specified column is INTEGER, DOUBLE, TEXT, or BLOB, a value of Long type will be returned. If the column is null/empty, **0** will be returned. If the value is of any other type, 14800000 will be returned. If the data type in the specified column is INTEGER and the value is greater than **Number.MAX_SAFE_INTEGER** or less than **Number.MIN_SAFE_INTEGER**, you are advised to use the [getString](#getstring) API to obtain the value without losing precision. If the data type in the specified column is DOUBLE, you are advised to use the [getDouble](#getdouble) API to obtain the value without losing precision.

**Since:** 23

<!--Device-ResultSet-getLong(columnIndex: int): long--><!--Device-ResultSet-getLong(columnIndex: int): long-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getRow

```TypeScript
getRow(): ValuesBucket
```

Obtains this row.

**Since:** 23

<!--Device-ResultSet-getRow(): ValuesBucket--><!--Device-ResultSet-getRow(): ValuesBucket-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getRows

```TypeScript
getRows(maxCount: number, position?: number): Promise<Array<ValuesBucket>>
```

Obtains a specified amount of data from the result set. This API uses a promise to return the result. Do not call this API concurrently with other APIs of [ResultSet](arkts-data-relationalstore.md#ohosdatarelationalstore). Otherwise , unexpected data may be obtained.

**Since:** 23

<!--Device-ResultSet-getRows(maxCount: int, position?: int): Promise<Array<ValuesBucket>>--><!--Device-ResultSet-getRows(maxCount: int, position?: int): Promise<Array<ValuesBucket>>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxCount | number | Yes |
| position | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;ValuesBucket & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |

## getRowsData

```TypeScript
getRowsData(maxCount: number, position?: number): Promise<RowsData>
```

Obtains data of a specified number of rows from the specified position. This API uses a promise to return the result. Do not call this API concurrently with other APIs of [ResultSet](arkts-data-relationalstore.md#ohosdatarelationalstore). Otherwise, unexpected data may be obtained.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResultSet-getRowsData(maxCount: int, position?: int): Promise<RowsData>--><!--Device-ResultSet-getRowsData(maxCount: int, position?: int): Promise<RowsData>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxCount | number | Yes |
| position | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[RowsData](arkts-arkdata-relationalstore-rowsdata-t.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getSendableRow

```TypeScript
getSendableRow(): sendableRelationalStore.ValuesBucket
```

Obtains the sendable data from the current row. The sendable data can be passed across threads.

**Since:** 12

<!--Device-ResultSet-getSendableRow(): sendableRelationalStore.ValuesBucket--><!--Device-ResultSet-getSendableRow(): sendableRelationalStore.ValuesBucket-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| sendableRelationalStore.ValuesBucket |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getString

```TypeScript
getString(columnIndex: number): string
```

Obtains the value from the specified column in the current row, and returns it in the form of a string. If the type of the value in the specified column is INTEGER, DOUBLE, TEXT, or BLOB, a string will be returned. If the value type is INTEGER and the column is null/empty, an empty string **""** will be returned. If the value is of any other type, 14800000 will be returned. If the value in the current column is of the DOUBLE type, the precision may be lost. You are advised to use [getDouble](#getdouble) to obtain the value.

**Since:** 23

<!--Device-ResultSet-getString(columnIndex: int): string--><!--Device-ResultSet-getString(columnIndex: int): string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getValue

```TypeScript
getValue(columnIndex: number): ValueType
```

Obtains the value from the specified column in the current row. If the value type is any of **ValueType**, the value of the corresponding type will be returned. Otherwise, 14800000 will be returned. If the value type is INTEGER and the value is greater than **Number.MAX_SAFE_INTEGER** or less than **Number.MIN_SAFE_INTEGER**, you are advised to use the [getString](#getstring) API to obtain the value without losing precision.

**Since:** 23

<!--Device-ResultSet-getValue(columnIndex: int): ValueType--><!--Device-ResultSet-getValue(columnIndex: int): ValueType-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## goTo

```TypeScript
goTo(offset: number): boolean
```

Moves the result set pointer based on the offset specified.

**Since:** 23

<!--Device-ResultSet-goTo(offset: int): boolean--><!--Device-ResultSet-goTo(offset: int): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## goToFirstRow

```TypeScript
goToFirstRow(): boolean
```

Moves to the first row of the result set.

**Since:** 23

<!--Device-ResultSet-goToFirstRow(): boolean--><!--Device-ResultSet-goToFirstRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## goToLastRow

```TypeScript
goToLastRow(): boolean
```

Moves to the last row of the result set.

**Since:** 23

<!--Device-ResultSet-goToLastRow(): boolean--><!--Device-ResultSet-goToLastRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## goToNextRow

```TypeScript
goToNextRow(): boolean
```

Moves to the next row in the result set.

**Since:** 23

<!--Device-ResultSet-goToNextRow(): boolean--><!--Device-ResultSet-goToNextRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## goToPreviousRow

```TypeScript
goToPreviousRow(): boolean
```

Moves to the previous row in the result set.

**Since:** 23

<!--Device-ResultSet-goToPreviousRow(): boolean--><!--Device-ResultSet-goToPreviousRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## goToRow

```TypeScript
goToRow(position: number): boolean
```

Moves to the specified row in the result set.

**Since:** 23

<!--Device-ResultSet-goToRow(position: int): boolean--><!--Device-ResultSet-goToRow(position: int): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## isColumnNull

```TypeScript
isColumnNull(columnIndex: number): boolean
```

Checks whether the value in the specified column is null.

**Since:** 23

<!--Device-ResultSet-isColumnNull(columnIndex: int): boolean--><!--Device-ResultSet-isColumnNull(columnIndex: int): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## columnCount

```TypeScript
columnCount: number
```

Number of columns in the result set.

**Type:** number

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
rowCount: number
```

Number of rows in the result set.

**Type:** number

**Since:** 23

<!--Device-ResultSet-rowCount: int--><!--Device-ResultSet-rowCount: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## rowIndex

```TypeScript
rowIndex: number
```

Index of the current row in the result set. Default value: **-1**. The index position starts from **0**.

**Type:** number

**Since:** 23

<!--Device-ResultSet-rowIndex: int--><!--Device-ResultSet-rowIndex: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core
