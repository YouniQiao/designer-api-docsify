# File

由open接口打开的File对象，持有文件描述符fd，提供文件锁和获取父目录等能力。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## getParent

```TypeScript
getParent(): string
```

获取File对象对应文件的父目录路径。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| 13900005 |
| 13900042 |
| 14300002 |

## lock

```TypeScript
lock(exclusive?: boolean): Promise<void>
```

对文件阻塞式施加共享锁或独占锁。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| exclusive | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900008 |
| 13900020 |
| 13900034 |
| 13900042 |
| 13900043 |

## lock

```TypeScript
lock(callback: AsyncCallback<void>): void
```

对文件阻塞式施加共享锁。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900008 |
| 13900020 |
| 13900034 |
| 13900042 |
| 13900043 |

## lock

```TypeScript
lock(exclusive: boolean, callback: AsyncCallback<void>): void
```

对文件阻塞式施加共享锁或独占锁。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| exclusive | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900008 |
| 13900020 |
| 13900034 |
| 13900042 |
| 13900043 |

## tryLock

```TypeScript
tryLock(exclusive?: boolean): void
```

文件非阻塞式施加共享锁或独占锁。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| exclusive | boolean | 否 |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900008 |
| 13900020 |
| 13900034 |
| 13900042 |
| 13900043 |

## unlock

```TypeScript
unlock(): void
```

以同步方式解锁文件。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900008 |
| 13900020 |
| 13900034 |
| 13900042 |
| 13900043 |

## fd

```TypeScript
readonly fd: number
```

已打开的文件描述符fd。

**类型：** number

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

## name

```TypeScript
readonly name: string
```

文件名。

**类型：** string

**起始版本：** 10

**系统能力：** SystemCapability.FileManagement.File.FileIO

## path

```TypeScript
readonly path: string
```

文件路径。

**类型：** string

**起始版本：** 10

**系统能力：** SystemCapability.FileManagement.File.FileIO
