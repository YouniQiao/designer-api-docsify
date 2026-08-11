# accessSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## accessSync

```TypeScript
declare function accessSync(path: string, mode?: AccessModeType): boolean
```

Checks whether a file or directory exists or has the operation permission. This API returns the result synchronously.

If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function accessSync(path: string, mode?: AccessModeType): boolean--><!--Device-unnamed-declare function accessSync(path: string, mode?: AccessModeType): boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| mode | [AccessModeType](arkts-corefile-file-fs-accessmodetype-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900005 |
| 13900023 |
| 13900033 |
| 13900002 |
| 13900018 |
| 13900012 |
| 13900013 |
| 13900030 |
| 13900008 |
| 13900042 |
| 13900011 |


## accessSync

```TypeScript
declare function accessSync(path: string, mode: AccessModeType, flag: AccessFlagType): boolean
```

Checks whether a file or directory is stored locally or has the operation permission. This API returns the result synchronously.

If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown.

**Since:** 12

<!--Device-unnamed-declare function accessSync(path: string, mode: AccessModeType, flag: AccessFlagType): boolean--><!--Device-unnamed-declare function accessSync(path: string, mode: AccessModeType, flag: AccessFlagType): boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| mode | [AccessModeType](arkts-corefile-file-fs-accessmodetype-e.md) | Yes |
| flag | [AccessFlagType](arkts-corefile-file-fs-accessflagtype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900005 |
| 13900023 |
| 13900033 |
| 13900018 |
| 13900012 |
| 13900013 |
| 13900030 |
| 13900011 |
