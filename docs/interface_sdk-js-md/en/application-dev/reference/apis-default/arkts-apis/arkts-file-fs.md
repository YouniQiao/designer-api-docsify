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
| [ConflictFiles](arkts-file-fs-conflictfiles-i.md) | Defines conflicting file information used in **copyDir()** or **moveDir()**. |
| [FileFilter](arkts-file-fs-filefilter-i.md) | Describes a file name filter, which can be used to customize file name filtering rules. |
| [Filter](arkts-file-fs-filter-i.md) | Defines the file filtering configuration used by **listFile()**. |
| [ListFileExtOptions](arkts-file-fs-listfileextoptions-i.md) | Defines the options used in **listFileExt**. |
| [ListFileOptions](arkts-file-fs-listfileoptions-i.md) | Defines the options used in **listFile()**. |
| [Options](arkts-file-fs-options-i.md) | Defines the options used in **readLines()**. |
| [RandomAccessFileOptions](arkts-file-fs-randomaccessfileoptions-i.md) | Defines the options used in **createRandomAccessFile()**. |
| [ReaderIteratorResult](arkts-file-fs-readeriteratorresult-i.md) | Represents the information obtained by the **ReaderIterator** object. |
| [ReadOptions](arkts-file-fs-readoptions-i.md) | Defines the options used in **read()**. |
| [ReadStreamOptions](arkts-file-fs-readstreamoptions-i.md) | Defines the options used in **createReadStream()**. |
| [ReadTextOptions](arkts-file-fs-readtextoptions-i.md) | Defines the options used in **readText()**. It inherits from [ReadOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-readoptions-i.md). |
| [WatchEvent](arkts-file-fs-watchevent-i.md) | Defines the event to observe. |
| [WriteOptions](arkts-file-fs-writeoptions-i.md) | Defines the options used in **write()**. It inherits from [Options](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-options-i.md). |
| [WriteStreamOptions](arkts-file-fs-writestreamoptions-i.md) | Defines the options used in **createWriteStream()**. |

### Types

| Name | Description |
| --- | --- |
| [AtomicFile](arkts-atomicfile-t.md) | AtomicFile |
| [TaskSignal](arkts-tasksignal-t.md) | Provides APIs for interrupting a copy task. |
| [Watcher](arkts-watcher-t.md) | Provides APIs for observing the changes of files or directories. Before using the APIs of **Watcher**, call **createWatcher()** to create a **Watcher** object. |
| [WatchEventListener](arkts-watcheventlistener-t.md) | Defines a watch event listener. When the monitored file or directory changes, a callback is triggered. |

