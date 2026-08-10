# Progress

拷贝进度回调数据

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-interface Progress--><!--Device-fileIo-interface Progress-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## processedSize

```TypeScript
readonly processedSize: long
```

已拷贝的数据大小，单位为Byte。

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Progress-readonly processedSize: long--><!--Device-Progress-readonly processedSize: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## totalSize

```TypeScript
readonly totalSize: long
```

待拷贝的数据总大小，单位为Byte。

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Progress-readonly totalSize: long--><!--Device-Progress-readonly totalSize: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

