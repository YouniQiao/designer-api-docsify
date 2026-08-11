# ReadTextOptions

Defines the options used in **readText()**. It inherits from [ReadOptions](arkts-corefile-file-fs-readoptions-i.md).

**Inheritance/Implementation:** ReadTextOptions extends [ReadOptions](arkts-corefile-file-fs-readoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface ReadTextOptions extends ReadOptions--><!--Device-unnamed-export interface ReadTextOptions extends ReadOptions-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## encoding

```TypeScript
encoding?: string
```

Format of the data to be encoded. This parameter is valid only when the data type is string.The default value is 'utf-8', which is the only value supported.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ReadTextOptions-encoding?: string--><!--Device-ReadTextOptions-encoding?: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

