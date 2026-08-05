# createRandomAccessFileSync

## createRandomAccessFileSync

```TypeScript
function createRandomAccessFileSync(file: string | File, mode?: int,
  options?: RandomAccessFileOptions): RandomAccessFile
```

Creates a RandomAccessFile instance based on a file path or file object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-function createRandomAccessFileSync(file: string | File, mode?: int,  options?: RandomAccessFileOptions): RandomAccessFile--><!--Device-fileIo-function createRandomAccessFileSync(file: string | File, mode?: int,  options?: RandomAccessFileOptions): RandomAccessFile-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| file | string \| File | Yes | Application sandbox path of the file or an opened file object. |
| mode | int | No | = OpenMode.READ\_\_\_ESCAPED\_UNDERSCORE\_\_\_ONLY] - Mode for creating the RandomAccessFile instance. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Defines the options used in createRandomAccessFile(). |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | RandomAccessFile instance created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900002 | No such file or directory |
| 13900004 | Interrupted system call |
| 13900006 | No such device or address |
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900014 | Device or resource busy |
| 13900015 | File exists |
| 13900017 | No such device |
| 13900018 | Not a directory |
| 13900019 | Is a directory |
| 13900020 | Invalid argument |
| 13900022 | Too many open files |
| 13900023 | Text file busy |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900027 | Read-only file system |
| 13900029 | Resource deadlock would occur |
| 13900030 | File name too long |
| 13900033 | Too many symbolic links encountered |
| 13900034 | Operation would block |
| 13900038 | Value too large for defined data type |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900044 | Network is unreachable |

