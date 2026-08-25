# createWriteStream

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## createWriteStream

```TypeScript
declare function createWriteStream(path: string, options?: WriteStreamOptions): WriteStream
```

以同步方法打开文件可写流。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| options | [WriteStreamOptions](arkts-corefile-file-fs-writestreamoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [WriteStream](arkts-corefile-file-fs-writestream-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900011 |
| 13900012 |
| 13900015 |
| 13900017 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900038 |
| 13900041 |
| 13900042 |
