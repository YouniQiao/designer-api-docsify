# listFileSync

## listFileSync

```TypeScript
function listFileSync(
  path: string,
  options?: ListFileOptions
): string[]
```

Lists the names of all files and directories in the current directory synchronously. A file name array is returned, which can be filtered by file name or file name extension. This API supports recursively listing the relative paths of all files by setting **recursion** in **ListFileOptions**. The relative path starts with a slash (/).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function listFileSync(  path: string,  options?: ListFileOptions): string[]--><!--Device-fileIo-function listFileSync(  path: string,  options?: ListFileOptions): string[]-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| options | [ListFileOptions](arkts-na-file-fs-listfileoptions-i.md) | No | Options for filtering files. The files are not filtered by default. |

**Return value:**

| Type | Description |
| --- | --- |
| string[] | File name array, which is encoded in UTF-8 format by default. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900018 | Not a directory |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

