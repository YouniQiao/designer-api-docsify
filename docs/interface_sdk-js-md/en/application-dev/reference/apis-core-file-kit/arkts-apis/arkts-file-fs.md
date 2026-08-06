# @ohos.file.fs(File Management)

This module is the core module of Core File Kit. It provides APIs for basic file operations, such as creating,
 opening, reading, writing, copying, moving, deleting, and querying files and directories in the application sandbox.


## Summary

### Namespaces

| Name | Description |
| --- | --- |
| [fileIo](arkts-corefile-fileio-n.md) | FileIO |

### Interfaces

| Name | Description |
| --- | --- |
| [ConflictFiles](arkts-corefile-file-fs-conflictfiles-i.md) | Defines conflicting file information used in **copyDir()** or **moveDir()**. |
| [FileFilter](arkts-corefile-file-fs-filefilter-i.md) | Describes a file name filter, which can be used to customize file name filtering rules. |
| [Filter](arkts-corefile-file-fs-filter-i.md) | Defines the file filtering configuration used by **listFile()**. |
| [ListFileExtOptions](arkts-corefile-file-fs-listfileextoptions-i.md) | Defines the options used in **listFileExt**. |
| [ListFileOptions](arkts-corefile-file-fs-listfileoptions-i.md) | Defines the options used in **listFile()**. |
| [Options](arkts-corefile-file-fs-options-i.md) | Defines the options used in **readLines()**. |
| [RandomAccessFileOptions](arkts-corefile-file-fs-randomaccessfileoptions-i.md) | Defines the options used in **createRandomAccessFile()**. |
| [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | Defines the options used in **read()**. |
| [ReadStreamOptions](arkts-corefile-file-fs-readstreamoptions-i.md) | Defines the options used in **createReadStream()**. |
| [ReadTextOptions](arkts-corefile-file-fs-readtextoptions-i.md) | Defines the options used in **readText()**. It inherits from [ReadOptions]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| [ReaderIteratorResult](arkts-corefile-file-fs-readeriteratorresult-i.md) | Represents the information obtained by the **ReaderIterator** object. |
| [WatchEvent](arkts-corefile-file-fs-watchevent-i.md) | Defines the event to observe. |
| [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | Defines the options used in **write()**. It inherits from [Options]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| [WriteStreamOptions](arkts-corefile-file-fs-writestreamoptions-i.md) | Defines the options used in **createWriteStream()**. |

### Types

| Name | Description |
| --- | --- |
| [AtomicFile](arkts-corefile-atomicfile-t.md) | AtomicFile |
| [TaskSignal](arkts-corefile-tasksignal-t.md) | Provides APIs for interrupting a copy task. |
| [WatchEventListener](arkts-corefile-watcheventlistener-t.md) | Defines a watch event listener. When the monitored file or directory changes, a callback is triggered. |
| [Watcher](arkts-corefile-watcher-t.md) | Provides APIs for observing the changes of files or directories. Before using the APIs of **Watcher**, call  **createWatcher()** to create a **Watcher** object. |

