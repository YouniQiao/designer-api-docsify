# mkdir

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## mkdir

```TypeScript
declare function mkdir(path: string): Promise<void>
```

创建单层目录，若父目录不存在则会报错。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900002 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900018 |
| 13900020 |
| 13900025 |
| 13900028 |
| 13900030 |
| 13900033 |
| 13900041 |
| 13900042 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir";
fileIo.mkdir(dirPath).then(() => {
  console.info(`Succeeded in making directory.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to make directory. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
let dirPath = pathDir + "/testDir";
fileIo.mkdir(dirPath).then(() => {
  console.info(`Succeeded in making directory.`);
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to make directory. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir1/testDir2/testDir3";
fileIo.mkdir(dirPath, true).then(() => {
  console.info(`Succeeded in making directory.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to make directory. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir1/testDir2/testDir3";
fileIo.mkdir(dirPath, true).then(() => {
  console.info(`Succeeded in making directory.`);
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to make directory. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir";
fileIo.mkdir(dirPath, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to make directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in making directory.`);
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir";
fileIo.mkdir(dirPath, (err: BusinessError<void> | null) => {
  if (err) {
    console.error(`Failed to make directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in making directory.`);
  }
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir1/testDir2/testDir3";
fileIo.mkdir(dirPath, true, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to make directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in making directory.`);
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir1/testDir2/testDir3";
fileIo.mkdir(dirPath, true, (err: BusinessError<void> | null) => {
  if (err) {
    console.error(`Failed to make directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in making directory.`);
  }
});
```


## mkdir

```TypeScript
declare function mkdir(path: string, recursion: boolean): Promise<void>
```

创建目录。使用Promise异步回调。当recursion指定为true时，可递归创建目录。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| recursion | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900002 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900018 |
| 13900020 |
| 13900025 |
| 13900028 |
| 13900030 |
| 13900033 |
| 13900041 |
| 13900042 |

**示例**

参见 [mkdir](#mkdir)


## mkdir

```TypeScript
declare function mkdir(path: string, callback: AsyncCallback<void>): void
```

创建单层目录，若父目录不存在则会报错。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900002 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900018 |
| 13900020 |
| 13900025 |
| 13900028 |
| 13900030 |
| 13900033 |
| 13900041 |
| 13900042 |

**示例**

参见 [mkdir](#mkdir)


## mkdir

```TypeScript
declare function mkdir(path: string, recursion: boolean, callback: AsyncCallback<void>): void
```

创建目录，当recursion指定为true，可递归创建目录。使用callback异步回调。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| recursion | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900002 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900018 |
| 13900020 |
| 13900025 |
| 13900028 |
| 13900030 |
| 13900033 |
| 13900041 |
| 13900042 |

**示例**

参见 [mkdir](#mkdir)
