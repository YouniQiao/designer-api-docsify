# TaskSignal

Provides APIs for interrupting a copy task.

**Since:** 12

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## cancel

```TypeScript
cancel(): void
```

Cancels a copy task.

**Since:** 12

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID |
| --- |
| 13900010 |
| 13900012 |
| 13900043 |

## onCancel

```TypeScript
onCancel(): Promise<string>
```


> **NOTE：**&gt;
> This API is supported since API version 12 and deprecated since API version 24.
Subscribes to the event reported when a copy task is canceled.

**Since:** 12

**Deprecated since:** 24

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900008 |
| 13900042 |
