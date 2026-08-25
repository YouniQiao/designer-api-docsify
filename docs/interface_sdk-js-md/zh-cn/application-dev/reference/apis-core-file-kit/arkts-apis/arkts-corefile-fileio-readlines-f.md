# readLines

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## readLines

```TypeScript
function readLines(filePath: string, options?: Options): Promise<ReaderIterator>
```

逐行读取文件文本内容，只支持读取utf-8格式文件。使用promise异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| options | [Options](arkts-corefile-file-fs-options-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900012 |
| 13900015 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900033 |
| 13900041 |
| 13900042 |
| 13900044 |


## readLines

```TypeScript
function readLines(filePath: string, callback: AsyncCallback<ReaderIterator>): void
```

逐行读取文件文本内容，只支持读取utf-8格式文件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900012 |
| 13900015 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900033 |
| 13900041 |
| 13900042 |


## readLines

```TypeScript
function readLines(filePath: string, options: Options, callback: AsyncCallback<ReaderIterator>): void
```

逐行读取文件文本内容，可配置读取选项，只支持读取utf-8格式文件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| options | [Options](arkts-corefile-file-fs-options-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900012 |
| 13900015 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900033 |
| 13900041 |
| 13900042 |
