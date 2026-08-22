# closeSync

## Modules to Import

```TypeScript
```

## closeSync

```TypeScript
function closeSync(file: int | File): void
```

Closes a file or directory synchronously. After the file or directory is closed, the FD becomes invalid and cannot be used for read/write operations.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-fileIo-function closeSync(file: int | File): void--><!--Device-fileIo-function closeSync(file: int | File): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| file | int \| [File](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-file-i.md) | Yes | File** object or FD of the file to close. After the function is disabled, the **File** object or FD cannot be used for read and write operations. If the file object or file descriptor is still used, an error may occur or the operation may fail. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

