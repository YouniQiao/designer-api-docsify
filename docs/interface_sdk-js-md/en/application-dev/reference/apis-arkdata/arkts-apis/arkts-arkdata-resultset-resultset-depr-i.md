# ResultSet

A result set is a set of results returned after the relational database (RDB) query APIs are called. You can use the **resultset** APIs to obtain required data.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [relationalStore](arkts-data-relationalstore.md)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## close

```TypeScript
close(): void
```

Closes this result set.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** close

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## getBlob

```TypeScript
getBlob(columnIndex: number): Uint8Array
```

Obtains the value from the specified column in the current row as a byte array.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** getBlob

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | Yes |

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

**Substitutes:** getColumnIndex

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

**Substitutes:** getColumnName

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | Yes |

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

**Substitutes:** getDouble

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | Yes |

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

**Substitutes:** getLong

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | Yes |

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

**Substitutes:** getString

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | Yes |

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

**Substitutes:** goTo

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

**Substitutes:** goToFirstRow

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

**Substitutes:** goToLastRow

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

**Substitutes:** goToNextRow

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

**Substitutes:** goToPreviousRow

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

**Substitutes:** goToRow

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

**Substitutes:** isColumnNull

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | Yes |

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

**Substitutes:** columnCount

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## columnNames

```TypeScript
columnNames: Array<string>
```

Names of all columns in the result set.

**Type:** Array&lt;string&gt;

**Since:** 7

**Deprecated since:** 9

**Substitutes:** columnNames

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isAtFirstRow

```TypeScript
isAtFirstRow: boolean
```

Whether the cursor is in the first row of the result set.

**Type:** boolean

**Since:** 7

**Deprecated since:** 9

**Substitutes:** isAtFirstRow

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isAtLastRow

```TypeScript
isAtLastRow: boolean
```

Whether the cursor is in the last row of the result set.

**Type:** boolean

**Since:** 7

**Deprecated since:** 9

**Substitutes:** isAtLastRow

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isClosed

```TypeScript
isClosed: boolean
```

Whether the result set is closed.

**Type:** boolean

**Since:** 7

**Deprecated since:** 9

**Substitutes:** isClosed

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isEnded

```TypeScript
isEnded: boolean
```

Whether the cursor is after the last row of the result set.

**Type:** boolean

**Since:** 7

**Deprecated since:** 9

**Substitutes:** isEnded

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## isStarted

```TypeScript
isStarted: boolean
```

Whether the cursor has been moved.

**Type:** boolean

**Since:** 7

**Deprecated since:** 9

**Substitutes:** isStarted

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## rowCount

```TypeScript
rowCount: number
```

Number of rows in the result set.

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** rowCount

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## rowIndex

```TypeScript
rowIndex: number
```

Index of the current row in the result set.

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** rowIndex

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core
