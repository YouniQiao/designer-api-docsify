# utimes

## Modules to Import

```TypeScript
```

## utimes

```TypeScript
function utimes(path: string, mtime: double): void
```

Changes the time when the file was last modified.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function utimes(path: string, mtime: double): void--><!--Device-fileIo-function utimes(path: string, mtime: double): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file. |
| mtime | double | Yes | New timestamp. The value is the number of milliseconds elapsed since the Epoch time (00:00:00 UTC on January 1, 1970). Only the time when the file was last modified can be changed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900001 | Operation not permitted |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900042 | Unknown error |
| 13900027 | Read-only file system |

