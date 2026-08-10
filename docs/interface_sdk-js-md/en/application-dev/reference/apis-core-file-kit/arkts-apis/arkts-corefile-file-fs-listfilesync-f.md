# listFileSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## listFileSync

```TypeScript
declare function listFileSync(
  path: string,
  options?: ListFileOptions
): string[]
```

默认以同步方式列出当前目录下所有文件名和目录名。支持过滤。

可通过配置options中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function listFileSync(  path: string,  options?: ListFileOptions): string[]--><!--Device-unnamed-declare function listFileSync(  path: string,  options?: ListFileOptions): string[]-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 目录的应用沙箱路径。 |
| options | [ListFileOptions](arkts-corefile-file-fs-listfileoptions-i.md) | No | 文件过滤选项。默认不进行过滤。<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| string[] | 返回文件名数组，默认以'utf-8'编码。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900018 | Not a directory |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

