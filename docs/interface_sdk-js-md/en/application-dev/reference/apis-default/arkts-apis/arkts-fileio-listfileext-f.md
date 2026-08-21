# listFileExt

## Modules to Import

```TypeScript
```

## listFileExt

```TypeScript
function listFileExt(
  path: string,
  options?: ListFileExtOptions
): Promise<string[]>
```

Lists all files in a directory. This API supports recursive listing of files and file filtering. This API uses a promise to return the result.

You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The relative path starts with a slash (/).

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileIo-function listFileExt(  path: string,  options?: ListFileExtOptions): Promise<string[]>--><!--Device-fileIo-function listFileExt(  path: string,  options?: ListFileExtOptions): Promise<string[]>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| options | [ListFileExtOptions](arkts-filefs-listfileextoptions-i.md) | No | Options for listing files. The default value is empty, indicating no recursive listing of files or file filtering and no limit on the number of files to be listed. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string[]&gt; | Promise used to return the files names listed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900011 | Out of memory |
| 13900018 | Not a directory |
| 13900020 | Invalid argument |

