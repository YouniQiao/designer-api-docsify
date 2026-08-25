# mkdtemp

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## mkdtemp

```TypeScript
declare function mkdtemp(prefix: string): Promise<string>
```

创建临时目录。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| prefix | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

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


## mkdtemp

```TypeScript
declare function mkdtemp(prefix: string, callback: AsyncCallback<string>): void
```

创建临时目录。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| prefix | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

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
