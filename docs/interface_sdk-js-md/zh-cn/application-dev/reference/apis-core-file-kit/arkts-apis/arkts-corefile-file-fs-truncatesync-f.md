# truncateSync

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## truncateSync

```TypeScript
declare function truncateSync(file: string | number, len?: number): void
```

以同步方法截断文件内容，将文件大小调整为指定长度，超出部分的内容将被删除。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [file](arkts-corefile-storagestatistics-storagestats-i-sys.md) | string \| number | 是 |
| len | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900012 |
| 13900013 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900023 |
| 13900024 |
| 13900027 |
| 13900030 |
| 13900033 |
| 13900042 |
