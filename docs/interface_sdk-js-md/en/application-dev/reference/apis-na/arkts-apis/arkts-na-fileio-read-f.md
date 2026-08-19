# read

## Modules to Import

```TypeScript
```

## read

```TypeScript
function read(
  fd: int,
  buffer: ArrayBuffer,
  options?: ReadOptions
): Promise<long>
```

Reads data from a file and returns the number of bytes read. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function read(  fd: int,  buffer: ArrayBuffer,  options?: ReadOptions): Promise<long>--><!--Device-fileIo-function read(  fd: int,  buffer: ArrayBuffer,  options?: ReadOptions): Promise<long>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | FD of the file. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| options | [ReadOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-readoptions-i.md) | No | The options are as follows: <br>- **offset** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position. <br>- **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the buffer length. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | Promise used to return the length of the data read, in bytes. |

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
function read(fd: int, buffer: ArrayBuffer, callback: AsyncCallback<long>): void
```

Reads data from a file and returns the number of bytes read. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function read(fd: int, buffer: ArrayBuffer, callback: AsyncCallback<long>): void--><!--Device-fileIo-function read(fd: int, buffer: ArrayBuffer, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | FD of the file. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
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
function read(
  fd: int,
  buffer: ArrayBuffer,
  options: ReadOptions,
  callback: AsyncCallback<long>
): void
```

Reads data from a file. Read options (such as the offset position and length of the data read) can be configured. The number of bytes read is returned. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fileIo-function read(  fd: int,  buffer: ArrayBuffer,  options: ReadOptions,  callback: AsyncCallback<long>): void--><!--Device-fileIo-function read(  fd: int,  buffer: ArrayBuffer,  options: ReadOptions,  callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | FD of the file. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| options | [ReadOptions](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-readoptions-i.md) | Yes | The options are as follows: <br>- **offset** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position. <br>- **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the buffer length. |
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

