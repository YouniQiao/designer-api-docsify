# fsyncSync

## fsyncSync

```TypeScript
function fsyncSync(fd: int): void
```

Synchronizes the cached data of a file to storage. This API returns the result synchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function fsyncSync(fd: int): void--><!--Device-fileIo-function fsyncSync(fd: int): void-End-->

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

