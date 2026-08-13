# LiteResultSet

提供查询数据库后生成的结果集的访问方法。结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。 LiteResultSet实例不会实时刷新。使用结果集后，如果数据库中的数据发生变化（如增删改操作），需要重新查询才能获取到最新的数据。 下列API示例中，都需先使用[queryWithoutRowCount](arkts-arkdata-relationalstore-rdbstore-i.md#queryWithoutRowCount)、 [querySqlWithoutRowCount](arkts-arkdata-relationalstore-rdbstore-i.md#querySqlWithoutRowCount)等query类方法中任一方法获取到LiteResultSet实例，再 通过此实例调用对应方法。 > **说明：** > > - 本class首批接口从API version 23开始支持。

**起始版本：** 23

**废弃版本：** -1

<!--Device-relationalStore-class LiteResultSet--><!--Device-relationalStore-class LiteResultSet-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## close

```TypeScript
close(): void
```

关闭结果集，若不关闭可能会引起fd泄漏和内存泄漏。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-close(): void--><!--Device-LiteResultSet-close(): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## getAsset

```TypeScript
getAsset(columnIndex: number): Asset
```

以[Asset](arkts-arkdata-relationalstore-asset-i.md#Asset)形式获取当前行中指定列的值。 如果当前列的数据类型为Asset类型，会以Asset类型返回指定值；如果当前列中的值为null时，会返回null；如果当前列的数据类型非Asset类型，则返回14800041。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-getAsset(columnIndex: int): Asset--><!--Device-LiteResultSet-getAsset(columnIndex: int): Asset-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Asset](arkts-arkdata-sendablerelationalstore-asset-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800041](../errorcode-data-rdb.md#14800041-类型转换失败) |
| [14800013](../errorcode-data-rdb.md#14800013-列号越界或列类型与当前调用接口不兼容) |
| [14800012](../errorcode-data-rdb.md#14800012-结果集为空或指定位置不合法) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## getAssets

```TypeScript
getAssets(columnIndex: number): Assets
```

以[Assets](arkts-arkdata-relationalstore-assets-t.md#Assets)形式获取当前行中指定列的值。 如果当前列的数据类型为Assets类型，会以Assets类型返回指定值；如果当前列中的值为null时，会返回null；如果当前列的数据类型非Assets类型，则返回14800041。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-getAssets(columnIndex: int): Assets--><!--Device-LiteResultSet-getAssets(columnIndex: int): Assets-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Assets](arkts-arkdata-sendablerelationalstore-assets-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800041](../errorcode-data-rdb.md#14800041-类型转换失败) |
| [14800013](../errorcode-data-rdb.md#14800013-列号越界或列类型与当前调用接口不兼容) |
| [14800012](../errorcode-data-rdb.md#14800012-结果集为空或指定位置不合法) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## getBlob

```TypeScript
getBlob(columnIndex: number): Uint8Array
```

以字节数组的形式获取当前行中指定列的值。 如果当前列的数据类型为INTEGER、DOUBLE、TEXT、BLOB类型，会转成字节数组类型返回指定值，如果该列内容为空时，会返回空字节数组。 如果当前列的数据类型为ASSET、ASSETS、FLOATVECTOR、BIGINT类型，会抛出错误码14800041。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-getBlob(columnIndex: int): Uint8Array--><!--Device-LiteResultSet-getBlob(columnIndex: int): Uint8Array-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [14800041](../errorcode-data-rdb.md#14800041-类型转换失败) |
| [14800013](../errorcode-data-rdb.md#14800013-列号越界或列类型与当前调用接口不兼容) |
| [14800012](../errorcode-data-rdb.md#14800012-结果集为空或指定位置不合法) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## getColumnIndex

```TypeScript
getColumnIndex(columnName: string): number
```

根据指定的列名获取列索引。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-getColumnIndex(columnName: string): int--><!--Device-LiteResultSet-getColumnIndex(columnName: string): int-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| columnName | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800019](../errorcode-data-rdb.md#14800019-sql必须是查询语句) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## getColumnName

```TypeScript
getColumnName(columnIndex: number): string
```

根据指定的列索引获取列名。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-getColumnName(columnIndex: int): string--><!--Device-LiteResultSet-getColumnName(columnIndex: int): string-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800019](../errorcode-data-rdb.md#14800019-sql必须是查询语句) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800013](../errorcode-data-rdb.md#14800013-列号越界或列类型与当前调用接口不兼容) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## getColumnNames

```TypeScript
getColumnNames(): Array<string>
```

获取结果集中所有列的名称。 列名以字符串数组的形式返回，数组中字符串的顺序与结果集中列的顺序一致。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-getColumnNames(): Array<string>--><!--Device-LiteResultSet-getColumnNames(): Array<string>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800019](../errorcode-data-rdb.md#14800019-sql必须是查询语句) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## getColumnType

```TypeScript
getColumnType(columnIdentifier: number | string): Promise<ColumnType>
```

根据指定的列索引或列名称获取列数据类型，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-getColumnType(columnIdentifier: int | string): Promise<ColumnType>--><!--Device-LiteResultSet-getColumnType(columnIdentifier: int | string): Promise<ColumnType>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| columnIdentifier | number \| string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ColumnType](arkts-arkdata-relationalstore-columntype-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800019](../errorcode-data-rdb.md#14800019-sql必须是查询语句) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800013](../errorcode-data-rdb.md#14800013-列号越界或列类型与当前调用接口不兼容) |
| [14800012](../errorcode-data-rdb.md#14800012-结果集为空或指定位置不合法) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## getColumnTypeSync

```TypeScript
getColumnTypeSync(columnIdentifier: number | string): ColumnType
```

根据指定的列索引或列名称获取列数据类型。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-getColumnTypeSync(columnIdentifier: int | string): ColumnType--><!--Device-LiteResultSet-getColumnTypeSync(columnIdentifier: int | string): ColumnType-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| columnIdentifier | number \| string | 是 |

**返回值：**

| 类型 |
| --- |
| [ColumnType](arkts-arkdata-relationalstore-columntype-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800019](../errorcode-data-rdb.md#14800019-sql必须是查询语句) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800013](../errorcode-data-rdb.md#14800013-列号越界或列类型与当前调用接口不兼容) |
| [14800012](../errorcode-data-rdb.md#14800012-结果集为空或指定位置不合法) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## getCurrentRowData

```TypeScript
getCurrentRowData(): RowData
```

获取当前行所有列的值。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-getCurrentRowData(): RowData--><!--Device-LiteResultSet-getCurrentRowData(): RowData-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| [RowData](arkts-arkdata-relationalstore-rowdata-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800019](../errorcode-data-rdb.md#14800019-sql必须是查询语句) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800012](../errorcode-data-rdb.md#14800012-结果集为空或指定位置不合法) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## getDouble

```TypeScript
getDouble(columnIndex: number): number
```

以double形式获取当前行中指定列的值。 如果当前列的数据类型为INTEGER、DOUBLE、TEXT会转成double类型返回指定值，非数字的TEXT、BLOB类型会返回0.0。如果该列内容为空时，会返回0.0。 如果当前列的数据类型为ASSET、ASSETS、FLOATVECTOR、BIGINT类型，会返回14800041。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-getDouble(columnIndex: int): double--><!--Device-LiteResultSet-getDouble(columnIndex: int): double-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [14800041](../errorcode-data-rdb.md#14800041-类型转换失败) |
| [14800013](../errorcode-data-rdb.md#14800013-列号越界或列类型与当前调用接口不兼容) |
| [14800012](../errorcode-data-rdb.md#14800012-结果集为空或指定位置不合法) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## getLong

```TypeScript
getLong(columnIndex: number): number
```

以Long形式获取当前行中指定列的值。 如果当前列的数据类型为INTEGER、DOUBLE、TEXT会转成Long类型返回指定值，非数字的TEXT、BLOB类型会返回0。如果该列内容为空时，会返回0。 如果当前列的数据类型为INTEGER，值大于Number.MAX_SAFE_INTEGER 或小于Number.MIN_SAFE_INTEGER时，如果不希望丢失精度，建议使用 [getString](#getString)接口获取。 如果当前列的数据类型为DOUBLE时，如果不希望丢失精度，建议使用[getDouble](#getDouble)接口获取。 如果当前列的数据类型为ASSET、ASSETS、FLOATVECTOR、BIGINT类型，会返回14800041。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-getLong(columnIndex: int): long--><!--Device-LiteResultSet-getLong(columnIndex: int): long-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [14800041](../errorcode-data-rdb.md#14800041-类型转换失败) |
| [14800013](../errorcode-data-rdb.md#14800013-列号越界或列类型与当前调用接口不兼容) |
| [14800012](../errorcode-data-rdb.md#14800012-结果集为空或指定位置不合法) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## getRow

```TypeScript
getRow(): ValuesBucket
```

获取当前行的数据。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-getRow(): ValuesBucket--><!--Device-LiteResultSet-getRow(): ValuesBucket-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800019](../errorcode-data-rdb.md#14800019-sql必须是查询语句) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800012](../errorcode-data-rdb.md#14800012-结果集为空或指定位置不合法) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## getRows

```TypeScript
getRows(maxCount: number, position?: number): Promise<Array<ValuesBucket>>
```

从结果集中获取指定数量的数据，使用Promise异步回调。禁止与[LiteResultSet](#LiteResultSet)的其他接口并发调用，否则获取的数据可能非预期。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-getRows(maxCount: int, position?: int): Promise<Array<ValuesBucket>>--><!--Device-LiteResultSet-getRows(maxCount: int, position?: int): Promise<Array<ValuesBucket>>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| maxCount | number | 是 |
| position | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;ValuesBucket & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800019](../errorcode-data-rdb.md#14800019-sql必须是查询语句) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800012](../errorcode-data-rdb.md#14800012-结果集为空或指定位置不合法) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## getRowsData

```TypeScript
getRowsData(maxCount: number, position?: number): Promise<RowsData>
```

从指定位置position开始，最多获取maxCount行数据。使用Promise异步回调。禁止与[LiteResultSet](#LiteResultSet)的其他接口并发调用，否则 获取的数据可能非预期。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-getRowsData(maxCount: int, position?: int): Promise<RowsData>--><!--Device-LiteResultSet-getRowsData(maxCount: int, position?: int): Promise<RowsData>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| maxCount | number | 是 |
| position | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[RowsData](arkts-arkdata-relationalstore-rowsdata-t.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800019](../errorcode-data-rdb.md#14800019-sql必须是查询语句) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800012](../errorcode-data-rdb.md#14800012-结果集为空或指定位置不合法) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## getString

```TypeScript
getString(columnIndex: number): string
```

以字符串形式获取当前行中指定列的值。 如果当前列中的值为INTEGER、DOUBLE、TEXT、BLOB类型，会以字符串形式返回指定值；如果该列内容为空，则会返回空字符串""。 如果当前列中的值为DOUBLE类型，可能存在精度的丢失，建议使用[getDouble](#getDouble)接口获取。 如果当前列的数据类型为ASSET、ASSETS、FLOATVECTOR、BIGINT类型，会返回14800041。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-getString(columnIndex: int): string--><!--Device-LiteResultSet-getString(columnIndex: int): string-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [14800041](../errorcode-data-rdb.md#14800041-类型转换失败) |
| [14800013](../errorcode-data-rdb.md#14800013-列号越界或列类型与当前调用接口不兼容) |
| [14800012](../errorcode-data-rdb.md#14800012-结果集为空或指定位置不合法) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## getValue

```TypeScript
getValue(columnIndex: number): ValueType
```

获取当前行中指定列的值。 如果值类型为INTEGER，值大于Number.MAX_SAFE_INTEGER或小于Number.MIN_SAFE_INTEGER时，如果不希望丢失精度，建议使用 [getString](#getString)接口获取。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-getValue(columnIndex: int): ValueType--><!--Device-LiteResultSet-getValue(columnIndex: int): ValueType-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800013](../errorcode-data-rdb.md#14800013-列号越界或列类型与当前调用接口不兼容) |
| [14800012](../errorcode-data-rdb.md#14800012-结果集为空或指定位置不合法) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## goToNextRow

```TypeScript
goToNextRow(): boolean
```

移动结果集到下一行。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-goToNextRow(): boolean--><!--Device-LiteResultSet-goToNextRow(): boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800019](../errorcode-data-rdb.md#14800019-sql必须是查询语句) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800012](../errorcode-data-rdb.md#14800012-结果集为空或指定位置不合法) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## isColumnNull

```TypeScript
isColumnNull(columnIndex: number): boolean
```

检查当前行中指定列的值是否为null。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiteResultSet-isColumnNull(columnIndex: int): boolean--><!--Device-LiteResultSet-isColumnNull(columnIndex: int): boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800019](../errorcode-data-rdb.md#14800019-sql必须是查询语句) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800013](../errorcode-data-rdb.md#14800013-列号越界或列类型与当前调用接口不兼容) |
| [14800012](../errorcode-data-rdb.md#14800012-结果集为空或指定位置不合法) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
