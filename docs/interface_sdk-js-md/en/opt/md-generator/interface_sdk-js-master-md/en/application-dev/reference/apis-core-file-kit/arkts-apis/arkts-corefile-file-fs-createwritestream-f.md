# createWriteStream

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## createWriteStream

```TypeScript
declare function createWriteStream(path: string, options?: WriteStreamOptions): WriteStream
```

Creates a writeable stream. This API returns the result synchronously.

**Since:** 12

<!--Device-unnamed-declare function createWriteStream(path: string, options?: WriteStreamOptions): WriteStream--><!--Device-unnamed-declare function createWriteStream(path: string, options?: WriteStreamOptions): WriteStream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| options | [WriteStreamOptions](arkts-corefile-file-fs-writestreamoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WriteStream](arkts-corefile-file-fs-writestream-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900022 |
| 13900017 |
| 13900019 |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900038 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900015 |
| 13900041 |
| 13900042 |
| 13900011 |
