# accessSync

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

## accessSync

```TypeScript
declare function accessSync(path: string, mode?: AccessModeType): boolean
```

Checks whether a file or directory exists or has the operation permission. This API returns the result synchronously. If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function accessSync(path: string, mode?: AccessModeType): boolean--><!--Device-unnamed-declare function accessSync(path: string, mode?: AccessModeType): boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file or directory. |
| mode | [AccessModeType](arkts-corefile-file-fs-accessmodetype-e.md) | No | Permission on the file or directory to check. If this parameter is left blank, the system checks whether the file or directory exists.<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The value **true** means the file exists; the value **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900023 | Text file busy |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900018 | Not a directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900030 | File name too long |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |


## accessSync

```TypeScript
declare function accessSync(path: string, mode: AccessModeType, flag: AccessFlagType): boolean
```

Checks whether a file or directory is stored locally or has the operation permission. This API returns the result synchronously. If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown.

**Since:** 12

<!--Device-unnamed-declare function accessSync(path: string, mode: AccessModeType, flag: AccessFlagType): boolean--><!--Device-unnamed-declare function accessSync(path: string, mode: AccessModeType, flag: AccessFlagType): boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file to check. |
| mode | [AccessModeType](arkts-corefile-file-fs-accessmodetype-e.md) | Yes | Permission on the file or directory to check. |
| flag | [AccessFlagType](arkts-corefile-file-fs-accessflagtype-e.md) | Yes | Position of the file or directory to check. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The value **true** means the file is a local file and has the related permission. The value **false** means the file does not exist or is on the cloud or a distributed device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |
| 13900005 | I/O error |
| 13900023 | Text file busy |
| 13900033 | Too many symbolic links encountered |
| 13900018 | Not a directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900030 | File name too long |
| 13900011 | Out of memory |

