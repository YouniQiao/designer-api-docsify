# fdopenStream

## Modules to Import

```TypeScript
```

## fdopenStream

```TypeScript
function fdopenStream(fd: int, mode: string): Promise<Stream>
```

Opens a file stream based on the file descriptor. This API uses a promise to return the result. To close the stream, use **close()** of [Stream](arkts-fileio-stream-i.md).

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-fileIo-function fdopenStream(fd: int, mode: string): Promise<Stream>--><!--Device-fileIo-function fdopenStream(fd: int, mode: string): Promise<Stream>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | FD of the file. |
| mode | string | Yes | r**: Open a file for reading. The file must exist. <br>- **r+**: Open a file for both reading and writing. The file must exist. <br>- **w**: Open a file for writing. If the file exists, clear its content. If the file does not exist, create a file. <br>- **w+**: Open a file for both reading and writing. If the file exists, clear its content. If the file does not exist, create a file. <br>- **a**: Open a file in append mode for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved). <br>- **a+**: Open a file in append mode for reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Stream](../../apis-core-file-kit/arkts-apis/arkts-corefile-filefs-stream-i.md)&gt; | Promise used to return the stream result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900002 | No such file or directory |
| 13900004 | Interrupted system call |
| 13900006 | No such device or address |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
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


## fdopenStream

```TypeScript
function fdopenStream(fd: int, mode: string, callback: AsyncCallback<Stream>): void
```

Opens a stream based on the file descriptor. To close the stream, use **close()** of [Stream](arkts-fileio-stream-i.md). This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-fileIo-function fdopenStream(fd: int, mode: string, callback: AsyncCallback<Stream>): void--><!--Device-fileIo-function fdopenStream(fd: int, mode: string, callback: AsyncCallback<Stream>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | FD of the file. |
| mode | string | Yes | r**: Open a file for reading. The file must exist. <br>- **r+**: Open a file for both reading and writing. The file must exist. <br>- **w**: Open a file for writing. If the file exists, clear its content. If the file does not exist, create a file. <br>- **w+**: Open a file for both reading and writing. If the file exists, clear its content. If the file does not exist, create a file. <br>- **a**: Open a file in append mode for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved). <br>- **a+**: Open a file in append mode for reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved). |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[Stream](../../apis-core-file-kit/arkts-apis/arkts-corefile-filefs-stream-i.md)&gt; | Yes | Callback used to return the **Stream** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900002 | No such file or directory |
| 13900004 | Interrupted system call |
| 13900006 | No such device or address |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
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

