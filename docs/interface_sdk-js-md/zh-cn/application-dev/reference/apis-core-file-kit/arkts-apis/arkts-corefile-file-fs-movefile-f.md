# moveFile

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## moveFile

```TypeScript
declare function moveFile(src: string, dest: string, mode?: number): Promise<void>
```

移动文件至目标路径，支持设置冲突处理模式。使用Promise异步回调。

> **说明：**&gt;
> 该接口不支持在分布式文件路径下操作。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | string | 是 |
| dest | string | 是 |
| mode | number | 否 |

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
| 13900014 |
| 13900015 |
| 13900016 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900025 |
| 13900027 |
| 13900028 |
| 13900032 |
| 13900033 |
| 13900041 |
| 13900042 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fileIo.moveFile(srcPath, destPath, 0).then(() => {
  console.info(`Succeeded in moving file.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to move file. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fileIo.moveFile(srcPath, destPath, 0).then(() => {
  console.info(`Succeeded in moving file.`);
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to move file. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fileIo.moveFile(srcPath, destPath, 0, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to move file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in moving file.`);
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fileIo.moveFile(srcPath, destPath, 0, (err: BusinessError<void> | null) => {
  if (err) {
    console.error(`Failed to move file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in moving file.`);
  }
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fileIo.moveFile(srcPath, destPath, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to move file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in moving file.`);
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fileIo.moveFile(srcPath, destPath, (err: BusinessError<void> | null) => {
  if (err) {
    console.error(`Failed to move file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in moving file.`);
  }
});
```


## moveFile

```TypeScript
declare function moveFile(src: string, dest: string, callback: AsyncCallback<void>): void
```

移动文件。如果移动位置存在同名文件，将强制覆盖。使用callback异步回调。

> **说明：**&gt;
> 该接口不支持在分布式文件路径下操作。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | string | 是 |
| dest | string | 是 |
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
| 13900014 |
| 13900015 |
| 13900016 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900025 |
| 13900027 |
| 13900028 |
| 13900032 |
| 13900033 |
| 13900041 |
| 13900042 |

**示例**

参见 [moveFile](#movefile)


## moveFile

```TypeScript
declare function moveFile(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void
```

移动文件至目标路径，支持设置冲突处理模式。使用callback异步回调。

> **说明：**&gt;
> 该接口不支持在分布式文件路径下操作。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | string | 是 |
| dest | string | 是 |
| mode | number | 是 |
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
| 13900014 |
| 13900015 |
| 13900016 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900025 |
| 13900027 |
| 13900028 |
| 13900032 |
| 13900033 |
| 13900041 |
| 13900042 |

**示例**

参见 [moveFile](#movefile)
