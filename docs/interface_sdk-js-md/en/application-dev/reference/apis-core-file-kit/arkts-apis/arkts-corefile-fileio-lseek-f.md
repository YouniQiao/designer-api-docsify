# lseek

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## lseek

```TypeScript
function lseek(fd: int, offset: long, whence?: WhenceType): long
```

调整文件偏移指针位置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-function lseek(fd: int, offset: long, whence?: WhenceType): long--><!--Device-fileIo-function lseek(fd: int, offset: long, whence?: WhenceType): long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | 文件描述符。 |
| offset | long | Yes | 相对偏移位置，单位为Byte。 |
| whence | [WhenceType](arkts-corefile-fileio-whencetype-e.md) | No | 偏移指针相对位置类型。不指定则默认为文件起始位置处。 |

**Return value:**

| Type | Description |
| --- | --- |
| long | 当前文件偏移指针位置（相对于文件头的偏移量，单位为Byte）。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900038 | Value too large for defined data type |
| 13900008 | Bad file descriptor |
| 13900026 | Illegal seek |
| 13900042 | Unknown error |

