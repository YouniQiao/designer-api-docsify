# WriteOptions

可选项类型，支持write接口使用，WriteOptions继承自[Options](arkts-corefile-file-fs-options-i.md)。

**Inheritance/Implementation:** WriteOptions extends [Options](arkts-corefile-file-fs-options-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface WriteOptions extends Options--><!--Device-unnamed-export interface WriteOptions extends Options-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## length

```TypeScript
length?: long
```

期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WriteOptions-length?: long--><!--Device-WriteOptions-length?: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## offset

```TypeScript
offset?: long
```

期望写入文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WriteOptions-offset?: long--><!--Device-WriteOptions-offset?: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

