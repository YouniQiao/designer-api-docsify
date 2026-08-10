# Progress

拷贝进度回调数据

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-interface Progress--><!--Device-unnamed-interface Progress-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## processedSize

```TypeScript
readonly processedSize: number
```

已拷贝的数据大小，单位为Byte。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-Progress-readonly processedSize: number--><!--Device-Progress-readonly processedSize: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## totalSize

```TypeScript
readonly totalSize: number
```

待拷贝的数据总大小，单位为Byte。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-Progress-readonly totalSize: number--><!--Device-Progress-readonly totalSize: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

