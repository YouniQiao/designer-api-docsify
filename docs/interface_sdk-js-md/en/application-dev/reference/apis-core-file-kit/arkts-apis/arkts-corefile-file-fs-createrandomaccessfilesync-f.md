# createRandomAccessFileSync

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## createRandomAccessFileSync

```TypeScript
declare function createRandomAccessFileSync(file: string | File, mode?: number,
  options?: RandomAccessFileOptions): RandomAccessFile
```

Creates a **RandomAccessFile** instance based on a file path or file object.

**Since:** 10

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [file](arkts-corefile-storagestatistics-storagestats-i-sys.md) | string \| [File](arkts-corefile-file-fs-file-i.md) | Yes |
| mode | number | No | [Mode](../../../reference/apis-core-file-kit/js-apis-file-fs.md#openmode) for creating the **RandomAccessFile** instance. This parameter is valid only when the application sandbox path of the file is passed in. One of the following options must be specified:   - **OpenMode.READ_ONLY(0o0)**: Create the file in read-only mode. This is the default value.   - **OpenMode.WRITE_ONLY(0o1)**: Create the file in write-only mode.    - **OpenMode.READ_WRITE(0o2)**: Create the file in read/write mode.   You can also specify the following options, separated by a bitwise OR operator (\|
| options | [RandomAccessFileOptions](arkts-corefile-file-fs-randomaccessfileoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RandomAccessFile](arkts-corefile-file-fs-randomaccessfile-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 13900044 |
