# read

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## read

```TypeScript
declare function read(
  fd: number,
  buffer: ArrayBuffer,
  options?: ReadOptions
): Promise<number>
```

Reads file data. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options?: ReadOptions): Promise<number>--><!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options?: ReadOptions): Promise<number>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | FD of the file. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | No | The options are as follows:<br>- **offset** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>- **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the buffer length.<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the length of the data read, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900013 | Bad address |
| 13900019 | Is a directory |
| 13900020 | Invalid argument |
| 13900034 | Operation would block |
| 13900042 | Unknown error |
| 13900044 | Network is unreachable<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
let arrayBuffer = new ArrayBuffer(4096);
fs.read(file.fd, arrayBuffer).then((readLen: number) => {
  console.info("read file data succeed");
  let buf = buffer.from(arrayBuffer, 0, readLen);
  console.info(`The content of file: ${buf.toString()}`);
}).catch((err: BusinessError) => {
  console.error("read file data failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fs.closeSync(file);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
let arrayBuffer = new ArrayBuffer(4096);
fs.read(file.fd, arrayBuffer, (err: BusinessError, readLen: number) => {
  if (err) {
    console.error("read failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("read file data succeed");
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info(`The content of file: ${buf.toString()}`);
  }
  fs.closeSync(file);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
stream.read(arrayBuffer, readOption).then((readLen: number) => {
  console.info("read data succeed");
  let buf = buffer.from(arrayBuffer, 0, readLen);
  console.info(`The content of file: ${buf.toString()}`);
  stream.close();
}).catch((err: BusinessError) => {
  console.error("read data failed with error message: " + err.message + ", error code: " + err.code);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
stream.read(arrayBuffer, readOption, (err: BusinessError, readLen: number) => {
  if (err) {
    console.error("read stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("read data succeed");
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info(`The content of file: ${buf.toString()}`);
    stream.close();
  }
});
```

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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
let length: number = 20;
let readOption: ReadOptions = {
  offset: 1,
  length: 5
};
let arrayBuffer = new ArrayBuffer(length);
randomAccessFile.read(arrayBuffer, readOption, (err: BusinessError, readLength: number) => {
  if (err) {
    console.error("read failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    if (readLength) {
      console.info("read succeed and size is:" + readLength);
    }
  }
  randomAccessFile.close();
  fs.closeSync(file);
});
```


## read

```TypeScript
declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<number>): void
```

Reads data from a file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | FD of the file. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the length of the data read, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900013 | Bad address |
| 13900019 | Is a directory |
| 13900020 | Invalid argument |
| 13900034 | Operation would block |
| 13900042 | Unknown error |

**Examples**

See [read](#read)


## read

```TypeScript
declare function read(
  fd: number,
  buffer: ArrayBuffer,
  options: ReadOptions,
  callback: AsyncCallback<number>
): void
```

Reads data from a file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options: ReadOptions,  callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options: ReadOptions,  callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | FD of the file. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | Yes | The options are as follows:<br>- **offset** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>- **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the buffer length.<br>**Since:** 11 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the length of the data read, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900013 | Bad address |
| 13900019 | Is a directory |
| 13900020 | Invalid argument |
| 13900034 | Operation would block |
| 13900042 | Unknown error |

**Examples**

See [read](#read)

