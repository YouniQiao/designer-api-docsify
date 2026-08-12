# RandomAccessFile

Provides APIs for randomly reading and writing a stream. Before invoking any API of **RandomAccessFile**, you need to use **createRandomAccessFile()** to create a **RandomAccessFile** instance synchronously or asynchronously.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface RandomAccessFile--><!--Device-unnamed-declare interface RandomAccessFile-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## close

```TypeScript
close(): void
```

Closes the **RandomAccessFile** instance. This API returns the result synchronously.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

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

## Examples

```TypeScript
let filePath = pathDir + "/test.txt";
let randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
randomAccessFile.close();
```

## getReadStream

```TypeScript
getReadStream(): ReadStream
```

Obtains a **ReadStream** instance of this **RandomAccessFile**.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-RandomAccessFile-getReadStream(): ReadStream--><!--Device-RandomAccessFile-getReadStream(): ReadStream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| [ReadStream](arkts-corefile-file-fs-readstream-c.md) | ReadStream** instance obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error |
| 13900012 | Permission denied |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

## Examples

```TypeScript
const filePath = pathDir + "/test.txt";
const randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
const rs = randomAccessFile.getReadStream();
rs.close();
randomAccessFile.close();
```

## getWriteStream

```TypeScript
getWriteStream(): WriteStream
```

Obtains a **WriteStream** instance of this **RandomAccessFile**.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-RandomAccessFile-getWriteStream(): WriteStream--><!--Device-RandomAccessFile-getWriteStream(): WriteStream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| [WriteStream](arkts-corefile-file-fs-writestream-c.md) | WriteStream** instance obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error |
| 13900012 | Permission denied |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

## Examples

```TypeScript
const filePath = pathDir + "/test.txt";
const randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
const ws = randomAccessFile.getWriteStream();
ws.close();
randomAccessFile.close();
```

## read

```TypeScript
read(
    buffer: ArrayBuffer,
    options?: ReadOptions
  ): Promise<number>
```

Reads data from a file. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-RandomAccessFile-read(    buffer: ArrayBuffer,    options?: ReadOptions  ): Promise<number>--><!--Device-RandomAccessFile-read(    buffer: ArrayBuffer,    options?: ReadOptions  ): Promise<number>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | No | The options are as follows:&lt;br&gt;- **length** (number): length of the data to read , in bytes. This parameter is optional. The default value is the buffer length.&lt;br&gt;- **offset** (number): start position to read the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is read from the **filePointer**.<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the data read, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900034 | Operation would block |
| 13900019 | Is a directory |
| 13900044 | Network is unreachable<br>**Applicable version:** 12 and later |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900042 | Unknown error |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let readOption: ReadOptions = {
  offset: 1,
  length: 5
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.read(arrayBuffer, readOption).then((readLength: number) => {
  console.info("randomAccessFile readLength: " + readLength);
}).catch((err: BusinessError) => {
  console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  randomAccessFile.close();
  fs.closeSync(file);
});
```

## read

```TypeScript
read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void
```

Reads data from a file. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-RandomAccessFile-read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void--><!--Device-RandomAccessFile-read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;number&gt; | Yes | Callback used to return the result. return the length of the data read, in bytes. |

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
    callback: AsyncCallback<number>
  ): void
```

Reads data from a file. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-RandomAccessFile-read(    buffer: ArrayBuffer,    options: ReadOptions,    callback: AsyncCallback<number>  ): void--><!--Device-RandomAccessFile-read(    buffer: ArrayBuffer,    options: ReadOptions,    callback: AsyncCallback<number>  ): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | Yes | The options are as follows:&lt;br&gt;- **length** (number): length of the data to read , in bytes. This parameter is optional. The default value is the buffer length.&lt;br&gt;- **offset** (number): start position to read the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is read from the **filePointer**.<br>**Since:** 11 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;number&gt; | Yes | Callback used to return the result. return the length of the data read, in bytes. |

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
  ): number
```

Reads data from a file. This API returns the result synchronously.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-RandomAccessFile-readSync(    buffer: ArrayBuffer,    options?: ReadOptions  ): number--><!--Device-RandomAccessFile-readSync(    buffer: ArrayBuffer,    options?: ReadOptions  ): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | No | The options are as follows:&lt;br&gt;- **length** (number): length of the data to read , in bytes. This parameter is optional. The default value is the buffer length.&lt;br&gt;- **offset** (number): start position to read the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is read from the **filePointer**.&lt;br&gt;<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| number | Length of the data read, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900034 | Operation would block |
| 13900019 | Is a directory |
| 13900044 | Network is unreachable<br>**Applicable version:** 12 and later |
| 13900013 | Bad address |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900042 | Unknown error |

## Examples

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
let length: number = 4096;
let arrayBuffer = new ArrayBuffer(length);
let readLength = randomAccessFile.readSync(arrayBuffer);
randomAccessFile.close();
fs.closeSync(file);
```

## setFilePointer

```TypeScript
setFilePointer(filePointer: number): void
```

Sets the file offset pointer.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-RandomAccessFile-setFilePointer(filePointer: number): void--><!--Device-RandomAccessFile-setFilePointer(filePointer: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePointer | number | Yes | Offset pointer to the **RandomAccessFile** instance, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900042 | Unknown error |

## Examples

```TypeScript
let filePath = pathDir + "/test.txt";
let randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
randomAccessFile.setFilePointer(1);
randomAccessFile.close();
```

## write

```TypeScript
write(
    buffer: ArrayBuffer | string,
    options?: WriteOptions
  ): Promise<number>
```

Writes data into a file. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-RandomAccessFile-write(    buffer: ArrayBuffer | string,    options?: WriteOptions  ): Promise<number>--><!--Device-RandomAccessFile-write(    buffer: ArrayBuffer | string,    options?: WriteOptions  ): Promise<number>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | No | The options are as follows:&lt;br&gt;- **length** (number): length of the data to write, in bytes. The default value is the buffer length.&lt;br&gt;- **offset** (number): start position to write the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is written from the **filePointer**.&lt;br&gt;- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the length of the data written, in bytes. |

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

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let writeOption: WriteOptions = {
  offset: 1,
  length: 5,
  encoding: 'utf-8'
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, writeOption).then((bytesWritten: number) => {
  console.info("randomAccessFile bytesWritten: " + bytesWritten);
}).catch((err: BusinessError) => {
  console.error("create randomAccessFile failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  randomAccessFile.close();
  fs.closeSync(file);
});
```

## write

```TypeScript
write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void
```

Writes data to a file. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-RandomAccessFile-write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void--><!--Device-RandomAccessFile-write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;number&gt; | Yes | Callback used to return the result. The call back returns the length of the data written, in bytes. |

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
    callback: AsyncCallback<number>
  ): void
```

Writes data to a file. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-RandomAccessFile-write(    buffer: ArrayBuffer | string,    options: WriteOptions,    callback: AsyncCallback<number>  ): void--><!--Device-RandomAccessFile-write(    buffer: ArrayBuffer | string,    options: WriteOptions,    callback: AsyncCallback<number>  ): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | Yes | The options are as follows:&lt;br&gt;- **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the buffer length.&lt;br&gt;- **offset** (number): start position to write the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is written from the **filePointer**.&lt;br&gt;- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.<br>**Since:** 11 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;number&gt; | Yes | Callback used to return the result. The call back returns the length of the data written, in bytes. |

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
  ): number
```

Writes data to a file. This API returns the result synchronously.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-RandomAccessFile-writeSync(    buffer: ArrayBuffer | string,    options?: WriteOptions  ): number--><!--Device-RandomAccessFile-writeSync(    buffer: ArrayBuffer | string,    options?: WriteOptions  ): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | No | The options are as follows:&lt;br&gt;- **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the buffer length.&lt;br&gt;- **offset** (number): start position to write the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is written from the **filePointer**.&lt;br&gt;- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| number | Length of the data written in the file, in bytes. |

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

## Examples

```TypeScript
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
let bytesWritten = randomAccessFile.writeSync("hello, world", writeOption);
randomAccessFile.close();
```

## fd

```TypeScript
readonly fd: number
```

FD of the file.

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-RandomAccessFile-readonly fd: number--><!--Device-RandomAccessFile-readonly fd: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## filePointer

```TypeScript
readonly filePointer: number
```

Offset pointer to the **RandomAccessFile** instance, in bytes.

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-RandomAccessFile-readonly filePointer: number--><!--Device-RandomAccessFile-readonly filePointer: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

