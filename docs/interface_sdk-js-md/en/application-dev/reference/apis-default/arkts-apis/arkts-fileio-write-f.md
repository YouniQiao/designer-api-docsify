# write

## Modules to Import

```TypeScript
```

## write

```TypeScript
function write(
  fd: int,
  buffer: ArrayBuffer | string,
  options?: WriteOptions
): Promise<long>
```

Writes data to a file and returns the number of bytes written. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-fileIo-function write(  fd: int,  buffer: ArrayBuffer | string,  options?: WriteOptions): Promise<long>--><!--Device-fileIo-function write(  fd: int,  buffer: ArrayBuffer | string,  options?: WriteOptions): Promise<long>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | FD of the file. |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-writeoptions-i.md) | No | The options are as follows: <br> - **offset** (number): start position to write the data in the file, in bytes. This parameter is optional. Bydefault, data is written from the current position. <br>- **length** (number): length of the data to write, in bytes. This parameter is optional. The default valueis the buffer length.<br> - **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported currently. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | Promise used to return the length of the data written, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900013 | Bad address |
| 13900020 | Invalid argument |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900034 | Operation would block |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |


## write

```TypeScript
function write(fd: int, buffer: ArrayBuffer | string, callback: AsyncCallback<long>): void
```

Writes data to a file and returns the number of bytes written. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-fileIo-function write(fd: int, buffer: ArrayBuffer | string, callback: AsyncCallback<long>): void--><!--Device-fileIo-function write(fd: int, buffer: ArrayBuffer | string, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | FD of the file. |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Callback used to return the length of the data written, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900013 | Bad address |
| 13900020 | Invalid argument |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900034 | Operation would block |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |


## write

```TypeScript
function write(
  fd: int,
  buffer: ArrayBuffer | string,
  options: WriteOptions,
  callback: AsyncCallback<long>
): void
```

Writes data to a file. Write options (such as the offset position and length of the data written) can be configured.The number of bytes written is returned. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-fileIo-function write(  fd: int,  buffer: ArrayBuffer | string,  options: WriteOptions,  callback: AsyncCallback<long>): void--><!--Device-fileIo-function write(  fd: int,  buffer: ArrayBuffer | string,  options: WriteOptions,  callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | FD of the file. |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-writeoptions-i.md) | Yes | The options are as follows: <br>- **offset** (number): start position to write the data in the file, in bytes. This parameter is optional. Bydefault, data is written from the current position. <br>- **length** (number): length of the data to write, in bytes. This parameter is optional. The default valueis the buffer length. <br>- **encoding** (string): format of the data to be encoded when the data is a string. The default value is**'utf-8'**, which is the only value supported currently. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Callback used to return the length of the data written, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900013 | Bad address |
| 13900020 | Invalid argument |
| 13900024 | File too large |
| 13900025 | No space left on device |
| 13900034 | Operation would block |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

