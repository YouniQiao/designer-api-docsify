# Stream

文件流，在调用Stream的方法前，需要先通过 fileIo.createStream方法或者 fileIo.fdopenStream（同步或异步）来构建一个Stream 实例。

**起始版本：** 9

<!--Device-unnamed-declare interface Stream--><!--Device-unnamed-declare interface Stream-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
```

## close

```TypeScript
close(): Promise<void>
```

关闭文件流，使用promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Stream-close(): Promise<void>--><!--Device-Stream-close(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.close().then(() => {
  console.info(`Succeeded in closing file stream.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to close file stream. Code: ${err.code}, message: ${err.message}`);
});
```

## close

```TypeScript
close(callback: AsyncCallback<void>): void
```

异步关闭文件流，使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Stream-close(callback: AsyncCallback<void>): void--><!--Device-Stream-close(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.close((err: BusinessError) => {
  if (err) {
    console.error(`Failed to close stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in closing stream.`);
  }
});
```

## closeSync

```TypeScript
closeSync(): void
```

同步关闭文件流。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Stream-closeSync(): void--><!--Device-Stream-closeSync(): void-End-->

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

**示例**

```TypeScript
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.closeSync();
```

## flush

```TypeScript
flush(): Promise<void>
```

刷新文件流，使用promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Stream-flush(): Promise<void>--><!--Device-Stream-flush(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.flush().then(() => {
  console.info(`Succeeded in flushing.`);
  stream.close();
}).catch((err: BusinessError) => {
  console.error(`Failed to flush. Code: ${err.code}, message: ${err.message}`);
});
```

## flush

```TypeScript
flush(callback: AsyncCallback<void>): void
```

异步刷新文件流，使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Stream-flush(callback: AsyncCallback<void>): void--><!--Device-Stream-flush(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.flush((err: BusinessError) => {
  if (err) {
    console.error(`Failed to flush stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in flushing.`);
    stream.close();
  }
});
```

## flushSync

```TypeScript
flushSync(): void
```

同步刷新文件流。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Stream-flushSync(): void--><!--Device-Stream-flushSync(): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

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

**示例**

```TypeScript
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
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

从流文件读取数据，使用promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Stream-read(      buffer: ArrayBuffer,      options?: ReadOptions  ): Promise<number>--><!--Device-Stream-read(      buffer: ArrayBuffer,      options?: ReadOptions  ): Promise<number>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
import { ReadOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
stream.read(arrayBuffer, readOption).then((readLen: number) => {
  let buf = buffer.from(arrayBuffer, 0, readLen);
  console.info(`Succeeded in reading data, the content of file is: ${buf.toString()}`);
  stream.close();
}).catch((err: BusinessError) => {
  console.error(`Failed to read data. Code: ${err.code}, message: ${err.message}`);
});
```

## read

```TypeScript
read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void
```

从流文件读取数据，使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Stream-read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void--><!--Device-Stream-read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void-End-->

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
stream.read(arrayBuffer, (err: BusinessError, readLen: number) => {
  if (err) {
    console.error(`Failed to read stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info(`Succeeded in reading data, the content of file is: ${buf.toString()}`);
    stream.close();
  }
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

从流文件读取数据，使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Stream-read(      buffer: ArrayBuffer,      options: ReadOptions,      callback: AsyncCallback<number>  ): void--><!--Device-Stream-read(      buffer: ArrayBuffer,      options: ReadOptions,      callback: AsyncCallback<number>  ): void-End-->

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
import { ReadOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
stream.read(arrayBuffer, readOption, (err: BusinessError, readLen: number) => {
  if (err) {
    console.error(`Failed to read stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info(`Succeeded in reading data, the content of file is: ${buf.toString()}`);
    stream.close();
  }
});
```

## readSync

```TypeScript
readSync(
      buffer: ArrayBuffer,
      options?: ReadOptions
  ): number
```

以同步方法从流文件读取数据。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Stream-readSync(      buffer: ArrayBuffer,      options?: ReadOptions  ): number--><!--Device-Stream-readSync(      buffer: ArrayBuffer,      options?: ReadOptions  ): number-End-->

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

**示例**

```TypeScript
import { ReadOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
let buf = new ArrayBuffer(4096);
let num = stream.readSync(buf, readOption);
stream.close();
```

## write

```TypeScript
write(
      buffer: ArrayBuffer | string,
      options?: WriteOptions
  ): Promise<number>
```

将数据写入流文件，使用promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Stream-write(      buffer: ArrayBuffer | string,      options?: WriteOptions  ): Promise<number>--><!--Device-Stream-write(      buffer: ArrayBuffer | string,      options?: WriteOptions  ): Promise<number>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

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

**示例**

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

## write

```TypeScript
write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void
```

将数据写入流文件，使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Stream-write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void--><!--Device-Stream-write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void-End-->

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

**示例**

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

## write

```TypeScript
write(
      buffer: ArrayBuffer | string,
      options: WriteOptions,
      callback: AsyncCallback<number>
  ): void
```

将数据写入流文件，使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Stream-write(      buffer: ArrayBuffer | string,      options: WriteOptions,      callback: AsyncCallback<number>  ): void--><!--Device-Stream-write(      buffer: ArrayBuffer | string,      options: WriteOptions,      callback: AsyncCallback<number>  ): void-End-->

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

**示例**

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

## writeSync

```TypeScript
writeSync(
      buffer: ArrayBuffer | string,
      options?: WriteOptions
  ): number
```

以同步方法将数据写入流文件。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Stream-writeSync(      buffer: ArrayBuffer | string,      options?: WriteOptions  ): number--><!--Device-Stream-writeSync(      buffer: ArrayBuffer | string,      options?: WriteOptions  ): number-End-->

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

**示例**

```TypeScript
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath,"r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
let num = stream.writeSync("hello, world", writeOption);
stream.close();
```
