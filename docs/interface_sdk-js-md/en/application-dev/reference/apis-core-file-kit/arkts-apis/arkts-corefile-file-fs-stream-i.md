# Stream

Provides API for stream operations. Before calling any API of **Stream**, you need to create a **Stream** instance by using fileIo.createStream or fileIo.fdopenStream.

**Since:** 9

<!--Device-unnamed-declare interface Stream--><!--Device-unnamed-declare interface Stream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## close

```TypeScript
close(): Promise<void>
```

Closes the file stream. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.close(file).then(() => {
  console.info("close file succeed");
}).catch((err: BusinessError) => {
  console.error("close file failed with error message: " + err.message + ", error code: " + err.code);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.close(file, (err: BusinessError) => {
  if (err) {
    console.error("close file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("close file succeed");
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.close().then(() => {
  console.info("close fileStream succeed");
}).catch((err: BusinessError) => {
  console.error("close fileStream  failed with error message: " + err.message + ", error code: " + err.code);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.close((err: BusinessError) => {
  if (err) {
    console.error("close stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("close stream succeed");
  }
});
```

```TypeScript
let filePath = pathDir + "/test.txt";
let randomAccessFile = fs.createRandomAccessFileSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
randomAccessFile.close();
```

```TypeScript
const filePath = pathDir + "/test.txt";
const rs = fs.createReadStream(filePath);
rs.close();
```

```TypeScript
const filePath = pathDir + "/test.txt";
const ws = fs.createWriteStream(filePath);
ws.close();
```

## close

```TypeScript
close(callback: AsyncCallback<void>): void
```

Closes the file stream. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Stream-close(callback: AsyncCallback<void>): void--><!--Device-Stream-close(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback invoked immediately after the stream is closed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

**Examples**

See [close](#close)

## closeSync

```TypeScript
closeSync(): void
```

Closes the file stream. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

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

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath);
fs.closeSync(file);
```

```TypeScript
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.closeSync();
```

## flush

```TypeScript
flush(): Promise<void>
```

Flushes the file stream. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Stream-flush(): Promise<void>--><!--Device-Stream-flush(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.flush().then(() => {
  console.info("flush succeed");
  stream.close();
}).catch((err: BusinessError) => {
  console.error("flush failed with error message: " + err.message + ", error code: " + err.code);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.flush((err: BusinessError) => {
  if (err) {
    console.error("flush stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("flush succeed");
    stream.close();
  }
});
```

## flush

```TypeScript
flush(callback: AsyncCallback<void>): void
```

Flushes the file stream. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Stream-flush(callback: AsyncCallback<void>): void--><!--Device-Stream-flush(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

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

**Examples**

See [flush](#flush)

## flushSync

```TypeScript
flushSync(): void
```

Flushes the file stream. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Stream-flushSync(): void--><!--Device-Stream-flushSync(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

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

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
stream.flushSync();
stream.close();
```

## read

```TypeScript
read(
      buffer: ArrayBuffer,
      options?: ReadOptions
  ): Promise<number>
```

Reads data from a stream file. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Stream-read(      buffer: ArrayBuffer,      options?: ReadOptions  ): Promise<number>--><!--Device-Stream-read(      buffer: ArrayBuffer,      options?: ReadOptions  ): Promise<number>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | No | The options are as follows:<br>- **length** (number): length of the data to read , in bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the data read, in bytes. |

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
read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void
```

Reads data from a stream file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Stream-read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void--><!--Device-Stream-read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the result. The callback returns the data read, in bytes. |

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
read(
      buffer: ArrayBuffer,
      options: ReadOptions,
      callback: AsyncCallback<number>
  ): void
```

Reads data from a stream file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Stream-read(      buffer: ArrayBuffer,      options: ReadOptions,      callback: AsyncCallback<number>  ): void--><!--Device-Stream-read(      buffer: ArrayBuffer,      options: ReadOptions,      callback: AsyncCallback<number>  ): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | Yes | The options are as follows:<br>- **length** (number): length of the data to read , in bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>**Since:** 11 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the result. The callback returns the data read, in bytes. |

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

## readSync

```TypeScript
readSync(
      buffer: ArrayBuffer,
      options?: ReadOptions
  ): number
```

Reads data from a stream file. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Stream-readSync(      buffer: ArrayBuffer,      options?: ReadOptions  ): number--><!--Device-Stream-readSync(      buffer: ArrayBuffer,      options?: ReadOptions  ): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | No | The options are as follows:<br>- **length** (number): length of the data to read , in bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position.<br><br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| number | Length of the data read, in bytes. |

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
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
let buf = new ArrayBuffer(4096);
fs.readSync(file.fd, buf);
fs.closeSync(file);
```

```TypeScript
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
let buf = new ArrayBuffer(4096);
let num = stream.readSync(buf, readOption);
stream.close();
```

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

## write

```TypeScript
write(
      buffer: ArrayBuffer | string,
      options?: WriteOptions
  ): Promise<number>
```

Writes data to a stream file. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Stream-write(      buffer: ArrayBuffer | string,      options?: WriteOptions  ): Promise<number>--><!--Device-Stream-write(      buffer: ArrayBuffer | string,      options?: WriteOptions  ): Promise<number>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | No | The options are as follows:<br>- **length** (number): length of the data to write, in bytes. The default value is the buffer length.<br>- **offset** (number): start position to write the data in the file, in bytes. This parameter is optional. By default, data is written from the current position.&lt; br&gt;- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the length of the data written, in bytes. |

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
let str: string = "hello, world";
fs.write(file.fd, str).then((writeLen: number) => {
  console.info("write data to file succeed and size is:" + writeLen);
}).catch((err: BusinessError) => {
  console.error("write data to file failed with error message: " + err.message + ", error code: " + err.code);
}).finally(() => {
  fs.closeSync(file);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
let str: string = "hello, world";
fs.write(file.fd, str, (err: BusinessError, writeLen: number) => {
  if (err) {
    console.error("write data to file failed with error message:" + err.message + ", error code: " + err.code);
  } else {
    console.info("write data to file succeed and size is:" + writeLen);
  }
  fs.closeSync(file);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
stream.write("hello, world", writeOption).then((number: number) => {
  console.info("write succeed and size is:" + number);
  stream.close();
}).catch((err: BusinessError) => {
  console.error("write failed with error message: " + err.message + ", error code: " + err.code);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath, "r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
stream.write("hello, world", writeOption, (err: BusinessError, bytesWritten: number) => {
  if (err) {
    console.error("write stream failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    if (bytesWritten) {
      console.info("write succeed and size is:" + bytesWritten);
    }
  }
  stream.close();
});
```

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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
let randomAccessFile = fs.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let writeOption: WriteOptions = {
  offset: 1,
  length: bufferLength,
  encoding: 'utf-8'
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, writeOption, (err: BusinessError, bytesWritten: number) => {
  if (err) {
    console.error("write failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    if (bytesWritten) {
      console.info("write succeed and size is:" + bytesWritten);
    }
  }
  randomAccessFile.close();
  fs.closeSync(file);
});
```

## write

```TypeScript
write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void
```

Writes data to a stream file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Stream-write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void--><!--Device-Stream-write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the result. The callback returns the length of the data written, in bytes. |

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

**Examples**

See [write](#write)

## write

```TypeScript
write(
      buffer: ArrayBuffer | string,
      options: WriteOptions,
      callback: AsyncCallback<number>
  ): void
```

Writes data to a stream file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Stream-write(      buffer: ArrayBuffer | string,      options: WriteOptions,      callback: AsyncCallback<number>  ): void--><!--Device-Stream-write(      buffer: ArrayBuffer | string,      options: WriteOptions,      callback: AsyncCallback<number>  ): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | Yes | The options are as follows:<br>- **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): start position to write the data in the file, in bytes. This parameter is optional. By default, data is written from the current position.<br>- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.<br>**Since:** 11 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the result. The callback returns the length of the data written, in bytes. |

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

**Examples**

See [write](#write)

## writeSync

```TypeScript
writeSync(
      buffer: ArrayBuffer | string,
      options?: WriteOptions
  ): number
```

Writes data to a stream file. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Stream-writeSync(      buffer: ArrayBuffer | string,      options?: WriteOptions  ): number--><!--Device-Stream-writeSync(      buffer: ArrayBuffer | string,      options?: WriteOptions  ): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | No | The options are as follows:<br>- **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): start position to write the data in the file, in bytes. This parameter is optional. By default, data is written from the current position.<br>- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| number | Length of the data written in the file, in bytes. |

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

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
let str: string = "hello, world";
let writeLen = fs.writeSync(file.fd, str);
console.info("write data to file succeed and size is:" + writeLen);
fs.closeSync(file);
```

```TypeScript
import { fileIo as fs, WriteOptions } from '@kit.CoreFileKit';
let filePath = pathDir + "/test.txt";
let stream = fs.createStreamSync(filePath,"r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
let num = stream.writeSync("hello, world", writeOption);
stream.close();
```

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

