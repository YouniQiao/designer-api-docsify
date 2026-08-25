# lseek

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## lseek

```TypeScript
function lseek(fd: int, offset: long, whence?: WhenceType): long
```

调整文件偏移指针位置。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | int | 是 |
| offset | long | 是 |
| whence | [WhenceType](arkts-corefile-file-fs-whencetype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| long |

**错误码：**

| 错误码ID |
| --- |
| 13900008 |
| 13900020 |
| 13900026 |
| 13900038 |
| 13900042 |
