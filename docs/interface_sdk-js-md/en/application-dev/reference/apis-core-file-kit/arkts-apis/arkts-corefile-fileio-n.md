# fileIo

FileIO

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [OpenMode](arkts-corefile-fileio-openmode-n.md) |

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [access](arkts-corefile-fileio-access-f.md) |
| [access](arkts-corefile-fileio-access-f.md) |
| [access](arkts-corefile-fileio-access-f.md) |
| [accessSync](arkts-corefile-fileio-accesssync-f.md) |
| [accessSync](arkts-corefile-fileio-accesssync-f.md) |
| [close](arkts-corefile-fileio-close-f.md) |
| [close](arkts-corefile-fileio-close-f.md) |
| [closeSync](arkts-corefile-fileio-closesync-f.md) |
| [copy](arkts-corefile-fileio-copy-f.md) |
| [copy](arkts-corefile-fileio-copy-f.md) |
| [copy](arkts-corefile-fileio-copy-f.md) |
| [copyDir](arkts-corefile-fileio-copydir-f.md) |
| [copyDir](arkts-corefile-fileio-copydir-f.md) |
| [copyDirWithConflictFiles](arkts-corefile-fileio-copydirwithconflictfiles-f.md) |
| [copyDir](arkts-corefile-fileio-copydir-f.md) |
| [copyDirWithConflictFiles](arkts-corefile-fileio-copydirwithconflictfiles-f.md) |
| [copyDirSync](arkts-corefile-fileio-copydirsync-f.md) |
| [copyFile](arkts-corefile-fileio-copyfile-f.md) |
| [copyFile](arkts-corefile-fileio-copyfile-f.md) |
| [copyFile](arkts-corefile-fileio-copyfile-f.md) |
| [copyFileSync](arkts-corefile-fileio-copyfilesync-f.md) |
| [createStream](arkts-corefile-fileio-createstream-f.md) |
| [createStream](arkts-corefile-fileio-createstream-f.md) |
| [createStreamSync](arkts-corefile-fileio-createstreamsync-f.md) |
| [createRandomAccessFile](arkts-corefile-fileio-createrandomaccessfile-f.md) |
| [createRandomAccessFile](arkts-corefile-fileio-createrandomaccessfile-f.md) |
| [createRandomAccessFile](arkts-corefile-fileio-createrandomaccessfile-f.md) |
| [createRandomAccessFileSync](arkts-corefile-fileio-createrandomaccessfilesync-f.md) |
| [createReadStream](arkts-corefile-fileio-createreadstream-f.md) |
| [createWriteStream](arkts-corefile-fileio-createwritestream-f.md) |
| [createWatcher](arkts-corefile-fileio-createwatcher-f.md) |
| [dup](arkts-corefile-fileio-dup-f.md) |
| [fdatasync](arkts-corefile-fileio-fdatasync-f.md) |
| [fdatasync](arkts-corefile-fileio-fdatasync-f.md) |
| [fdatasyncSync](arkts-corefile-fileio-fdatasyncsync-f.md) |
| [fdopenStream](arkts-corefile-fileio-fdopenstream-f.md) |
| [fdopenStream](arkts-corefile-fileio-fdopenstream-f.md) |
| [fdopenStreamSync](arkts-corefile-fileio-fdopenstreamsync-f.md) |
| [fsync](arkts-corefile-fileio-fsync-f.md) |
| [fsync](arkts-corefile-fileio-fsync-f.md) |
| [fsyncSync](arkts-corefile-fileio-fsyncsync-f.md) |
| [listFile](arkts-corefile-fileio-listfile-f.md) |
| [listFile](arkts-corefile-fileio-listfile-f.md) |
| [listFile](arkts-corefile-fileio-listfile-f.md) |
| [listFileSync](arkts-corefile-fileio-listfilesync-f.md) |
| [listFileExt](arkts-corefile-fileio-listfileext-f.md) |
| [listFileExtSync](arkts-corefile-fileio-listfileextsync-f.md) |
| [lseek](arkts-corefile-fileio-lseek-f.md) |
| [lstat](arkts-corefile-fileio-lstat-f.md) |
| [lstat](arkts-corefile-fileio-lstat-f.md) |
| [lstatSync](arkts-corefile-fileio-lstatsync-f.md) |
| [mkdir](arkts-corefile-fileio-mkdir-f.md) |
| [mkdir](arkts-corefile-fileio-mkdir-f.md) |
| [mkdir](arkts-corefile-fileio-mkdir-f.md) |
| [mkdir](arkts-corefile-fileio-mkdir-f.md) |
| [mkdirSync](arkts-corefile-fileio-mkdirsync-f.md) |
| [mkdirSync](arkts-corefile-fileio-mkdirsync-f.md) |
| [mkdtemp](arkts-corefile-fileio-mkdtemp-f.md) |
| [mkdtemp](arkts-corefile-fileio-mkdtemp-f.md) |
| [mkdtempSync](arkts-corefile-fileio-mkdtempsync-f.md) |
| [mmap](arkts-corefile-fileio-mmap-f.md) |
| [mmapSync](arkts-corefile-fileio-mmapsync-f.md) |
| [moveDir](arkts-corefile-fileio-movedir-f.md) |
| [moveDir](arkts-corefile-fileio-movedir-f.md) |
| [moveDirWithConflictFiles](arkts-corefile-fileio-movedirwithconflictfiles-f.md) |
| [moveDir](arkts-corefile-fileio-movedir-f.md) |
| [moveDirWithConflictFiles](arkts-corefile-fileio-movedirwithconflictfiles-f.md) |
| [moveDirSync](arkts-corefile-fileio-movedirsync-f.md) |
| [moveFile](arkts-corefile-fileio-movefile-f.md) |
| [moveFile](arkts-corefile-fileio-movefile-f.md) |
| [moveFile](arkts-corefile-fileio-movefile-f.md) |
| [moveFileSync](arkts-corefile-fileio-movefilesync-f.md) |
| [open](arkts-corefile-fileio-open-f.md) |
| [open](arkts-corefile-fileio-open-f.md) |
| [open](arkts-corefile-fileio-open-f.md) |
| [openSync](arkts-corefile-fileio-opensync-f.md) |
| [read](arkts-corefile-fileio-read-f.md) |
| [read](arkts-corefile-fileio-read-f.md) |
| [read](arkts-corefile-fileio-read-f.md) |
| [readSync](arkts-corefile-fileio-readsync-f.md) |
| [readLines](arkts-corefile-fileio-readlines-f.md) |
| [readLines](arkts-corefile-fileio-readlines-f.md) |
| [readLines](arkts-corefile-fileio-readlines-f.md) |
| [readLinesSync](arkts-corefile-fileio-readlinessync-f.md) |
| [readText](arkts-corefile-fileio-readtext-f.md) |
| [readText](arkts-corefile-fileio-readtext-f.md) |
| [readText](arkts-corefile-fileio-readtext-f.md) |
| [readTextSync](arkts-corefile-fileio-readtextsync-f.md) |
| [rename](arkts-corefile-fileio-rename-f.md) |
| [rename](arkts-corefile-fileio-rename-f.md) |
| [renameSync](arkts-corefile-fileio-renamesync-f.md) |
| [rmdir](arkts-corefile-fileio-rmdir-f.md) |
| [rmdir](arkts-corefile-fileio-rmdir-f.md) |
| [rmdirSync](arkts-corefile-fileio-rmdirsync-f.md) |
| [stat](arkts-corefile-fileio-stat-f.md) |
| [stat](arkts-corefile-fileio-stat-f.md) |
| [statSync](arkts-corefile-fileio-statsync-f.md) |
| [symlink](arkts-corefile-fileio-symlink-f.md) |
| [symlink](arkts-corefile-fileio-symlink-f.md) |
| [symlinkSync](arkts-corefile-fileio-symlinksync-f.md) |
| [truncate](arkts-corefile-fileio-truncate-f.md) |
| [truncate](arkts-corefile-fileio-truncate-f.md) |
| [truncate](arkts-corefile-fileio-truncate-f.md) |
| [truncateSync](arkts-corefile-fileio-truncatesync-f.md) |
| [unlink](arkts-corefile-fileio-unlink-f.md) |
| [unlink](arkts-corefile-fileio-unlink-f.md) |
| [unlinkSync](arkts-corefile-fileio-unlinksync-f.md) |
| [utimes](arkts-corefile-fileio-utimes-f.md) |
| [write](arkts-corefile-fileio-write-f.md) |
| [write](arkts-corefile-fileio-write-f.md) |
| [write](arkts-corefile-fileio-write-f.md) |
| [writeSync](arkts-corefile-fileio-writesync-f.md) |
| [connectDfs](arkts-corefile-fileio-connectdfs-f.md) |
| [disconnectDfs](arkts-corefile-fileio-disconnectdfs-f.md) |
| [setxattr](arkts-corefile-fileio-setxattr-f.md) |
| [setxattrSync](arkts-corefile-fileio-setxattrsync-f.md) |
| [getxattr](arkts-corefile-fileio-getxattr-f.md) |
| [getxattrSync](arkts-corefile-fileio-getxattrsync-f.md) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TaskSignal](arkts-corefile-fileio-tasksignal-c.md) |
| [ReadStream](arkts-corefile-fileio-readstream-c.md) |
| [WriteStream](arkts-corefile-fileio-writestream-c.md) |
| [AtomicFile](arkts-corefile-fileio-atomicfile-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DfsListeners](arkts-corefile-fileio-dfslisteners-i.md) |
| [Progress](arkts-corefile-fileio-progress-i.md) |
| [CopyOptions](arkts-corefile-fileio-copyoptions-i.md) |
| [File](arkts-corefile-fileio-file-i.md) |
| [FileMapping](arkts-corefile-fileio-filemapping-i.md) |
| [RandomAccessFile](arkts-corefile-fileio-randomaccessfile-i.md) |
| [Stat](arkts-corefile-fileio-stat-i.md) |
| [Stream](arkts-corefile-fileio-stream-i.md) |
| [Watcher](arkts-corefile-fileio-watcher-i.md) |
| [ReaderIterator](arkts-corefile-fileio-readeriterator-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [MappingMode](arkts-corefile-fileio-mappingmode-e.md) |
| [WhenceType](arkts-corefile-fileio-whencetype-e.md) |
| [LocationType](arkts-corefile-fileio-locationtype-e.md) |
| [AccessModeType](arkts-corefile-fileio-accessmodetype-e.md) |
| [AccessFlagType](arkts-corefile-fileio-accessflagtype-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DfsListenerCallback](arkts-corefile-fileio-dfslistenercallback-t.md) |
| [ProgressListener](arkts-corefile-fileio-progresslistener-t.md) |
