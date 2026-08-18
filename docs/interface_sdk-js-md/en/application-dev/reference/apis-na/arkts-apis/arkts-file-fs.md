# @ohos.file.fs

FileIO

## Modules to Import

```TypeScript
```

## Summary

### Namespaces

| Name | Description |
| --- | --- |
| [fileIo](arkts-na-fileio-n.md) | FileIO |

### Interfaces

| Name | Description |
| --- | --- |
| [ConflictFiles](arkts-na-file-fs-conflictfiles-i.md) | Defines conflicting file information used in **copyDir()** or **moveDir()**. |
| [FileFilter](arkts-na-file-fs-filefilter-i.md) | Describes a file name filter, which can be used to customize file name filtering rules. |
| [Filter](arkts-na-file-fs-filter-i.md) | Defines the file filtering configuration used by **listFile()**. |
| [ListFileExtOptions](arkts-na-file-fs-listfileextoptions-i.md) | Defines the options used in **listFileExt**. |
| [ListFileOptions](arkts-na-file-fs-listfileoptions-i.md) | Defines the options used in **listFile()**. |
| [Options](arkts-na-file-fs-options-i.md) | Defines the options used in **readLines()**. |
| [RandomAccessFileOptions](arkts-na-file-fs-randomaccessfileoptions-i.md) | Defines the options used in **createRandomAccessFile()**. |
| [ReadOptions](arkts-na-file-fs-readoptions-i.md) | Defines the options used in **read()**. |
| [ReadStreamOptions](arkts-na-file-fs-readstreamoptions-i.md) | Defines the options used in **createReadStream()**. |
| [ReadTextOptions](arkts-na-file-fs-readtextoptions-i.md) | Defines the options used in **readText()**. It inherits from [ReadOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-readoptions-i.md#readoptions). |
| [ReaderIteratorResult](arkts-na-file-fs-readeriteratorresult-i.md) | Represents the information obtained by the **ReaderIterator** object. |
| [WatchEvent](arkts-na-file-fs-watchevent-i.md) | Defines the event to observe. |
| [WriteOptions](arkts-na-file-fs-writeoptions-i.md) | Defines the options used in **write()**. It inherits from [Options](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-options-i.md#options). |
| [WriteStreamOptions](arkts-na-file-fs-writestreamoptions-i.md) | Defines the options used in **createWriteStream()**. |

### Types

| Name | Description |
| --- | --- |
| [AtomicFile](arkts-na-atomicfile-t.md) | AtomicFile |
| [TaskSignal](arkts-na-tasksignal-t.md) | Provides APIs for interrupting a copy task. |
| [WatchEventListener](arkts-na-watcheventlistener-t.md) | Defines a watch event listener. When the monitored file or directory changes, a callback is triggered. |
| [Watcher](arkts-na-watcher-t.md) | Provides APIs for observing the changes of files or directories. Before using the APIs of **Watcher**, call **createWatcher()** to create a **Watcher** object. |

