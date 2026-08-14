# statSync

## statSync

```TypeScript
function statSync(file: string | int): Stat
```

Obtains detailed attributes of a file or directory synchronously. The returned **Stat** object contains attributes such as the file size, permission mode, access time, and modification time.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function statSync(file: string | int): Stat--><!--Device-fileIo-function statSync(file: string | int): Stat-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| file | string \| int | Yes | Application sandbox path, URI, or FD of the file or directory. <br>**Note：**: URIs can be passed since API version 22. |

**Return value:**

| Type | Description |
| --- | --- |
| [Stat](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-stat-i.md) | Detailed information of a file or directory. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900018 | Not a directory |
| 13900030 | File name too long |
| 13900031 | Function not implemented |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900038 | Value too large for defined data type |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

