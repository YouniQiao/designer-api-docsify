# lseek

## Modules to Import

```TypeScript
import { ConflictFiles } from 'ConflictFiles';
import { FileFilter } from 'FileFilter';
import { Filter } from 'Filter';
import { Options } from 'Options';
import { ReaderIteratorResult } from 'ReaderIteratorResult';
import { WatchEvent } from 'WatchEvent';
import { WatchEventListener } from 'WatchEventListener';
import { Watcher } from 'Watcher';
import { ReadOptions } from 'ReadOptions';
import { ReadTextOptions } from 'ReadTextOptions';
import { WriteOptions } from 'WriteOptions';
import { ListFileExtOptions } from 'ListFileExtOptions';
import { ListFileOptions } from 'ListFileOptions';
import { DfsListeners } from 'DfsListeners';
import { TaskSignal } from 'TaskSignal';
```

## lseek

```TypeScript
declare function lseek(fd: number, offset: number, whence?: WhenceType): number
```

Adjusts the position of the file offset pointer.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-unnamed-declare function lseek(fd: number, offset: number, whence?: WhenceType): number--><!--Device-unnamed-declare function lseek(fd: number, offset: number, whence?: WhenceType): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor. |
| offset | number | Yes | Relative offset, in bytes. |
| whence | [WhenceType](arkts-corefile-file-fs-whencetype-e.md) | No | Where to start the offset. If this parameter is not specified, the file start position is used by default. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Position of the current offset as measured from the beginning of the file, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900038 | Value too large for defined data type |
| 13900008 | Bad file descriptor |
| 13900026 | Illegal seek |
| 13900042 | Unknown error |

