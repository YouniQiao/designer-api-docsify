# ResultSet

结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。

> **说明：**
> 
> 从API Version 9开始，该接口不再维护，推荐使用新接口[ResultSet](arkts-arkdata-relationalstore-resultset-i.md#ResultSet)。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [relationalStore](arkts-data-relationalstore.md#relationalStore)

<!--Device-unnamed-export interface ResultSet--><!--Device-unnamed-export interface ResultSet-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## close

```TypeScript
close(): void
```

关闭结果集。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [close](ohos.data.relationalStore.ResultSet.close)

<!--Device-ResultSet-close(): void--><!--Device-ResultSet-close(): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## 示例

```TypeScript
let predicatesClose = new dataRdb.RdbPredicates("EMPLOYEE");
let promiseClose = rdbStore.query(predicatesClose, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
promiseClose.then((resultSet) => {
  resultSet.close();
}).catch((err) => {
  console.error('resultset close failed');
});
```

## getBlob

```TypeScript
getBlob(columnIndex: number): Uint8Array
```

以字节数组的形式获取当前行中指定列的值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getBlob](ohos.data.relationalStore.ResultSet.getBlob)

<!--Device-ResultSet-getBlob(columnIndex: number): Uint8Array--><!--Device-ResultSet-getBlob(columnIndex: number): Uint8Array-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

## 示例

```TypeScript
const codes = resultSet.getBlob(resultSet.getColumnIndex("CODES"));
```

## getColumnIndex

```TypeScript
getColumnIndex(columnName: string): number
```

根据指定的列名获取列索引。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getColumnIndex](ohos.data.relationalStore.ResultSet.getColumnIndex)

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

## 示例

```TypeScript
const success = resultSet.goToFirstRow();
if (success) {
  const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
  const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
  const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
  const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
}
```

## getColumnName

```TypeScript
getColumnName(columnIndex: number): string
```

根据指定的列索引获取列名。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getColumnName](ohos.data.relationalStore.ResultSet.getColumnName)

<!--Device-ResultSet-getColumnName(columnIndex: number): string--><!--Device-ResultSet-getColumnName(columnIndex: number): string-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## 示例

```TypeScript
const id = resultSet.getColumnName(0);
const name = resultSet.getColumnName(1);
const age = resultSet.getColumnName(2);
```

## getDouble

```TypeScript
getDouble(columnIndex: number): number
```

以double形式获取当前行中指定列的值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getDouble](ohos.data.relationalStore.ResultSet.getDouble)

<!--Device-ResultSet-getDouble(columnIndex: number): number--><!--Device-ResultSet-getDouble(columnIndex: number): number-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
```

## getLong

```TypeScript
getLong(columnIndex: number): number
```

以Long形式获取当前行中指定列的值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getLong](ohos.data.relationalStore.ResultSet.getLong)

<!--Device-ResultSet-getLong(columnIndex: number): number--><!--Device-ResultSet-getLong(columnIndex: number): number-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
```

## getString

```TypeScript
getString(columnIndex: number): string
```

以字符串形式获取当前行中指定列的值。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getString](ohos.data.relationalStore.ResultSet.getString)

<!--Device-ResultSet-getString(columnIndex: number): string--><!--Device-ResultSet-getString(columnIndex: number): string-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## 示例

```TypeScript
const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
```

## goTo

```TypeScript
goTo(offset: number): boolean
```

向前或向后移至结果集的指定行，相对于其当前位置偏移。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [goTo](ohos.data.relationalStore.ResultSet.goTo)

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

## 示例

```TypeScript
let predicatesgoto = new dataRdb.RdbPredicates("EMPLOYEE");
let promisequerygoto = rdbStore.query(predicatesgoto, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
promisequerygoto.then((resultSet) => {
  resultSet.goTo(1);
  resultSet.close();
}).catch((err) => {
  console.error('query failed');
});
```

## goToFirstRow

```TypeScript
goToFirstRow(): boolean
```

转到结果集的第一行。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [goToFirstRow](ohos.data.relationalStore.ResultSet.goToFirstRow)

<!--Device-ResultSet-goToFirstRow(): boolean--><!--Device-ResultSet-goToFirstRow(): boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
let predicatesgoFirst = new dataRdb.RdbPredicates("EMPLOYEE");
let promisequerygoFirst = rdbStore.query(predicatesgoFirst, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
promisequerygoFirst.then((resultSet) => {
  resultSet.goToFirstRow();
  resultSet.close();
}).catch((err) => {
  console.error('query failed');
});
```

## goToLastRow

```TypeScript
goToLastRow(): boolean
```

转到结果集的最后一行。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [goToLastRow](ohos.data.relationalStore.ResultSet.goToLastRow)

<!--Device-ResultSet-goToLastRow(): boolean--><!--Device-ResultSet-goToLastRow(): boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
let predicatesgoLast = new dataRdb.RdbPredicates("EMPLOYEE");
let promisequerygoLast = rdbStore.query(predicatesgoLast, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
promisequerygoLast.then((resultSet) => {
  resultSet.goToLastRow();
  resultSet.close();
}).catch((err) => {
  console.error('query failed');
});
```

## goToNextRow

```TypeScript
goToNextRow(): boolean
```

转到结果集的下一行。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [goToNextRow](ohos.data.relationalStore.ResultSet.goToNextRow)

<!--Device-ResultSet-goToNextRow(): boolean--><!--Device-ResultSet-goToNextRow(): boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
let predicatesgoNext = new dataRdb.RdbPredicates("EMPLOYEE");
let promisequerygoNext = rdbStore.query(predicatesgoNext, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
promisequerygoNext.then((resultSet) => {
  resultSet.close();
}).catch((err) => {
  console.error('query failed');
});
```

## goToPreviousRow

```TypeScript
goToPreviousRow(): boolean
```

转到结果集的上一行。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [goToPreviousRow](ohos.data.relationalStore.ResultSet.goToPreviousRow)

<!--Device-ResultSet-goToPreviousRow(): boolean--><!--Device-ResultSet-goToPreviousRow(): boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
let predicatesgoPrev = new dataRdb.RdbPredicates("EMPLOYEE");
let promisequerygoPrev = rdbStore.query(predicatesgoPrev, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
promisequerygoPrev.then((resultSet) => {
  resultSet.close();
}).catch((err) => {
  console.error('query failed');
});
```

## goToRow

```TypeScript
goToRow(position: number): boolean
```

转到结果集的指定行。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [goToRow](ohos.data.relationalStore.ResultSet.goToRow)

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

## 示例

```TypeScript
let predicatesgotorow = new dataRdb.RdbPredicates("EMPLOYEE");
let promisequerygotorow = rdbStore.query(predicatesgotorow, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
promisequerygotorow.then((resultSet) => {
  resultSet.goToRow(5);
  resultSet.close();
}).catch((err) => {
  console.error('query failed');
});
```

## isColumnNull

```TypeScript
isColumnNull(columnIndex: number): boolean
```

检查当前行中指定列的值是否为null。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isColumnNull](ohos.data.relationalStore.ResultSet.isColumnNull)

<!--Device-ResultSet-isColumnNull(columnIndex: number): boolean--><!--Device-ResultSet-isColumnNull(columnIndex: number): boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
const isColumnNull = resultSet.isColumnNull(resultSet.getColumnIndex("CODES"));
```

## columnCount

```TypeScript
columnCount: number
```

columnCount: number

获取结果集中的列数。

**类型：** number

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [columnCount](ohos.data.relationalStore.ResultSet.columnCount)

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

**替代接口：** [columnNames](ohos.data.relationalStore.ResultSet.columnNames)

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

**替代接口：** [isAtFirstRow](ohos.data.relationalStore.ResultSet.isAtFirstRow)

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

**替代接口：** [isAtLastRow](ohos.data.relationalStore.ResultSet.isAtLastRow)

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

**替代接口：** [isClosed](ohos.data.relationalStore.ResultSet.isClosed)

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

**替代接口：** [isEnded](ohos.data.relationalStore.ResultSet.isEnded)

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

**替代接口：** [isStarted](ohos.data.relationalStore.ResultSet.isStarted)

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

**替代接口：** [rowCount](ohos.data.relationalStore.ResultSet.rowCount)

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

**替代接口：** [rowIndex](ohos.data.relationalStore.ResultSet.rowIndex)

<!--Device-ResultSet-rowIndex: number--><!--Device-ResultSet-rowIndex: number-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core
