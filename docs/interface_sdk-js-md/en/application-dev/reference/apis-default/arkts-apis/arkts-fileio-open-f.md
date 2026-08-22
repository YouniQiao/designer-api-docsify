# open

## Modules to Import

```TypeScript
```

## open

```TypeScript
function open(path: string, mode?: int): Promise<File>
```

Opens a file or directory. This API supports the use of a URI. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-fileIo-function open(path: string, mode?: int): Promise<File>--><!--Device-fileIo-function open(path: string, mode?: int): Promise<File>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path or URI of the file or directory. |
| mode | int | No | [OpenMode](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileio-openmode-n.md) for opening the file or directory. You must specify one of the following options. By default, the file is opened in read-only mode. <br>- **OpenMode.READ_ONLY(0o0)**: Open the file in read-only mode. <br>- **OpenMode.WRITE_ONLY(0o1)**: Open the file in write-only mode. <br>- **OpenMode.READ_WRITE(0o2)**: Open the file in read/write mode. <br>You can add the following function options in bitwise OR mode. By default, no additional option is added. <br>- **OpenMode.CREATE(0o100)**: Create a file if the file does not exist. <br>- **OpenMode.TRUNC(0o1000)**: If the file exists and is opened in write mode, truncate the file length to 0. <br>- **OpenMode.APPEND(0o2000)**: Open the file in append mode. New data will be added to the end of the file. <br>- **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform non-blocking operations on the opened file and in subsequent I/Os. <br>- **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an exception. The write permission is not allowed. <br>- **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception. <br>- **OpenMode.SYNC(0o4010000)**: Open the file in synchronous I/O mode. <br>- **OpenMode.UNCACHE(0o10000000000)**: Disable the page cache for reading and writing a file. This option is supported since API version 26.0.0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[File](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-file-i.md)&gt; | Promise used to return the **File** object. |

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


## open

```TypeScript
function open(path: string, callback: AsyncCallback<File>): void
```

Opens a file or directory. This API supports the use of a URI. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-fileIo-function open(path: string, callback: AsyncCallback<File>): void--><!--Device-fileIo-function open(path: string, callback: AsyncCallback<File>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path or URI of a file or directory. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[File](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-file-i.md)&gt; | Yes | Callback used to return the **File** object. |

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


## open

```TypeScript
function open(path: string, mode: int, callback: AsyncCallback<File>): void
```

Opens a file or directory with the specified mode. This API uses an asynchronous callback to return the result.

This API supports the use of a URI.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-fileIo-function open(path: string, mode: int, callback: AsyncCallback<File>): void--><!--Device-fileIo-function open(path: string, mode: int, callback: AsyncCallback<File>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path or URI of a file or directory. |
| mode | int | Yes | [OpenMode](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileio-openmode-n.md) for opening the file or directory. You must specify one of the following options. By default, the file is opened in read-only mode. <br>- **OpenMode.READ_ONLY(0o0)**: Open the file in read-only mode. <br>- **OpenMode.WRITE_ONLY(0o1)**: Open the file in write-only mode. <br>- **OpenMode.READ_WRITE(0o2)**: Open the file in read/write mode. <br>You can also specify the following options, separated by a bitwise OR operator (\|). By default, no additional options are given. <br>- **OpenMode.CREATE(0o100)**: If the file does not exist, create it. <br>- **OpenMode.TRUNC(0o1000)**: If the file exists and is opened in write mode, truncate the file length to 0. <br>- **OpenMode.APPEND(0o2000)**: Open the file in append mode. New data will be added to the end of the file. <br>- **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform non-blocking operations on the opened file and in subsequent I/Os. <br>- **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an exception. The write permission is not allowed. <br>- **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception. <br>- **OpenMode.SYNC(0o4010000)**: Open the file in synchronous I/O mode. <br>- **OpenMode.UNCACHE(0o10000000000)**: Disable the page cache for reading and writing a file. This option is supported since API version 26.0.0. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[File](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-file-i.md)&gt; | Yes | Callback used to return the **File** object. |

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

