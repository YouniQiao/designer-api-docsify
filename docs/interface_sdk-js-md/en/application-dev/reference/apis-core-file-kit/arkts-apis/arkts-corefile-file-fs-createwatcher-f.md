# createWatcher

## Modules to Import

```TypeScript
import { ConflictFiles } from 'ConflictFiles';
import { FileFilter } from 'FileFilter';
import { Filter } from 'Filter';
import { Options } from 'Options';
import { ReaderIteratorResult } from 'ReaderIteratorResult';
import { WatchEvent } from 'WatchEvent';
import { WatchEventListener } from 'WatchEventListener';
import { Watcher } from 'Watcher';
import { ReadOptions } from 'ReadOptions';
import { ReadTextOptions } from 'ReadTextOptions';
import { WriteOptions } from 'WriteOptions';
import { ListFileExtOptions } from 'ListFileExtOptions';
import { ListFileOptions } from 'ListFileOptions';
import { DfsListeners } from 'DfsListeners';
import { TaskSignal } from 'TaskSignal';
```

## createWatcher

```TypeScript
declare function createWatcher(path: string, events: number, listener: WatchEventListener): Watcher
```

Creates a **Watcher** object to listen for file or directory changes.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-unnamed-declare function createWatcher(path: string, events: number, listener: WatchEventListener): Watcher--><!--Device-unnamed-declare function createWatcher(path: string, events: number, listener: WatchEventListener): Watcher-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file or directory to observe. |
| events | number | Yes | Events to observe. Multiple events can be separated by vertical bars ( |
| listener | [WatchEventListener](arkts-corefile-file-fs-watcheventlistener-i.md) | Yes | Callback invoked when an observed event occurs. The callback will be invoked each time an observed event occurs. |

**Return value:**

| Type | Description |
| --- | --- |
| [Watcher](arkts-corefile-file-fs-watcher-i.md) | Watcher** object created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900021 | File table overflow |
| 13900022 | Too many open files |
| 13900018 | Not a directory |
| 13900030 | File name too long |
| 13900025 | No space left on device |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900015 | File exists |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

