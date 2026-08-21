# ReadStream

Defines a readable stream. You need to use [fileIo.createReadStream](arkts-fileio-createreadstream-f.md) to create a **ReadStream** instance, which is inherited from [stream.Readable](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md).

The data obtained by **ReadStream** is a decoded string. Currently, only the UTF-8 format is supported.

**Inheritance/Implementation:** ReadStream extends [stream.Readable](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-class ReadStream--><!--Device-fileIo-class ReadStream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
```

## close

```TypeScript
close(): void
```

Closes this readable stream.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ReadStream-close(): void--><!--Device-ReadStream-close(): void-End-->

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

The ReadStream constructor.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ReadStream-constructor()--><!--Device-ReadStream-constructor()-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## seek

```TypeScript
seek(offset: long, whence?: WhenceType): long
```

Adjusts the position of the readable stream offset pointer.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ReadStream-seek(offset: long, whence?: WhenceType): long--><!--Device-ReadStream-seek(offset: long, whence?: WhenceType): long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | long | Yes | Relative offset, in bytes. |
| whence | [WhenceType](../../apis-core-file-kit/arkts-apis/arkts-corefile-filefs-whencetype-e.md) | No | = WhenceType.SEEK_SET] - Where to start the offset. The default value is SEEK_SET, <br>which indicates the beginning of the file. |

**Return value:**

| Type | Description |
| --- | --- |
| long | Position of the current offset pointer (offset relative to the file header, in bytes). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error |
| 13900020 | Invalid argument |
| 13900026 | Illegal seek |
| 13900042 | Unknown error |

## bytesRead

```TypeScript
readonly bytesRead: long
```

Number of bytes read by the readable stream.

**Type:** long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ReadStream-readonly bytesRead: long--><!--Device-ReadStream-readonly bytesRead: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## path

```TypeScript
readonly path: string
```

Path of the file corresponding to the readable stream.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ReadStream-readonly path: string--><!--Device-ReadStream-readonly path: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

