# dup

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## dup

```TypeScript
declare function dup(fd: number): File
```

复制文件描述符，并返回对应的File对象。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**返回值：**

| 类型 |
| --- |
| [File](arkts-corefile-file-fs-file-i.md) |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900014 |
| 13900020 |
| 13900022 |
| 13900042 |

**示例**

ArkTS-Dyn示例：

```TypeScript
let filePath = pathDir + "/test.txt";
let file1 = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
let fd: number = file1.fd;
let file2 = fileIo.dup(fd);
console.info(`Succeeded in getting file name of the file2 is ${file2.name}`);
fileIo.closeSync(file1);
fileIo.closeSync(file2);
```

ArkTS-Sta示例：

```TypeScript
let filePath = pathDir + "/test.txt";
let file1 = fileIo.openSync(filePath,fileIo.OpenMode.READ_WRITE);
let fd: int = file1.fd;
let file2 = fileIo.dup(fd);
console.info(`Succeeded in getting file name of the file2 is ${file2.name}`);
fileIo.closeSync(file1);
fileIo.closeSync(file2);
```
