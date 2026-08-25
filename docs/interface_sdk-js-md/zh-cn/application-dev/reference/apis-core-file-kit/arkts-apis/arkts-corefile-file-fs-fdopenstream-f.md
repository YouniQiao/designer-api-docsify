# fdopenStream

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## fdopenStream

```TypeScript
declare function fdopenStream(fd: number, mode: string): Promise<Stream>
```

基于文件描述符打开文件流。使用Promise异步回调。需要配合[Stream](arkts-corefile-file-fs-stream-i.md)中的close()函数关闭文件流。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| mode | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Stream](arkts-corefile-file-fs-stream-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900010 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fdopenStream(file.fd, "r+").then((stream: fileIo.Stream) => {
  console.info(`Succeeded in opening stream.`);
  stream.closeSync();
}).catch((err: BusinessError) => {
  console.error(`Failed to open stream. Code: ${err.code}, message: ${err.message}`);
  // 文件流打开失败后，文件描述符需要手动关闭
  fileIo.closeSync(file);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fdopenStream(file.fd, "r+").then((stream:fileIo.Stream) => {
  console.info(`Succeeded in opening stream.`);
  stream.closeSync();
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to open stream. Code: ${err.code}, message: ${err.message}`);
  // 文件流打开失败后，文件描述符需要手动关闭
  fileIo.closeSync(file);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY);
fileIo.fdopenStream(file.fd, "r+", (err: BusinessError, stream: fileIo.Stream) => {
  if (err) {
    console.error(`Failed to fdopen stream. Code: ${err.code}, message: ${err.message}`);
    // 文件流打开失败后，文件描述符需要手动关闭
    fileIo.closeSync(file);
  } else {
    console.info(`Succeeded in fdopening stream.`);
    stream.closeSync();
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath,fileIo.OpenMode.READ_ONLY);
fileIo.fdopenStream(file.fd, "r+", (err: BusinessError<void> | null, stream:fileIo.Stream | undefined) => {
  if (err) {
    console.error(`Failed to fdopen stream. Code: ${err.code}, message: ${err.message}`);
    stream?.closeSync();
  } else {
    console.info(`Succeeded in fdopening stream.`);
    // 文件流打开失败后，文件描述符需要手动关闭
   fileIo.closeSync(file);
  }
});
```


## fdopenStream

```TypeScript
declare function fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void
```

基于文件描述符打开文件流，需要配合[Stream](arkts-corefile-file-fs-stream-i.md)中的close()函数关闭文件流。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| mode | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Stream](arkts-corefile-file-fs-stream-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900010 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |

**示例**

参见 [fdopenStream](#fdopenstream)
