# mkdirSync

## mkdirSync

```TypeScript
function mkdirSync(path: string): void
```

Creates a single-level directory synchronously. If the parent directory does not exist, an error is reported.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function mkdirSync(path: string): void--><!--Device-fileIo-function mkdirSync(path: string): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |

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


## mkdirSync

```TypeScript
function mkdirSync(path: string, recursion: boolean): void
```

Creates a directory. This API returns the result synchronously. The value **true** means to create a directory recursively.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function mkdirSync(path: string, recursion: boolean): void--><!--Device-fileIo-function mkdirSync(path: string, recursion: boolean): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| recursion | boolean | Yes | Whether to create a directory recursively. <br> The value **true** means to create a directory recursively. The value **false** means to create a single- level directory. |

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

