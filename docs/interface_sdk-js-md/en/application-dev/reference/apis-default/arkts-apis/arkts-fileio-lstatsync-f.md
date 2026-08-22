# lstatSync

## Modules to Import

```TypeScript
```

## lstatSync

```TypeScript
function lstatSync(path: string): Stat
```

Obtains information about a symbolic link that is used to refer to a file or directory synchronously. The attributes of the symbolic link are returned, instead of the attributes of the target file.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-fileIo-function lstatSync(path: string): Stat--><!--Device-fileIo-function lstatSync(path: string): Stat-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path or URI of the file. <br>**Note：**: URIs can be passed since API version 22. |

**Return value:**

| Type | Description |
| --- | --- |
| [Stat](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-stat-i.md) | File information obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900002 | No such file or directory |
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900018 | Not a directory |
| 13900030 | File name too long |
| 13900033 | Too many symbolic links encountered |
| 13900038 | Value too large for defined data type |
| 13900042 | Unknown error |

