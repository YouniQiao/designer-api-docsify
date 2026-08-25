# open

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## open

```TypeScript
declare function open(path: string, mode?: number): Promise<File>
```

打开文件或目录，支持使用URI打开文件。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[File](arkts-corefile-file-fs-file-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
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
| 13900044 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.open(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE).then((file: fileIo.File) => {
  console.info(`Succeeded in getting file fd: ${file.fd}`);
  fileIo.closeSync(file);
}).catch((err: BusinessError) => {
  console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.open(filePath,fileIo.OpenMode.READ_WRITE |fileIo.OpenMode.CREATE).then((file:fileIo.File) => {
  console.info(`Succeeded in getting file fd: ${file.fd}`);
 fileIo.closeSync(file);
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.open(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE, (err: BusinessError, file: fileIo.File) => {
  if (err) {
    console.error(`Failed to open. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting file fd: ${file.fd}`);
    fileIo.closeSync(file);
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.open(filePath,fileIo.OpenMode.READ_WRITE |fileIo.OpenMode.CREATE, (err: BusinessError<void> | null, file:fileIo.File | undefined) => {
  if (err) {
    console.error(`Failed to open. Code: ${err.code}, message: ${err.message}`);
  } else if (file) {
    console.info(`Succeeded in getting file fd: ${file.fd}`);
    fileIo.closeSync(file);
  }
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.open(filePath, (err: BusinessError, file: fileIo.File) => {
  if (err) {
    console.error(`Failed to open. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting file fd: ${file.fd}`);
    fileIo.closeSync(file);
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.open(filePath, (err: BusinessError<void> | null, file:fileIo.File | undefined) => {
  if (err) {
    console.error(`Failed to open. Code: ${err.code}, message: ${err.message}`);
  } else if (file) {
    console.info(`Succeeded in getting file fd: ${file.fd}`);
    fileIo.closeSync(file);
  }
});
```


## open

```TypeScript
declare function open(path: string, callback: AsyncCallback<File>): void
```

打开文件或目录，支持使用URI打开文件。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[File](arkts-corefile-file-fs-file-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
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

参见 [open](#open)


## open

```TypeScript
declare function open(path: string, mode: number, callback: AsyncCallback<File>): void
```

打开文件或目录，可设置打开文件的选项。使用callback异步回调。支持使用URI打开文件。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[File](arkts-corefile-file-fs-file-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
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

参见 [open](#open)
