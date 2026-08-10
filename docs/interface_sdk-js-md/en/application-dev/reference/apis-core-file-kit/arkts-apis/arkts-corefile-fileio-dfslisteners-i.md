# DfsListeners

事件监听类。创建DFSListener对象，用于监听分布式文件系统状态。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-export interface DfsListeners--><!--Device-fileIo-export interface DfsListeners-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## onStatus

```TypeScript
onStatus: DfsListenerCallback
```

分布式文件系统状态监听器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DfsListeners-onStatus: DfsListenerCallback--><!--Device-DfsListeners-onStatus: DfsListenerCallback-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

