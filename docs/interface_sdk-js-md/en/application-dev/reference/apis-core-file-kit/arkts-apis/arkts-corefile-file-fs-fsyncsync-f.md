# fsyncSync

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## fsyncSync

```TypeScript
declare function fsyncSync(fd: number): void
```

Synchronizes the cached data of a file to storage. This API returns the result synchronously.

**Since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900005 |
| 13900008 |
| 13900020 |
| 13900025 |
| 13900027 |
| 13900041 |
| 13900042 |
