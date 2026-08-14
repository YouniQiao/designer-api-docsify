# OpenMode

Mode Indicates the open flags.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-fileIo-namespace OpenMode--><!--Device-fileIo-namespace OpenMode-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { ConflictFiles } from 'ConflictFiles';
import { FileFilter } from 'FileFilter';
import { Filter } from 'Filter';
import { Options } from 'Options';
import { ReaderIteratorResult } from 'ReaderIteratorResult';
import { WatchEvent } from 'WatchEvent';
import { WatchEventListener } from 'WatchEventListener';
import { Watcher } from 'Watcher';
import { ReadOptions } from 'ReadOptions';
import { ReadTextOptions } from 'ReadTextOptions';
import { WriteOptions } from 'WriteOptions';
import { ListFileExtOptions } from 'ListFileExtOptions';
import { ListFileOptions } from 'ListFileOptions';
import { DfsListeners } from 'DfsListeners';
import { TaskSignal } from 'TaskSignal';
```

## Summary

### Constants

| Name | Description |
| --- | --- |
| [READ_ONLY](arkts-corefile-openmode-con.md#READ_ONLY) | Open the file in read-only mode. |
| [WRITE_ONLY](arkts-corefile-openmode-con.md#WRITE_ONLY) | Open the file in write-only mode. |
| [READ_WRITE](arkts-corefile-openmode-con.md#READ_WRITE) | Open the file in read/write mode. |
| [CREATE](arkts-corefile-openmode-con.md#CREATE) | Create a file if the specified file does not exist. |
| [TRUNC](arkts-corefile-openmode-con.md#TRUNC) | If the file exists and is opened in write-only or read/write mode, truncate the file length to 0. |
| [APPEND](arkts-corefile-openmode-con.md#APPEND) | Open the file in append mode. New data will be written to the end of the file. |
| [NONBLOCK](arkts-corefile-openmode-con.md#NONBLOCK) | If **path** points to a named pipe (FIFO), block special file, or character special file, perform non-blocking operations on the open file and in subsequent I/Os. |
| [DIR](arkts-corefile-openmode-con.md#DIR) | If **path** does not point to a directory, throw an exception. |
| [NOFOLLOW](arkts-corefile-openmode-con.md#NOFOLLOW) | If **path** points to a symbolic link, throw an exception. |
| [SYNC](arkts-corefile-openmode-con.md#SYNC) | Open the file in synchronous I/O mode. |
| [UNCACHE](arkts-corefile-openmode-con.md#UNCACHE) | UNCACHE IO. |

