# Progress

Defines the copy progress information.

**Since:** 11

<!--Device-unnamed-interface Progress--><!--Device-unnamed-interface Progress-End-->

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

## processedSize

```TypeScript
readonly processedSize: number
```

Size of the copied data, in bytes.

**Type:** number

**Since:** 11

<!--Device-Progress-readonly processedSize: number--><!--Device-Progress-readonly processedSize: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## totalSize

```TypeScript
readonly totalSize: number
```

Total size of the data to be copied, in bytes.

**Type:** number

**Since:** 11

<!--Device-Progress-readonly totalSize: number--><!--Device-Progress-readonly totalSize: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

