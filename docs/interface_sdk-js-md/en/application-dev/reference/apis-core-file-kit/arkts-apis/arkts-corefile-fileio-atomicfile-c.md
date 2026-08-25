# AtomicFile

AtomicFile is a class used to perform atomic read and write operations on files. A temporary file is written and renamed to the original file location, which ensures file integrity. If the write operation fails, the temporary file is deleted without modifying the original file content. You can call finishWrite() or failWrite() to write or roll back file content.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor(path: string)
```

The AtomicFile constructor.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## delete

```TypeScript
delete(): void
```

Deletes the AtomicFile class, including the original files and temporary files.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900027 |
| 13900042 |

## failWrite

```TypeScript
failWrite(): void
```

Rolls back the file after the file fails to be written.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID |
| --- |
| 13900042 |

## finishWrite

```TypeScript
finishWrite(): void
```

Finishes writing file data when the write operation is complete.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID |
| --- |
| 13900042 |

## getBaseFile

```TypeScript
getBaseFile(): File
```

Obtains the file object through the AtomicFile object. The FD needs to be closed by calling close().

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [File](arkts-corefile-file-fs-file-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13900002 |
| 13900005 |
| 13900012 |
| 13900042 |

## openRead

```TypeScript
openRead(): ReadStream
```

Creates a ReadStream instance.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ReadStream](arkts-corefile-file-fs-readstream-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900042 |

## readFully

```TypeScript
readFully(): ArrayBuffer
```

Reads all content of a file.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArrayBuffer |

**Error codes:**

| Error Code ID |
| --- |
| 13900005 |
| 13900042 |

## startWrite

```TypeScript
startWrite(): WriteStream
```

Starts to write new file data in the WriteStream object returned. If the file does not exist, create a file. Call finishWrite() if the write operation is successful; call failWrite() if the write operation fails.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WriteStream](arkts-corefile-file-fs-writestream-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900027 |
| 13900042 |
