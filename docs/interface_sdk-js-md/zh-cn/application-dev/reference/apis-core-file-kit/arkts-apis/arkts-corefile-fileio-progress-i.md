# Progress

拷贝进度回调数据

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-fileIo-interface Progress--><!--Device-fileIo-interface Progress-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## processedSize

```TypeScript
readonly processedSize: long
```

已拷贝的数据大小，单位为Byte。

**类型：** long

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-Progress-readonly processedSize: long--><!--Device-Progress-readonly processedSize: long-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

## totalSize

```TypeScript
readonly totalSize: long
```

待拷贝的数据总大小，单位为Byte。

**类型：** long

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-Progress-readonly totalSize: long--><!--Device-Progress-readonly totalSize: long-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

