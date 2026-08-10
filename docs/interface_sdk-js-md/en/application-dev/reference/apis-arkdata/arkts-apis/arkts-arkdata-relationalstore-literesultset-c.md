# LiteResultSet

提供查询数据库后生成的结果集的访问方法。结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。

LiteResultSet实例不会实时刷新。使用结果集后，如果数据库中的数据发生变化（如增删改操作），需要重新查询才能获取到最新的数据。

下列API示例中，都需先使用[queryWithoutRowCount](arkts-arkdata-relationalstore-rdbstore-i.md#querywithoutrowcount)、  
[querySqlWithoutRowCount](arkts-arkdata-relationalstore-rdbstore-i.md#querysqlwithoutrowcount)等query类方法中任一方法获取到LiteResultSet实例，再通过此实例调用对应方法。

> **说明：**
> 
> - 本class首批接口从API version 23开始支持。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

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

关闭结果集，若不关闭可能会引起fd泄漏和内存泄漏。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-close(): void--><!--Device-LiteResultSet-close(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## getAsset

ArkTS-Dyn:
```TypeScript
getAsset(columnIndex: number): Asset
```

ArkTS-Sta:
```TypeScript
getAsset(columnIndex: int): Asset
```

以[Asset](arkts-arkdata-relationalstore-asset-i.md)形式获取当前行中指定列的值。

如果当前列的数据类型为Asset类型，会以Asset类型返回指定值；如果当前列中的值为null时，会返回null；如果当前列的数据类型非Asset类型，则返回14800041。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getAsset(columnIndex: int): Asset--><!--Device-LiteResultSet-getAsset(columnIndex: int): Asset-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的列索引，从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Asset](arkts-arkdata-commontype-asset-i.md) | 以Asset形式返回指定列的值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800041 | Type conversion failed. |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |

## getAssets

ArkTS-Dyn:
```TypeScript
getAssets(columnIndex: number): Assets
```

ArkTS-Sta:
```TypeScript
getAssets(columnIndex: int): Assets
```

以[Assets](arkts-arkdata-relationalstore-assets-t.md)形式获取当前行中指定列的值。

如果当前列的数据类型为Assets类型，会以Assets类型返回指定值；如果当前列中的值为null时，会返回null；如果当前列的数据类型非Assets类型，则返回14800041。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getAssets(columnIndex: int): Assets--><!--Device-LiteResultSet-getAssets(columnIndex: int): Assets-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的列索引，从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Assets](arkts-arkdata-sendablerelationalstore-assets-t.md) | 以Assets形式返回指定列的值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800041 | Type conversion failed. |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |

## getBlob

ArkTS-Dyn:
```TypeScript
getBlob(columnIndex: number): Uint8Array
```

ArkTS-Sta:
```TypeScript
getBlob(columnIndex: int): Uint8Array
```

以字节数组的形式获取当前行中指定列的值。

如果当前列的数据类型为INTEGER、DOUBLE、TEXT、BLOB类型，会转成字节数组类型返回指定值，如果该列内容为空时，会返回空字节数组。

如果当前列的数据类型为ASSET、ASSETS、FLOATVECTOR、BIGINT类型，会抛出错误码14800041。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getBlob(columnIndex: int): Uint8Array--><!--Device-LiteResultSet-getBlob(columnIndex: int): Uint8Array-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的列索引，从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 以字节数组的形式返回指定列的值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800041 | Type conversion failed. |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |

## getColumnIndex

ArkTS-Dyn:
```TypeScript
getColumnIndex(columnName: string): number
```

ArkTS-Sta:
```TypeScript
getColumnIndex(columnName: string): int
```

根据指定的列名获取列索引。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getColumnIndex(columnName: string): int--><!--Device-LiteResultSet-getColumnIndex(columnName: string): int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnName | string | Yes | 表示结果集中指定列的名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 返回指定列的索引。当结果集中包含重名列时，返回值会不符合预期。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800014 | The target instance is already closed. |
| 14800030 | SQLite: Unable to open the database file. |

## getColumnName

ArkTS-Dyn:
```TypeScript
getColumnName(columnIndex: number): string
```

ArkTS-Sta:
```TypeScript
getColumnName(columnIndex: int): string
```

根据指定的列索引获取列名。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getColumnName(columnIndex: int): string--><!--Device-LiteResultSet-getColumnName(columnIndex: int): string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示结果集中指定列的索引，从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回指定列的名称。当结果集中包含重名列时，返回值会不符合预期。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800026 | SQLite: The database is out of memory. |
| 14800013 | Column index is out of bounds. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800014 | The target instance is already closed. |
| 14800030 | SQLite: Unable to open the database file. |

## getColumnNames

```TypeScript
getColumnNames(): Array<string>
```

获取结果集中所有列的名称。

列名以字符串数组的形式返回，数组中字符串的顺序与结果集中列的顺序一致。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getColumnNames(): Array<string>--><!--Device-LiteResultSet-getColumnNames(): Array<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 返回结果集中所有列的名称。支持获取包含重名列的列名。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800014 | The target instance is already closed. |
| 14800030 | SQLite: Unable to open the database file. |

## getColumnType

ArkTS-Dyn:
```TypeScript
getColumnType(columnIdentifier: number | string): Promise<ColumnType>
```

ArkTS-Sta:
```TypeScript
getColumnType(columnIdentifier: int | string): Promise<ColumnType>
```

根据指定的列索引或列名称获取列数据类型，使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getColumnType(columnIdentifier: int | string): Promise<ColumnType>--><!--Device-LiteResultSet-getColumnType(columnIdentifier: int | string): Promise<ColumnType>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIdentifier | ArkTS-Dyn: number \| string  <br>ArkTS-Sta：int \| string | Yes | 表示结果集中指定列的索引或名称，索引从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ColumnType&gt; | Promise对象。返回指定列的数据类型。当结果集中包含重名列时，通过列名获取的结果会不符合预期。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800026 | SQLite: The database is out of memory. |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800014 | The target instance is already closed. |
| 14800030 | SQLite: Unable to open the database file. |

## getColumnTypeSync

ArkTS-Dyn:
```TypeScript
getColumnTypeSync(columnIdentifier: number | string): ColumnType
```

ArkTS-Sta:
```TypeScript
getColumnTypeSync(columnIdentifier: int | string): ColumnType
```

根据指定的列索引或列名称获取列数据类型。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getColumnTypeSync(columnIdentifier: int | string): ColumnType--><!--Device-LiteResultSet-getColumnTypeSync(columnIdentifier: int | string): ColumnType-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIdentifier | ArkTS-Dyn: number \| string  <br>ArkTS-Sta：int \| string | Yes | 表示结果集中指定列的索引或名称，索引从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ColumnType](arkts-arkdata-relationalstore-columntype-e.md) | 返回指定列的数据类型。当结果集中包含重名列时，通过列名获取的结果会不符合预期。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800026 | SQLite: The database is out of memory. |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800014 | The target instance is already closed. |
| 14800030 | SQLite: Unable to open the database file. |

## getCurrentRowData

```TypeScript
getCurrentRowData(): RowData
```

获取当前行所有列的值。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getCurrentRowData(): RowData--><!--Device-LiteResultSet-getCurrentRowData(): RowData-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| [RowData](arkts-arkdata-relationalstore-rowdata-t.md) | 返回当前行所有列的值。支持获取包含重名列的值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800026 | SQLite: The database is out of memory. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800014 | The target instance is already closed. |
| 14800030 | SQLite: Unable to open the database file. |

## getDouble

ArkTS-Dyn:
```TypeScript
getDouble(columnIndex: number): number
```

ArkTS-Sta:
```TypeScript
getDouble(columnIndex: int): double
```

以double形式获取当前行中指定列的值。

如果当前列的数据类型为INTEGER、DOUBLE、TEXT会转成double类型返回指定值，非数字的TEXT、BLOB类型会返回0.0。如果该列内容为空时，会返回0.0。

如果当前列的数据类型为ASSET、ASSETS、FLOATVECTOR、BIGINT类型，会返回14800041。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getDouble(columnIndex: int): double--><!--Device-LiteResultSet-getDouble(columnIndex: int): double-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的列索引，从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 以double形式返回指定列的值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800041 | Type conversion failed. |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |

## getLong

ArkTS-Dyn:
```TypeScript
getLong(columnIndex: number): number
```

ArkTS-Sta:
```TypeScript
getLong(columnIndex: int): long
```

以Long形式获取当前行中指定列的值。

如果当前列的数据类型为INTEGER、DOUBLE、TEXT会转成Long类型返回指定值，非数字的TEXT、BLOB类型会返回0。如果该列内容为空时，会返回0。

如果当前列的数据类型为INTEGER，值大于Number.MAX_SAFE_INTEGER 或小于Number.MIN_SAFE_INTEGER时，如果不希望丢失精度，建议使用  
[getString](arkts-arkdata-relationalstore-literesultset-c.md#getstring)接口获取。

如果当前列的数据类型为DOUBLE时，如果不希望丢失精度，建议使用[getDouble](arkts-arkdata-relationalstore-literesultset-c.md#getdouble)接口获取。

如果当前列的数据类型为ASSET、ASSETS、FLOATVECTOR、BIGINT类型，会返回14800041。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getLong(columnIndex: int): long--><!--Device-LiteResultSet-getLong(columnIndex: int): long-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的列索引，从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 以Long形式返回指定列的值。 &lt;br&gt;该接口支持的精度范围是：Number.MIN_SAFE_INTEGER ~ Number.MAX_SAFE_INTEGER，若超出该范围，建议对于DOUBLE类型的值使用 [getDouble]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800041 | Type conversion failed. |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |

## getRow

```TypeScript
getRow(): ValuesBucket
```

获取当前行的数据。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getRow(): ValuesBucket--><!--Device-LiteResultSet-getRow(): ValuesBucket-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 返回指定行的值。当结果集中包含重名列时，返回值会不符合预期，建议使用 [getCurrentRowData]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800026 | SQLite: The database is out of memory. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800014 | The target instance is already closed. |
| 14800030 | SQLite: Unable to open the database file. |

## getRows

ArkTS-Dyn:
```TypeScript
getRows(maxCount: number, position?: number): Promise<Array<ValuesBucket>>
```

ArkTS-Sta:
```TypeScript
getRows(maxCount: int, position?: int): Promise<Array<ValuesBucket>>
```

从结果集中获取指定数量的数据，使用Promise异步回调。禁止与[LiteResultSet](arkts-arkdata-relationalstore-literesultset-c.md)的其他接口并发调用，否则获取的数据可能非预期。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getRows(maxCount: int, position?: int): Promise<Array<ValuesBucket>>--><!--Device-LiteResultSet-getRows(maxCount: int, position?: int): Promise<Array<ValuesBucket>>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| maxCount | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 正整数，指定要从结果集中获取数据的条数。 |
| position | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 非负整数，指定从结果集中获取数据的起始位置，不填则从结果集的当前行（默认首次获取数据时为当前结果集的第一行）开始获取数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;ValuesBucket&gt;&gt; | 返回maxCount条数据，剩余数据不足maxCount条则返回剩余数据，返回空数组时代表已经遍历到结果集的末尾。当结果集中包含重名列时，返回 值会不符合预期，建议使用[getRowsData]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800026 | SQLite: The database is out of memory. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800014 | The target instance is already closed. |
| 14800030 | SQLite: Unable to open the database file. |

## getRowsData

ArkTS-Dyn:
```TypeScript
getRowsData(maxCount: number, position?: number): Promise<RowsData>
```

ArkTS-Sta:
```TypeScript
getRowsData(maxCount: int, position?: int): Promise<RowsData>
```

从指定位置position开始，最多获取maxCount行数据。使用Promise异步回调。禁止与[LiteResultSet](arkts-arkdata-relationalstore-literesultset-c.md)的其他接口并发调用，否则获取的数据可能非预期。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getRowsData(maxCount: int, position?: int): Promise<RowsData>--><!--Device-LiteResultSet-getRowsData(maxCount: int, position?: int): Promise<RowsData>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| maxCount | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 正整数，指定从结果集中获取数据的条数。不为正整数则参数非法，抛出错误码14800001。 |
| position | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 非负整数，指定从结果集中获取数据的起始位置，不填则从结果集的当前行（默认首次获取数据时为当前结果集的第一行）开始获取数据。不为非负整数则参数非法，抛出错误码1480000 1。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;RowsData&gt; | 返回maxCount条数据，剩余数据不足maxCount条则返回剩余数据，返回空数组时代表已经遍历到结果集的末尾。支持获取包含重名列的值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800026 | SQLite: The database is out of memory. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800014 | The target instance is already closed. |
| 14800030 | SQLite: Unable to open the database file. |

## getString

ArkTS-Dyn:
```TypeScript
getString(columnIndex: number): string
```

ArkTS-Sta:
```TypeScript
getString(columnIndex: int): string
```

以字符串形式获取当前行中指定列的值。

如果当前列中的值为INTEGER、DOUBLE、TEXT、BLOB类型，会以字符串形式返回指定值；如果该列内容为空，则会返回空字符串""。

如果当前列中的值为DOUBLE类型，可能存在精度的丢失，建议使用[getDouble](arkts-arkdata-relationalstore-literesultset-c.md#getdouble)接口获取。

如果当前列的数据类型为ASSET、ASSETS、FLOATVECTOR、BIGINT类型，会返回14800041。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getString(columnIndex: int): string--><!--Device-LiteResultSet-getString(columnIndex: int): string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的列索引，从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 以字符串形式返回指定列的值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800041 | Type conversion failed. |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |

## getValue

ArkTS-Dyn:
```TypeScript
getValue(columnIndex: number): ValueType
```

ArkTS-Sta:
```TypeScript
getValue(columnIndex: int): ValueType
```

获取当前行中指定列的值。

如果值类型为INTEGER，值大于Number.MAX_SAFE_INTEGER或小于Number.MIN_SAFE_INTEGER时，如果不希望丢失精度，建议使用  
[getString](arkts-arkdata-relationalstore-literesultset-c.md#getstring)接口获取。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getValue(columnIndex: int): ValueType--><!--Device-LiteResultSet-getValue(columnIndex: int): ValueType-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的列索引，从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 允许返回的数据字段类型。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |

## goToNextRow

```TypeScript
goToNextRow(): boolean
```

移动结果集到下一行。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-goToNextRow(): boolean--><!--Device-LiteResultSet-goToNextRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果成功移动结果集到下一行，返回true；否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800026 | SQLite: The database is out of memory. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800014 | The target instance is already closed. |
| 14800030 | SQLite: Unable to open the database file. |

## isColumnNull

ArkTS-Dyn:
```TypeScript
isColumnNull(columnIndex: number): boolean
```

ArkTS-Sta:
```TypeScript
isColumnNull(columnIndex: int): boolean
```

检查当前行中指定列的值是否为null。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-isColumnNull(columnIndex: int): boolean--><!--Device-LiteResultSet-isColumnNull(columnIndex: int): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的列索引，从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果当前行中指定列的值为null，则返回true；否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800026 | SQLite: The database is out of memory. |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800014 | The target instance is already closed. |
| 14800030 | SQLite: Unable to open the database file |

