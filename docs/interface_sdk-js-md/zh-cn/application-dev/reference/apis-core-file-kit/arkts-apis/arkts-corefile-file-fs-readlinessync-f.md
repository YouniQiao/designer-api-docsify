# readLinesSync

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## readLinesSync

```TypeScript
declare function readLinesSync(filePath: string, options?: Options): ReaderIterator
```

以同步方式逐行读取文件的文本内容，只支持读取utf-8格式文件。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| options | [Options](arkts-corefile-file-fs-options-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md) |

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

**示例**

```TypeScript
import { Options } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
let readerIterator = fileIo.readLinesSync(filePath, options);
for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
  console.info(`Succeeded in reading lines, content: ${it.value}`);
}
```
