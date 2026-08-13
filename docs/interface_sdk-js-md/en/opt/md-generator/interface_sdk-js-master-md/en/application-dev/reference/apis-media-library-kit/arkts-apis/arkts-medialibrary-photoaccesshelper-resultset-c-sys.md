# ResultSet (System API)

Defines APIs to access the result set obtained by querying the RDB store. Before calling any of the following APIs, you must use [query](arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#query) to obtain a ResultSet instance.

**Since:** 23

**Deprecated since:** -1

<!--Device-photoAccessHelper-class ResultSet--><!--Device-photoAccessHelper-class ResultSet-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## close

```TypeScript
close(): void
```

Closes this resultSet to release memory. If it is not closed, memory leaks may occur.

**Since:** 23

**Deprecated since:** -1

<!--Device-ResultSet-close(): void--><!--Device-ResultSet-close(): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('close');
  try {
    let resultSet: photoAccessHelper.ResultSet = await phAccessHelper.query('SELECT * from Photos');
    resultSet.close();
  } catch (err) {
    console.error(`close failed with error: ${err.code}, ${err.message}`);
  }
}
```

## getRow

```TypeScript
getRow(): ValuesBucket
```

Obtains the values of all columns in the specified row.

**Since:** 23

**Deprecated since:** -1

<!--Device-ResultSet-getRow(): ValuesBucket--><!--Device-ResultSet-getRow(): ValuesBucket-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ValuesBucket](../../apis-arkdata/arkts-apis/arkts-arkdata-rdb-valuesbucket-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getRow');
  try {
    let resultSet: photoAccessHelper.ResultSet = await phAccessHelper.query('SELECT * from Photos');
    resultSet.goToFirstRow();
    const row = resultSet.getRow();
    resultSet.close();
  } catch (err) {
    console.error(`getRow failed with error: ${err.code}, ${err.message}`);
  }
}
```

## getValue

```TypeScript
getValue(columnIndex: number): ValueType
```

Obtains the value of the specified column in the current row.

**Since:** 23

**Deprecated since:** -1

<!--Device-ResultSet-getValue(columnIndex: int): ValueType--><!--Device-ResultSet-getValue(columnIndex: int): ValueType-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

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
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getValue');
  try {
    let resultSet: photoAccessHelper.ResultSet = await phAccessHelper.query('SELECT * from Photos');
    resultSet.goToFirstRow();
    const codes = resultSet.getValue(0);
    resultSet.close();
  } catch (err) {
    console.error(`getValue failed with error: ${err.code}, ${err.message}`);
  }
}
```

## goToFirstRow

```TypeScript
goToFirstRow(): boolean
```

Moves the cursor to the first row of the result set.

**Since:** 23

**Deprecated since:** -1

<!--Device-ResultSet-goToFirstRow(): boolean--><!--Device-ResultSet-goToFirstRow(): boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('goToFirstRow');
  try {
    let resultSet: photoAccessHelper.ResultSet = await phAccessHelper.query('SELECT * from Photos');
    resultSet.goToFirstRow();
    resultSet.close();
  } catch (err) {
    console.error(`goToFirstRow failed with error: ${err.code}, ${err.message}`);
  }
}
```

## goToNextRow

```TypeScript
goToNextRow(): boolean
```

Moves the cursor to the next row in the result set.

**Since:** 23

**Deprecated since:** -1

<!--Device-ResultSet-goToNextRow(): boolean--><!--Device-ResultSet-goToNextRow(): boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('goToNextRow');
  try {
    let resultSet: photoAccessHelper.ResultSet = await phAccessHelper.query('SELECT * from Photos');
    resultSet.goToNextRow();
    resultSet.close();
  } catch (err) {
    console.error(`goToNextRow failed with error: ${err.code}, ${err.message}`);
  }
}
```

## goToRow

```TypeScript
goToRow(position: number): boolean
```

Moves the cursor to the specified row in the result set.

**Since:** 23

**Deprecated since:** -1

<!--Device-ResultSet-goToRow(position: int): boolean--><!--Device-ResultSet-goToRow(position: int): boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

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
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [23800151](../errorcode-medialibrary.md#23800151-failed-to-verify-scene-parameters) |

## Examples

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('goToRow');
  try {
    let resultSet: photoAccessHelper.ResultSet = await phAccessHelper.query('SELECT * from Photos');
    resultSet.goToRow(0);
    resultSet.close();
  } catch (err) {
    console.error(`goToRow failed with error: ${err.code}, ${err.message}`);
  }
}
```

## columnCount

```TypeScript
columnCount: number
```

Number of columns in the result set.

**Type:** number

**Since:** 23

**Deprecated since:** -1

<!--Device-ResultSet-columnCount: int--><!--Device-ResultSet-columnCount: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## isAtLastRow

```TypeScript
isAtLastRow: boolean
```

Whether the cursor is in the last row of the result set. **true** if the cursor is in the last row; **false** otherwise.

**Type:** boolean

**Since:** 23

**Deprecated since:** -1

<!--Device-ResultSet-isAtLastRow: boolean--><!--Device-ResultSet-isAtLastRow: boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## rowCount

```TypeScript
rowCount: number
```

Number of rows in the result set.

**Type:** number

**Since:** 23

**Deprecated since:** -1

<!--Device-ResultSet-rowCount: int--><!--Device-ResultSet-rowCount: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## rowIndex

```TypeScript
rowIndex: number
```

Index of the current row in the result set.

**Type:** number

**Since:** 23

**Deprecated since:** -1

<!--Device-ResultSet-rowIndex: int--><!--Device-ResultSet-rowIndex: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.
