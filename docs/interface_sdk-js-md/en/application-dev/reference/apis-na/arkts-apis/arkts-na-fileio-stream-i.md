# Stream

Provides APIs for stream operations, such as reading and writing data streams of files. After using an API of the **Stream** class, you need to call **close** to close the file stream. Before calling an API of the **Stream** class, you need to create a **Stream** instance by using [fileIo.createStream](arkts-na-fileio-createstream-f.md#createStream) or [fileIo.fdopenStream](arkts-na-fileio-fdopenstream-f.md#fdopenStream).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-interface Stream--><!--Device-fileIo-interface Stream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## close

```TypeScript
close(): Promise<void>
```

Closes the file stream. After the stream is closed, it cannot be used for read or write operations. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-Stream-close(): Promise<void>--><!--Device-Stream-close(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

## close

```TypeScript
close(callback: AsyncCallback<void>): void
```

Closes the file stream. After the stream is closed, it cannot be used for read or write operations. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-Stream-close(callback: AsyncCallback<void>): void--><!--Device-Stream-close(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the file stream is closed successfully, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

## closeSync

```TypeScript
closeSync(): void
```

Closes the file stream synchronously. After the stream is closed, it cannot be used for read or write operations.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-Stream-closeSync(): void--><!--Device-Stream-closeSync(): void-End-->

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

## flush

```TypeScript
flush(): Promise<void>
```

Flushes all data from this stream. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-Stream-flush(): Promise<void>--><!--Device-Stream-flush(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

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

## flush

```TypeScript
flush(callback: AsyncCallback<void>): void
```

Flushes the file stream. This API returns the result asynchronously. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-Stream-flush(callback: AsyncCallback<void>): void--><!--Device-Stream-flush(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the file stream is refreshed successfully, **err** is **undefined**; otherwise, **err** is an error object. |

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

## flushSync

```TypeScript
flushSync(): void
```

Flushes the file stream. This API returns the result synchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-Stream-flushSync(): void--><!--Device-Stream-flushSync(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

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

## read

```TypeScript
read(
    buffer: ArrayBuffer,
    options?: ReadOptions
  ): Promise<long>
```

Reads data from a stream file and returns the number of bytes read. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-Stream-read(    buffer: ArrayBuffer,    options?: ReadOptions  ): Promise<long>--><!--Device-Stream-read(    buffer: ArrayBuffer,    options?: ReadOptions  ): Promise<long>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](arkts-na-file-fs-readoptions-i.md) | No | The options are as follows: &lt;br&gt;- **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the buffer length. &lt;br&gt;- **offset** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position. |

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

Reads data from a stream file and returns the number of bytes read. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-Stream-read(buffer: ArrayBuffer, callback: AsyncCallback<long>): void--><!--Device-Stream-read(buffer: ArrayBuffer, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Callback used to return the data read, in bytes. |

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

Reads data from a stream file and returns the number of bytes read. The read options can be configured. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-Stream-read(    buffer: ArrayBuffer,    options: ReadOptions,    callback: AsyncCallback<long>  ): void--><!--Device-Stream-read(    buffer: ArrayBuffer,    options: ReadOptions,    callback: AsyncCallback<long>  ): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](arkts-na-file-fs-readoptions-i.md) | Yes | The options are as follows: &lt;br&gt;- **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the buffer length. &lt;br&gt;- **offset** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Callback used to return the data read, in bytes. |

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

Reads data from a stream file synchronously and returns the number of bytes read.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-Stream-readSync(    buffer: ArrayBuffer,    options?: ReadOptions  ): long--><!--Device-Stream-readSync(    buffer: ArrayBuffer,    options?: ReadOptions  ): long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](arkts-na-file-fs-readoptions-i.md) | No | The options are as follows: &lt;br&gt;- **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the buffer length. &lt;br&gt;- **offset** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position. &lt;br&gt; |

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

## write

```TypeScript
write(
    buffer: ArrayBuffer | string,
    options?: WriteOptions
  ): Promise<long>
```

Writes data to a stream file and returns the number of bytes written. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-Stream-write(    buffer: ArrayBuffer | string,    options?: WriteOptions  ): Promise<long>--><!--Device-Stream-write(    buffer: ArrayBuffer | string,    options?: WriteOptions  ): Promise<long>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](arkts-na-file-fs-writeoptions-i.md) | No | The options are as follows: &lt;br&gt;- **length** (number): length of the data to write, in bytes. The default value is the buffer length. &lt;br&gt;- **offset** (number): start position to write the data in the file, in bytes. This parameter is optional. By default, data is written from the current position. &lt;br&gt;- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported. |

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

Writes data to a stream file and returns the number of bytes written. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-Stream-write(buffer: ArrayBuffer | string, callback: AsyncCallback<long>): void--><!--Device-Stream-write(buffer: ArrayBuffer | string, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Callback used to return the length of the data written, in bytes. |

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

Writes data to a stream file and returns the number of bytes written. The write options can be configured. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-Stream-write(    buffer: ArrayBuffer | string,    options: WriteOptions,    callback: AsyncCallback<long>  ): void--><!--Device-Stream-write(    buffer: ArrayBuffer | string,    options: WriteOptions,    callback: AsyncCallback<long>  ): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](arkts-na-file-fs-writeoptions-i.md) | Yes | The options are as follows: &lt;br&gt;- **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the buffer length. &lt;br&gt;- **offset** (number): start position to write the data in the file, in bytes. This parameter is optional. By default, data is written from the current position. &lt;br&gt;- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Callback used to return the length of the data written, in bytes. |

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

Writes data to a stream file synchronously and returns the number of bytes written.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-Stream-writeSync(    buffer: ArrayBuffer | string,    options?: WriteOptions  ): long--><!--Device-Stream-writeSync(    buffer: ArrayBuffer | string,    options?: WriteOptions  ): long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](arkts-na-file-fs-writeoptions-i.md) | No | The options are as follows: &lt;br&gt;- **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the buffer length. &lt;br&gt;- **offset** (number): start position to write the data in the file, in bytes. This parameter is optional. By default, data is written from the current position. &lt;br&gt;- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported. |

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

