# CopyOptions

Defines the callback for listening for the copy progress.

**Since:** 11

<!--Device-unnamed-interface CopyOptions--><!--Device-unnamed-interface CopyOptions-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## copySignal

```TypeScript
copySignal?: TaskSignal
```

Signal used to cancel a copy task.

**Type:** TaskSignal

**Since:** 12

<!--Device-CopyOptions-copySignal?: TaskSignal--><!--Device-CopyOptions-copySignal?: TaskSignal-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## progressListener

```TypeScript
progressListener?: ProgressListener
```

Listener used to observe the copy progress.

**Type:** ProgressListener

**Since:** 11

<!--Device-CopyOptions-progressListener?: ProgressListener--><!--Device-CopyOptions-progressListener?: ProgressListener-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

