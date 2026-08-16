# createWriteStream

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

## createWriteStream

```TypeScript
declare function createWriteStream(path: string, options?: WriteStreamOptions): WriteStream
```

Creates a writeable stream. This API returns the result synchronously.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-declare function createWriteStream(path: string, options?: WriteStreamOptions): WriteStream--><!--Device-unnamed-declare function createWriteStream(path: string, options?: WriteStreamOptions): WriteStream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Path of the file. |
| options | [WriteStreamOptions](../../apis-na/arkts-apis/arkts-na-file-fs-writestreamoptions-i.md) | No | The options are as follows:<br>- **start** (number): start position to write the data, in bytes. This parameter is optional. By default, data is written from the current position.<br>- **mode** (number): mode for creating the writeable stream. This parameter is optional. The default value is the write-only mode. |

**Return value:**

| Type | Description |
| --- | --- |
| [WriteStream](arkts-corefile-file-fs-writestream-c.md) | WriteStream** instance obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900022 | Too many open files |
| 13900017 | No such device |
| 13900019 | Is a directory |
| 13900030 | File name too long |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900027 | Read-only file system |
| 13900004 | Interrupted system call |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error |
| 13900038 | Value too large for defined data type |
| 13900001 | Operation not permitted |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900015 | File exists |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

