# listFileExtSync

## listFileExtSync

```TypeScript
function listFileExtSync(
  path: string,
  options?: ListFileExtOptions
): string[]
```

Lists all file names in a directory. This API returns the result synchronously. This API supports recursive listing of all file names and custom file name filtering. The returned result starts with a slash (/) and contains the subdirectory.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileIo-function listFileExtSync(  path: string,  options?: ListFileExtOptions): string[]--><!--Device-fileIo-function listFileExtSync(  path: string,  options?: ListFileExtOptions): string[]-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Options for filtering files. The files are not filtered by default. |

**Return value:**

| Type | Description |
| --- | --- |
| string[] | List of the file names obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900011 | Out of memory |
| 13900018 | Not a directory |
| 13900020 | Invalid argument |

