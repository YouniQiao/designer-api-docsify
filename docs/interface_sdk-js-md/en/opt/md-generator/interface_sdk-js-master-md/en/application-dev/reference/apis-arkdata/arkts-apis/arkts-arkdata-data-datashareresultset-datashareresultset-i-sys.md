# DataShareResultSet (System API)

Provides APIs for accessing the result sets returned.

The column or key names are returned as a string array, in which the strings are in the same order as the columns or keys in the result set.

**Since:** 9

<!--Device-unnamed-export default interface DataShareResultSet--><!--Device-unnamed-export default interface DataShareResultSet-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { DataType } from 'kits/@kit.ArkData';
```

## close

```TypeScript
close(): void
```

Closes this result set.

Calling this API will invalidate the result set and release all its resources.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-close(): void--><!--Device-DataShareResultSet-close(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

## Examples

```TypeScript
if (resultSet != undefined) {
  (resultSet as DataShareResultSet).close();
}
```

## getBlob

```TypeScript
getBlob(columnIndex: number): Uint8Array
```

Obtains the value in the form of a byte array based on the specified column and the current row.

If the specified column or key is empty or the value is not of the Blob type, you need to determine whether to throw an exception.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-getBlob(columnIndex: int): Uint8Array--><!--Device-DataShareResultSet-getBlob(columnIndex: int): Uint8Array-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

## Examples

```TypeScript
let columnIndex = 1;
if (resultSet != undefined) {
  let goToFirstRow = (resultSet as DataShareResultSet).goToFirstRow();
  if (!goToFirstRow) {
    console.error("failed to go to first row");
  } else {
    let getBlob = (resultSet as DataShareResultSet).getBlob(columnIndex);
    console.info('resultSet.getBlob: ' + getBlob);
  }
}
```

## getColumnIndex

```TypeScript
getColumnIndex(columnName: string): number
```

Obtains the column index based on a column name.

The column name is passed in as an input parameter.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-getColumnIndex(columnName: string): int--><!--Device-DataShareResultSet-getColumnIndex(columnName: string): int-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let ColumnName = "name";
if (resultSet != undefined) {
  let getColumnIndex = (resultSet as DataShareResultSet).getColumnIndex(ColumnName);
  console.info('resultSet.getColumnIndex: ' + getColumnIndex);
}
```

## getColumnName

```TypeScript
getColumnName(columnIndex: number): string
```

Obtains the column name based on a column index.

The column index is passed in as an input parameter.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-getColumnName(columnIndex: int): string--><!--Device-DataShareResultSet-getColumnName(columnIndex: int): string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
let columnIndex = 1;
if (resultSet != undefined) {
  let getColumnName = (resultSet as DataShareResultSet).getColumnName(columnIndex);
  console.info('resultSet.getColumnName: ' + getColumnName);
}
```

## getDataType

```TypeScript
getDataType(columnIndex: number): DataType
```

Obtains the data type based on the specified column index.

If the specified column or key is empty or the value is not of the DataType type, you need to determine whether to throw an exception.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-getDataType(columnIndex: int): DataType--><!--Device-DataShareResultSet-getDataType(columnIndex: int): DataType-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-datatype-e.md) |

## Examples

```TypeScript
let columnIndex = 1;
if (resultSet != undefined) {
  let getDataType = (resultSet as DataShareResultSet).getDataType(columnIndex);
  console.info('resultSet.getDataType: ' + getDataType);
}
```

## getDouble

```TypeScript
getDouble(columnIndex: number): number
```

Obtains the value in the form of a double-precision floating-point number based on the specified column and the current row.

If the specified column or key is empty or the value is not of the double type, you need to determine whether to throw an exception.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-getDouble(columnIndex: int): double--><!--Device-DataShareResultSet-getDouble(columnIndex: int): double-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let columnIndex = 1;
if (resultSet != undefined) {
  let goToFirstRow = (resultSet as DataShareResultSet).goToFirstRow();
  let getDouble = (resultSet as DataShareResultSet).getDouble(columnIndex);
  console.info('resultSet.getDouble: ' + getDouble);
}
```

## getLong

```TypeScript
getLong(columnIndex: number): number
```

Obtains the value in the form of a long integer based on the specified column and the current row.

If the specified column or key is empty or the value is not of the long type, you need to determine whether to throw an exception.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-getLong(columnIndex: int): long--><!--Device-DataShareResultSet-getLong(columnIndex: int): long-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let columnIndex = 1;
if (resultSet != undefined) {
  let goToFirstRow = (resultSet as DataShareResultSet).goToFirstRow();
  let getLong = (resultSet as DataShareResultSet).getLong(columnIndex);
  console.info('resultSet.getLong: ' + getLong);
}
```

## getString

```TypeScript
getString(columnIndex: number): string
```

Obtains the value in the form of a string based on the specified column and the current row.

If the specified column or key is empty or the value is not of the string type, you need to determine whether to throw an exception.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-getString(columnIndex: int): string--><!--Device-DataShareResultSet-getString(columnIndex: int): string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
let columnIndex = 1;
if (resultSet != undefined) {
  let goToFirstRow = (resultSet as DataShareResultSet).goToFirstRow();
  let getString = (resultSet as DataShareResultSet).getString(columnIndex);
  console.info('resultSet.getString: ' + getString);
}
```

## goTo

```TypeScript
goTo(offset: number): boolean
```

Moves based on the specified offset.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-goTo(offset: int): boolean--><!--Device-DataShareResultSet-goTo(offset: int): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let goToNum = 1;
if (resultSet != undefined) {
  let isGoTo = (resultSet as DataShareResultSet).goTo(goToNum);
  console.info('resultSet.goTo: ' + isGoTo);
}
```

## goToFirstRow

```TypeScript
goToFirstRow(): boolean
```

Moves to the first row of the result set.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-goToFirstRow(): boolean--><!--Device-DataShareResultSet-goToFirstRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
// Create a resultSet object. For details, see Usage in this topic.
if (resultSet != undefined) {
  let isGoToFirstRow = (resultSet as DataShareResultSet).goToFirstRow();
  console.info('resultSet.goToFirstRow: ' + isGoToFirstRow);
}
```

## goToLastRow

```TypeScript
goToLastRow(): boolean
```

Moves to the last row of the result set.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-goToLastRow(): boolean--><!--Device-DataShareResultSet-goToLastRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
if (resultSet != undefined) {
  let isGoToLastRow = (resultSet as DataShareResultSet).goToLastRow();
  console.info('resultSet.goToLastRow: ' + isGoToLastRow);
}
```

## goToNextRow

```TypeScript
goToNextRow(): boolean
```

Moves to the next row in the result set.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-goToNextRow(): boolean--><!--Device-DataShareResultSet-goToNextRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
if (resultSet != undefined) {
  let isGoToNextRow = (resultSet as DataShareResultSet).goToNextRow();
  console.info('resultSet.goToNextRow: ' + isGoToNextRow);
}
```

## goToPreviousRow

```TypeScript
goToPreviousRow(): boolean
```

Moves to the previous row in the result set.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-goToPreviousRow(): boolean--><!--Device-DataShareResultSet-goToPreviousRow(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
if (resultSet != undefined) {
  let isGoToPreviousRow = (resultSet as DataShareResultSet).goToPreviousRow();
  console.info('resultSet.goToPreviousRow: ' + isGoToPreviousRow);
}
```

## goToRow

```TypeScript
goToRow(position: number): boolean
```

Moves to the specified row in the result set.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-goToRow(position: int): boolean--><!--Device-DataShareResultSet-goToRow(position: int): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let goToRowNum = 2;
if (resultSet != undefined) {
  let isGoToRow = (resultSet as DataShareResultSet).goToRow(goToRowNum);
  console.info('resultSet.goToRow: ' + isGoToRow);
}
```

## columnCount

```TypeScript
columnCount: number
```

Number of columns in the result set.

**Type:** number

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-columnCount: int--><!--Device-DataShareResultSet-columnCount: int-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

## columnNames

```TypeScript
columnNames: Array<string>
```

Names of all columns in the result set.

**Type:** Array&lt;string&gt;

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-columnNames: Array<string>--><!--Device-DataShareResultSet-columnNames: Array<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

## isClosed

```TypeScript
isClosed: boolean
```

Whether the result set is closed. The value **true** means the result set is closed; the value **false** means the opposite.

**Type:** boolean

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-isClosed: boolean--><!--Device-DataShareResultSet-isClosed: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

## rowCount

```TypeScript
rowCount: number
```

Number of rows in the result set.

**Type:** number

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareResultSet-rowCount: int--><!--Device-DataShareResultSet-rowCount: int-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.
