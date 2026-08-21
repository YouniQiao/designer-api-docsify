# @ohos.file.fs

FileIO

## Modules to Import

```TypeScript
```

## Summary

### Namespaces

| Name | Description |
| --- | --- |
| [fileIo](arkts-fileio-n.md) | FileIO |

### Interfaces

| Name | Description |
| --- | --- |
| [ConflictFiles](arkts-filefs-conflictfiles-i.md) | Defines conflicting file information used in **copyDir()** or **moveDir()**. |
| [FileFilter](arkts-filefs-filefilter-i.md) | Describes a file name filter, which can be used to customize file name filtering rules. |
| [Filter](arkts-filefs-filter-i.md) | Defines the file filtering configuration used by **listFile()**. |
| [ListFileExtOptions](arkts-filefs-listfileextoptions-i.md) | Defines the options used in **listFileExt**. |
| [ListFileOptions](arkts-filefs-listfileoptions-i.md) | Defines the options used in **listFile()**. |
| [Options](arkts-filefs-options-i.md) | Defines the options used in **readLines()**. |
| [RandomAccessFileOptions](arkts-filefs-randomaccessfileoptions-i.md) | Defines the options used in **createRandomAccessFile()**. |
| [ReadOptions](arkts-filefs-readoptions-i.md) | Defines the options used in **read()**. |
| [ReadStreamOptions](arkts-filefs-readstreamoptions-i.md) | Defines the options used in **createReadStream()**. |
| [ReadTextOptions](arkts-filefs-readtextoptions-i.md) | Defines the options used in **readText()**. It inherits from [ReadOptions](arkts-filefs-readoptions-i.md). |
| [ReaderIteratorResult](arkts-filefs-readeriteratorresult-i.md) | Represents the information obtained by the **ReaderIterator** object. |
| [WatchEvent](arkts-filefs-watchevent-i.md) | Defines the event to observe. |
| [WriteOptions](arkts-filefs-writeoptions-i.md) | Defines the options used in **write()**. It inherits from [Options](arkts-filefs-options-i.md). |
| [WriteStreamOptions](arkts-filefs-writestreamoptions-i.md) | Defines the options used in **createWriteStream()**. |

### Types

| Name | Description |
| --- | --- |
| [AtomicFile](arkts-atomicfile-t.md) | AtomicFile |
| [TaskSignal](arkts-tasksignal-t.md) | Provides APIs for interrupting a copy task. |
| [WatchEventListener](arkts-watcheventlistener-t.md) | Defines a watch event listener. When the monitored file or directory changes, a callback is triggered. |
| [Watcher](arkts-watcher-t.md) | Provides APIs for observing the changes of files or directories. Before using the APIs of **Watcher**, call **createWatcher()** to create a **Watcher** object. |

