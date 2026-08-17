# lseek

## lseek

```TypeScript
function lseek(fd: int, offset: long, whence?: WhenceType): long
```

Adjusts the position of the file offset pointer.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function lseek(fd: int, offset: long, whence?: WhenceType): long--><!--Device-fileIo-function lseek(fd: int, offset: long, whence?: WhenceType): long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | File descriptor. |
| offset | long | Yes | Relative offset, in bytes. |
| whence | [WhenceType](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-whencetype-e.md) | No | Where to start the offset. If this parameter is not specified, the file start position is used by default. |

**Return value:**

| Type | Description |
| --- | --- |
| long | Position of the current offset as measured from the beginning of the file, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900038 | Value too large for defined data type |
| 13900008 | Bad file descriptor |
| 13900026 | Illegal seek |
| 13900042 | Unknown error |

