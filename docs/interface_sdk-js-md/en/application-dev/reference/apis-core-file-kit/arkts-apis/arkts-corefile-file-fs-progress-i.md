# Progress

Defines the copy progress information.

**Since:** 11

<!--Device-unnamed-interface Progress--><!--Device-unnamed-interface Progress-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
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

