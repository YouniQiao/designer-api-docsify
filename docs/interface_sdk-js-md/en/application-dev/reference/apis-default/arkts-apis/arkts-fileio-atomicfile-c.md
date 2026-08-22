# AtomicFile

AtomicFile is a class used to perform atomic read and write operations on files. A temporary file is written and renamed to the original file location, which ensures file integrity. If the write operation fails, the temporary file is deleted without modifying the original file content. You can call finishWrite() or failWrite() to write or roll back file content.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-fileIo-export class AtomicFile--><!--Device-fileIo-export class AtomicFile-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(path: string)
```

The AtomicFile constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AtomicFile-constructor(path: string)--><!--Device-AtomicFile-constructor(path: string)-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |  |

## delete

```TypeScript
delete(): void
```

Deletes the AtomicFile class, including the original files and temporary files.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AtomicFile-delete(): void--><!--Device-AtomicFile-delete(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 |  |
| 13900002 |  |
| 13900012 |  |
| 13900027 |  |
| 13900042 |  |

## failWrite

```TypeScript
failWrite(): void
```

Rolls back the file after the file fails to be written.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AtomicFile-failWrite(): void--><!--Device-AtomicFile-failWrite(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900042 |  |

## finishWrite

```TypeScript
finishWrite(): void
```

Finishes writing file data when the write operation is complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AtomicFile-finishWrite(): void--><!--Device-AtomicFile-finishWrite(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900042 |  |

## getBaseFile

```TypeScript
getBaseFile(): File
```

Obtains the file object through the AtomicFile object. The FD needs to be closed by calling close().

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AtomicFile-getBaseFile(): File--><!--Device-AtomicFile-getBaseFile(): File-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| [File](../../apis-core-file-kit/arkts-apis/arkts-corefile-filefs-file-i.md) | File object opened. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 |  |
| 13900005 |  |
| 13900012 |  |
| 13900042 |  |

## openRead

```TypeScript
openRead(): ReadStream
```

Creates a ReadStream instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AtomicFile-openRead(): ReadStream--><!--Device-AtomicFile-openRead(): ReadStream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| [ReadStream](../../apis-core-file-kit/arkts-apis/arkts-corefile-filefs-readstream-c.md) | ReadStream instance obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 |  |
| 13900002 |  |
| 13900012 |  |
| 13900042 |  |

## readFully

```TypeScript
readFully(): ArrayBuffer
```

Reads all content of a file.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AtomicFile-readFully(): ArrayBuffer--><!--Device-AtomicFile-readFully(): ArrayBuffer-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer | Full content of a file. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900005 |  |
| 13900042 |  |

## startWrite

```TypeScript
startWrite(): WriteStream
```

Starts to write new file data in the WriteStream object returned. If the file does not exist, create a file. Call finishWrite() if the write operation is successful; call failWrite() if the write operation fails.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AtomicFile-startWrite(): WriteStream--><!--Device-AtomicFile-startWrite(): WriteStream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| [WriteStream](../../apis-core-file-kit/arkts-apis/arkts-corefile-filefs-writestream-c.md) | Returns the file write stream. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 |  |
| 13900002 |  |
| 13900012 |  |
| 13900027 |  |
| 13900042 |  |

