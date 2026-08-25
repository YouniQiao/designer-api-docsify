# createWriteStream

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## createWriteStream

```TypeScript
declare function createWriteStream(path: string, options?: WriteStreamOptions): WriteStream
```

以同步方法打开文件可写流。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

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

**示例**

ArkTS-Dyn示例：

```TypeScript
// 创建文件可读流
const rs = fileIo.createReadStream(`${pathDir}/read.txt`);
// 创建文件可写流
const ws = fileIo.createWriteStream(`${pathDir}/write.txt`);
// 暂停模式拷贝文件
rs.on('readable', () => {
  const data = rs.read();
  if (!data) {
    return;
  }
  ws.write(data);
});
```

ArkTS-Sta示例：

```TypeScript
// 创建文件可读流
const rs = fileIo.createReadStream(`${pathDir}/read.txt`);
// 创建文件可写流
const ws = fileIo.createWriteStream(`${pathDir}/write.txt`);
// 暂停模式拷贝文件
rs.on('readable', () => {
  const data = rs.read();
  if (data == undefined) {
    return;
  }
  if (data instanceof String) {
    ws.write(data);
  }
  if (data instanceof buffer.Buffer) {
    ws.write(data.toString())
  }
});
```
