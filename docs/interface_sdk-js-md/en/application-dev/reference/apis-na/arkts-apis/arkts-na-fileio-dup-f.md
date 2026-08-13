# dup

## dup

```TypeScript
function dup(fd: int): File
```

Duplicates the file descriptor and returns the corresponding **File** object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function dup(fd: int): File--><!--Device-fileIo-function dup(fd: int): File-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | File descriptor. |

**Return value:**

| Type | Description |
| --- | --- |
| [File](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-file-i.md) | File object opened. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900022 | Too many open files |
| 13900014 | Device or resource busy |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |

