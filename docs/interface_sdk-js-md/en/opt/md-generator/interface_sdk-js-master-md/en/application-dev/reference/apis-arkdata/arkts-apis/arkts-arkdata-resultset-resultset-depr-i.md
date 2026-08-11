# ResultSet

A result set is a set of results returned after the relational database (RDB) query APIs are called. You can use the  
**resultset** APIs to obtain required data.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.data.relationalStore:relationalStore](arkts-data-relationalstore.md)

<!--Device-unnamed-export interface ResultSet--><!--Device-unnamed-export interface ResultSet-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## close

```TypeScript
close(): void
```

Closes this result set.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.close

<!--Device-ResultSet-close(): void--><!--Device-ResultSet-close(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## getBlob

```TypeScript
getBlob(columnIndex: number): Uint8Array
```

Obtains the value from the specified column in the current row as a byte array.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.getBlob

<!--Device-ResultSet-getBlob(columnIndex: number): Uint8Array--><!--Device-ResultSet-getBlob(columnIndex: number): Uint8Array-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

## getColumnIndex

```TypeScript
getColumnIndex(columnName: string): number
```

Obtains the column index based on the column name.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.getColumnIndex

<!--Device-ResultSet-getColumnIndex(columnName: string): number--><!--Device-ResultSet-getColumnIndex(columnName: string): number-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getColumnName

```TypeScript
getColumnName(columnIndex: number): string
```

Obtains the column name based on the column index.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.getColumnName

<!--Device-ResultSet-getColumnName(columnIndex: number): string--><!--Device-ResultSet-getColumnName(columnIndex: number): string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getDouble

```TypeScript
getDouble(columnIndex: number): number
```

Obtains the value from the specified column in the current row as a Double.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.getDouble

<!--Device-ResultSet-getDouble(columnIndex: number): number--><!--Device-ResultSet-getDouble(columnIndex: number): number-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getLong

```TypeScript
getLong(columnIndex: number): number
```

Obtains the value from the specified column in the current row as a Long.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.getLong

<!--Device-ResultSet-getLong(columnIndex: number): number--><!--Device-ResultSet-getLong(columnIndex: number): number-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getString

```TypeScript
getString(columnIndex: number): string
```

Obtains the value from the specified column in the current row as a string.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.getString

<!--Device-ResultSet-getString(columnIndex: number): string--><!--Device-ResultSet-getString(columnIndex: number): string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## goTo

```TypeScript
goTo(offset: number): boolean
```

Moves the result set forward or backward to the specified row with an offset relative to the current position.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.goTo

<!--Device-ResultSet-goTo(offset: number): boolean--><!--Device-ResultSet-goTo(offset: number): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## goToFirstRow

```TypeScript
goToFirstRow(): boolean
```

Moves the cursor to the first row of the result set.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.goToFirstRow

<!--Device-ResultSet-goToFirstRow(): boolean--><!--Device-ResultSet-goToFirstRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## goToLastRow

```TypeScript
goToLastRow(): boolean
```

Moves the cursor to the last row of the result set.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.goToLastRow

<!--Device-ResultSet-goToLastRow(): boolean--><!--Device-ResultSet-goToLastRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## goToNextRow

```TypeScript
goToNextRow(): boolean
```

Moves the cursor to the next row in the result set.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.goToNextRow

<!--Device-ResultSet-goToNextRow(): boolean--><!--Device-ResultSet-goToNextRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## goToPreviousRow

```TypeScript
goToPreviousRow(): boolean
```

Moves the cursor to the previous row in the result set.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.goToPreviousRow

<!--Device-ResultSet-goToPreviousRow(): boolean--><!--Device-ResultSet-goToPreviousRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## goToRow

```TypeScript
goToRow(position: number): boolean
```

Moves the cursor to the specified row in the result set.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.goToRow

<!--Device-ResultSet-goToRow(position: number): boolean--><!--Device-ResultSet-goToRow(position: number): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isColumnNull

```TypeScript
isColumnNull(columnIndex: number): boolean
```

Checks whether the value in the specified column of the current row is null.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.isColumnNull

<!--Device-ResultSet-isColumnNull(columnIndex: number): boolean--><!--Device-ResultSet-isColumnNull(columnIndex: number): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## columnCount

```TypeScript
columnCount: number
```

Number of columns in the result set.

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.columnCount

<!--Device-ResultSet-columnCount: number--><!--Device-ResultSet-columnCount: number-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## columnNames

```TypeScript
columnNames: Array<string>
```

Names of all columns in the result set.

**Type:** Array&lt;string&gt;

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.columnNames

<!--Device-ResultSet-columnNames: Array<string>--><!--Device-ResultSet-columnNames: Array<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isAtFirstRow

```TypeScript
isAtFirstRow: boolean
```

Whether the cursor is in the first row of the result set.

**Type:** boolean

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.isAtFirstRow

<!--Device-ResultSet-isAtFirstRow: boolean--><!--Device-ResultSet-isAtFirstRow: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isAtLastRow

```TypeScript
isAtLastRow: boolean
```

Whether the cursor is in the last row of the result set.

**Type:** boolean

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.isAtLastRow

<!--Device-ResultSet-isAtLastRow: boolean--><!--Device-ResultSet-isAtLastRow: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isClosed

```TypeScript
isClosed: boolean
```

Whether the result set is closed.

**Type:** boolean

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.isClosed

<!--Device-ResultSet-isClosed: boolean--><!--Device-ResultSet-isClosed: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isEnded

```TypeScript
isEnded: boolean
```

Whether the cursor is after the last row of the result set.

**Type:** boolean

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.isEnded

<!--Device-ResultSet-isEnded: boolean--><!--Device-ResultSet-isEnded: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isStarted

```TypeScript
isStarted: boolean
```

Whether the cursor has been moved.

**Type:** boolean

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.isStarted

<!--Device-ResultSet-isStarted: boolean--><!--Device-ResultSet-isStarted: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## rowCount

```TypeScript
rowCount: number
```

Number of rows in the result set.

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.rowCount

<!--Device-ResultSet-rowCount: number--><!--Device-ResultSet-rowCount: number-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## rowIndex

```TypeScript
rowIndex: number
```

Index of the current row in the result set.

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.data.relationalStore.ResultSet.rowIndex

<!--Device-ResultSet-rowIndex: number--><!--Device-ResultSet-rowIndex: number-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core
