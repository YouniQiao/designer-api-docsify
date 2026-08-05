# listFile

## listFile

```TypeScript
function listFile(
  path: string,
  options?: ListFileOptions
): Promise<string[]>
```

Lists all file names in a directory. This API supports recursive listing of all file names and file filtering. The returned result starts with a slash (/) and contains the subdirectory. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-function listFile(  path: string,  options?: ListFileOptions): Promise<string[]>--><!--Device-fileIo-function listFile(  path: string,  options?: ListFileOptions): Promise<string[]>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Options for filtering files. The files are not filtered by default. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string[]&gt; | Promise used to return the file names listed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |
| 13900018 | Not a directory |
| 13900042 | Unknown error |


## listFile

```TypeScript
function listFile(path: string, callback: AsyncCallback<string[]>): void
```

Lists the names of all files and directories in the current path. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-function listFile(path: string, callback: AsyncCallback<string[]>): void--><!--Device-fileIo-function listFile(path: string, callback: AsyncCallback<string[]>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string[]&gt; | Yes | Callback used to return the file names listed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |
| 13900018 | Not a directory |
| 13900042 | Unknown error |


## listFile

```TypeScript
function listFile(
  path: string,
  options: ListFileOptions,
  callback: AsyncCallback<string[]>
): void
```

Lists all file names in a directory. This API supports recursive listing of all file names and file filtering. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-function listFile(  path: string,  options: ListFileOptions,  callback: AsyncCallback<string[]>): void--><!--Device-fileIo-function listFile(  path: string,  options: ListFileOptions,  callback: AsyncCallback<string[]>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Options for filtering files. The files are not filtered by default. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string[]&gt; | Yes | Callback used to return the file names listed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |
| 13900018 | Not a directory |
| 13900042 | Unknown error |

