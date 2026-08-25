# fileIo(@ohos.file.fs (文件管理))

本模块是Core File Kit的核心模块，提供基础文件操作API，用于对应用沙箱内的文件和目录进行创建、打开、读写、拷贝、移动、删除、查询属性等操作。模块提供了多种文件访问模式，开发者可根据场景选择：基于文件描述符（fd）：通过open获取File对象，再使用read/write进行读写，适用于通用文件读写场景。 基于流（Stream）：通过createStream/fdopenStream创建Stream，或通过createReadStream/createWriteStream创建ReadStream/WriteStream，适用于流式数据处理或大文件分块读写等场景。 基于RandomAccessFile：通过createRandomAccessFile创建RandomAccessFile对象，支持独立的偏移指针和随机读写，适用于需要频繁跳转读写位置的场景。 此外，模块还提供文件监听（Watcher）、内存映射（FileMapping）、安全原子写入（AtomicFile）等其他能力。

> **使用说明：**
使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取沙箱路径的方式及其接口用法可参考： [应用上下文Context-获取应用文件路径](../../../application-models/application-context-stage.md#获取应用文件路径)。&lt;br/  
&gt; 指向资源的字符串称为URI。对于只支持沙箱路径作为入参的接口，可以使用构造fileUri对象并获取其沙箱路径的属性的方式将URI转换为沙箱路径，然后使用文件接口。 URI定义及其转换方式请参考：[文件URI](../../../reference/apis-core-file-kit/js-apis-file-fileuri.md)。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## 汇总

### 命名空间

| 名称 |
| --- |
| [OpenMode(@ohos.file.fs (文件管理))](arkts-corefile-fileio-openmode-n.md) |

### 函数

| 名称 |
| --- |
| [access(@ohos.file.fs (文件管理))](arkts-corefile-fileio-access-f.md) |
| [access(@ohos.file.fs (文件管理))](arkts-corefile-fileio-access-f.md) |
| [access(@ohos.file.fs (文件管理))](arkts-corefile-fileio-access-f.md) |
| [accessSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-accesssync-f.md) |
| [accessSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-accesssync-f.md) |
| [close(@ohos.file.fs (文件管理))](arkts-corefile-fileio-close-f.md) |
| [close(@ohos.file.fs (文件管理))](arkts-corefile-fileio-close-f.md) |
| [closeSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-closesync-f.md) |
| [copy(@ohos.file.fs (文件管理))](arkts-corefile-fileio-copy-f.md) |
| [copy(@ohos.file.fs (文件管理))](arkts-corefile-fileio-copy-f.md) |
| [copy(@ohos.file.fs (文件管理))](arkts-corefile-fileio-copy-f.md) |
| [copyDir(@ohos.file.fs (文件管理))](arkts-corefile-fileio-copydir-f.md) |
| [copyDir(@ohos.file.fs (文件管理))](arkts-corefile-fileio-copydir-f.md) |
| [copyDirWithConflictFiles(@ohos.file.fs (文件管理))](arkts-corefile-fileio-copydirwithconflictfiles-f.md) |
| [copyDir(@ohos.file.fs (文件管理))](arkts-corefile-fileio-copydir-f.md) |
| [copyDirWithConflictFiles(@ohos.file.fs (文件管理))](arkts-corefile-fileio-copydirwithconflictfiles-f.md) |
| [copyDirSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-copydirsync-f.md) |
| [copyFile(@ohos.file.fs (文件管理))](arkts-corefile-fileio-copyfile-f.md) |
| [copyFile(@ohos.file.fs (文件管理))](arkts-corefile-fileio-copyfile-f.md) |
| [copyFile(@ohos.file.fs (文件管理))](arkts-corefile-fileio-copyfile-f.md) |
| [copyFileSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-copyfilesync-f.md) |
| [createStream(@ohos.file.fs (文件管理))](arkts-corefile-fileio-createstream-f.md) |
| [createStream(@ohos.file.fs (文件管理))](arkts-corefile-fileio-createstream-f.md) |
| [createStreamSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-createstreamsync-f.md) |
| [createRandomAccessFile(@ohos.file.fs (文件管理))](arkts-corefile-fileio-createrandomaccessfile-f.md) |
| [createRandomAccessFile(@ohos.file.fs (文件管理))](arkts-corefile-fileio-createrandomaccessfile-f.md) |
| [createRandomAccessFile(@ohos.file.fs (文件管理))](arkts-corefile-fileio-createrandomaccessfile-f.md) |
| [createRandomAccessFileSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-createrandomaccessfilesync-f.md) |
| [createReadStream(@ohos.file.fs (文件管理))](arkts-corefile-fileio-createreadstream-f.md) |
| [createWriteStream(@ohos.file.fs (文件管理))](arkts-corefile-fileio-createwritestream-f.md) |
| [createWatcher(@ohos.file.fs (文件管理))](arkts-corefile-fileio-createwatcher-f.md) |
| [dup(@ohos.file.fs (文件管理))](arkts-corefile-fileio-dup-f.md) |
| [fdatasync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-fdatasync-f.md) |
| [fdatasync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-fdatasync-f.md) |
| [fdatasyncSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-fdatasyncsync-f.md) |
| [fdopenStream(@ohos.file.fs (文件管理))](arkts-corefile-fileio-fdopenstream-f.md) |
| [fdopenStream(@ohos.file.fs (文件管理))](arkts-corefile-fileio-fdopenstream-f.md) |
| [fdopenStreamSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-fdopenstreamsync-f.md) |
| [fsync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-fsync-f.md) |
| [fsync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-fsync-f.md) |
| [fsyncSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-fsyncsync-f.md) |
| [listFile(@ohos.file.fs (文件管理))](arkts-corefile-fileio-listfile-f.md) |
| [listFile(@ohos.file.fs (文件管理))](arkts-corefile-fileio-listfile-f.md) |
| [listFile(@ohos.file.fs (文件管理))](arkts-corefile-fileio-listfile-f.md) |
| [listFileSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-listfilesync-f.md) |
| [listFileExt(@ohos.file.fs (文件管理))](arkts-corefile-fileio-listfileext-f.md) |
| [listFileExtSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-listfileextsync-f.md) |
| [lseek(@ohos.file.fs (文件管理))](arkts-corefile-fileio-lseek-f.md) |
| [lstat(@ohos.file.fs (文件管理))](arkts-corefile-fileio-lstat-f.md) |
| [lstat(@ohos.file.fs (文件管理))](arkts-corefile-fileio-lstat-f.md) |
| [lstatSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-lstatsync-f.md) |
| [mkdir(@ohos.file.fs (文件管理))](arkts-corefile-fileio-mkdir-f.md) |
| [mkdir(@ohos.file.fs (文件管理))](arkts-corefile-fileio-mkdir-f.md) |
| [mkdir(@ohos.file.fs (文件管理))](arkts-corefile-fileio-mkdir-f.md) |
| [mkdir(@ohos.file.fs (文件管理))](arkts-corefile-fileio-mkdir-f.md) |
| [mkdirSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-mkdirsync-f.md) |
| [mkdirSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-mkdirsync-f.md) |
| [mkdtemp(@ohos.file.fs (文件管理))](arkts-corefile-fileio-mkdtemp-f.md) |
| [mkdtemp(@ohos.file.fs (文件管理))](arkts-corefile-fileio-mkdtemp-f.md) |
| [mkdtempSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-mkdtempsync-f.md) |
| [mmap(@ohos.file.fs (文件管理))](arkts-corefile-fileio-mmap-f.md) |
| [mmapSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-mmapsync-f.md) |
| [moveDir(@ohos.file.fs (文件管理))](arkts-corefile-fileio-movedir-f.md) |
| [moveDir(@ohos.file.fs (文件管理))](arkts-corefile-fileio-movedir-f.md) |
| [moveDirWithConflictFiles(@ohos.file.fs (文件管理))](arkts-corefile-fileio-movedirwithconflictfiles-f.md) |
| [moveDir(@ohos.file.fs (文件管理))](arkts-corefile-fileio-movedir-f.md) |
| [moveDirWithConflictFiles(@ohos.file.fs (文件管理))](arkts-corefile-fileio-movedirwithconflictfiles-f.md) |
| [moveDirSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-movedirsync-f.md) |
| [moveFile(@ohos.file.fs (文件管理))](arkts-corefile-fileio-movefile-f.md) |
| [moveFile(@ohos.file.fs (文件管理))](arkts-corefile-fileio-movefile-f.md) |
| [moveFile(@ohos.file.fs (文件管理))](arkts-corefile-fileio-movefile-f.md) |
| [moveFileSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-movefilesync-f.md) |
| [open(@ohos.file.fs (文件管理))](arkts-corefile-fileio-open-f.md) |
| [open(@ohos.file.fs (文件管理))](arkts-corefile-fileio-open-f.md) |
| [open(@ohos.file.fs (文件管理))](arkts-corefile-fileio-open-f.md) |
| [openSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-opensync-f.md) |
| [read(@ohos.file.fs (文件管理))](arkts-corefile-fileio-read-f.md) |
| [read(@ohos.file.fs (文件管理))](arkts-corefile-fileio-read-f.md) |
| [read(@ohos.file.fs (文件管理))](arkts-corefile-fileio-read-f.md) |
| [readSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-readsync-f.md) |
| [readLines(@ohos.file.fs (文件管理))](arkts-corefile-fileio-readlines-f.md) |
| [readLines(@ohos.file.fs (文件管理))](arkts-corefile-fileio-readlines-f.md) |
| [readLines(@ohos.file.fs (文件管理))](arkts-corefile-fileio-readlines-f.md) |
| [readLinesSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-readlinessync-f.md) |
| [readText(@ohos.file.fs (文件管理))](arkts-corefile-fileio-readtext-f.md) |
| [readText(@ohos.file.fs (文件管理))](arkts-corefile-fileio-readtext-f.md) |
| [readText(@ohos.file.fs (文件管理))](arkts-corefile-fileio-readtext-f.md) |
| [readTextSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-readtextsync-f.md) |
| [rename(@ohos.file.fs (文件管理))](arkts-corefile-fileio-rename-f.md) |
| [rename(@ohos.file.fs (文件管理))](arkts-corefile-fileio-rename-f.md) |
| [renameSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-renamesync-f.md) |
| [rmdir(@ohos.file.fs (文件管理))](arkts-corefile-fileio-rmdir-f.md) |
| [rmdir(@ohos.file.fs (文件管理))](arkts-corefile-fileio-rmdir-f.md) |
| [rmdirSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-rmdirsync-f.md) |
| [stat(@ohos.file.fs (文件管理))](arkts-corefile-fileio-stat-f.md) |
| [stat(@ohos.file.fs (文件管理))](arkts-corefile-fileio-stat-f.md) |
| [statSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-statsync-f.md) |
| [symlink(@ohos.file.fs (文件管理))](arkts-corefile-fileio-symlink-f.md) |
| [symlink(@ohos.file.fs (文件管理))](arkts-corefile-fileio-symlink-f.md) |
| [symlinkSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-symlinksync-f.md) |
| [truncate(@ohos.file.fs (文件管理))](arkts-corefile-fileio-truncate-f.md) |
| [truncate(@ohos.file.fs (文件管理))](arkts-corefile-fileio-truncate-f.md) |
| [truncate(@ohos.file.fs (文件管理))](arkts-corefile-fileio-truncate-f.md) |
| [truncateSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-truncatesync-f.md) |
| [unlink(@ohos.file.fs (文件管理))](arkts-corefile-fileio-unlink-f.md) |
| [unlink(@ohos.file.fs (文件管理))](arkts-corefile-fileio-unlink-f.md) |
| [unlinkSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-unlinksync-f.md) |
| [utimes(@ohos.file.fs (文件管理))](arkts-corefile-fileio-utimes-f.md) |
| [write(@ohos.file.fs (文件管理))](arkts-corefile-fileio-write-f.md) |
| [write(@ohos.file.fs (文件管理))](arkts-corefile-fileio-write-f.md) |
| [write(@ohos.file.fs (文件管理))](arkts-corefile-fileio-write-f.md) |
| [writeSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-writesync-f.md) |
| [connectDfs(@ohos.file.fs (文件管理))](arkts-corefile-fileio-connectdfs-f.md) |
| [disconnectDfs(@ohos.file.fs (文件管理))](arkts-corefile-fileio-disconnectdfs-f.md) |
| [setxattr(@ohos.file.fs (文件管理))](arkts-corefile-fileio-setxattr-f.md) |
| [setxattrSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-setxattrsync-f.md) |
| [getxattr(@ohos.file.fs (文件管理))](arkts-corefile-fileio-getxattr-f.md) |
| [getxattrSync(@ohos.file.fs (文件管理))](arkts-corefile-fileio-getxattrsync-f.md) |

### 类

| 名称 |
| --- |
| [TaskSignal(@ohos.file.fs (文件管理))](arkts-corefile-fileio-tasksignal-c.md) |
| [ReadStream(@ohos.file.fs (文件管理))](arkts-corefile-fileio-readstream-c.md) |
| [WriteStream(@ohos.file.fs (文件管理))](arkts-corefile-fileio-writestream-c.md) |
| [AtomicFile(@ohos.file.fs (文件管理))](arkts-corefile-fileio-atomicfile-c.md) |

### 接口

| 名称 |
| --- |
| [DfsListeners(@ohos.file.fs (文件管理))](arkts-corefile-fileio-dfslisteners-i.md) |
| [Progress(@ohos.file.fs (文件管理))](arkts-corefile-fileio-progress-i.md) |
| [CopyOptions(@ohos.file.fs (文件管理))](arkts-corefile-fileio-copyoptions-i.md) |
| [File(@ohos.file.fs (文件管理))](arkts-corefile-fileio-file-i.md) |
| [FileMapping(@ohos.file.fs (文件管理))](arkts-corefile-fileio-filemapping-i.md) |
| [RandomAccessFile(@ohos.file.fs (文件管理))](arkts-corefile-fileio-randomaccessfile-i.md) |
| [Stat(@ohos.file.fs (文件管理))](arkts-corefile-fileio-stat-i.md) |
| [Stream(@ohos.file.fs (文件管理))](arkts-corefile-fileio-stream-i.md) |
| [Watcher(@ohos.file.fs (文件管理))](arkts-corefile-fileio-watcher-i.md) |
| [ReaderIterator(@ohos.file.fs (文件管理))](arkts-corefile-fileio-readeriterator-i.md) |

### 枚举

| 名称 |
| --- |
| [MappingMode(@ohos.file.fs (文件管理))](arkts-corefile-fileio-mappingmode-e.md) |
| [WhenceType(@ohos.file.fs (文件管理))](arkts-corefile-fileio-whencetype-e.md) |
| [LocationType(@ohos.file.fs (文件管理))](arkts-corefile-fileio-locationtype-e.md) |
| [AccessModeType(@ohos.file.fs (文件管理))](arkts-corefile-fileio-accessmodetype-e.md) |
| [AccessFlagType(@ohos.file.fs (文件管理))](arkts-corefile-fileio-accessflagtype-e.md) |

### 类型

| 名称 |
| --- |
| [DfsListenerCallback(@ohos.file.fs (文件管理))](arkts-corefile-fileio-dfslistenercallback-t.md) |
| [ProgressListener(@ohos.file.fs (文件管理))](arkts-corefile-fileio-progresslistener-t.md) |
