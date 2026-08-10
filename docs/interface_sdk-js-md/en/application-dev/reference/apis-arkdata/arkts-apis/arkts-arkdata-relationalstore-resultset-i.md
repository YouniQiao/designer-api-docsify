# ResultSet

提供通过查询数据库生成的数据库结果集的访问方法。结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。

ResultSet实例不会实时刷新。使用结果集后，如果数据库中的数据发生变化（如增删改操作），需要重新查询才能获取到最新的数据。

下列API示例中，都需先使用  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)、  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querysql)、  
[remoteQuery](arkts-arkdata-relationalstore-rdbstore-i.md#remotequery)、[queryLockedRow](arkts-arkdata-relationalstore-rdbstore-i.md#querylockedrow)等query类方法中任一方法获取到ResultSet实例，再通过此实例调用对应方法。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-relationalStore-interface ResultSet--><!--Device-relationalStore-interface ResultSet-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## close

```TypeScript
close(): void
```

关闭结果集，若不关闭可能会引起FD（File Descriptor）泄漏和内存泄漏。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-close(): void--><!--Device-ResultSet-close(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800000 | Inner error.<br>**Applicable version:** 12 and later |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |

## getAsset

ArkTS-Dyn:
```TypeScript
getAsset(columnIndex: number): Asset
```

ArkTS-Sta:
```TypeScript
getAsset(columnIndex: int): Asset
```

以[Asset](arkts-arkdata-relationalstore-asset-i.md)形式获取当前行中指定列的值，如果当前列的数据类型为Asset类型，会以Asset类型返回指定值，如果当前列中的值为null时，会返回null，其他类型则抛出错误码14800000。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ResultSet-getAsset(columnIndex: int): Asset--><!--Device-ResultSet-getAsset(columnIndex: int): Asset-End-->

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
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error.<br>**Applicable version:** 12 and later |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## getAssets

ArkTS-Dyn:
```TypeScript
getAssets(columnIndex: number): Assets
```

ArkTS-Sta:
```TypeScript
getAssets(columnIndex: int): Assets
```

以[Assets](arkts-arkdata-relationalstore-assets-t.md)形式获取当前行中指定列的值，如果当前列的数据类型为Assets类型，会以Assets类型返回指定值，如果当前列中的值为null时，会返回null，其他类型则抛出14800000。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ResultSet-getAssets(columnIndex: int): Assets--><!--Device-ResultSet-getAssets(columnIndex: int): Assets-End-->

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
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error.<br>**Applicable version:** 12 and later |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## getBlob

ArkTS-Dyn:
```TypeScript
getBlob(columnIndex: number): Uint8Array
```

ArkTS-Sta:
```TypeScript
getBlob(columnIndex: int): Uint8Array
```

以字节数组的形式获取当前行中指定列的值，如果当前列的数据类型为INTEGER、DOUBLE、TEXT、BLOB类型，会转成字节数组类型返回指定值，如果该列内容为空时，会返回空字节数组，其他类型则抛出错误码14800000。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-getBlob(columnIndex: int): Uint8Array--><!--Device-ResultSet-getBlob(columnIndex: int): Uint8Array-End-->

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
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error.<br>**Applicable version:** 12 and later |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-getColumnIndex(columnName: string): int--><!--Device-ResultSet-getColumnIndex(columnName: string): int-End-->

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
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error.<br>**Applicable version:** 12 and later |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800013 | Column index is out of bounds. |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800019 | The SQL must be a query statement.<br>**Applicable version:** 12 and later |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-getColumnName(columnIndex: int): string--><!--Device-ResultSet-getColumnName(columnIndex: int): string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的列索引，从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回指定列的名称。当结果集中包含重名列时，返回值会不符合预期。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error.<br>**Applicable version:** 12 and later |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800013 | Column index is out of bounds. |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800019 | The SQL must be a query statement.<br>**Applicable version:** 12 and later |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## getColumnNames

```TypeScript
getColumnNames(): Array<string>
```

获取结果集中所有列的名称。

列名以字符串数组的形式返回，数组中字符串的顺序与结果集中列的顺序一致。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResultSet-getColumnNames(): Array<string>--><!--Device-ResultSet-getColumnNames(): Array<string>-End-->

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

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-ResultSet-getColumnType(columnIdentifier: int | string): Promise<ColumnType>--><!--Device-ResultSet-getColumnType(columnIdentifier: int | string): Promise<ColumnType>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIdentifier | ArkTS-Dyn: number \| string  <br>ArkTS-Sta：int \| string | Yes | 表示结果集中指定列的索引或列名。索引必须是非负整数，且必须小于属性columnNames的长度。列名必须是属性columnNames内的名 称。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ColumnType&gt; | Promise对象。返回指定列的数据类型。当结果集中包含重名列时，通过列名获取的结果会不符合预期，建议使用列索引形式获取。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch. |
| 14800000 | Inner error. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800024 | SQLite: The database file is locked. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800026 | SQLite: The database is out of memory. |
| 14800029 | SQLite: The database is full. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
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

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-ResultSet-getColumnTypeSync(columnIdentifier: int | string): ColumnType--><!--Device-ResultSet-getColumnTypeSync(columnIdentifier: int | string): ColumnType-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIdentifier | ArkTS-Dyn: number \| string  <br>ArkTS-Sta：int \| string | Yes | 表示结果集中指定列的索引或名称。索引必须是非负整数，最大不能超过属性columnNames的长度。列名必须是属性columnNames内的名 称。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ColumnType](arkts-arkdata-relationalstore-columntype-e.md) | 返回指定列的数据类型。当结果集中包含重名列时，通过列名获取的结果会不符合预期，建议使用列索引形式获取。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch. |
| 14800000 | Inner error. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800019 | The SQL must be a query statement. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800024 | SQLite: The database file is locked. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800026 | SQLite: The database is out of memory. |
| 14800029 | SQLite: The database is full. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800030 | SQLite: Unable to open the database file. |

## getCurrentRowData

```TypeScript
getCurrentRowData(): RowData
```

获取当前行所有列的值。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResultSet-getCurrentRowData(): RowData--><!--Device-ResultSet-getCurrentRowData(): RowData-End-->

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

以double形式获取当前行中指定列的值，如果当前列的数据类型为INTEGER、DOUBLE、TEXT、BLOB类型，会转成double类型返回指定值，如果该列内容为空时，会返回0.0，其他类型则抛出错误码14800000。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-getDouble(columnIndex: int): double--><!--Device-ResultSet-getDouble(columnIndex: int): double-End-->

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
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error.<br>**Applicable version:** 12 and later |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## getLong

ArkTS-Dyn:
```TypeScript
getLong(columnIndex: number): number
```

ArkTS-Sta:
```TypeScript
getLong(columnIndex: int): long
```

以Long形式获取当前行中指定列的值，如果当前列的数据类型为INTEGER、DOUBLE、TEXT、BLOB类型，会转成Long类型返回指定值，如果该列内容为空时，会返回0，其他类型则抛出错误码14800000。如果当前列的数据类型为INTEGER，值大于 Number.MAX_SAFE_INTEGER 或小于 Number.MIN_SAFE_INTEGER 且不希望丢失精度，建议使用  
[getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)接口获取。如果当前列的数据类型为DOUBLE且不希望丢失精度，建议使用  
[getDouble](arkts-arkdata-relationalstore-resultset-i.md#getdouble)接口获取。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-getLong(columnIndex: int): long--><!--Device-ResultSet-getLong(columnIndex: int): long-End-->

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
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error.<br>**Applicable version:** 12 and later |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## getRow

```TypeScript
getRow(): ValuesBucket
```

获取当前行。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ResultSet-getRow(): ValuesBucket--><!--Device-ResultSet-getRow(): ValuesBucket-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 返回指定行的值。当结果集中包含重名列时，返回值会不符合预期，建议使用 [getCurrentRowData]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error. |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800013 | Column index is out of bounds.<br>**Applicable version:** 12 and later |
| 14800012 | ResultSet is empty or pointer index is out of bounds.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## getRows

ArkTS-Dyn:
```TypeScript
getRows(maxCount: number, position?: number): Promise<Array<ValuesBucket>>
```

ArkTS-Sta:
```TypeScript
getRows(maxCount: int, position?: int): Promise<Array<ValuesBucket>>
```

从结果集中获取指定数量的数据，使用Promise异步回调。禁止与[ResultSet](arkts-arkdata-relationalstore-resultset-i.md)的其他接口并发调用，否则获取的数据可能非预期。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-ResultSet-getRows(maxCount: int, position?: int): Promise<Array<ValuesBucket>>--><!--Device-ResultSet-getRows(maxCount: int, position?: int): Promise<Array<ValuesBucket>>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| maxCount | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 正整数，指定要从结果集中获取数据的条数。不为正整数则参数非法，抛出错误码401。 |
| position | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 非负整数，指定从结果集中获取数据的起始位置，不填则从结果集的当前行（默认首次获取数据时为当前结果集的第一行）开始获取数据。不为非负整数则参数非法，抛出错误码401。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;ValuesBucket&gt;&gt; | 返回maxCount条数据，剩余数据不足maxCount条则返回剩余数据，返回空数组时代表已经遍历到结果集的末尾。当结果集中包含重名列时，返回 值会不符合预期，建议使用[getRowsData]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch. |
| 14800000 | Inner error. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800024 | SQLite: The database file is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800029 | SQLite: The database is full. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |

## getRowsData

ArkTS-Dyn:
```TypeScript
getRowsData(maxCount: number, position?: number): Promise<RowsData>
```

ArkTS-Sta:
```TypeScript
getRowsData(maxCount: int, position?: int): Promise<RowsData>
```

从指定位置position开始，最多获取maxCount行数据。使用Promise异步回调。禁止与[ResultSet](arkts-arkdata-relationalstore-resultset-i.md)的其他接口并发调用，否则获取的数据可能非预期。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResultSet-getRowsData(maxCount: int, position?: int): Promise<RowsData>--><!--Device-ResultSet-getRowsData(maxCount: int, position?: int): Promise<RowsData>-End-->

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

## getSendableRow

```TypeScript
getSendableRow(): sendableRelationalStore.ValuesBucket
```

获取当前行数据的sendable形式，用于跨线程传递。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ResultSet-getSendableRow(): sendableRelationalStore.ValuesBucket--><!--Device-ResultSet-getSendableRow(): sendableRelationalStore.ValuesBucket-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| sendableRelationalStore.ValuesBucket | 当前行数据的sendable形式，用于跨线程传递。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch. |
| 14800000 | Inner error. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800024 | SQLite: The database file is locked. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800026 | SQLite: The database is out of memory. |
| 14800029 | SQLite: The database is full. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
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

以字符串形式获取当前行中指定列的值，如果当前列中的值为INTEGER、DOUBLE、TEXT、BLOB类型，会以字符串形式返回指定值，如果是当前列中的值为INTEGER，并且为空，则会返回空字符串""，其他类型则抛出错误码14800000。如果当前列中的值为DOUBLE类型，可能存在精度的丢失，建议使用[getDouble](arkts-arkdata-relationalstore-resultset-i.md#getdouble)接口获取。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-getString(columnIndex: int): string--><!--Device-ResultSet-getString(columnIndex: int): string-End-->

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
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error.<br>**Applicable version:** 12 and later |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## getValue

ArkTS-Dyn:
```TypeScript
getValue(columnIndex: number): ValueType
```

ArkTS-Sta:
```TypeScript
getValue(columnIndex: int): ValueType
```

获取当前行中指定列的值，如果值类型是ValueType中指定的任意类型，返回指定类型的值，否则抛出错误码14800000。如果值类型为INTEGER，值大于 Number.MAX_SAFE_INTEGER 或小于 Number.MIN_SAFE_INTEGER 且不希望丢失精度，建议使用[getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)接口获取。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ResultSet-getValue(columnIndex: int): ValueType--><!--Device-ResultSet-getValue(columnIndex: int): ValueType-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的列索引，从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 表示允许的数据字段类型。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch. |
| 14800000 | Inner error. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800024 | SQLite: The database file is locked. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800026 | SQLite: The database is out of memory. |
| 14800029 | SQLite: The database is full. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800030 | SQLite: Unable to open the database file. |

## goTo

ArkTS-Dyn:
```TypeScript
goTo(offset: number): boolean
```

ArkTS-Sta:
```TypeScript
goTo(offset: int): boolean
```

指定相对当前结果集指针位置的偏移量，以移动结果集的指针位置。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-goTo(offset: int): boolean--><!--Device-ResultSet-goTo(offset: int): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示相对当前结果集指针位置的偏移量，正值表示向后移动，负值表示向前移动。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果成功移动结果集，则为true；否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error.<br>**Applicable version:** 12 and later |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800019 | The SQL must be a query statement.<br>**Applicable version:** 12 and later |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## goToFirstRow

```TypeScript
goToFirstRow(): boolean
```

转到结果集的第一行。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-goToFirstRow(): boolean--><!--Device-ResultSet-goToFirstRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果成功移动结果集，则为true；否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error.<br>**Applicable version:** 12 and later |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 14800019 | The SQL must be a query statement.<br>**Applicable version:** 12 and later |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## goToLastRow

```TypeScript
goToLastRow(): boolean
```

转到结果集的最后一行。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-goToLastRow(): boolean--><!--Device-ResultSet-goToLastRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果成功移动结果集，则为true；否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error.<br>**Applicable version:** 12 and later |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 14800019 | The SQL must be a query statement.<br>**Applicable version:** 12 and later |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## goToNextRow

```TypeScript
goToNextRow(): boolean
```

转到结果集的下一行。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-goToNextRow(): boolean--><!--Device-ResultSet-goToNextRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果成功移动结果集，则为true；否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error.<br>**Applicable version:** 12 and later |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 14800019 | The SQL must be a query statement.<br>**Applicable version:** 12 and later |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## goToPreviousRow

```TypeScript
goToPreviousRow(): boolean
```

转到结果集的上一行。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-goToPreviousRow(): boolean--><!--Device-ResultSet-goToPreviousRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果成功移动结果集，则为true；否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error.<br>**Applicable version:** 12 and later |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 14800019 | The SQL must be a query statement.<br>**Applicable version:** 12 and later |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## goToRow

ArkTS-Dyn:
```TypeScript
goToRow(position: number): boolean
```

ArkTS-Sta:
```TypeScript
goToRow(position: int): boolean
```

转到结果集的指定行。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-goToRow(position: int): boolean--><!--Device-ResultSet-goToRow(position: int): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示要移动到的指定位置。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果成功移动结果集，则为true；否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error.<br>**Applicable version:** 12 and later |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800012 | ResultSet is empty or pointer index is out of bounds. |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800019 | The SQL must be a query statement.<br>**Applicable version:** 12 and later |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-isColumnNull(columnIndex: int): boolean--><!--Device-ResultSet-isColumnNull(columnIndex: int): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| columnIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的列索引，从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果当前行中指定列的值为null，则返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error.<br>**Applicable version:** 12 and later |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800013 | Column index is out of bounds. |
| 14800012 | ResultSet is empty or pointer index is out of bounds.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## columnCount

```TypeScript
columnCount: int
```

columnCount: int

获取结果集中列的数量。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-columnCount: int--><!--Device-ResultSet-columnCount: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## columnNames

```TypeScript
columnNames: Array<string>
```

columnNames: Array\&lt;string\&gt;

获取结果集中所有列的名称。当结果集中包含重名列时，获取的列名会不符合预期，建议使用[getColumnNames](arkts-arkdata-relationalstore-resultset-i.md#getcolumnnames)接口获取。

**Type:** Array&lt;string&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-columnNames: Array<string>--><!--Device-ResultSet-columnNames: Array<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isAtFirstRow

```TypeScript
isAtFirstRow: boolean
```

isAtFirstRow: boolean

检查结果集指针是否位于第一行（行索引为0），true表示位于第一行，false表示不位于第一行。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-isAtFirstRow: boolean--><!--Device-ResultSet-isAtFirstRow: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isAtLastRow

```TypeScript
isAtLastRow: boolean
```

isAtLastRow: boolean

检查结果集指针是否位于最后一行，true表示位于最后一行，false表示不位于最后一行。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-isAtLastRow: boolean--><!--Device-ResultSet-isAtLastRow: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isClosed

```TypeScript
isClosed: boolean
```

isClosed: boolean

检查当前结果集是否关闭，true表示结果集已关闭，false表示结果集未关闭。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-isClosed: boolean--><!--Device-ResultSet-isClosed: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isEnded

```TypeScript
isEnded: boolean
```

isEnded: boolean

检查结果集指针是否位于最后一行之后，true表示位于最后一行之后，false表示不位于最后一行之后。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-isEnded: boolean--><!--Device-ResultSet-isEnded: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isStarted

```TypeScript
isStarted: boolean
```

isStarted: boolean

检查指针是否移动过，true表示指针已移动过，false表示指针未移动过。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-isStarted: boolean--><!--Device-ResultSet-isStarted: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## rowCount

```TypeScript
rowCount: int
```

rowCount: int

获取结果集中行的数量。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-rowCount: int--><!--Device-ResultSet-rowCount: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## rowIndex

```TypeScript
rowIndex: int
```

rowIndex: int

获取结果集当前行的索引位置，默认值为-1。索引位置下标从0开始。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResultSet-rowIndex: int--><!--Device-ResultSet-rowIndex: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

