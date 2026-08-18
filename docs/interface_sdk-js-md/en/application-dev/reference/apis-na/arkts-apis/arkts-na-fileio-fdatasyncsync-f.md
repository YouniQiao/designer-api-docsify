# fdatasyncSync

## Modules to Import

```TypeScript
```

## fdatasyncSync

```TypeScript
function fdatasyncSync(fd: int): void
```

Synchronizes the data of a file. This API returns the result synchronously.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function fdatasyncSync(fd: int): void--><!--Device-fileIo-function fdatasyncSync(fd: int): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | FD of the file. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900027 | Read-only file system |

