# symlink

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## symlink

```TypeScript
declare function symlink(target: string, srcPath: string): Promise<void>
```

基于文件路径创建符号链接。使用Promise异步回调。

> **说明：**&gt;
> 从API version 11开始，不支持三方应用使用。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | string | 是 |
| srcPath | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900002 |
| 13900005 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900018 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900041 |
| 13900042 |


## symlink

```TypeScript
declare function symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void
```

基于文件路径创建符号链接。使用callback异步回调。

> **说明：**&gt;
> 从API version 11开始，不支持三方应用使用。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | string | 是 |
| srcPath | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900002 |
| 13900005 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900018 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900041 |
| 13900042 |
