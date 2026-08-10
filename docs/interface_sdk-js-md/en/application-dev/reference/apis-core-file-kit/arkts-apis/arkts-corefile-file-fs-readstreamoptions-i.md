# ReadStreamOptions

可选项类型，支持 createReadStream 接口使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface ReadStreamOptions--><!--Device-unnamed-export interface ReadStreamOptions-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## end

```TypeScript
end?: long
```

表示期望读取结束的位置，单位为Byte。可选，默认文件末尾。

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ReadStreamOptions-end?: long--><!--Device-ReadStreamOptions-end?: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## start

```TypeScript
start?: long
```

表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ReadStreamOptions-start?: long--><!--Device-ReadStreamOptions-start?: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

