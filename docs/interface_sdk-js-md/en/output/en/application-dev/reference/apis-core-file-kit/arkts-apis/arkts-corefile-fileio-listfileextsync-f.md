# listFileExtSync

## listFileExtSync

```TypeScript
function listFileExtSync(
  path: string,
  options?: ListFileExtOptions
): string[]
```

Lists all files in a directory. This API supports recursive listing of files and file filtering and returns the result synchronously. You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The relative path starts with a slash (/).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileIo-function listFileExtSync(  path: string,  options?: ListFileExtOptions): string[]--><!--Device-fileIo-function listFileExtSync(  path: string,  options?: ListFileExtOptions): string[]-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Options for listing files. The default value is empty, indicating no recursive listing of files or file filtering and no limit on the number of files to be listed. |

**Return value:**

| Type | Description |
| --- | --- |
| string[] | File names listed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900011 | Out of memory |
| 13900018 | Not a directory |
| 13900020 | Invalid argument |

