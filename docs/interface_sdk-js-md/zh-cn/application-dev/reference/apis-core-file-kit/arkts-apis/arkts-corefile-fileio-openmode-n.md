# OpenMode(@ohos.file.fs (文件管理))

open接口flags参数常量，用于指定文件打开模式（如只读、只写、读写、创建等）。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## 汇总

### 常量

| 名称 |
| --- |
| [READ_ONLY(@ohos.file.fs (文件管理))](arkts-corefile-openmode-con.md#read_only) |
| [WRITE_ONLY(@ohos.file.fs (文件管理))](arkts-corefile-openmode-con.md#write_only) |
| [READ_WRITE(@ohos.file.fs (文件管理))](arkts-corefile-openmode-con.md#read_write) |
| [CREATE(@ohos.file.fs (文件管理))](arkts-corefile-openmode-con.md#create) |
| [TRUNC(@ohos.file.fs (文件管理))](arkts-corefile-openmode-con.md#trunc) |
| [APPEND(@ohos.file.fs (文件管理))](arkts-corefile-openmode-con.md#append) |
| [NONBLOCK(@ohos.file.fs (文件管理))](arkts-corefile-openmode-con.md#nonblock) |
| [DIR(@ohos.file.fs (文件管理))](arkts-corefile-openmode-con.md#dir) |
| [NOFOLLOW(@ohos.file.fs (文件管理))](arkts-corefile-openmode-con.md#nofollow) |
| [SYNC(@ohos.file.fs (文件管理))](arkts-corefile-openmode-con.md#sync) |
| [UNCACHE(@ohos.file.fs (文件管理))](arkts-corefile-openmode-con.md#uncache) |
