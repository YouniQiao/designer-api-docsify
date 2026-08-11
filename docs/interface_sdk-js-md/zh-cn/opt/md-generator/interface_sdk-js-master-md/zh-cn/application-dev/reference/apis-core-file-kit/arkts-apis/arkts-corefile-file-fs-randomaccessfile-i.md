# RandomAccessFile

随机读写文件流。在调用RandomAccessFile的方法前，需要先通过createRandomAccessFile()方法（同步或异步）来构建一个RandomAccessFile实例。

**起始版本：** 10

<!--Device-unnamed-declare interface RandomAccessFile--><!--Device-unnamed-declare interface RandomAccessFile-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

## close

```TypeScript
close(): void
```

以同步方式关闭RandomAccessFile对象。

**起始版本：** 10

<!--Device-RandomAccessFile-close(): void--><!--Device-RandomAccessFile-close(): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |

## 示例

```TypeScript
let filePath = pathDir + "/test.txt";
let randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
randomAccessFile.close();
```

## getReadStream

```TypeScript
getReadStream(): ReadStream
```

获取当前 RandomAccessFile 的一个 ReadStream 实例。

**起始版本：** 12

<!--Device-RandomAccessFile-getReadStream(): ReadStream--><!--Device-RandomAccessFile-getReadStream(): ReadStream-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| [ReadStream](arkts-corefile-file-fs-readstream-c.md) |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| 13900012 |
| 13900008 |
| 13900042 |
| 13900011 |

## 示例

```TypeScript
const filePath = pathDir + "/test.txt";
const randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
const rs = randomAccessFile.getReadStream();
rs.close();
randomAccessFile.close();
```

## getWriteStream

```TypeScript
getWriteStream(): WriteStream
```

获取当前 RandomAccessFile 的一个 WriteStream 实例。

**起始版本：** 12

<!--Device-RandomAccessFile-getWriteStream(): WriteStream--><!--Device-RandomAccessFile-getWriteStream(): WriteStream-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| [WriteStream](arkts-corefile-file-fs-writestream-c.md) |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| 13900012 |
| 13900008 |
| 13900042 |
| 13900011 |

## 示例

```TypeScript
const filePath = pathDir + "/test.txt";
const randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
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

从文件读取数据，使用promise异步回调。

**起始版本：** 10

<!--Device-RandomAccessFile-read(    buffer: ArrayBuffer,    options?: ReadOptions  ): Promise<number>--><!--Device-RandomAccessFile-read(    buffer: ArrayBuffer,    options?: ReadOptions  ): Promise<number>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900020 |
| 13900005 |
| 13900034 |
| 13900019 |
| 13900044 |
| 13900013 |
| 13900008 |
| 13900010 |
| 13900042 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { ReadOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let readOption: ReadOptions = {
  offset: 1,
  length: 5
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.read(arrayBuffer, readOption).then((readLength: number) => {
  console.info(`Succeeded in reading, read length: ${readLength}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```

## read

```TypeScript
read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void
```

从文件读取数据，使用callback异步回调。

**起始版本：** 10

<!--Device-RandomAccessFile-read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void--><!--Device-RandomAccessFile-read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900020 |
| 13900005 |
| 13900034 |
| 13900019 |
| 13900013 |
| 13900008 |
| 13900010 |
| 13900042 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let length: number = 20;

let arrayBuffer = new ArrayBuffer(length);
randomAccessFile.read(arrayBuffer, (err: BusinessError, readLength: number) => {
  if (err) {
    console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (readLength) {
      console.info(`Succeeded in reading, size is: ${readLength}`);
    }
  }
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```

## read

```TypeScript
read(
    buffer: ArrayBuffer,
    options: ReadOptions,
    callback: AsyncCallback<number>
  ): void
```

从文件读取数据，使用callback异步回调。

**起始版本：** 10

<!--Device-RandomAccessFile-read(    buffer: ArrayBuffer,    options: ReadOptions,    callback: AsyncCallback<number>  ): void--><!--Device-RandomAccessFile-read(    buffer: ArrayBuffer,    options: ReadOptions,    callback: AsyncCallback<number>  ): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900020 |
| 13900005 |
| 13900034 |
| 13900019 |
| 13900013 |
| 13900008 |
| 13900010 |
| 13900042 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { ReadOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let length: number = 20;
let readOption: ReadOptions = {
  offset: 1,
  length: 5
};
let arrayBuffer = new ArrayBuffer(length);
randomAccessFile.read(arrayBuffer, readOption, (err: BusinessError, readLength: number) => {
  if (err) {
    console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (readLength) {
      console.info(`Succeeded in reading, size is: ${readLength}`);
    }
  }
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```

## readSync

```TypeScript
readSync(
    buffer: ArrayBuffer,
    options?: ReadOptions
  ): number
```

以同步方法从文件读取数据。

**起始版本：** 10

<!--Device-RandomAccessFile-readSync(    buffer: ArrayBuffer,    options?: ReadOptions  ): number--><!--Device-RandomAccessFile-readSync(    buffer: ArrayBuffer,    options?: ReadOptions  ): number-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900020 |
| 13900005 |
| 13900034 |
| 13900019 |
| 13900044 |
| 13900013 |
| 13900008 |
| 13900010 |
| 13900042 |

## 示例

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let length: number = 4096;
let arrayBuffer = new ArrayBuffer(length);
let readLength = randomAccessFile.readSync(arrayBuffer);
randomAccessFile.close();
fileIo.closeSync(file);
```

## setFilePointer

```TypeScript
setFilePointer(filePointer: number): void
```

设置文件偏移指针。

**起始版本：** 10

<!--Device-RandomAccessFile-setFilePointer(filePointer: number): void--><!--Device-RandomAccessFile-setFilePointer(filePointer: number): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [filePointer](#filepointer) | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900020 |
| 13900005 |
| 13900008 |
| 13900042 |

## 示例

```TypeScript
let filePath = pathDir + "/test.txt";
let randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
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

将数据写入文件，使用promise异步回调。

**起始版本：** 10

<!--Device-RandomAccessFile-write(    buffer: ArrayBuffer | string,    options?: WriteOptions  ): Promise<number>--><!--Device-RandomAccessFile-write(    buffer: ArrayBuffer | string,    options?: WriteOptions  ): Promise<number>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900020 |
| 13900005 |
| 13900001 |
| 13900034 |
| 13900013 |
| 13900008 |
| 13900024 |
| 13900025 |
| 13900041 |
| 13900010 |
| 13900042 |

## 示例

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

## write

```TypeScript
write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void
```

将数据写入文件，使用callback异步回调。

**起始版本：** 10

<!--Device-RandomAccessFile-write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void--><!--Device-RandomAccessFile-write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900020 |
| 13900005 |
| 13900001 |
| 13900034 |
| 13900013 |
| 13900008 |
| 13900024 |
| 13900025 |
| 13900041 |
| 13900010 |
| 13900042 |

## 示例

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

## write

```TypeScript
write(
    buffer: ArrayBuffer | string,
    options: WriteOptions,
    callback: AsyncCallback<number>
  ): void
```

将数据写入文件，使用callback异步回调。

**起始版本：** 10

<!--Device-RandomAccessFile-write(    buffer: ArrayBuffer | string,    options: WriteOptions,    callback: AsyncCallback<number>  ): void--><!--Device-RandomAccessFile-write(    buffer: ArrayBuffer | string,    options: WriteOptions,    callback: AsyncCallback<number>  ): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900020 |
| 13900005 |
| 13900001 |
| 13900034 |
| 13900013 |
| 13900008 |
| 13900024 |
| 13900025 |
| 13900041 |
| 13900010 |
| 13900042 |

## 示例

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

## writeSync

```TypeScript
writeSync(
    buffer: ArrayBuffer | string,
    options?: WriteOptions
  ): number
```

以同步方法将数据写入文件。

**起始版本：** 10

<!--Device-RandomAccessFile-writeSync(    buffer: ArrayBuffer | string,    options?: WriteOptions  ): number--><!--Device-RandomAccessFile-writeSync(    buffer: ArrayBuffer | string,    options?: WriteOptions  ): number-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900020 |
| 13900005 |
| 13900001 |
| 13900034 |
| 13900013 |
| 13900008 |
| 13900024 |
| 13900025 |
| 13900041 |
| 13900010 |
| 13900042 |

## 示例

```TypeScript
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
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

打开的文件描述符。

**类型：** number

**起始版本：** 10

<!--Device-RandomAccessFile-readonly fd: number--><!--Device-RandomAccessFile-readonly fd: number-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

## filePointer

```TypeScript
readonly filePointer: number
```

RandomAccessFile对象的偏移指针，单位为Byte。

**类型：** number

**起始版本：** 10

<!--Device-RandomAccessFile-readonly filePointer: number--><!--Device-RandomAccessFile-readonly filePointer: number-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO
