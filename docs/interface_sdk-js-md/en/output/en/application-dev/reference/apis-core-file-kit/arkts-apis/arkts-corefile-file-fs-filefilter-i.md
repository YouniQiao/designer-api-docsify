# FileFilter

Describes a file name filter, which can be used to customize file name filtering rules.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export interface FileFilter--><!--Device-unnamed-export interface FileFilter-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## filter

```TypeScript
filter(name: string): boolean
```

Filters files of the [listFileExt]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or [listFileExtSync]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API and determines whether a specified file name should be included in the returned file list. > **NOTE** > > This function is frequently called. Do not perform time-consuming operations, such as file I/O operations and > network requests.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileFilter-filter(name: string): boolean--><!--Device-FileFilter-filter(name: string): boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name or relative path of the file to be filtered. In recursive mode, the value is a relative file path, which starts with a slash (/). |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the file is included in the returned file list. The value **true** indicates the file |

