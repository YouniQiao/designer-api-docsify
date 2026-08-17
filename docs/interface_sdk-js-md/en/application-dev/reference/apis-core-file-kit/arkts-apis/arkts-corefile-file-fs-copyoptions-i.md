# CopyOptions

Defines the callback for listening for the copy progress.

**Since:** 11

<!--Device-unnamed-interface CopyOptions--><!--Device-unnamed-interface CopyOptions-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

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

## copySignal

```TypeScript
copySignal?: TaskSignal
```

Signal used to cancel a copy task.

**Type:** [TaskSignal](arkts-corefile-file-fs-tasksignal-c.md)

**Since:** 12

<!--Device-CopyOptions-copySignal?: TaskSignal--><!--Device-CopyOptions-copySignal?: TaskSignal-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## progressListener

```TypeScript
progressListener?: ProgressListener
```

Listener used to observe the copy progress.

**Type:** [ProgressListener](arkts-corefile-progresslistener-t.md)

**Since:** 11

<!--Device-CopyOptions-progressListener?: ProgressListener--><!--Device-CopyOptions-progressListener?: ProgressListener-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

