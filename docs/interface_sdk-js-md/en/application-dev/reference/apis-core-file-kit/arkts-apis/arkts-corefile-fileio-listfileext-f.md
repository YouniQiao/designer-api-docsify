# listFileExt

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## listFileExt

```TypeScript
function listFileExt(
  path: string,
  options?: ListFileExtOptions
): Promise<string[]>
```

列出目录下所有文件名，支持递归列出和自定义文件名过滤。使用Promise异步回调。

可通过配置options中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileIo-function listFileExt(  path: string,  options?: ListFileExtOptions): Promise<string[]>--><!--Device-fileIo-function listFileExt(  path: string,  options?: ListFileExtOptions): Promise<string[]>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 目录的应用沙箱路径。 |
| options | [ListFileExtOptions](arkts-corefile-file-fs-listfileextoptions-i.md) | No | 文件列出选项。默认为空，表示不递归、不限制列出数量、不进行过滤。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string[]&gt; | Promise对象，返回文件名数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900002 | No such file or directory |
| 13900018 | Not a directory |
| 13900011 | Out of memory |

