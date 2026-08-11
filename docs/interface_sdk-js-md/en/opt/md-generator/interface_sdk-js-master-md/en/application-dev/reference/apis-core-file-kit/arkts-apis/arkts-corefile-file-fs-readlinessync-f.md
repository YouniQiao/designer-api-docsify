# readLinesSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## readLinesSync

```TypeScript
declare function readLinesSync(filePath: string, options?: Options): ReaderIterator
```

Reads the text content of a file line by line. This API returns the result synchronously.

**Since:** 11

<!--Device-unnamed-declare function readLinesSync(filePath: string, options?: Options): ReaderIterator--><!--Device-unnamed-declare function readLinesSync(filePath: string, options?: Options): ReaderIterator-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900022 |
| 13900019 |
| 13900030 |
| 13900025 |
| 13900027 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900044 |
| 13900015 |
| 13900041 |
| 13900042 |
