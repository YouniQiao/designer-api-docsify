# @ohos.file.fs

FileIO

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [fileIo](arkts-corefile-fileio-n.md) |

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [access](arkts-corefile-file-fs-access-f.md) |
| [access](arkts-corefile-file-fs-access-f.md) |
| [access](arkts-corefile-file-fs-access-f.md) |
| [accessSync](arkts-corefile-file-fs-accesssync-f.md) |
| [accessSync](arkts-corefile-file-fs-accesssync-f.md) |
| [close](arkts-corefile-file-fs-close-f.md) |
| [close](arkts-corefile-file-fs-close-f.md) |
| [closeSync](arkts-corefile-file-fs-closesync-f.md) |
| [connectDfs](arkts-corefile-file-fs-connectdfs-f.md) |
| [copy](arkts-corefile-file-fs-copy-f.md) |
| [copy](arkts-corefile-file-fs-copy-f.md) |
| [copy](arkts-corefile-file-fs-copy-f.md) |
| [copyDir](arkts-corefile-file-fs-copydir-f.md) |
| [copyDir](arkts-corefile-file-fs-copydir-f.md) |
| [copyDir](arkts-corefile-file-fs-copydir-f.md) |
| [copyDir](arkts-corefile-file-fs-copydir-f.md) |
| [copyDir](arkts-corefile-file-fs-copydir-f.md) |
| [copyDirSync](arkts-corefile-file-fs-copydirsync-f.md) |
| [copyFile](arkts-corefile-file-fs-copyfile-f.md) |
| [copyFile](arkts-corefile-file-fs-copyfile-f.md) |
| [copyFile](arkts-corefile-file-fs-copyfile-f.md) |
| [copyFileSync](arkts-corefile-file-fs-copyfilesync-f.md) |
| [createRandomAccessFile](arkts-corefile-file-fs-createrandomaccessfile-f.md) |
| [createRandomAccessFile](arkts-corefile-file-fs-createrandomaccessfile-f.md) |
| [createRandomAccessFile](arkts-corefile-file-fs-createrandomaccessfile-f.md) |
| [createRandomAccessFileSync](arkts-corefile-file-fs-createrandomaccessfilesync-f.md) |
| [createReadStream](arkts-corefile-file-fs-createreadstream-f.md) |
| [createStream](arkts-corefile-file-fs-createstream-f.md) |
| [createStream](arkts-corefile-file-fs-createstream-f.md) |
| [createStreamSync](arkts-corefile-file-fs-createstreamsync-f.md) |
| [createWatcher](arkts-corefile-file-fs-createwatcher-f.md) |
| [createWriteStream](arkts-corefile-file-fs-createwritestream-f.md) |
| [disconnectDfs](arkts-corefile-file-fs-disconnectdfs-f.md) |
| [dup](arkts-corefile-file-fs-dup-f.md) |
| [fdatasync](arkts-corefile-file-fs-fdatasync-f.md) |
| [fdatasync](arkts-corefile-file-fs-fdatasync-f.md) |
| [fdatasyncSync](arkts-corefile-file-fs-fdatasyncsync-f.md) |
| [fdopenStream](arkts-corefile-file-fs-fdopenstream-f.md) |
| [fdopenStream](arkts-corefile-file-fs-fdopenstream-f.md) |
| [fdopenStreamSync](arkts-corefile-file-fs-fdopenstreamsync-f.md) |
| [fsync](arkts-corefile-file-fs-fsync-f.md) |
| [fsync](arkts-corefile-file-fs-fsync-f.md) |
| [fsyncSync](arkts-corefile-file-fs-fsyncsync-f.md) |
| [getxattr](arkts-corefile-file-fs-getxattr-f.md) |
| [getxattrSync](arkts-corefile-file-fs-getxattrsync-f.md) |
| [listFile](arkts-corefile-file-fs-listfile-f.md) |
| [listFile](arkts-corefile-file-fs-listfile-f.md) |
| [listFile](arkts-corefile-file-fs-listfile-f.md) |
| [listFileExt](arkts-corefile-file-fs-listfileext-f.md) |
| [listFileExtSync](arkts-corefile-file-fs-listfileextsync-f.md) |
| [listFileSync](arkts-corefile-file-fs-listfilesync-f.md) |
| [lseek](arkts-corefile-file-fs-lseek-f.md) |
| [lstat](arkts-corefile-file-fs-lstat-f.md) |
| [lstat](arkts-corefile-file-fs-lstat-f.md) |
| [lstatSync](arkts-corefile-file-fs-lstatsync-f.md) |
| [mkdir](arkts-corefile-file-fs-mkdir-f.md) |
| [mkdir](arkts-corefile-file-fs-mkdir-f.md) |
| [mkdir](arkts-corefile-file-fs-mkdir-f.md) |
| [mkdir](arkts-corefile-file-fs-mkdir-f.md) |
| [mkdirSync](arkts-corefile-file-fs-mkdirsync-f.md) |
| [mkdirSync](arkts-corefile-file-fs-mkdirsync-f.md) |
| [mkdtemp](arkts-corefile-file-fs-mkdtemp-f.md) |
| [mkdtemp](arkts-corefile-file-fs-mkdtemp-f.md) |
| [mkdtempSync](arkts-corefile-file-fs-mkdtempsync-f.md) |
| [mmap](arkts-corefile-file-fs-mmap-f.md) |
| [mmapSync](arkts-corefile-file-fs-mmapsync-f.md) |
| [moveDir](arkts-corefile-file-fs-movedir-f.md) |
| [moveDir](arkts-corefile-file-fs-movedir-f.md) |
| [moveDir](arkts-corefile-file-fs-movedir-f.md) |
| [moveDir](arkts-corefile-file-fs-movedir-f.md) |
| [moveDir](arkts-corefile-file-fs-movedir-f.md) |
| [moveDirSync](arkts-corefile-file-fs-movedirsync-f.md) |
| [moveFile](arkts-corefile-file-fs-movefile-f.md) |
| [moveFile](arkts-corefile-file-fs-movefile-f.md) |
| [moveFile](arkts-corefile-file-fs-movefile-f.md) |
| [moveFileSync](arkts-corefile-file-fs-movefilesync-f.md) |
| [open](arkts-corefile-file-fs-open-f.md) |
| [open](arkts-corefile-file-fs-open-f.md) |
| [open](arkts-corefile-file-fs-open-f.md) |
| [openSync](arkts-corefile-file-fs-opensync-f.md) |
| [read](arkts-corefile-file-fs-read-f.md) |
| [read](arkts-corefile-file-fs-read-f.md) |
| [read](arkts-corefile-file-fs-read-f.md) |
| [readLines](arkts-corefile-file-fs-readlines-f.md) |
| [readLines](arkts-corefile-file-fs-readlines-f.md) |
| [readLines](arkts-corefile-file-fs-readlines-f.md) |
| [readLinesSync](arkts-corefile-file-fs-readlinessync-f.md) |
| [readSync](arkts-corefile-file-fs-readsync-f.md) |
| [readText](arkts-corefile-file-fs-readtext-f.md) |
| [readText](arkts-corefile-file-fs-readtext-f.md) |
| [readText](arkts-corefile-file-fs-readtext-f.md) |
| [readTextSync](arkts-corefile-file-fs-readtextsync-f.md) |
| [rename](arkts-corefile-file-fs-rename-f.md) |
| [rename](arkts-corefile-file-fs-rename-f.md) |
| [renameSync](arkts-corefile-file-fs-renamesync-f.md) |
| [rmdir](arkts-corefile-file-fs-rmdir-f.md) |
| [rmdir](arkts-corefile-file-fs-rmdir-f.md) |
| [rmdirSync](arkts-corefile-file-fs-rmdirsync-f.md) |
| [setxattr](arkts-corefile-file-fs-setxattr-f.md) |
| [setxattrSync](arkts-corefile-file-fs-setxattrsync-f.md) |
| [stat](arkts-corefile-file-fs-stat-f.md) |
| [stat](arkts-corefile-file-fs-stat-f.md) |
| [statSync](arkts-corefile-file-fs-statsync-f.md) |
| [symlink](arkts-corefile-file-fs-symlink-f.md) |
| [symlink](arkts-corefile-file-fs-symlink-f.md) |
| [symlinkSync](arkts-corefile-file-fs-symlinksync-f.md) |
| [truncate](arkts-corefile-file-fs-truncate-f.md) |
| [truncate](arkts-corefile-file-fs-truncate-f.md) |
| [truncate](arkts-corefile-file-fs-truncate-f.md) |
| [truncateSync](arkts-corefile-file-fs-truncatesync-f.md) |
| [unlink](arkts-corefile-file-fs-unlink-f.md) |
| [unlink](arkts-corefile-file-fs-unlink-f.md) |
| [unlinkSync](arkts-corefile-file-fs-unlinksync-f.md) |
| [utimes](arkts-corefile-file-fs-utimes-f.md) |
| [write](arkts-corefile-file-fs-write-f.md) |
| [write](arkts-corefile-file-fs-write-f.md) |
| [write](arkts-corefile-file-fs-write-f.md) |
| [writeSync](arkts-corefile-file-fs-writesync-f.md) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AtomicFile](arkts-corefile-file-fs-atomicfile-c.md) |
| [ReadStream](arkts-corefile-file-fs-readstream-c.md) |
| [TaskSignal](arkts-corefile-file-fs-tasksignal-c.md) |
| [WriteStream](arkts-corefile-file-fs-writestream-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConflictFiles](arkts-corefile-file-fs-conflictfiles-i.md) |
| [CopyOptions](arkts-corefile-file-fs-copyoptions-i.md) |
| [DfsListeners](arkts-corefile-file-fs-dfslisteners-i.md) |
| [File](arkts-corefile-file-fs-file-i.md) |
| [FileFilter](arkts-corefile-file-fs-filefilter-i.md) |
| [FileMapping](arkts-corefile-file-fs-filemapping-i.md) |
| [Filter](arkts-corefile-file-fs-filter-i.md) |
| [ListFileExtOptions](arkts-corefile-file-fs-listfileextoptions-i.md) |
| [ListFileOptions](arkts-corefile-file-fs-listfileoptions-i.md) |
| [Options](arkts-corefile-file-fs-options-i.md) |
| [Progress](arkts-corefile-file-fs-progress-i.md) |
| [RandomAccessFile](arkts-corefile-file-fs-randomaccessfile-i.md) |
| [RandomAccessFileOptions](arkts-corefile-file-fs-randomaccessfileoptions-i.md) |
| [ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md) |
| [ReaderIteratorResult](arkts-corefile-file-fs-readeriteratorresult-i.md) |
| [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) |
| [ReadStreamOptions](arkts-corefile-file-fs-readstreamoptions-i.md) |
| [ReadTextOptions](arkts-corefile-file-fs-readtextoptions-i.md) |
| [Stat](arkts-corefile-file-fs-stat-i.md) |
| [Stream](arkts-corefile-file-fs-stream-i.md) |
| [Watcher](arkts-corefile-file-fs-watcher-i.md) |
| [WatchEvent](arkts-corefile-file-fs-watchevent-i.md) |
| [WatchEventListener](arkts-corefile-file-fs-watcheventlistener-i.md) |
| [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) |
| [WriteStreamOptions](arkts-corefile-file-fs-writestreamoptions-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AccessFlagType](arkts-corefile-file-fs-accessflagtype-e.md) |
| [AccessModeType](arkts-corefile-file-fs-accessmodetype-e.md) |
| [LocationType](arkts-corefile-file-fs-locationtype-e.md) |
| [MappingMode](arkts-corefile-file-fs-mappingmode-e.md) |
| [WhenceType](arkts-corefile-file-fs-whencetype-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ProgressListener](arkts-corefile-progresslistener-t.md) |
