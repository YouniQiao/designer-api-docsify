# readText

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## readText

```TypeScript
declare function readText(
  filePath: string,
  options?: ReadTextOptions
): Promise<string>
```

基于文本方式读取文件（即直接读取文件的文本内容）。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| options | [ReadTextOptions](arkts-corefile-file-fs-readtextoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900013 |
| 13900019 |
| 13900020 |
| 13900024 |
| 13900025 |
| 13900034 |
| 13900041 |
| 13900042 |
| 13900044 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.readText(filePath).then((str: string) => {
  console.info(`Succeeded in reading text, text is: ${str}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to read text. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.readText(filePath).then((str: string) => {
  console.info(`Succeeded in reading text, text is: ${str}`);
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
   console.error(`Failed to read text. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";

fileIo.readText(filePath, (err: BusinessError, str: string) => {
  if (err) {
    console.error(`Failed to read text. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in reading text, text is: ${str}`);
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";

fileIo.readText(filePath, (err: BusinessError<void> | null, str: string | undefined) => {
  if (err) {
    console.error(`Failed to read text. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in reading text, text is: ${str}`);
  }
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { ReadTextOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stat = fileIo.statSync(filePath);
let readTextOption: ReadTextOptions = {
    offset: 1,
    length: stat.size,
    encoding: 'utf-8'
};
fileIo.readText(filePath, readTextOption, (err: BusinessError, str: string) => {
  if (err) {
    console.error(`Failed to read text. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in reading text, text is: ${str}`);
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { ReadTextOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let readTextOption: ReadTextOptions = {
    offset: 1,
    length: 0,
    encoding: 'utf-8'
};
let stat = fileIo.statSync(filePath);
readTextOption.length = stat.size;
fileIo.readText(filePath, readTextOption, (err: BusinessError<void> | null, str: string | undefined) => {
  if (err) {
    console.error(`Failed to read text. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in reading text, text is: ${str}`);
  }
});
```


## readText

```TypeScript
declare function readText(filePath: string, callback: AsyncCallback<string>): void
```

基于文本方式读取文件内容。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900013 |
| 13900019 |
| 13900020 |
| 13900024 |
| 13900025 |
| 13900034 |
| 13900041 |
| 13900042 |

**示例**

参见 [readText](#readtext)


## readText

```TypeScript
declare function readText(
  filePath: string,
  options: ReadTextOptions,
  callback: AsyncCallback<string>
): void
```

基于文本方式读取文件内容，支持配置读取选项。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| options | [ReadTextOptions](arkts-corefile-file-fs-readtextoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900013 |
| 13900019 |
| 13900020 |
| 13900024 |
| 13900025 |
| 13900034 |
| 13900041 |
| 13900042 |

**示例**

参见 [readText](#readtext)
