# RandomAccessFile

Provides APIs for randomly reading and writing a stream based on offset pointers. Before invoking any API of **RandomAccessFile**, you need to use **createRandomAccessFile()** to create a **RandomAccessFile** instance synchronously or asynchronously.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-interface RandomAccessFile--><!--Device-fileIo-interface RandomAccessFile-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
```

## close

```TypeScript
close(): void
```

Closes a **RandomAccessFile** object synchronously. After the object is closed, it cannot be used for read or write operations.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-RandomAccessFile-close(): void--><!--Device-RandomAccessFile-close(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

## getReadStream

```TypeScript
getReadStream(): ReadStream
```

Obtains a **ReadStream** instance of this **RandomAccessFile** to read data from a stream file.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-RandomAccessFile-getReadStream(): ReadStream--><!--Device-RandomAccessFile-getReadStream(): ReadStream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| [ReadStream](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-readstream-c.md) | ReadStream** instance obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error |
| 13900012 | Permission denied |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

## getWriteStream

```TypeScript
getWriteStream(): WriteStream
```

Obtains a **WriteStream** instance of this **RandomAccessFile** to write data to a stream file.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-RandomAccessFile-getWriteStream(): WriteStream--><!--Device-RandomAccessFile-getWriteStream(): WriteStream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| [WriteStream](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-writestream-c.md) | WriteStream** instance obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error |
| 13900012 | Permission denied |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

## read

```TypeScript
read(
    buffer: ArrayBuffer,
    options?: ReadOptions
  ): Promise<long>
```

Reads data from a file and returns the number of bytes read. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-RandomAccessFile-read(    buffer: ArrayBuffer,    options?: ReadOptions  ): Promise<long>--><!--Device-RandomAccessFile-read(    buffer: ArrayBuffer,    options?: ReadOptions  ): Promise<long>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-readoptions-i.md) | No | The options are as follows: <br>- **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the buffer length.<br> - **offset** (number): start position to read the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is read from the **filePointer**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | Promise used to return the data read, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900034 | Operation would block |
| 13900019 | Is a directory |
| 13900044 | Network is unreachable |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900042 | Unknown error |

## read

```TypeScript
read(buffer: ArrayBuffer, callback: AsyncCallback<long>): void
```

Reads data from a file and returns the number of bytes read. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-RandomAccessFile-read(buffer: ArrayBuffer, callback: AsyncCallback<long>): void--><!--Device-RandomAccessFile-read(buffer: ArrayBuffer, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;long&gt; | Yes | Callback used to return the length of the data read, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900034 | Operation would block |
| 13900019 | Is a directory |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900042 | Unknown error |

## read

```TypeScript
read(
    buffer: ArrayBuffer,
    options: ReadOptions,
    callback: AsyncCallback<long>
  ): void
```

Reads data from a file and returns the number of bytes read. The read options can be configured. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-RandomAccessFile-read(    buffer: ArrayBuffer,    options: ReadOptions,    callback: AsyncCallback<long>  ): void--><!--Device-RandomAccessFile-read(    buffer: ArrayBuffer,    options: ReadOptions,    callback: AsyncCallback<long>  ): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-readoptions-i.md) | Yes | The options are as follows: <br>- **length** (number): length of the data to read, in bytes. This parameter is optional. The default valueis the buffer length.<br>- **offset** (number): start position to read the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is read from the **filePointer**. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;long&gt; | Yes | Callback used to return the length of the data read, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900034 | Operation would block |
| 13900019 | Is a directory |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900042 | Unknown error |

## readSync

```TypeScript
readSync(
    buffer: ArrayBuffer,
    options?: ReadOptions
  ): long
```

Reads data from a file synchronously and returns the number of bytes read.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-RandomAccessFile-readSync(    buffer: ArrayBuffer,    options?: ReadOptions  ): long--><!--Device-RandomAccessFile-readSync(    buffer: ArrayBuffer,    options?: ReadOptions  ): long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-readoptions-i.md) | No | The options are as follows: <br>- **length** (number): length of the data to read, in bytes. This parameter is optional. The default valueis the buffer length.<br>- **offset** (number): start position to read the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is read from the **filePointer**. |

**Return value:**

| Type | Description |
| --- | --- |
| long | Length of the data read, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900034 | Operation would block |
| 13900019 | Is a directory |
| 13900044 | Network is unreachable |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900042 | Unknown error |

## setFilePointer

```TypeScript
setFilePointer(filePointer: long): void
```

Sets the file offset pointer to specify the start position of subsequent read and write operations.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-RandomAccessFile-setFilePointer(filePointer: long): void--><!--Device-RandomAccessFile-setFilePointer(filePointer: long): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePointer | long | Yes | Offset pointer to the **RandomAccessFile** instance, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |

## write

```TypeScript
write(
    buffer: ArrayBuffer | string,
    options?: WriteOptions
  ): Promise<long>
```

Writes data to a file. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-RandomAccessFile-write(    buffer: ArrayBuffer | string,    options?: WriteOptions  ): Promise<long>--><!--Device-RandomAccessFile-write(    buffer: ArrayBuffer | string,    options?: WriteOptions  ): Promise<long>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-writeoptions-i.md) | No | The options are as follows: <br>- **length** (number): length of the data to write, in bytes. The default value is the buffer length. <br>- **offset** (number): start position to write the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is written from the **filePointer**. <br>- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | Promise used to return the length of the data written, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900001 | Operation not permitted |
| 13900034 | Operation would block |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900010 | Try again |
| 13900042 | Unknown error |

## write

```TypeScript
write(buffer: ArrayBuffer | string, callback: AsyncCallback<long>): void
```

Writes data to a file. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-RandomAccessFile-write(buffer: ArrayBuffer | string, callback: AsyncCallback<long>): void--><!--Device-RandomAccessFile-write(buffer: ArrayBuffer | string, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;long&gt; | Yes | Callback used to return the length of the data written, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900001 | Operation not permitted |
| 13900034 | Operation would block |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900010 | Try again |
| 13900042 | Unknown error |

## write

```TypeScript
write(
    buffer: ArrayBuffer | string,
    options: WriteOptions,
    callback: AsyncCallback<long>
  ): void
```

Writes data to a file. Write options can be configured. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-RandomAccessFile-write(    buffer: ArrayBuffer | string,    options: WriteOptions,    callback: AsyncCallback<long>  ): void--><!--Device-RandomAccessFile-write(    buffer: ArrayBuffer | string,    options: WriteOptions,    callback: AsyncCallback<long>  ): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-writeoptions-i.md) | Yes | The options are as follows: <br>- **length** (number): length of the data to write, in bytes. The default value is the buffer length. <br>- **offset** (number): start position to write the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is written from the **filePointer**. <br>- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;long&gt; | Yes | Callback used to return the length of the data written, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900001 | Operation not permitted |
| 13900034 | Operation would block |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900010 | Try again |
| 13900042 | Unknown error |

## writeSync

```TypeScript
writeSync(
    buffer: ArrayBuffer | string,
    options?: WriteOptions
  ): long
```

Writes data to a file. This API returns the result synchronously.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-RandomAccessFile-writeSync(    buffer: ArrayBuffer | string,    options?: WriteOptions  ): long--><!--Device-RandomAccessFile-writeSync(    buffer: ArrayBuffer | string,    options?: WriteOptions  ): long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-writeoptions-i.md) | No | The options are as follows: <br>- **length** (number): length of the data to write, in bytes. The default value is the buffer length. <br>- **offset** (number): start position to write the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is written from the **filePointer**. <br>- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported. |

**Return value:**

| Type | Description |
| --- | --- |
| long | Length of the data written in the file, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900001 | Operation not permitted |
| 13900034 | Operation would block |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900010 | Try again |
| 13900042 | Unknown error |

## fd

```TypeScript
readonly fd: int
```

FD of the file.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-RandomAccessFile-readonly fd: int--><!--Device-RandomAccessFile-readonly fd: int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## filePointer

```TypeScript
readonly filePointer: long
```

Offset pointer to the **RandomAccessFile** instance, in bytes. This parameter indicates the current read/write position.

**Type:** long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-RandomAccessFile-readonly filePointer: long--><!--Device-RandomAccessFile-readonly filePointer: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

