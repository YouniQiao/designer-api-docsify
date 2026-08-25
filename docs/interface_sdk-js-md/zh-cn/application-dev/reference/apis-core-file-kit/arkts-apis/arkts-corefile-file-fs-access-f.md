# access

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## access

```TypeScript
declare function access(path: string, mode?: AccessModeType): Promise<boolean>
```

检查文件或目录是否存在，或校验操作权限。使用Promise异步回调。校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | [AccessModeType](arkts-corefile-file-fs-accessmodetype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900005 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900018 |
| 13900020 |
| 13900023 |
| 13900030 |
| 13900033 |
| 13900042 |


## access

```TypeScript
declare function access(path: string, callback: AsyncCallback<boolean>): void
```

检查文件或目录是否存在。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900005 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900018 |
| 13900020 |
| 13900023 |
| 13900030 |
| 13900033 |
| 13900042 |


## access

```TypeScript
declare function access(path: string, mode: AccessModeType, flag: AccessFlagType): Promise<boolean>
```

检查文件或目录是否在本地，或校验操作权限。使用Promise异步回调。校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | [AccessModeType](arkts-corefile-file-fs-accessmodetype-e.md) | 是 |
| flag | [AccessFlagType](arkts-corefile-file-fs-accessflagtype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900005 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900018 |
| 13900020 |
| 13900023 |
| 13900030 |
| 13900033 |
