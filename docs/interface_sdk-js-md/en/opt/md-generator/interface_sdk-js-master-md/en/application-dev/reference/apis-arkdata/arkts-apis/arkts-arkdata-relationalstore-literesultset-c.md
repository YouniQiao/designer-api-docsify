# LiteResultSet

Defines APIs to access the result set obtained by querying the RDB store. This result set is the collection of results returned with the **query()** method called.

The **LiteResultSet** instance is not refreshed in real time. After using the result set, if the data in the database is changed (by being added, deleted, or modified), you need to query the result set again to obtain the latest data.

In the following API examples, you need to obtain an **LiteResultSet** instance by using a query method, such as   
[queryWithoutRowCount](arkts-arkdata-relationalstore-rdbstore-i.md#querywithoutrowcount) or   
[querySqlWithoutRowCount](arkts-arkdata-relationalstore-rdbstore-i.md#querysqlwithoutrowcount), and then call the corresponding method through this instance.

> **NOTE：**
> 
> - The initial APIs of this class are supported since API version 23.

**Since:** 23

<!--Device-relationalStore-class LiteResultSet--><!--Device-relationalStore-class LiteResultSet-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## close

```TypeScript
close(): void
```

Closes this **resultSet** to release memory. If the **resultSet** is not closed, FD or memory leaks may occur.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-close(): void--><!--Device-LiteResultSet-close(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## getAsset

```TypeScript
getAsset(columnIndex: number): Asset
```

Obtains the value in the specified column in the current row as an   
[Asset](arkts-arkdata-relationalstore-asset-i.md).

If the data type of the current column is Asset, the value is returned as an Asset. If the value in the current column is **null**, **null** is returned. If the data type of the current column is not Asset, 14800041 is returned.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getAsset(columnIndex: int): Asset--><!--Device-LiteResultSet-getAsset(columnIndex: int): Asset-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Asset](arkts-arkdata-sendablerelationalstore-asset-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800041](../errorcode-data-rdb.md#14800041-type-conversion-failure) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## getAssets

```TypeScript
getAssets(columnIndex: number): Assets
```

Obtains the value in the specified column in the current row as   
[Assets](arkts-arkdata-relationalstore-assets-t.md).

If the data type of the current column is Assets, the value is returned as Assets. If the value in the current column is **null**, **null** is returned. If the data type of the current column is not Assets, 14800041 is returned.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getAssets(columnIndex: int): Assets--><!--Device-LiteResultSet-getAssets(columnIndex: int): Assets-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Assets](arkts-arkdata-sendablerelationalstore-assets-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800041](../errorcode-data-rdb.md#14800041-type-conversion-failure) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## getBlob

```TypeScript
getBlob(columnIndex: number): Uint8Array
```

Obtains the value in the specified column in the current row as a byte array.

If the data type of the current column is INTEGER, DOUBLE, TEXT, or BLOB, the data is converted to a byte array and returned. If the content of the column is null/empty, an empty byte array is returned.

If the data type of the current column is ASSET, ASSETS, FLOATVECTOR, or BIGINT, 14800041 is returned.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getBlob(columnIndex: int): Uint8Array--><!--Device-LiteResultSet-getBlob(columnIndex: int): Uint8Array-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [14800041](../errorcode-data-rdb.md#14800041-type-conversion-failure) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## getColumnIndex

```TypeScript
getColumnIndex(columnName: string): number
```

Obtains the column index based on the column name.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getColumnIndex(columnName: string): int--><!--Device-LiteResultSet-getColumnIndex(columnName: string): int-End-->

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
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getColumnName

```TypeScript
getColumnName(columnIndex: number): string
```

Obtains the column name based on the column index.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getColumnName(columnIndex: int): string--><!--Device-LiteResultSet-getColumnName(columnIndex: int): string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getColumnNames

```TypeScript
getColumnNames(): Array<string>
```

Obtains the names of all columns in the result set.

The column names are returned in a string array. The sequence of strings in the array is the same as that of columns in the result set.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getColumnNames(): Array<string>--><!--Device-LiteResultSet-getColumnNames(): Array<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;string&gt; |

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

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getColumnType(columnIdentifier: int | string): Promise<ColumnType>--><!--Device-LiteResultSet-getColumnType(columnIdentifier: int | string): Promise<ColumnType>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIdentifier | number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ColumnType&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getColumnTypeSync

```TypeScript
getColumnTypeSync(columnIdentifier: number | string): ColumnType
```

Obtains the column type based on the specified column index or column name.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getColumnTypeSync(columnIdentifier: int | string): ColumnType--><!--Device-LiteResultSet-getColumnTypeSync(columnIdentifier: int | string): ColumnType-End-->

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
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getCurrentRowData

```TypeScript
getCurrentRowData(): RowData
```

Obtains the values of all columns in this row.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getCurrentRowData(): RowData--><!--Device-LiteResultSet-getCurrentRowData(): RowData-End-->

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

Obtains the value in the specified column in the current row as a Double.

If the data type of the current column is INTEGER, DOUBLE, or TEXT, the value is converted to the Double type and returned. Non-numeric TEXT and BLOB types return **0.0**. If the content of the column is null/empty, **0.0** is returned.

If the data type of the current column is ASSET, ASSETS, FLOATVECTOR, or BIGINT, 14800041 is returned.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getDouble(columnIndex: int): double--><!--Device-LiteResultSet-getDouble(columnIndex: int): double-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [14800041](../errorcode-data-rdb.md#14800041-type-conversion-failure) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## getLong

```TypeScript
getLong(columnIndex: number): number
```

Obtains the value from the specified column in the current row, and returns a value of Long type.

If the data type of the current column is INTEGER, DOUBLE, TEXT, or BLOB, a value of Long type is returned. If the column is null, **0** is returned. If the data type is INTEGER and the value is greater than  
**Number.MAX_SAFE_INTEGER** or less than **Number.MIN_SAFE_INTEGER**, you are advised to use the  
[getString](arkts-arkdata-relationalstore-literesultset-c.md#getstring) API to obtain the value without losing precision. If the data type in the specified column is DOUBLE, you are advised to use the  
[getDouble](arkts-arkdata-relationalstore-literesultset-c.md#getdouble) API to obtain the value without precision loss.

If the data type of the current column is ASSET, ASSETS, FLOATVECTOR, or BIGINT, 14800041 is returned.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getLong(columnIndex: int): long--><!--Device-LiteResultSet-getLong(columnIndex: int): long-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [14800041](../errorcode-data-rdb.md#14800041-type-conversion-failure) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## getRow

```TypeScript
getRow(): ValuesBucket
```

Obtains data for the current row.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getRow(): ValuesBucket--><!--Device-LiteResultSet-getRow(): ValuesBucket-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) |

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

## getRows

```TypeScript
getRows(maxCount: number, position?: number): Promise<Array<ValuesBucket>>
```

Obtains a specified amount of data from the result set. This API uses a promise to return the result. Do not call this API concurrently with other APIs of [LiteResultSet](arkts-data-relationalstore.md). Otherwise, unexpected data may be obtained.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getRows(maxCount: int, position?: int): Promise<Array<ValuesBucket>>--><!--Device-LiteResultSet-getRows(maxCount: int, position?: int): Promise<Array<ValuesBucket>>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxCount | number | Yes |
| position | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;ValuesBucket&gt;&gt; |

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

## getRowsData

```TypeScript
getRowsData(maxCount: number, position?: number): Promise<RowsData>
```

Obtains data of a specified number of rows from the specified position. This API uses a promise to return the result. Do not call this API concurrently with other APIs of   
[ResultSet](arkts-data-relationalstore.md). Otherwise, unexpected data may be obtained.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getRowsData(maxCount: int, position?: int): Promise<RowsData>--><!--Device-LiteResultSet-getRowsData(maxCount: int, position?: int): Promise<RowsData>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxCount | number | Yes |
| position | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;RowsData&gt; |

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

## getString

```TypeScript
getString(columnIndex: number): string
```

Obtains the value in the specified column in the current row as a string.

If the data type of the current column is INTEGER, DOUBLE, TEXT, or BLOB type, the value is returned as a string.If the content of the column is null/empty, an empty string **""** is returned.

If the data type of the current column is DOUBLE, precision loss may occur. You are advised to use   
[getDouble](arkts-arkdata-relationalstore-literesultset-c.md#getdouble) API to obtain the value.

If the data type of the current column is ASSET, ASSETS, FLOATVECTOR, or BIGINT, 14800041 is returned.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getString(columnIndex: int): string--><!--Device-LiteResultSet-getString(columnIndex: int): string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [14800041](../errorcode-data-rdb.md#14800041-type-conversion-failure) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## getValue

```TypeScript
getValue(columnIndex: number): ValueType
```

Obtains the value of the specified column in the current row.

If the value type is INTEGER and the value is greater than **Number.MAX_SAFE_INTEGER** or less than   
**Number.MIN_SAFE_INTEGER**, you are advised to use the   
[getString](arkts-arkdata-relationalstore-literesultset-c.md#getstring) API to obtain the value without precision loss.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getValue(columnIndex: int): ValueType--><!--Device-LiteResultSet-getValue(columnIndex: int): ValueType-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## goToNextRow

```TypeScript
goToNextRow(): boolean
```

Moves the result set to the next row.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-goToNextRow(): boolean--><!--Device-LiteResultSet-goToNextRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

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

## isColumnNull

```TypeScript
isColumnNull(columnIndex: number): boolean
```

Checks whether the value in the specified column is null.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-isColumnNull(columnIndex: int): boolean--><!--Device-LiteResultSet-isColumnNull(columnIndex: int): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800019](../errorcode-data-rdb.md#14800019-sql-query-statement-required) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |
