# FileFilter

文件名过滤器接口，可通过该接口自定义文件名过滤规则。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## filter

```TypeScript
filter(name: string): boolean
```

用于[listFileExt](arkts-corefile-file-fs-listfileext-f.md)或[listFileExtSync](arkts-corefile-file-fs-listfileextsync-f.md)接口的文件过滤，判断指定文件名是否应包含在返回的文件列表中。注意：此函数被频繁调用。尽量避免文件I/O、网络请求等耗时操作。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
