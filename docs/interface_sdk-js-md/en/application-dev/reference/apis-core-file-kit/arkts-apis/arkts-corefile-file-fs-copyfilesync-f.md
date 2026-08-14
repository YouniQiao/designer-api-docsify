# copyFileSync

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

## copyFileSync

```TypeScript
declare function copyFileSync(src: string | number, dest: string | number, mode?: number): void
```

Copies a file. This API returns the result synchronously.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function copyFileSync(src: string | number, dest: string | number, mode?: number): void--><!--Device-unnamed-declare function copyFileSync(src: string | number, dest: string | number, mode?: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string \| number | Yes | Path or FD of the file to copy. |
| dest | string \| number | Yes | Destination path of the file or FD of the file created. |
| mode | number | No | Whether to overwrite the file with the same name in the destination directory. The default value is **0**, which is the only value supported.<br>**0**: overwrite the file with the same name and truncate the part that is not overwritten. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900018 | Not a directory |
| 13900019 | Is a directory |
| 13900030 | File name too long |
| 13900031 | Function not implemented |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900038 | Value too large for defined data type |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900034 | Operation would block |
| 13900012 | Permission denied |
| 13900044 | Network is unreachable<br>**Applicable version:** 12 and later |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

