# closeSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## closeSync

```TypeScript
declare function closeSync(file: number | File): void
```

Closes a file or directory. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function closeSync(file: number | File): void--><!--Device-unnamed-declare function closeSync(file: number | File): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| file | number \| [File](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-request-file-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |
