# @ohos.file.fs

FileIO

## 导入模块

```TypeScript
```

## 汇总

### 命名空间

| 名称 | 说明 |
| --- | --- |
| [fileIo](arkts-fileio-n.md) | FileIO |

### 接口

| 名称 | 说明 |
| --- | --- |
| [ConflictFiles](arkts-filefs-conflictfiles-i.md) | 冲突文件信息，支持copyDir及moveDir接口使用。 |
| [FileFilter](arkts-filefs-filefilter-i.md) | 文件名过滤器接口，可通过该接口自定义文件名过滤规则。 |
| [Filter](arkts-filefs-filter-i.md) | 文件过滤配置项，支持listFile接口使用。 |
| [ListFileExtOptions](arkts-filefs-listfileextoptions-i.md) | 可选项类型，支持listFileExt接口使用。 |
| [ListFileOptions](arkts-filefs-listfileoptions-i.md) | 可选项类型，支持listFile接口使用。 |
| [Options](arkts-filefs-options-i.md) | 可选项类型，支持readLines接口使用。 |
| [RandomAccessFileOptions](arkts-filefs-randomaccessfileoptions-i.md) | 可选项类型，支持 createRandomAccessFile 接口使用。 |
| [ReadOptions](arkts-filefs-readoptions-i.md) | 可选项类型，支持read接口使用。 |
| [ReadStreamOptions](arkts-filefs-readstreamoptions-i.md) | 可选项类型，支持 createReadStream 接口使用。 |
| [ReadTextOptions](arkts-filefs-readtextoptions-i.md) | 可选项类型，支持readText接口使用，ReadTextOptions继承自[ReadOptions](arkts-filefs-readoptions-i.md)。 |
| [ReaderIteratorResult](arkts-filefs-readeriteratorresult-i.md) | 文件读取迭代器返回结果，支持ReaderIterator接口使用。 |
| [WatchEvent](arkts-filefs-watchevent-i.md) | 事件类 |
| [WriteOptions](arkts-filefs-writeoptions-i.md) | 可选项类型，支持write接口使用，WriteOptions继承自[Options](arkts-filefs-options-i.md)。 |
| [WriteStreamOptions](arkts-filefs-writestreamoptions-i.md) | 可选项类型，支持 createWriteStream 接口使用。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [AtomicFile](arkts-atomicfile-t.md) | AtomicFile类。 |
| [TaskSignal](arkts-tasksignal-t.md) | 拷贝中断信号。 |
| [WatchEventListener](arkts-watcheventlistener-t.md) | 事件监听类，当监听的文件或目录发生变动事件时触发回调。 |
| [Watcher](arkts-watcher-t.md) | 文件目录变化监听对象。由createWatcher接口获得。 |

