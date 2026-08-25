# fdatasyncSync

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## fdatasyncSync

```TypeScript
declare function fdatasyncSync(fd: number): void
```

以同步方法实现文件内容的数据同步。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900005 |
| 13900008 |
| 13900020 |
| 13900025 |
| 13900027 |
| 13900041 |
| 13900042 |

**示例**

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fdatasyncSync(file.fd);
fileIo.closeSync(file);
```
