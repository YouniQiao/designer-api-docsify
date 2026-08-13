# fsyncSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## fsyncSync

```TypeScript
declare function fsyncSync(fd: number): void
```

Synchronizes the cached data of a file to storage. This API returns the result synchronously.

**Since:** 9

**Deprecated since:** -1

<!--Device-unnamed-declare function fsyncSync(fd: number): void--><!--Device-unnamed-declare function fsyncSync(fd: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |
| 13900027 |
