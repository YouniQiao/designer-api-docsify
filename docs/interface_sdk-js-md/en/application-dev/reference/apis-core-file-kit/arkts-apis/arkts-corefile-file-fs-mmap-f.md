# mmap

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

## mmap

```TypeScript
declare function mmap(file: number | File, mode: MappingMode, offset: number, size: number): Promise<FileMapping>
```

Creates a file mapping object based on a file descriptor or file object, using promise asynchronous callback. Maps file contents to memory for efficient read and write access to files. Note: In the read/write mode (MappingMode.READ_WRITE), if the mapping range exceeds the raw file size, the file size will be automatically expanded.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare function mmap(file: number | File, mode: MappingMode, offset: number, size: number): Promise<FileMapping>--><!--Device-unnamed-declare function mmap(file: number | File, mode: MappingMode, offset: number, size: number): Promise<FileMapping>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| file | number \| [File](arkts-corefile-file-fs-file-i.md) | Yes | File object or open file descriptor fd that has been opened. |
| mode | [MappingMode](arkts-corefile-file-fs-mappingmode-e.md) | Yes | Option to create a file memory-mapped object. You must specify one of the following options: <br>MappingMode.READ_ONLY(0): read-only mode. The file mapping area is not writable. An exception is thrown when the file mapping area is modified. <br>MappingMode.READ_WRITE(1): read/write mode. The modification is written to the file mapping area and then synchronized to the file by the operating system (non-real-time). <br>MappingMode.PRIVATE(2): private mode. It is a copy-on-write mapping mechanism. Modifications to the mapping area are visible only to the current process and do not affect the original file. |
| offset | number | Yes | Start position of the file mapping area, in bytes. |
| size | number | Yes | Size of the file mapping area, in bytes. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[FileMapping](arkts-corefile-file-fs-filemapping-i.md)&gt; | Promise object. Returns a FileMapping object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900021 | File table overflow |
| 13900023 | Text file busy |
| 13900017 | No such device |
| 13900050 | Internal resource error |
| 13900024 | File too large |
| 13900056 | Mmap does not support mapping this file |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900038 | Value too large for defined data type |
| 13900001 | Operation not permitted |
| 13900012 | Permission denied |
| 13900015 | File exists |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900011 | Out of memory |

