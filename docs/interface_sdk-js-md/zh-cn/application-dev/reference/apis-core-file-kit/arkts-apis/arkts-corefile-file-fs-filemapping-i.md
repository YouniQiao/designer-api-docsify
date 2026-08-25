# FileMapping

文件映射对象，在调用FileMapping的方法前，需要先通过[mmap()](arkts-corefile-file-fs-mmap-f.md)或方法[mmapSync()](arkts-corefile-file-fs-mmapsync-f.md)构建一个FileMapping实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## capacity

```TypeScript
capacity(): number
```

获取文件映射区的容量。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

**示例**

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);
let cap = mapping.capacity();
console.info(`Succeeded in getting capacity, the capacity is: ${cap}`);
mapping.unmapSync();
fileIo.closeSync(file);
```

## flip

```TypeScript
flip(): void
```

翻转文件映射区，将写入准备状态切换为读取准备状态。调用后，limit被设置为当前position的值，position被重置为0。推荐在一系列[write()](#write)操作完成后，调用此方法准备后续的[read()](#read)操作。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

**示例**

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);

let writeData = new ArrayBuffer(50);
mapping.write(writeData);
mapping.flip(); // limit=50, position=0
console.info("Succeeded in flip.");

let readBuffer = new ArrayBuffer(50);
mapping.read(readBuffer);

mapping.unmapSync();
fileIo.closeSync(file);
```

## getLimit

```TypeScript
getLimit(): number
```

获取文件映射区可读写区域的上界。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

**示例**

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);
let lim = mapping.getLimit();
console.info(`Succeeded in getting limit, the limit is: ${lim}`);
mapping.unmapSync();
fileIo.closeSync(file);
```

## getPosition

```TypeScript
getPosition(): number
```

获取文件映射区的当前位置。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

**示例**

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);
let pos = mapping.getPosition();
console.info(`Succeeded in getting position, the position is: ${pos}`);
mapping.unmapSync();
fileIo.closeSync(file);
```

## msync

```TypeScript
msync(): Promise<void>
```

将整个文件映射区的数据同步到磁盘文件。使用Promise异步回调。 注意：如果文件不在本地设备上，调用此接口不保证所有更改都已持久化存储。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900011 |
| 13900014 |
| 13900020 |
| 13900050 |
| 13900052 |
| 13900055 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);

let buffer = new ArrayBuffer(11);
mapping.write(buffer);

mapping.msync().then(() => {
  console.info("Succeeded in msync.");
}).catch((err: BusinessError) => {
  console.error(`Failed to msync. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  mapping.unmapSync();
  fileIo.closeSync(file);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);

let buffer = new ArrayBuffer(11);
mapping.write(buffer);

mapping.msync().then(() => {
  console.info("Succeeded in msync.");
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to msync. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  mapping.unmapSync();
  fileIo.closeSync(file);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);

let buffer = new ArrayBuffer(11);
mapping.write(50, buffer);

mapping.msync(50, buffer.byteLength).then(() => {
  console.info("Succeeded in msync.");
}).catch((err: BusinessError) => {
  console.error(`Failed to msync. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  mapping.unmapSync();
  fileIo.closeSync(file);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);

let buffer = new ArrayBuffer(11);
mapping.write(50, buffer);

mapping.msync(50, buffer.byteLength).then(() => {
  console.info("Succeeded in msync.");
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to msync. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  mapping.unmapSync();
  fileIo.closeSync(file);
});
```

## msync

```TypeScript
msync(position: number, length: number): Promise<void>
```

将文件映射区指定范围内的数据同步到磁盘文件。使用Promise异步回调。 注意：如果文件不在本地设备上，调用此接口不保证所有更改都已持久化存储。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | number | 是 |
| length | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900011 |
| 13900014 |
| 13900020 |
| 13900050 |
| 13900052 |
| 13900055 |

**示例**

参见 [msync](#msync)

## msyncSync

```TypeScript
msyncSync(): void
```

以同步方法将整个文件映射区的数据同步到磁盘文件。 注意：如果文件不在本地设备上，调用此接口不保证所有更改都已持久化存储。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**错误码：**

| 错误码ID |
| --- |
| 13900011 |
| 13900014 |
| 13900020 |
| 13900050 |
| 13900052 |
| 13900055 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);

let buffer = new ArrayBuffer(11);
mapping.write(buffer);

mapping.msyncSync();
console.info("Succeeded in msync.");

mapping.unmapSync();
fileIo.closeSync(file);
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);

let buffer = new ArrayBuffer(11);
mapping.write(50, buffer);

mapping.msyncSync(50, buffer.byteLength);
console.info("Succeeded in msync.");

mapping.unmapSync();
fileIo.closeSync(file);
```

## msyncSync

```TypeScript
msyncSync(position: number, length: number): void
```

以同步方法将文件映射区指定范围内的数据同步到磁盘文件。 注意：如果文件不在本地设备上，调用此接口不保证所有更改都已持久化存储。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | number | 是 |
| length | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900011 |
| 13900014 |
| 13900020 |
| 13900050 |
| 13900052 |
| 13900055 |

**示例**

参见 [msyncSync](#msyncsync)

## read

```TypeScript
read(buffer: ArrayBuffer, length?: number): number
```

从当前位置读取数据，并将位置后移实际读取的字节数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| length | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900051 |
| 13900052 |
| 13900054 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
let arrayBuffer = new ArrayBuffer(4096);
fileIo.read(file.fd, arrayBuffer).then((readLen: number) => {
  let buf = buffer.from(arrayBuffer, 0, readLen);
  console.info(`Succeeded in reading file data. The content of file: ${buf.toString()}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to read file data. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  fileIo.closeSync(file);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath,fileIo.OpenMode.READ_WRITE);
let arrayBuffer = new ArrayBuffer(4096);
fileIo.read(file.fd, arrayBuffer).then((readLen: long) => {
  console.info(`Succeeded in reading file data. The content of file: ${buf.toString()}`);
  let buf = buffer.from(arrayBuffer, 0, readLen.toInt());
  console.info(`The content of file: ${buf.toString()}`);
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to read file data. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  fileIo.closeSync(file);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
let arrayBuffer = new ArrayBuffer(4096);
fileIo.read(file.fd, arrayBuffer, (err: BusinessError, readLen: number) => {
  if (err) {
    console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
  } else {
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info(`Succeeded in reading file data. The content of file: ${buf.toString()}`);
  }
  fileIo.closeSync(file);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath,fileIo.OpenMode.READ_WRITE);
let arrayBuffer = new ArrayBuffer(4096);
fileIo.read(file.fd, arrayBuffer, (err: BusinessError<void> | null, readLen: long | undefined) => {
  if (err) {
    console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
  } else {
    let buf = buffer.from(arrayBuffer, 0, readLen?.toInt());
    console.info(`Succeeded in reading file data. The content of file: ${buf.toString()}`);
  }
  fileIo.closeSync(file);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
  import { buffer } from '@kit.ArkTS';
  import { ReadOptions } from '@kit.CoreFileKit';

  let filePath = pathDir + "/test.txt";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  let arrayBuffer = new ArrayBuffer(4096);
  let readOption: ReadOptions = {
    offset: 1,
    length: 5
  };
  fileIo.read(file.fd, arrayBuffer, readOption, (err: BusinessError, readLen: number) => {
    if (err) {
      console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
    } else {
      let buf = buffer.from(arrayBuffer, 0, readLen);
      console.info(`Succeeded in reading file data. The content of file: ${buf.toString()}`);
    }
    fileIo.closeSync(file);
  });
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
import { ReadOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath,fileIo.OpenMode.READ_WRITE);
let arrayBuffer = new ArrayBuffer(4096);
let readOption: ReadOptions = {
  offset: 1,
  length: 5
};
fileIo.read(file.fd, arrayBuffer, readOption, (err: BusinessError<void> | null, readLen: long | undefined) => {
  if (err) {
    console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
  } else {
    let buf = buffer.from(arrayBuffer, 0, readLen?.toInt());
    console.info(`Succeeded in reading file data. The content of file: ${buf.toString()}`);
  }
  fileIo.closeSync(file);
});
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

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
stream.read(arrayBuffer, readOption).then((readLen: long) => {
  console.info('Succeeded in reading data');
  let buf = buffer.from(arrayBuffer, 0, readLen.toInt());
  console.info(`The content of file: ${buf.toString()}`);
  stream.close();
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to read data. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);

stream.read(arrayBuffer, (err: BusinessError<void> | null, readLen: long | undefined) => {
  if (err) {
    console.error(`Failed to read stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in reading data');
    let buf = buffer.from(arrayBuffer, 0, readLen?.toInt());
    console.info(`The content of file: ${buf.toString()}`);
    stream.close();
  }
});
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

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
stream.read(arrayBuffer, readOption, (err: BusinessError<void> | null, readLen: long | undefined) => {
  if (err) {
    console.error(`Failed to read stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in reading data');
    let buf = buffer.from(arrayBuffer, 0, readLen?.toInt());
    console.info(`The content of file: ${buf.toString()}`);
    stream.close();
  }
});
```

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);

let buffer = new ArrayBuffer(100);
let bytesRead = mapping.read(buffer);
console.info(`Succeeded in reading data, size is: ${bytesRead}`);

mapping.unmapSync();
fileIo.closeSync(file);
```

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);

let buffer = new ArrayBuffer(100);
let bytesRead = mapping.read(50, buffer, 50);
console.info(`Succeeded in reading data, size is: ${bytesRead}`);

mapping.unmapSync();
fileIo.closeSync(file);
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { ReadOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath,fileIo.OpenMode.CREATE |fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let bufferLength: long = 4096;
let readOption: ReadOptions = {
  offset: 1,
  length: 5
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.read(arrayBuffer, readOption).then((readLength: long) => {
  console.info(`Succeeded in reading, read length: ${readLength}`);
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let length: long = 20;

let arrayBuffer = new ArrayBuffer(length);
randomAccessFile.read(arrayBuffer, (err: BusinessError | null, readLength: long | undefined) => {
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

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { ReadOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath,fileIo.OpenMode.CREATE |fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let length: long = 20;
let readOption: ReadOptions = {
  offset: 1,
  length: 5
};
let arrayBuffer = new ArrayBuffer(length);
randomAccessFile.read(arrayBuffer, readOption, (err: BusinessError | null, readLength: long | undefined) => {
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
read(position: number, buffer: ArrayBuffer, length?: number): number
```

从指定位置读取数据，当前位置不会发生移动。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | number | 是 |
| buffer | ArrayBuffer | 是 |
| length | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900051 |
| 13900052 |
| 13900054 |

**示例**

参见 [read](#read)

## remaining

```TypeScript
remaining(): number
```

获取从当前位置（position）到可读写区域的上界（limit）之间的剩余字节数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

**示例**

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);

mapping.setPosition(100);
let remaining = mapping.remaining();
console.info(`Succeeded in getting remaining, the remaining is: ${remaining}`);

mapping.unmapSync();
fileIo.closeSync(file);
```

## setLimit

```TypeScript
setLimit(limit: number): void
```

设置文件映射区可读写区域的上界。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| limit | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

**示例**

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);
mapping.setLimit(512);
console.info("Succeeded in setLimit.");
mapping.unmapSync();
fileIo.closeSync(file);
```

## setPosition

```TypeScript
setPosition(position: number): void
```

设置文件映射区的当前位置。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900052 |

**示例**

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);
mapping.setPosition(100);
console.info("Succeeded in setPosition.");
mapping.unmapSync();
fileIo.closeSync(file);
```

## unmap

```TypeScript
unmap(): Promise<void>
```

释放文件映射区。使用Promise异步回调。调用后，position、limit和capacity均被重置为0，FileMapping对象不可再进行任何操作。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);

let buffer = new ArrayBuffer(11);
mapping.write(buffer);
mapping.unmap().then(() => {
  console.info("Succeeded in unmap.");
}).catch((err: BusinessError) => {
  console.error(`Failed to unmap. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  fileIo.closeSync(file);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);

let buffer = new ArrayBuffer(11);
mapping.write(buffer);
mapping.unmap().then(() => {
  console.info("Succeeded in unmap.");
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to unmap. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  fileIo.closeSync(file);
});
```

## unmapSync

```TypeScript
unmapSync(): void
```

以同步方法释放文件映射区。调用后，position、limit和capacity均被重置为0，FileMapping对象不可再进行任何操作。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let mapping = fileIo.mmapSync(file, fileIo.MappingMode.READ_WRITE, 0, 1024);

mapping.unmapSync();
console.info("Succeeded in unmap.");
fileIo.closeSync(file);
```

## write

```TypeScript
write(data: ArrayBuffer, length?: number): number
```

从当前位置写入数据，并将位置后移实际写入的字节数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | ArrayBuffer | 是 |
| length | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900051 |
| 13900052 |
| 13900053 |
| 13900054 |

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
write(position: number, data: ArrayBuffer, length?: number): number
```

从指定位置写入数据，当前位置不会发生移动。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | number | 是 |
| data | ArrayBuffer | 是 |
| length | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900050 |
| 13900051 |
| 13900052 |
| 13900053 |
| 13900054 |

**示例**

参见 [write](#write)
