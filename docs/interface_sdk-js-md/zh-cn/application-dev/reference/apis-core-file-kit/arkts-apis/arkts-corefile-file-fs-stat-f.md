# stat

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## stat

```TypeScript
declare function stat(file: string | number): Promise<Stat>
```

获取文件或目录详细属性信息，返回包含文件大小、权限模式、访问时间、修改时间等属性的Stat对象。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [file](arkts-corefile-storagestatistics-storagestats-i-sys.md) | string \| number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Stat](arkts-corefile-file-fs-stat-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900018 |
| 13900030 |
| 13900031 |
| 13900033 |
| 13900038 |
| 13900042 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.stat(filePath).then((stat: fileIo.Stat) => {
  console.info(`Succeeded in getting file info, the size of file is ${stat.size}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get file info. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.stat(filePath).then((stat:fileIo.Stat) => {
console.info(`Succeeded in getting file info, the size of file is ${stat.size}`);
}).catch((error: Error) => {
let err: BusinessError = error as BusinessError;
console.error(`Failed to get file info. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

fileIo.stat(pathDir, (err: BusinessError, stat: fileIo.Stat) => {
if (err) {
  console.error(`Failed to get file info. Code: ${err.code}, message: ${err.message}`);
} else {
  console.info(`Succeeded in getting file info, the size of file is ${stat.size}`);
}
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

fileIo.stat(pathDir, (err: BusinessError | null, stat:fileIo.Stat | undefined) => {
if (err) {
  console.error(`Failed to get file info. Code: ${err.code}, message: ${err.message}`);
} else {
  console.info(`Succeeded in getting file info, the size of file is ${stat.size}`);
}
});
```


## stat

```TypeScript
declare function stat(file: string | number, callback: AsyncCallback<Stat>): void
```

获取文件或目录的详细属性信息，返回包含文件大小、权限模式、访问时间、修改时间等属性的Stat对象。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [file](arkts-corefile-storagestatistics-storagestats-i-sys.md) | string \| number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Stat](arkts-corefile-file-fs-stat-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900018 |
| 13900030 |
| 13900031 |
| 13900033 |
| 13900038 |
| 13900042 |

**示例**

参见 [stat](#stat)
