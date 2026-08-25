# createWatcher

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## createWatcher

```TypeScript
declare function createWatcher(path: string, events: number, listener: WatchEventListener): Watcher
```

创建Watcher对象，用于监听文件或目录的创建、删除、修改等变动事件。

**起始版本：** 10

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| events | number | 是 | 监听变动的事件集，多个事件通过或(\|
| listener | [WatchEventListener](arkts-corefile-file-fs-watcheventlistener-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Watcher](arkts-corefile-file-fs-watcher-i.md) |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900018 |
| 13900020 |
| 13900021 |
| 13900022 |
| 13900025 |
| 13900030 |
| 13900042 |
