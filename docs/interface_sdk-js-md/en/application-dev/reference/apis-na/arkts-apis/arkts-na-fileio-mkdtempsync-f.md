# mkdtempSync

## mkdtempSync

```TypeScript
function mkdtempSync(prefix: string): string
```

Creates a temporary directory. This API returns the result synchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function mkdtempSync(prefix: string): string--><!--Device-fileIo-function mkdtempSync(prefix: string): string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| prefix | string | Yes | String to be replaced with six randomly generated characters to create a unique temporary directory. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Unique directory generated. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900018 | Not a directory |
| 13900028 | Too many links |
| 13900030 | File name too long |
| 13900025 | No space left on device |
| 13900001 | Operation not permitted |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900015 | File exists |
| 13900008 | Bad file descriptor |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

