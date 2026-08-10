# ResultSet（系统接口）

Defines APIs to access the result set obtained by querying the RDB store.

Before calling any of the following APIs, you must use [query](arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#query) to obtain a ResultSet instance.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-class ResultSet--><!--Device-photoAccessHelper-class ResultSet-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## close

```TypeScript
close(): void
```

Closes this resultSet to release memory. If it is not closed, memory leaks may occur.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-ResultSet-close(): void--><!--Device-ResultSet-close(): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 202 | Called by non-system application |

## 示例

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

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-ResultSet-getRow(): ValuesBucket--><!--Device-ResultSet-getRow(): ValuesBucket-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ValuesBucket](../../apis-arkdata/arkts-apis/arkts-arkdata-rdb-valuesbucket-t.md) | Values of all columns in the specified row. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 202 | Called by non-system application |

## 示例

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

ArkTS-Dyn:
```TypeScript
getValue(columnIndex: number): ValueType
```

ArkTS-Sta:
```TypeScript
getValue(columnIndex: int): ValueType
```

Obtains the value of the specified column in the current row.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-ResultSet-getValue(columnIndex: int): ValueType--><!--Device-ResultSet-getValue(columnIndex: int): ValueType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Index of the specified column, starting from 0. The value ranges from 0 to the total number of columns in the result set minus 1. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Allowed data field types. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 202 | Called by non-system application |
| 23800151 | Scene parameters validate failed, possible causes: columnIndex invalid. |

## 示例

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

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-ResultSet-goToFirstRow(): boolean--><!--Device-ResultSet-goToFirstRow(): boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Operation result. **true** if the cursor is moved to the first row; **false** otherwise. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 202 | Called by non-system application |

## 示例

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

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-ResultSet-goToNextRow(): boolean--><!--Device-ResultSet-goToNextRow(): boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Operation result. **true** if the cursor is moved to the next row; **false** otherwise. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 202 | Called by non-system application |

## 示例

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

ArkTS-Dyn:
```TypeScript
goToRow(position: number): boolean
```

ArkTS-Sta:
```TypeScript
goToRow(position: int): boolean
```

Moves the cursor to the specified row in the result set.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-ResultSet-goToRow(position: int): boolean--><!--Device-ResultSet-goToRow(position: int): boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Index of the specified row, starting from 0. The value ranges from 0 to the total number of rows in the result set minus 1. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Operation result. **true** if the cursor is moved to the specified row; **false** otherwise. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 202 | Called by non-system application |
| 23800151 | Scene parameters validate failed, possible causes: position invalid. |

## 示例

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
columnCount: int
```

Number of columns in the result set.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-ResultSet-columnCount: int--><!--Device-ResultSet-columnCount: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## isAtLastRow

```TypeScript
isAtLastRow: boolean
```

Whether the cursor is in the last row of the result set. **true** if the cursor is in the last row; **false** otherwise.

**类型：** boolean

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-ResultSet-isAtLastRow: boolean--><!--Device-ResultSet-isAtLastRow: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## rowCount

```TypeScript
rowCount: int
```

Number of rows in the result set.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-ResultSet-rowCount: int--><!--Device-ResultSet-rowCount: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## rowIndex

```TypeScript
rowIndex: int
```

Index of the current row in the result set.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-ResultSet-rowIndex: int--><!--Device-ResultSet-rowIndex: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

