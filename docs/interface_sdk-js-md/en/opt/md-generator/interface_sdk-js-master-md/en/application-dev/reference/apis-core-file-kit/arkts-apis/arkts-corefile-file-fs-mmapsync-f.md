# mmapSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## mmapSync

```TypeScript
declare function mmapSync(file: number | File, mode: MappingMode, offset: number, size: number): FileMapping
```

Creates a file mapping object based on a file descriptor or file object by using the synchronization method. Maps file contents to memory for efficient read and write access to files. Note: In the read/write mode (MappingMode.READ_WRITE), if the mapping range exceeds the raw file size, the file size will be automatically expanded.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare function mmapSync(file: number | File, mode: MappingMode, offset: number, size: number): FileMapping--><!--Device-unnamed-declare function mmapSync(file: number | File, mode: MappingMode, offset: number, size: number): FileMapping-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [file](arkts-corefile-storagestatistics-storagestats-i-sys.md) | number \| [File](arkts-corefile-file-fs-file-i.md) | Yes |
| mode | [MappingMode](arkts-corefile-file-fs-mappingmode-e.md) | Yes |
| offset | number | Yes |
| size | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FileMapping](arkts-corefile-file-fs-filemapping-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900021 |
| 13900023 |
| 13900017 |
| 13900050 |
| 13900024 |
| 13900056 |
| 13900004 |
| 13900005 |
| 13900038 |
| 13900001 |
| 13900012 |
| 13900015 |
| 13900008 |
| 13900010 |
| 13900011 |
