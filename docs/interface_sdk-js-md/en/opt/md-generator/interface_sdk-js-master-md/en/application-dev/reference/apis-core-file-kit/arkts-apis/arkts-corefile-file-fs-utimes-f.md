# utimes

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## utimes

```TypeScript
declare function utimes(path: string, mtime: number): void
```

Changes the time when the file was last modified.

**Since:** 11

**Deprecated since:** -1

<!--Device-unnamed-declare function utimes(path: string, mtime: number): void--><!--Device-unnamed-declare function utimes(path: string, mtime: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| mtime | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900042 |
| 13900027 |
