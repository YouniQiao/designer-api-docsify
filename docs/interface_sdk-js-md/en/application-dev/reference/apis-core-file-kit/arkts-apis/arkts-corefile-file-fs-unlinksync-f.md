# unlinkSync

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

## unlinkSync

```TypeScript
declare function unlinkSync(path: string): void
```

Removes a file. This API returns the result synchronously.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function unlinkSync(path: string): void--><!--Device-unnamed-declare function unlinkSync(path: string): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900018 | Not a directory |
| 13900019 | Is a directory |
| 13900030 | File name too long |
| 13900027 | Read-only file system |
| 13900005 | I/O error |
| 13900001 | Operation not permitted |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900014 | Device or resource busy |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

