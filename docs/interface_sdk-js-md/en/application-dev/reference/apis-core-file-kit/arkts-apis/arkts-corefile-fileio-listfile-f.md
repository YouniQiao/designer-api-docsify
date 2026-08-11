# listFile

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## listFile

```TypeScript
function listFile(
  path: string,
  options?: ListFileOptions
): Promise<string[]>
```

Lists the names of all files and directories in the current directory. A file name array is returned, which can be filtered by file name or file name extension. This API uses a promise to return the result.

This API supports recursively listing the relative paths of all files by setting **recursion** in  
**ListFileOptions**. The relative path starts with a slash (/).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-function listFile(  path: string,  options?: ListFileOptions): Promise<string[]>--><!--Device-fileIo-function listFile(  path: string,  options?: ListFileOptions): Promise<string[]>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| options | [ListFileOptions](arkts-corefile-file-fs-listfileoptions-i.md) | No | Options for filtering files. The files are not filtered by default. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string[]&gt; | Promise used to return the file name array, which is encoded in UTF-8 format by default. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900018 | Not a directory |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |


## listFile

```TypeScript
function listFile(path: string, callback: AsyncCallback<string[]>): void
```

Lists the names of all files and directories in the current path. A file name array is returned. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-function listFile(path: string, callback: AsyncCallback<string[]>): void--><!--Device-fileIo-function listFile(path: string, callback: AsyncCallback<string[]>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string[]&gt; | Yes | Callback used to return the file name array, which is encoded in UTF-8 format by default. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900018 | Not a directory |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |


## listFile

```TypeScript
function listFile(
  path: string,
  options: ListFileOptions,
  callback: AsyncCallback<string[]>
): void
```

Lists the names of all files and directories in the current directory. A file name array is returned, which can be filtered by file name or file name extension. This API uses an asynchronous callback to return the result.

This API supports recursively listing the relative paths of all files by setting **recursion** in  
**ListFileOptions**. The relative path starts with a slash (/).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-function listFile(  path: string,  options: ListFileOptions,  callback: AsyncCallback<string[]>): void--><!--Device-fileIo-function listFile(  path: string,  options: ListFileOptions,  callback: AsyncCallback<string[]>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| options | [ListFileOptions](arkts-corefile-file-fs-listfileoptions-i.md) | Yes | Options for filtering files. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string[]&gt; | Yes | Callback used to return the file name array, which is encoded in UTF-8 format by default. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900018 | Not a directory |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

