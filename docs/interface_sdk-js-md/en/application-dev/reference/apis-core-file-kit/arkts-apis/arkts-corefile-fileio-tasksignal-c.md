# TaskSignal

Provides APIs for interrupting a copy task.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-class TaskSignal--><!--Device-fileIo-class TaskSignal-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## cancel

```TypeScript
cancel(): void
```

Cancels a copy task.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-TaskSignal-cancel(): void--><!--Device-TaskSignal-cancel(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900012 | Permission denied by the file system |
| 13900010 | Try again |
| 13900043 | No task can be canceled. |

