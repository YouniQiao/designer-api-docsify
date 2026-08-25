# mmapSync

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## mmapSync

```TypeScript
function mmapSync(file: int | File, mode: MappingMode, offset: long, size: int): FileMapping
```

Creates a file mapping object synchronously based on a file descriptor or file object for efficient read and write access to files.

> **NOTE：**&gt;
> 1. Memory mapping can be performed only for regular files. Non-regular files, such as
> pipeline, socket, and device
> files, are not supported. You can use [statSync()](arkts-corefile-fileio-statsync-f.md) to obtain file attributes and then call
> [Stat.isFile()](arkts-corefile-fileio-stat-i.md#isfile) to check whether the file is a regular file.&gt;
> 2. If the mapping range exceeds the raw file size and the write permission is granted for the file, the mapping
> file size will be automatically expanded.&gt;
> 3. For files from external storage or network files, the establishment of mappings and access
> to the mapped memory
> are not guaranteed due to differences in the underlying file system. This may cause the application to terminate
> unexpectedly. You are advised to use other file access APIs such as [read](arkts-corefile-fileio-read-f.md),
> [write](arkts-corefile-fileio-write-f.md), or [Stream](arkts-corefile-fileio-stream-i.md) in this scenario.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [file](arkts-corefile-storagestatistics-storagestats-i-sys.md) | int \| [File](arkts-corefile-file-fs-file-i.md) | Yes |
| mode | [MappingMode](arkts-corefile-file-fs-mappingmode-e.md) | Yes |
| offset | long | Yes |
| size | int | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FileMapping](arkts-corefile-file-fs-filemapping-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900011 |
| 13900012 |
| 13900015 |
| 13900017 |
| 13900020 |
| 13900021 |
| 13900023 |
| 13900024 |
| 13900038 |
| 13900050 |
| 13900056 |
