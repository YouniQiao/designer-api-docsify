# fdatasyncSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## fdatasyncSync

```TypeScript
declare function fdatasyncSync(fd: number): void
```

Synchronizes the data of a file. This API returns the result synchronously.

**Since:** 9

<!--Device-unnamed-declare function fdatasyncSync(fd: number): void--><!--Device-unnamed-declare function fdatasyncSync(fd: number): void-End-->

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
