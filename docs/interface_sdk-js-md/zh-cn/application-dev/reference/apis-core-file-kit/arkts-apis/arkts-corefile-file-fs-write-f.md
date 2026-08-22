# write

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## write

```TypeScript
declare function write(
  fd: number,
  buffer: ArrayBuffer | string,
  options?: WriteOptions
): Promise<number>
```

将数据写入文件，返回实际写入的字节数。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options?: WriteOptions): Promise<number>--><!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options?: WriteOptions): Promise<number>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符fd。 |
| buffer | ArrayBuffer \| string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | 否 | 支持如下选项：<br/>- offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写入。<br/>- length， number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。<br/>- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认'utf-8'。当前仅支持'utf-8'。<br>**起始版本：** 11 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象。返回实际写入的数据长度，单位为Byte。 |

**错误码：**

| 错误码ID | 错误信息 |
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

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let str: string = "hello, world";
fileIo.write(file.fd, str).then((writeLen: number) => {
  console.info(`Succeeded in writing data to file, size is: ${writeLen}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to write data to file. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  fileIo.closeSync(file);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath,fileIo.OpenMode.READ_WRITE |fileIo.OpenMode.CREATE);
let str: string = "hello, world";
fileIo.write(file.fd, str).then((writeLen: long) => {
  console.info(`Succeeded in writing data to file, size is: ${writeLen}`);
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to write data to file. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  fileIo.closeSync(file);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let str: string = "hello, world";
fileIo.write(file.fd, str, (err: BusinessError, writeLen: number) => {
  if (err) {
    console.error(`Failed to write data to file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in writing data to file, size is: ${writeLen}`);
  }
  fileIo.closeSync(file);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath,fileIo.OpenMode.READ_WRITE |fileIo.OpenMode.CREATE);
let str: string = "hello, world";
fileIo.write(file.fd, str, (err: BusinessError<void> | null, writeLen: long | undefined) => {
  if (err) {
    console.error(`Failed to write data to file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in writing data to file, size is: ${writeLen}`);
  }
  fileIo.closeSync(file);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let str: string = "hello, world";
let writeOptions: WriteOptions = {
    offset: 1,
    length: 5
};
fileIo.write(file.fd, str, writeOptions, (err: BusinessError, writeLen: number) => {
  if (err) {
    console.error(`Failed to write data to file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in writing data to file, size is: ${writeLen}`);
  }
  fileIo.closeSync(file);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath,fileIo.OpenMode.READ_WRITE |fileIo.OpenMode.CREATE);
let str: string = "hello, world";
let writeOptions: WriteOptions = {
    offset: 1,
    length: 5
};
fileIo.write(file.fd, str, writeOptions, (err: BusinessError<void> | null, writeLen: long | undefined) => {
  if (err) {
    console.error(`Failed to write data to file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in writing data to file, size is: ${writeLen}`);
  }
  fileIo.closeSync(file);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
stream.write("hello, world", writeOption).then((number: number) => {
  console.info(`Succeeded in writing, size is: ${number}`);
  stream.close();
}).catch((err: BusinessError) => {
  console.error(`Failed to write. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
stream.write("hello, world", writeOption).then((number: long) => {
  console.info(`Succeeded in writing, size is: ${number}`);
  stream.close();
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to write. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");

stream.write("hello, world", (err: BusinessError, bytesWritten: number) => {
  if (err) {
    console.error(`Failed to write stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (bytesWritten) {
      console.info(`Succeeded in writing, size is: ${bytesWritten}`);
    }
  }
  stream.close();
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");

stream.write("hello, world", (err: BusinessError<void> | null, bytesWritten: long | undefined) => {
  if (err) {
    console.error(`Failed to write stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (bytesWritten) {
      console.info(`Succeeded in writing, size is: ${bytesWritten}`);
      stream.close();
    }
  }
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
stream.write("hello, world", writeOption, (err: BusinessError, bytesWritten: number) => {
  if (err) {
    console.error(`Failed to write stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (bytesWritten) {
      console.info(`Succeeded in writing, size is: ${bytesWritten}`);
    }
  }
  stream.close();
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
stream.write("hello, world", writeOption, (err: BusinessError<void> | null, bytesWritten: long | undefined) => {
  if (err) {
    console.error(`Failed to write stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (bytesWritten) {
      console.info(`Succeeded in writing, size is: ${bytesWritten}`);
      stream.close();
    }
  }
});
```

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);

let buffer = new ArrayBuffer(11);
let bytesWritten = mapping.write(buffer);
console.info(`Succeeded in writing data to file, size is: ${bytesWritten}`);

mapping.msyncSync();
mapping.unmapSync();
fileIo.closeSync(file);
```

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);

let buffer = new ArrayBuffer(11);
let bytesWritten = mapping.write(50, buffer);
console.info(`Succeeded in writing data to file, size is: ${bytesWritten}`);

mapping.msyncSync();
mapping.unmapSync();
fileIo.closeSync(file);
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let writeOption: WriteOptions = {
  offset: 1,
  length: 5,
  encoding: 'utf-8'
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, writeOption).then((bytesWritten: number) => {
  console.info(`Succeeded in writing, bytes written: ${bytesWritten}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to write. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath,fileIo.OpenMode.CREATE |fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let writeOption: WriteOptions = {
  offset: 1,
  length: 5,
  encoding: 'utf-8'
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, writeOption).then((bytesWritten: long) => {
  console.info(`Succeeded in writing, bytes written: ${bytesWritten}`);
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to write. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, (err: BusinessError, bytesWritten: number) => {
  if (err) {
    console.error(`Failed to write. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (bytesWritten) {
      console.info(`Succeeded in writing, size is: ${bytesWritten}`);
    }
  }
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let bufferLength: long = 4096;
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, (err: BusinessError | null, bytesWritten: long | undefined) => {
  if (err) {
    console.error(`Failed to write. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (bytesWritten) {
      console.info(`Succeeded in writing, size is: ${bytesWritten}`);
    }
  }
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let writeOption: WriteOptions = {
  offset: 1,
  length: bufferLength,
  encoding: 'utf-8'
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, writeOption, (err: BusinessError, bytesWritten: number) => {
  if (err) {
    console.error(`Failed to write. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (bytesWritten) {
      console.info(`Succeeded in writing, size is: ${bytesWritten}`);
    }
  }
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath,fileIo.OpenMode.CREATE |fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let bufferLength: long = 4096;
let writeOption: WriteOptions = {
  offset: 1,
  length: bufferLength,
  encoding: 'utf-8'
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, writeOption, (err: BusinessError | null, bytesWritten: long | undefined) => {
  if (err) {
    console.error(`Failed to write. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (bytesWritten) {
      console.info(`Succeeded in writing, size is: ${bytesWritten}`);
    }
  }
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```


## write

```TypeScript
declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void
```

将数据写入文件，返回实际写入的字节数。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符fd。 |
| buffer | ArrayBuffer \| string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 | 回调函数，返回实际写入的数据长度，单位为Byte。 |

**错误码：**

| 错误码ID | 错误信息 |
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

**示例**

参见 [write](#write)


## write

```TypeScript
declare function write(
  fd: number,
  buffer: ArrayBuffer | string,
  options: WriteOptions,
  callback: AsyncCallback<number>
): void
```

将数据写入文件，支持配置写入选项（如偏移位置和写入长度），返回实际写入的字节数。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options: WriteOptions,  callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options: WriteOptions,  callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符fd。 |
| buffer | ArrayBuffer \| string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | 是 | 支持如下选项：<br/>- offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。<br/>- length， number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。<br/>- encoding，string类型，当数据是string类型时有效，表示数据的编码方式， 默认'utf-8'。当前仅支持'utf-8'。<br>**起始版本：** 11 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 | 回调函数，返回实际写入的数据长度，单位为Byte。 |

**错误码：**

| 错误码ID | 错误信息 |
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

**示例**

参见 [write](#write)

