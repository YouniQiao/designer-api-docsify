# lstat

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## lstat

```TypeScript
declare function lstat(path: string): Promise<Stat>
```

获取符号链接文件信息，返回符号链接本身的属性而非目标文件的属性。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Stat](arkts-corefile-file-fs-stat-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900018 |
| 13900030 |
| 13900033 |
| 13900038 |
| 13900042 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/linkToFile";
fileIo.lstat(filePath).then((stat: fileIo.Stat) => {
  console.info(`Succeeded in getting symbolic link info, the size of file is ${stat.size}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get symbolic link info. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/linkToFile";
fileIo.lstat(filePath).then((stat:fileIo.Stat) => {
  console.info(`Succeeded in getting symbolic link info, the size of file is ${stat.size}`);
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to get symbolic link info. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/linkToFile";
fileIo.lstat(filePath, (err: BusinessError, stat: fileIo.Stat) => {
  if (err) {
    console.error(`Failed to get symbolic link info. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting symbolic link info, the size of file is ${stat.size}`);
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/linkToFile";
fileIo.lstat(filePath, (err: BusinessError<void> | null, stat:fileIo.Stat | undefined) => {
  if (err) {
    console.error(`Failed to get symbolic link info. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting symbolic link info, the size of file is ${stat.size}`);
  }
});
```


## lstat

```TypeScript
declare function lstat(path: string, callback: AsyncCallback<Stat>): void
```

获取符号链接文件信息，返回符号链接本身的属性而非目标文件的属性。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Stat](arkts-corefile-file-fs-stat-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900018 |
| 13900030 |
| 13900033 |
| 13900038 |
| 13900042 |

**示例**

参见 [lstat](#lstat)
