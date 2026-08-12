# @ohos.file.fs

FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [fileIo](arkts-corefile-fileio-n.md) |

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [access](arkts-corefile-file-fs-access-f.md#access) |
| [access](arkts-corefile-file-fs-access-f.md#access-1) |
| [access](arkts-corefile-file-fs-access-f.md#access-2) |
| [accessSync](arkts-corefile-file-fs-accesssync-f.md#accesssync) |
| [accessSync](arkts-corefile-file-fs-accesssync-f.md#accesssync-1) |
| [close](arkts-corefile-file-fs-close-f.md#close) |
| [close](arkts-corefile-file-fs-close-f.md#close-1) |
| [closeSync](arkts-corefile-file-fs-closesync-f.md#closesync) |
| [connectDfs](arkts-corefile-file-fs-connectdfs-f.md#connectdfs) |
| [copy](arkts-corefile-file-fs-copy-f.md#copy) |
| [copy](arkts-corefile-file-fs-copy-f.md#copy-1) |
| [copy](arkts-corefile-file-fs-copy-f.md#copy-2) |
| [copyDir](arkts-corefile-file-fs-copydir-f.md#copydir) |
| [copyDir](arkts-corefile-file-fs-copydir-f.md#copydir-1) |
| [copyDir](arkts-corefile-file-fs-copydir-f.md#copydir-2) |
| [copyDir](arkts-corefile-file-fs-copydir-f.md#copydir-3) |
| [copyDir](arkts-corefile-file-fs-copydir-f.md#copydir-4) |
| [copyDirSync](arkts-corefile-file-fs-copydirsync-f.md#copydirsync) |
| [copyFile](arkts-corefile-file-fs-copyfile-f.md#copyfile) |
| [copyFile](arkts-corefile-file-fs-copyfile-f.md#copyfile-1) |
| [copyFile](arkts-corefile-file-fs-copyfile-f.md#copyfile-2) |
| [copyFileSync](arkts-corefile-file-fs-copyfilesync-f.md#copyfilesync) |
| [createRandomAccessFile](arkts-corefile-file-fs-createrandomaccessfile-f.md#createrandomaccessfile) |
| [createRandomAccessFile](arkts-corefile-file-fs-createrandomaccessfile-f.md#createrandomaccessfile-1) |
| [createRandomAccessFile](arkts-corefile-file-fs-createrandomaccessfile-f.md#createrandomaccessfile-2) |
| [createRandomAccessFileSync](arkts-corefile-file-fs-createrandomaccessfilesync-f.md#createrandomaccessfilesync) |
| [createReadStream](arkts-corefile-file-fs-createreadstream-f.md#createreadstream) |
| [createStream](arkts-corefile-file-fs-createstream-f.md#createstream) |
| [createStream](arkts-corefile-file-fs-createstream-f.md#createstream-1) |
| [createStreamSync](arkts-corefile-file-fs-createstreamsync-f.md#createstreamsync) |
| [createWatcher](arkts-corefile-file-fs-createwatcher-f.md#createwatcher) |
| [createWriteStream](arkts-corefile-file-fs-createwritestream-f.md#createwritestream) |
| [disconnectDfs](arkts-corefile-file-fs-disconnectdfs-f.md#disconnectdfs) |
| [dup](arkts-corefile-file-fs-dup-f.md#dup) |
| [fdatasync](arkts-corefile-file-fs-fdatasync-f.md#fdatasync) |
| [fdatasync](arkts-corefile-file-fs-fdatasync-f.md#fdatasync-1) |
| [fdatasyncSync](arkts-corefile-file-fs-fdatasyncsync-f.md#fdatasyncsync) |
| [fdopenStream](arkts-corefile-file-fs-fdopenstream-f.md#fdopenstream) |
| [fdopenStream](arkts-corefile-file-fs-fdopenstream-f.md#fdopenstream-1) |
| [fdopenStreamSync](arkts-corefile-file-fs-fdopenstreamsync-f.md#fdopenstreamsync) |
| [fsync](arkts-corefile-file-fs-fsync-f.md#fsync) |
| [fsync](arkts-corefile-file-fs-fsync-f.md#fsync-1) |
| [fsyncSync](arkts-corefile-file-fs-fsyncsync-f.md#fsyncsync) |
| [getxattr](arkts-corefile-file-fs-getxattr-f.md#getxattr) |
| [getxattrSync](arkts-corefile-file-fs-getxattrsync-f.md#getxattrsync) |
| [listFile](arkts-corefile-file-fs-listfile-f.md#listfile) |
| [listFile](arkts-corefile-file-fs-listfile-f.md#listfile-1) |
| [listFile](arkts-corefile-file-fs-listfile-f.md#listfile-2) |
| [listFileExt](arkts-corefile-file-fs-listfileext-f.md#listfileext) |
| [listFileExtSync](arkts-corefile-file-fs-listfileextsync-f.md#listfileextsync) |
| [listFileSync](arkts-corefile-file-fs-listfilesync-f.md#listfilesync) |
| [lseek](arkts-corefile-file-fs-lseek-f.md#lseek) |
| [lstat](arkts-corefile-file-fs-lstat-f.md#lstat) |
| [lstat](arkts-corefile-file-fs-lstat-f.md#lstat-1) |
| [lstatSync](arkts-corefile-file-fs-lstatsync-f.md#lstatsync) |
| [mkdir](arkts-corefile-file-fs-mkdir-f.md#mkdir) |
| [mkdir](arkts-corefile-file-fs-mkdir-f.md#mkdir-1) |
| [mkdir](arkts-corefile-file-fs-mkdir-f.md#mkdir-2) |
| [mkdir](arkts-corefile-file-fs-mkdir-f.md#mkdir-3) |
| [mkdirSync](arkts-corefile-file-fs-mkdirsync-f.md#mkdirsync) |
| [mkdirSync](arkts-corefile-file-fs-mkdirsync-f.md#mkdirsync-1) |
| [mkdtemp](arkts-corefile-file-fs-mkdtemp-f.md#mkdtemp) |
| [mkdtemp](arkts-corefile-file-fs-mkdtemp-f.md#mkdtemp-1) |
| [mkdtempSync](arkts-corefile-file-fs-mkdtempsync-f.md#mkdtempsync) |
| [mmap](arkts-corefile-file-fs-mmap-f.md#mmap) |
| [mmapSync](arkts-corefile-file-fs-mmapsync-f.md#mmapsync) |
| [moveDir](arkts-corefile-file-fs-movedir-f.md#movedir) |
| [moveDir](arkts-corefile-file-fs-movedir-f.md#movedir-1) |
| [moveDir](arkts-corefile-file-fs-movedir-f.md#movedir-2) |
| [moveDir](arkts-corefile-file-fs-movedir-f.md#movedir-3) |
| [moveDir](arkts-corefile-file-fs-movedir-f.md#movedir-4) |
| [moveDirSync](arkts-corefile-file-fs-movedirsync-f.md#movedirsync) |
| [moveFile](arkts-corefile-file-fs-movefile-f.md#movefile) |
| [moveFile](arkts-corefile-file-fs-movefile-f.md#movefile-1) |
| [moveFile](arkts-corefile-file-fs-movefile-f.md#movefile-2) |
| [moveFileSync](arkts-corefile-file-fs-movefilesync-f.md#movefilesync) |
| [open](arkts-corefile-file-fs-open-f.md#open) |
| [open](arkts-corefile-file-fs-open-f.md#open-1) |
| [open](arkts-corefile-file-fs-open-f.md#open-2) |
| [openSync](arkts-corefile-file-fs-opensync-f.md#opensync) |
| [read](arkts-corefile-file-fs-read-f.md#read) |
| [read](arkts-corefile-file-fs-read-f.md#read-1) |
| [read](arkts-corefile-file-fs-read-f.md#read-2) |
| [readLines](arkts-corefile-file-fs-readlines-f.md#readlines) |
| [readLines](arkts-corefile-file-fs-readlines-f.md#readlines-1) |
| [readLines](arkts-corefile-file-fs-readlines-f.md#readlines-2) |
| [readLinesSync](arkts-corefile-file-fs-readlinessync-f.md#readlinessync) |
| [readSync](arkts-corefile-file-fs-readsync-f.md#readsync) |
| [readText](arkts-corefile-file-fs-readtext-f.md#readtext) |
| [readText](arkts-corefile-file-fs-readtext-f.md#readtext-1) |
| [readText](arkts-corefile-file-fs-readtext-f.md#readtext-2) |
| [readTextSync](arkts-corefile-file-fs-readtextsync-f.md#readtextsync) |
| [rename](arkts-corefile-file-fs-rename-f.md#rename) |
| [rename](arkts-corefile-file-fs-rename-f.md#rename-1) |
| [renameSync](arkts-corefile-file-fs-renamesync-f.md#renamesync) |
| [rmdir](arkts-corefile-file-fs-rmdir-f.md#rmdir) |
| [rmdir](arkts-corefile-file-fs-rmdir-f.md#rmdir-1) |
| [rmdirSync](arkts-corefile-file-fs-rmdirsync-f.md#rmdirsync) |
| [setxattr](arkts-corefile-file-fs-setxattr-f.md#setxattr) |
| [setxattrSync](arkts-corefile-file-fs-setxattrsync-f.md#setxattrsync) |
| [stat](arkts-corefile-file-fs-stat-f.md#stat) |
| [stat](arkts-corefile-file-fs-stat-f.md#stat-1) |
| [statSync](arkts-corefile-file-fs-statsync-f.md#statsync) |
| [symlink](arkts-corefile-file-fs-symlink-f.md#symlink) |
| [symlink](arkts-corefile-file-fs-symlink-f.md#symlink-1) |
| [symlinkSync](arkts-corefile-file-fs-symlinksync-f.md#symlinksync) |
| [truncate](arkts-corefile-file-fs-truncate-f.md#truncate) |
| [truncate](arkts-corefile-file-fs-truncate-f.md#truncate-1) |
| [truncate](arkts-corefile-file-fs-truncate-f.md#truncate-2) |
| [truncateSync](arkts-corefile-file-fs-truncatesync-f.md#truncatesync) |
| [unlink](arkts-corefile-file-fs-unlink-f.md#unlink) |
| [unlink](arkts-corefile-file-fs-unlink-f.md#unlink-1) |
| [unlinkSync](arkts-corefile-file-fs-unlinksync-f.md#unlinksync) |
| [utimes](arkts-corefile-file-fs-utimes-f.md#utimes) |
| [write](arkts-corefile-file-fs-write-f.md#write) |
| [write](arkts-corefile-file-fs-write-f.md#write-1) |
| [write](arkts-corefile-file-fs-write-f.md#write-2) |
| [writeSync](arkts-corefile-file-fs-writesync-f.md#writesync) |

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
| [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) |
| [ReadStreamOptions](arkts-corefile-file-fs-readstreamoptions-i.md) |
| [ReadTextOptions](arkts-corefile-file-fs-readtextoptions-i.md) |
| [ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md) |
| [ReaderIteratorResult](arkts-corefile-file-fs-readeriteratorresult-i.md) |
| [Stat](arkts-corefile-file-fs-stat-i.md) |
| [Stream](arkts-corefile-file-fs-stream-i.md) |
| [WatchEvent](arkts-corefile-file-fs-watchevent-i.md) |
| [WatchEventListener](arkts-corefile-file-fs-watcheventlistener-i.md) |
| [Watcher](arkts-corefile-file-fs-watcher-i.md) |
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
