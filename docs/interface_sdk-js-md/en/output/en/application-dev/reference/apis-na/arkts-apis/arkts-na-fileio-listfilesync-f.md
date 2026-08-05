# listFileSync

## listFileSync

```TypeScript
function listFileSync(
  path: string,
  options?: ListFileOptions
): string[]
```

Lists all file names in a directory. This API returns the result synchronously. This API supports recursive listing of all file names and file filtering.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-function listFileSync(  path: string,  options?: ListFileOptions): string[]--><!--Device-fileIo-function listFileSync(  path: string,  options?: ListFileOptions): string[]-End-->

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
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |
| 13900018 | Not a directory |
| 13900042 | Unknown error |

