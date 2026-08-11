# ResultSet

结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。

> **说明：**
> 
> 从API Version 9开始，该接口不再维护，推荐使用新接口[ResultSet](arkts-arkdata-relationalstore-resultset-i.md)。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [@ohos.data.relationalStore:relationalStore](arkts-data-relationalstore.md)

<!--Device-unnamed-export interface ResultSet--><!--Device-unnamed-export interface ResultSet-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## close

```TypeScript
close(): void
```

关闭结果集。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.close

<!--Device-ResultSet-close(): void--><!--Device-ResultSet-close(): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## getBlob

```TypeScript
getBlob(columnIndex: number): Uint8Array
```

以字节数组的形式获取当前行中指定列的值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.getBlob

<!--Device-ResultSet-getBlob(columnIndex: number): Uint8Array--><!--Device-ResultSet-getBlob(columnIndex: number): Uint8Array-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| columnIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

## getColumnIndex

```TypeScript
getColumnIndex(columnName: string): number
```

根据指定的列名获取列索引。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.getColumnIndex

<!--Device-ResultSet-getColumnIndex(columnName: string): number--><!--Device-ResultSet-getColumnIndex(columnName: string): number-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| columnName | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getColumnName

```TypeScript
getColumnName(columnIndex: number): string
```

根据指定的列索引获取列名。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.getColumnName

<!--Device-ResultSet-getColumnName(columnIndex: number): string--><!--Device-ResultSet-getColumnName(columnIndex: number): string-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| columnIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## getDouble

```TypeScript
getDouble(columnIndex: number): number
```

以double形式获取当前行中指定列的值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.getDouble

<!--Device-ResultSet-getDouble(columnIndex: number): number--><!--Device-ResultSet-getDouble(columnIndex: number): number-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| columnIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getLong

```TypeScript
getLong(columnIndex: number): number
```

以Long形式获取当前行中指定列的值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.getLong

<!--Device-ResultSet-getLong(columnIndex: number): number--><!--Device-ResultSet-getLong(columnIndex: number): number-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| columnIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getString

```TypeScript
getString(columnIndex: number): string
```

以字符串形式获取当前行中指定列的值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.getString

<!--Device-ResultSet-getString(columnIndex: number): string--><!--Device-ResultSet-getString(columnIndex: number): string-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| columnIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## goTo

```TypeScript
goTo(offset: number): boolean
```

向前或向后移至结果集的指定行，相对于其当前位置偏移。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.goTo

<!--Device-ResultSet-goTo(offset: number): boolean--><!--Device-ResultSet-goTo(offset: number): boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## goToFirstRow

```TypeScript
goToFirstRow(): boolean
```

转到结果集的第一行。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.goToFirstRow

<!--Device-ResultSet-goToFirstRow(): boolean--><!--Device-ResultSet-goToFirstRow(): boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## goToLastRow

```TypeScript
goToLastRow(): boolean
```

转到结果集的最后一行。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.goToLastRow

<!--Device-ResultSet-goToLastRow(): boolean--><!--Device-ResultSet-goToLastRow(): boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## goToNextRow

```TypeScript
goToNextRow(): boolean
```

转到结果集的下一行。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.goToNextRow

<!--Device-ResultSet-goToNextRow(): boolean--><!--Device-ResultSet-goToNextRow(): boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## goToPreviousRow

```TypeScript
goToPreviousRow(): boolean
```

转到结果集的上一行。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.goToPreviousRow

<!--Device-ResultSet-goToPreviousRow(): boolean--><!--Device-ResultSet-goToPreviousRow(): boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## goToRow

```TypeScript
goToRow(position: number): boolean
```

转到结果集的指定行。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.goToRow

<!--Device-ResultSet-goToRow(position: number): boolean--><!--Device-ResultSet-goToRow(position: number): boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isColumnNull

```TypeScript
isColumnNull(columnIndex: number): boolean
```

检查当前行中指定列的值是否为null。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.isColumnNull

<!--Device-ResultSet-isColumnNull(columnIndex: number): boolean--><!--Device-ResultSet-isColumnNull(columnIndex: number): boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| columnIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## columnCount

```TypeScript
columnCount: number
```

columnCount: number

获取结果集中的列数。

**类型：** number

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.columnCount

<!--Device-ResultSet-columnCount: number--><!--Device-ResultSet-columnCount: number-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## columnNames

```TypeScript
columnNames: Array<string>
```

columnNames: Array&lt;string&gt;

获取结果集中所有列的名称。

**类型：** Array&lt;string&gt;

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.columnNames

<!--Device-ResultSet-columnNames: Array<string>--><!--Device-ResultSet-columnNames: Array<string>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## isAtFirstRow

```TypeScript
isAtFirstRow: boolean
```

isAtFirstRow: boolean

检查结果集是否位于第一行。

**类型：** boolean

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.isAtFirstRow

<!--Device-ResultSet-isAtFirstRow: boolean--><!--Device-ResultSet-isAtFirstRow: boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## isAtLastRow

```TypeScript
isAtLastRow: boolean
```

isAtLastRow: boolean

检查结果集是否位于最后一行。

**类型：** boolean

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.isAtLastRow

<!--Device-ResultSet-isAtLastRow: boolean--><!--Device-ResultSet-isAtLastRow: boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## isClosed

```TypeScript
isClosed: boolean
```

isClosed: boolean

检查当前结果集是否关闭。

**类型：** boolean

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.isClosed

<!--Device-ResultSet-isClosed: boolean--><!--Device-ResultSet-isClosed: boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## isEnded

```TypeScript
isEnded: boolean
```

isEnded: boolean

检查结果集是否位于最后一行之后。

**类型：** boolean

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.isEnded

<!--Device-ResultSet-isEnded: boolean--><!--Device-ResultSet-isEnded: boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## isStarted

```TypeScript
isStarted: boolean
```

isStarted: boolean

检查指针是否移动过。

**类型：** boolean

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.isStarted

<!--Device-ResultSet-isStarted: boolean--><!--Device-ResultSet-isStarted: boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## rowCount

```TypeScript
rowCount: number
```

rowCount: number

获取结果集中的行数。

**类型：** number

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.rowCount

<!--Device-ResultSet-rowCount: number--><!--Device-ResultSet-rowCount: number-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## rowIndex

```TypeScript
rowIndex: number
```

rowIndex: number

获取结果集当前行的索引。

**类型：** number

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.data.relationalStore.ResultSet.rowIndex

<!--Device-ResultSet-rowIndex: number--><!--Device-ResultSet-rowIndex: number-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core
