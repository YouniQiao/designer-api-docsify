# createWatcher

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## createWatcher

```TypeScript
declare function createWatcher(path: string, events: number, listener: WatchEventListener): Watcher
```

Creates a **Watcher** object to listen for file or directory changes.

**Since:** 10

<!--Device-unnamed-declare function createWatcher(path: string, events: number, listener: WatchEventListener): Watcher--><!--Device-unnamed-declare function createWatcher(path: string, events: number, listener: WatchEventListener): Watcher-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| events | number | Yes |
| listener | [WatchEventListener](arkts-corefile-file-fs-watcheventlistener-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Watcher](arkts-corefile-file-fs-watcher-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900021 |
| 13900022 |
| 13900018 |
| 13900030 |
| 13900025 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900008 |
| 13900042 |
| 13900011 |
