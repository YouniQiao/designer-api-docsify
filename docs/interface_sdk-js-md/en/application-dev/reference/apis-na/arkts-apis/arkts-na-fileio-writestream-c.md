# WriteStream

Defines a writeable stream. You need to use [fileIo.createWriteStream](arkts-na-fileio-createwritestream-f.md) to create a **WriteStream** instance, which is inherited from [stream.Writable](../../apis-arkts/arkts-apis/arkts-arkts-stream-writable-c.md).

**Inheritance/Implementation:** WriteStream extends [stream.Writable](../../apis-arkts/arkts-apis/arkts-arkts-stream-writable-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-class WriteStream--><!--Device-fileIo-class WriteStream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
```

## close

```TypeScript
close(): void
```

Closes this writeable stream.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-WriteStream-close(): void--><!--Device-WriteStream-close(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

## constructor

```TypeScript
constructor()
```

The WriteStream constructor.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-WriteStream-constructor()--><!--Device-WriteStream-constructor()-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## seek

```TypeScript
seek(offset: long, whence?: WhenceType): long
```

Adjusts the position of the writeable stream offset pointer.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-WriteStream-seek(offset: long, whence?: WhenceType): long--><!--Device-WriteStream-seek(offset: long, whence?: WhenceType): long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | long | Yes | Relative offset, in bytes. |
| whence | [WhenceType](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-whencetype-e.md) | No | = WhenceType.SEEK_SET] - Where to start the offset. <br>The default value is SEEK_SET, which indicates the beginning of the file. |

**Return value:**

| Type | Description |
| --- | --- |
| long | Position of the current offset pointer (offset relative to the file header, in bytes). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error |
| 13900026 | Illegal seek |
| 13900042 | Unknown error |

## bytesWritten

```TypeScript
readonly bytesWritten: long
```

Number of bytes written to the writable stream.

**Type:** long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-WriteStream-readonly bytesWritten: long--><!--Device-WriteStream-readonly bytesWritten: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## path

```TypeScript
readonly path: string
```

Path of the file corresponding to the writeable stream.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-WriteStream-readonly path: string--><!--Device-WriteStream-readonly path: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

