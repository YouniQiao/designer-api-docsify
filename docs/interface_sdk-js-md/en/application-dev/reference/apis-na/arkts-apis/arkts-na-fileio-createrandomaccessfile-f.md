# createRandomAccessFile

## createRandomAccessFile

```TypeScript
function createRandomAccessFile(file: string | File, mode?: int,
  options?: RandomAccessFileOptions): Promise<RandomAccessFile>
```

Creates a **RandomAccessFile** instance based on a file path or file object. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function createRandomAccessFile(file: string | File, mode?: int,  options?: RandomAccessFileOptions): Promise<RandomAccessFile>--><!--Device-fileIo-function createRandomAccessFile(file: string | File, mode?: int,  options?: RandomAccessFileOptions): Promise<RandomAccessFile>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| file | string \| [File](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-file-i.md) | Yes | Application sandbox path of the file or an opened file object. |
| mode | int | No | [OpenMode](arkts-na-fileio-openmode-n.md#OpenMode) for creating the **RandomAccessFile** instance. This parameter is valid only when the application sandbox path of the file is passed in. One of the following options must be specified: &lt;br&gt;- **OpenMode.READ_ONLY(0o0)**: Create the file in read-only mode. This is the default value. &lt;br&gt;- **OpenMode.WRITE_ONLY(0o1)**: Create the file in write-only mode. &lt;br&gt;- **OpenMode.READ_WRITE(0o2)**: Create the file in read/write mode. &lt;br&gt;You can also specify the following options, separated by a bitwise OR operator (\|). By default, no additional options are given. &lt;br&gt;- **OpenMode.CREATE(0o100)**: If the file does not exist, create it. &lt;br&gt;- **OpenMode.TRUNC(0o1000)**: If the **RandomAccessFile** object already exists and is created in write mode, truncate the file length to 0. &lt;br&gt;- **OpenMode.APPEND(0o2000)**: Create the file in append mode. New data will be added to the end of the **RandomAccessFile** object. &lt;br&gt;- **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform non-blocking operations on the opened file and in subsequent I/Os. &lt;br&gt;- **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an exception. The write permission is not allowed. &lt;br&gt;- **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception. &lt;br&gt;- **OpenMode.SYNC(0o4010000)**: Create a **RandomAccessFile** instance in synchronous I/O mode. |
| options | [RandomAccessFileOptions](arkts-na-file-fs-randomaccessfileoptions-i.md) | No | The options are as follows: &lt;br&gt;- **start** (number): start position to read data, in bytes. This parameter is optional. By default, data is read from the current position. &lt;br&gt;- **end** (number): end position to read data, in bytes. This parameter is optional. The default value is the end of the file. &lt;br&gt;This parameter takes effect only for file stream objects obtained by [getreadstream](arkts-na-fileio-randomaccessfile-i.md#getReadStream) and [getwritestream](arkts-na-fileio-randomaccessfile-i.md#getWriteStream). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[RandomAccessFile](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-randomaccessfile-i.md)&gt; | Promise used to return the **RandomAccessFile** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900038 | Value too large for defined data type |
| 13900033 | Too many symbolic links encountered |
| 13900034 | Operation would block |
| 13900044 | Network is unreachable |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900020 | Invalid argument |
| 13900022 | Too many open files |
| 13900023 | Text file busy |
| 13900017 | No such device |
| 13900018 | Not a directory |
| 13900019 | Is a directory |
| 13900029 | Resource deadlock would occur |
| 13900030 | File name too long |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900027 | Read-only file system |
| 13900004 | Interrupted system call |
| 13900006 | No such device or address |
| 13900001 | Operation not permitted |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900014 | Device or resource busy |
| 13900015 | File exists |
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |


## createRandomAccessFile

```TypeScript
function createRandomAccessFile(file: string | File, callback: AsyncCallback<RandomAccessFile>): void
```

Creates a **RandomAccessFile** instance in read-only mode based on a file path or file object. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function createRandomAccessFile(file: string | File, callback: AsyncCallback<RandomAccessFile>): void--><!--Device-fileIo-function createRandomAccessFile(file: string | File, callback: AsyncCallback<RandomAccessFile>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| file | string \| [File](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-file-i.md) | Yes | Application sandbox path of the file or an opened file object. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RandomAccessFile](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-randomaccessfile-i.md)&gt; | Yes | Callback used to return the **RandomAccessFile** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900038 | Value too large for defined data type |
| 13900033 | Too many symbolic links encountered |
| 13900034 | Operation would block |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900020 | Invalid argument |
| 13900022 | Too many open files |
| 13900023 | Text file busy |
| 13900017 | No such device |
| 13900018 | Not a directory |
| 13900019 | Is a directory |
| 13900029 | Resource deadlock would occur |
| 13900030 | File name too long |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900027 | Read-only file system |
| 13900004 | Interrupted system call |
| 13900006 | No such device or address |
| 13900001 | Operation not permitted |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900014 | Device or resource busy |
| 13900015 | File exists |
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |


## createRandomAccessFile

```TypeScript
function createRandomAccessFile(file: string | File, mode: int, callback: AsyncCallback<RandomAccessFile>): void
```

Creates a **RandomAccessFile** instance based on a file path or file object. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-function createRandomAccessFile(file: string | File, mode: int, callback: AsyncCallback<RandomAccessFile>): void--><!--Device-fileIo-function createRandomAccessFile(file: string | File, mode: int, callback: AsyncCallback<RandomAccessFile>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| file | string \| [File](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-file-i.md) | Yes | Application sandbox path of the file or an opened file object. |
| mode | int | Yes | [OpenMode](arkts-na-fileio-openmode-n.md#OpenMode) for creating the **RandomAccessFile** instance. This parameter is valid only when the application sandbox path of the file is passed in. One of the following options must be specified: &lt;br&gt;- **OpenMode.READ_ONLY(0o0)**: Create the file in read-only mode. This is the default value. &lt;br&gt;- **OpenMode.WRITE_ONLY(0o1)**: Create the file in write-only mode. &lt;br&gt;- **OpenMode.READ_WRITE(0o2)**: Create the file in read/write mode. &lt;br&gt;You can also specify the following options, separated by a bitwise OR operator (\|). By default, no additional options are given. &lt;br&gt;- **OpenMode.CREATE(0o100)**: If the file does not exist, create it. &lt;br&gt;- **OpenMode.TRUNC(0o1000)**: If the **RandomAccessFile** object already exists and is created in write mode, truncate the file length to 0. &lt;br&gt;- **OpenMode.APPEND(0o2000)**: Create the file in append mode. New data will be added to the end of the **RandomAccessFile** object. &lt;br&gt;- **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform non-blocking operations on the opened file and in subsequent I/Os. &lt;br&gt;- **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an exception. The write permission is not allowed. &lt;br&gt;- **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception. &lt;br&gt;- **OpenMode.SYNC(0o4010000)**: Create a **RandomAccessFile** instance in synchronous I/O mode. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RandomAccessFile](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-randomaccessfile-i.md)&gt; | Yes | Callback used to return the **RandomAccessFile** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900038 | Value too large for defined data type |
| 13900033 | Too many symbolic links encountered |
| 13900034 | Operation would block |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |
| 13900020 | Invalid argument |
| 13900022 | Too many open files |
| 13900023 | Text file busy |
| 13900017 | No such device |
| 13900018 | Not a directory |
| 13900019 | Is a directory |
| 13900029 | Resource deadlock would occur |
| 13900030 | File name too long |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900027 | Read-only file system |
| 13900004 | Interrupted system call |
| 13900006 | No such device or address |
| 13900001 | Operation not permitted |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900013 | Bad address |
| 13900014 | Device or resource busy |
| 13900015 | File exists |
| 13900008 | Bad file descriptor |
| 13900011 | Out of memory |

