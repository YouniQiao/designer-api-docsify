# TaskSignal

拷贝中断信号。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## cancel

```TypeScript
cancel(): void
```

取消拷贝任务。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.File.FileIO

**错误码：**

| 错误码ID |
| --- |
| 13900010 |
| 13900012 |
| 13900043 |

## onCancel

```TypeScript
onCancel(): Promise<string>
```


> **说明：**&gt;
> 从API version 12开始支持，从API version 24开始废弃。
取消拷贝事件监听。

**起始版本：** 12

**废弃版本：** 24

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900008 |
| 13900042 |
