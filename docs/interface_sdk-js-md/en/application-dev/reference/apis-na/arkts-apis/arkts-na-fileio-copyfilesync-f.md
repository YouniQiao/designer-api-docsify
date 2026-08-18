# copyFileSync

## Modules to Import

```TypeScript
```

## copyFileSync

```TypeScript
function copyFileSync(src: string | int, dest: string | int, mode?: int): void
```

Copies a file. This API returns the result synchronously.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function copyFileSync(src: string | int, dest: string | int, mode?: int): void--><!--Device-fileIo-function copyFileSync(src: string | int, dest: string | int, mode?: int): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string \| int | Yes | Path or FD of the file to copy. |
| dest | string \| int | Yes | Destination path of the file or FD of the file created. |
| mode | int | No | Whether to overwrite the file with the same name in the destination directory. The default value is **0**, which is the only value supported. <br>**0**: Overwrite the file with the same name completely and truncate the part that is not overwritten. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900018 | Not a directory |
| 13900019 | Is a directory |
| 13900030 | File name too long |
| 13900031 | Function not implemented |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900038 | Value too large for defined data type |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900034 | Operation would block |
| 13900012 | Permission denied |
| 13900044 | Network is unreachable |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

