# rmdir

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## rmdir

```TypeScript
declare function rmdir(path: string): Promise<void>
```

删除目录及其所有子目录和文件。使用Promise异步回调。

> **说明：**&gt;
> 该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlink接口删除单个文件。

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
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900018 |
| 13900020 |
| 13900027 |
| 13900030 |
| 13900032 |
| 13900042 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir";
fileIo.rmdir(dirPath).then(() => {
  console.info(`Succeeded in removing directory.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to remove directory. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir";
fileIo.rmdir(dirPath).then(() => {
  console.info(`Succeeded in removing directory.`);
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to remove directory. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir";
fileIo.rmdir(dirPath, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to remove directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in removing directory.`);
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir";
fileIo.rmdir(dirPath, (err: BusinessError<void> | null) => {
  if (err) {
    console.error(`Failed to remove directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in removing directory.`);
  }
});
```


## rmdir

```TypeScript
declare function rmdir(path: string, callback: AsyncCallback<void>): void
```

删除目录及其所有子目录和文件。使用callback异步回调。

> **说明：**&gt;
> 该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlink接口删除单个文件。

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
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900018 |
| 13900020 |
| 13900027 |
| 13900030 |
| 13900032 |
| 13900042 |

**示例**

参见 [rmdir](#rmdir)
