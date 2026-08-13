# setxattr

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## setxattr

```TypeScript
declare function setxattr(path: string, key: string, value: string): Promise<void>
```

Sets an extended attribute of a file or directory. This API uses a promise to return the result.

**Since:** 12

**Deprecated since:** -1

<!--Device-unnamed-declare function setxattr(path: string, key: string, value: string): Promise<void>--><!--Device-unnamed-declare function setxattr(path: string, key: string, value: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| key | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13900038 |
| 13900002 |
| 13900012 |
| 13900031 |
| 13900025 |
| 13900041 |
| 13900042 |
| 13900011 |
