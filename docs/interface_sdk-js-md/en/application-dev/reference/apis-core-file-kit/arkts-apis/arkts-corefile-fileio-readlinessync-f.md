# readLinesSync

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## readLinesSync

```TypeScript
function readLinesSync(filePath: string, options?: Options): ReaderIterator
```

Reads a file text line by line synchronously. Only the files in UTF-8 format are supported.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| options | [Options](arkts-corefile-file-fs-options-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13900002 |
| 13900012 |
| 13900015 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900033 |
| 13900041 |
| 13900042 |
| 13900044 |
