# @ohos.file.fs(@ohos.file.fs (文件管理))

本模块是Core File Kit的核心模块，提供基础文件操作API，用于对应用沙箱内的文件和目录进行创建、打开、读写、拷贝、移动、删除、查询属性等操作。模块提供了多种文件访问模式，开发者可根据场景选择：基于文件描述符（fd）：通过open获取File对象，再使用read/write进行读写，适用于通用文件读写场景。 基于流（Stream）：通过createStream/fdopenStream创建Stream，或通过createReadStream/createWriteStream创建ReadStream/WriteStream，适用于流式数据处理或大文件分块读写等场景。 基于RandomAccessFile：通过createRandomAccessFile创建RandomAccessFile对象，支持独立的偏移指针和随机读写，适用于需要频繁跳转读写位置的场景。 此外，模块还提供文件监听（Watcher）、内存映射（FileMapping）、安全原子写入（AtomicFile）等其他能力。

> **使用说明：**
使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取沙箱路径的方式及其接口用法可参考： [应用上下文Context-获取应用文件路径](../../../application-models/application-context-stage.md#获取应用文件路径)。指向资源的字符串称为URI。对于只支持沙箱路径作为入参的接口，可以使用构造fileUri对象并获取其沙箱路径的属性的方式将URI转换为沙箱路径，然后使用文件接口。 URI定义及其转换方式请参考：[文件URI](../../../reference/apis-core-file-kit/js-apis-file-fileuri.md)。

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## 汇总

### 命名空间

| 名称 |
| --- |
| [fileIo(@ohos.file.fs (文件管理))](arkts-corefile-fileio-n.md) |

### 函数

| 名称 |
| --- |
| [access(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-access-f.md) |
| [access(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-access-f.md) |
| [access(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-access-f.md) |
| [accessSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-accesssync-f.md) |
| [accessSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-accesssync-f.md) |
| [close(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-close-f.md) |
| [close(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-close-f.md) |
| [closeSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-closesync-f.md) |
| [connectDfs(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-connectdfs-f.md) |
| [copy(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-copy-f.md) |
| [copy(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-copy-f.md) |
| [copy(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-copy-f.md) |
| [copyDir(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-copydir-f.md) |
| [copyDir(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-copydir-f.md) |
| [copyDir(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-copydir-f.md) |
| [copyDir(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-copydir-f.md) |
| [copyDir(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-copydir-f.md) |
| [copyDirSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-copydirsync-f.md) |
| [copyFile(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-copyfile-f.md) |
| [copyFile(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-copyfile-f.md) |
| [copyFile(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-copyfile-f.md) |
| [copyFileSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-copyfilesync-f.md) |
| [createRandomAccessFile(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-createrandomaccessfile-f.md) |
| [createRandomAccessFile(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-createrandomaccessfile-f.md) |
| [createRandomAccessFile(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-createrandomaccessfile-f.md) |
| [createRandomAccessFileSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-createrandomaccessfilesync-f.md) |
| [createReadStream(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-createreadstream-f.md) |
| [createStream(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-createstream-f.md) |
| [createStream(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-createstream-f.md) |
| [createStreamSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-createstreamsync-f.md) |
| [createWatcher(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-createwatcher-f.md) |
| [createWriteStream(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-createwritestream-f.md) |
| [disconnectDfs(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-disconnectdfs-f.md) |
| [dup(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-dup-f.md) |
| [fdatasync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-fdatasync-f.md) |
| [fdatasync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-fdatasync-f.md) |
| [fdatasyncSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-fdatasyncsync-f.md) |
| [fdopenStream(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-fdopenstream-f.md) |
| [fdopenStream(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-fdopenstream-f.md) |
| [fdopenStreamSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-fdopenstreamsync-f.md) |
| [fsync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-fsync-f.md) |
| [fsync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-fsync-f.md) |
| [fsyncSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-fsyncsync-f.md) |
| [getxattr(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-getxattr-f.md) |
| [getxattrSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-getxattrsync-f.md) |
| [listFile(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-listfile-f.md) |
| [listFile(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-listfile-f.md) |
| [listFile(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-listfile-f.md) |
| [listFileExt(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-listfileext-f.md) |
| [listFileExtSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-listfileextsync-f.md) |
| [listFileSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-listfilesync-f.md) |
| [lseek(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-lseek-f.md) |
| [lstat(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-lstat-f.md) |
| [lstat(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-lstat-f.md) |
| [lstatSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-lstatsync-f.md) |
| [mkdir(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-mkdir-f.md) |
| [mkdir(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-mkdir-f.md) |
| [mkdir(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-mkdir-f.md) |
| [mkdir(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-mkdir-f.md) |
| [mkdirSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-mkdirsync-f.md) |
| [mkdirSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-mkdirsync-f.md) |
| [mkdtemp(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-mkdtemp-f.md) |
| [mkdtemp(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-mkdtemp-f.md) |
| [mkdtempSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-mkdtempsync-f.md) |
| [mmap(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-mmap-f.md) |
| [mmapSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-mmapsync-f.md) |
| [moveDir(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-movedir-f.md) |
| [moveDir(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-movedir-f.md) |
| [moveDir(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-movedir-f.md) |
| [moveDir(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-movedir-f.md) |
| [moveDir(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-movedir-f.md) |
| [moveDirSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-movedirsync-f.md) |
| [moveFile(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-movefile-f.md) |
| [moveFile(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-movefile-f.md) |
| [moveFile(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-movefile-f.md) |
| [moveFileSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-movefilesync-f.md) |
| [open(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-open-f.md) |
| [open(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-open-f.md) |
| [open(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-open-f.md) |
| [openSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-opensync-f.md) |
| [read(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-read-f.md) |
| [read(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-read-f.md) |
| [read(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-read-f.md) |
| [readLines(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-readlines-f.md) |
| [readLines(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-readlines-f.md) |
| [readLines(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-readlines-f.md) |
| [readLinesSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-readlinessync-f.md) |
| [readSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-readsync-f.md) |
| [readText(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-readtext-f.md) |
| [readText(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-readtext-f.md) |
| [readText(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-readtext-f.md) |
| [readTextSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-readtextsync-f.md) |
| [rename(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-rename-f.md) |
| [rename(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-rename-f.md) |
| [renameSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-renamesync-f.md) |
| [rmdir(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-rmdir-f.md) |
| [rmdir(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-rmdir-f.md) |
| [rmdirSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-rmdirsync-f.md) |
| [setxattr(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-setxattr-f.md) |
| [setxattrSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-setxattrsync-f.md) |
| [stat(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-stat-f.md) |
| [stat(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-stat-f.md) |
| [statSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-statsync-f.md) |
| [symlink(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-symlink-f.md) |
| [symlink(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-symlink-f.md) |
| [symlinkSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-symlinksync-f.md) |
| [truncate(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-truncate-f.md) |
| [truncate(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-truncate-f.md) |
| [truncate(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-truncate-f.md) |
| [truncateSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-truncatesync-f.md) |
| [unlink(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-unlink-f.md) |
| [unlink(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-unlink-f.md) |
| [unlinkSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-unlinksync-f.md) |
| [utimes(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-utimes-f.md) |
| [write(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-write-f.md) |
| [write(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-write-f.md) |
| [write(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-write-f.md) |
| [writeSync(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-writesync-f.md) |

### 类

| 名称 |
| --- |
| [AtomicFile(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-atomicfile-c.md) |
| [ReadStream(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-readstream-c.md) |
| [TaskSignal(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-tasksignal-c.md) |
| [WriteStream(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-writestream-c.md) |

### 接口

| 名称 |
| --- |
| [ConflictFiles(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-conflictfiles-i.md) |
| [CopyOptions(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-copyoptions-i.md) |
| [DfsListeners(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-dfslisteners-i.md) |
| [File(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-file-i.md) |
| [FileFilter(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-filefilter-i.md) |
| [FileMapping(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-filemapping-i.md) |
| [Filter(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-filter-i.md) |
| [ListFileExtOptions(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-listfileextoptions-i.md) |
| [ListFileOptions(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-listfileoptions-i.md) |
| [Options(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-options-i.md) |
| [Progress(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-progress-i.md) |
| [RandomAccessFile(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-randomaccessfile-i.md) |
| [RandomAccessFileOptions(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-randomaccessfileoptions-i.md) |
| [ReaderIterator(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-readeriterator-i.md) |
| [ReaderIteratorResult(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-readeriteratorresult-i.md) |
| [ReadOptions(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-readoptions-i.md) |
| [ReadStreamOptions(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-readstreamoptions-i.md) |
| [ReadTextOptions(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-readtextoptions-i.md) |
| [Stat(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-stat-i.md) |
| [Stream(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-stream-i.md) |
| [Watcher(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-watcher-i.md) |
| [WatchEvent(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-watchevent-i.md) |
| [WatchEventListener(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-watcheventlistener-i.md) |
| [WriteOptions(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-writeoptions-i.md) |
| [WriteStreamOptions(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-writestreamoptions-i.md) |

### 枚举

| 名称 |
| --- |
| [AccessFlagType(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-accessflagtype-e.md) |
| [AccessModeType(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-accessmodetype-e.md) |
| [LocationType(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-locationtype-e.md) |
| [MappingMode(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-mappingmode-e.md) |
| [WhenceType(@ohos.file.fs (文件管理))](arkts-corefile-file-fs-whencetype-e.md) |

### 类型

| 名称 |
| --- |
| [ProgressListener(@ohos.file.fs (文件管理))](arkts-corefile-progresslistener-t.md) |
