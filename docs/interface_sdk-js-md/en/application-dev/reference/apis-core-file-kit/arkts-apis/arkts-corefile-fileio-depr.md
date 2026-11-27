# @ohos.fileio(File Management)

fileio

## Modules to Import

```TypeScript
import fileIO from '@ohos.fileio';
```

## Summary

### Namespaces

| Name | Description |
| --- | --- |
| [fileIO](arkts-corefile-fileio-depr-fileio-n.md) | fileio |

### Functions

| Name | Description |
| --- | --- |
| [access](arkts-corefile-fileio-depr--f.md#access-1) | Checks whether this process can access a file. This API uses a promise to return the result. |
| [access](arkts-corefile-fileio-depr--f.md#access-2) | Checks whether this process can access a file. This API uses an asynchronous callback to return the result. |
| [access](arkts-corefile-fileio-depr--f.md#access-3) | Checks whether this process can access a file. This API uses an asynchronous callback to return the result. |
| [accessSync](arkts-corefile-fileio-depr--f.md#accesssync) | Checks whether this process can access a file. This API returns the result synchronously. |
| [chmod](arkts-corefile-fileio-depr--f.md#chmod-1) | Changes file permissions. This API uses a promise to return the result. |
| [chmod](arkts-corefile-fileio-depr--f.md#chmod-2) | Changes file permissions. This API uses an asynchronous callback to return the result. |
| [chmodSync](arkts-corefile-fileio-depr--f.md#chmodsync) | Changes file permissions. This API returns the result synchronously. |
| [chown](arkts-corefile-fileio-depr--f.md#chown-1) | Changes the file owner based on the file path. This API uses a promise to return the result. |
| [chown](arkts-corefile-fileio-depr--f.md#chown-2) | Changes the file owner based on the file path. This API uses an asynchronous callback to return the result. |
| [chownSync](arkts-corefile-fileio-depr--f.md#chownsync) | Changes the file owner based on its path. This API returns the result synchronously. |
| [close](arkts-corefile-fileio-depr--f.md#close-1) | Closes a file. This API uses a promise to return the result. |
| [close](arkts-corefile-fileio-depr--f.md#close-2) | Closes a file. This API uses an asynchronous callback to return the result. |
| [closeSync](arkts-corefile-fileio-depr--f.md#closesync-1) | Closes a file. This API returns the result synchronously. |
| [copyFile](arkts-corefile-fileio-depr--f.md#copyfile-1) | Copies a file. This API uses a promise to return the result. |
| [copyFile](arkts-corefile-fileio-depr--f.md#copyfile-2) | Copies a file. This API uses an asynchronous callback to return the result. |
| [copyFile](arkts-corefile-fileio-depr--f.md#copyfile-3) | Copies a file. This API uses an asynchronous callback to return the result. |
| [copyFileSync](arkts-corefile-fileio-depr--f.md#copyfilesync) | Copies a file. This API returns the result synchronously. |
| [createStream](arkts-corefile-fileio-depr--f.md#createstream-1) | Creates a stream based on the file path. This API uses a promise to return the result. |
| [createStream](arkts-corefile-fileio-depr--f.md#createstream-2) | Creates a stream based on the file path. This API uses an asynchronous callback to return the result. |
| [createStreamSync](arkts-corefile-fileio-depr--f.md#createstreamsync) | Creates a stream based on the file path. This API returns the result synchronously. |
| [createWatcher](arkts-corefile-fileio-depr--f.md#createwatcher) | Listens for file or directory changes. This API uses an asynchronous callback to return the result. |
| [fchmod](arkts-corefile-fileio-depr--f.md#fchmod-1) | Changes file permissions based on the file descriptor. This API uses a promise to return the result. |
| [fchmod](arkts-corefile-fileio-depr--f.md#fchmod-2) | Changes file permissions based on the file descriptor. This API uses an asynchronous callback to return the result. |
| [fchmodSync](arkts-corefile-fileio-depr--f.md#fchmodsync) | Changes the file permissions based on the file descriptor. This API returns the result synchronously. |
| [fchown](arkts-corefile-fileio-depr--f.md#fchown-1) | Changes the file owner based on the file descriptor. This API uses a promise to return the result. |
| [fchown](arkts-corefile-fileio-depr--f.md#fchown-2) | Changes the file owner based on the file descriptor. This API uses an asynchronous callback to return the result. |
| [fchownSync](arkts-corefile-fileio-depr--f.md#fchownsync) | Changes the file owner based on the file descriptor. This API returns the result synchronously. |
| [fdatasync](arkts-corefile-fileio-depr--f.md#fdatasync-1) | Synchronizes the data of a file. This API uses a promise to return the result. |
| [fdatasync](arkts-corefile-fileio-depr--f.md#fdatasync-2) | Synchronizes the data of a file. This API uses an asynchronous callback to return the result. |
| [fdatasyncSync](arkts-corefile-fileio-depr--f.md#fdatasyncsync) | Synchronizes the data of a file. This API returns the result synchronously. |
| [fdopenStream](arkts-corefile-fileio-depr--f.md#fdopenstream-1) | Opens a stream based on the file descriptor. This API uses a promise to return the result. |
| [fdopenStream](arkts-corefile-fileio-depr--f.md#fdopenstream-2) | Opens a stream based on the file descriptor. This API uses an asynchronous callback to return the result. |
| [fdopenStreamSync](arkts-corefile-fileio-depr--f.md#fdopenstreamsync) | Opens a stream based on the file descriptor. This API returns the result synchronously. |
| [fstat](arkts-corefile-fileio-depr--f.md#fstat-1) | Obtains file status based on the file descriptor. This API uses a promise to return the result. |
| [fstat](arkts-corefile-fileio-depr--f.md#fstat-2) | Obtains file status based on the file descriptor. This API uses an asynchronous callback to return the result. |
| [fstatSync](arkts-corefile-fileio-depr--f.md#fstatsync) | Obtains file status based on the file descriptor. This API returns the result synchronously. |
| [fsync](arkts-corefile-fileio-depr--f.md#fsync-1) | Synchronizes a file. This API uses a promise to return the result. |
| [fsync](arkts-corefile-fileio-depr--f.md#fsync-2) | Synchronizes a file. This API uses an asynchronous callback to return the result. |
| [fsyncSync](arkts-corefile-fileio-depr--f.md#fsyncsync) | Synchronizes a file. This API returns the result synchronously. |
| [ftruncate](arkts-corefile-fileio-depr--f.md#ftruncate-1) | Truncates a file based on the file descriptor. This API uses a promise to return the result. |
| [ftruncate](arkts-corefile-fileio-depr--f.md#ftruncate-2) | Truncates a file based on the file descriptor. This API uses an asynchronous callback to return the result. |
| [ftruncate](arkts-corefile-fileio-depr--f.md#ftruncate-3) | Truncates a file based on the file descriptor. This API uses an asynchronous callback to return the result. |
| [ftruncateSync](arkts-corefile-fileio-depr--f.md#ftruncatesync) | Truncates a file based on the file descriptor. This API returns the result synchronously. |
| [hash](arkts-corefile-fileio-depr--f.md#hash-1) | Calculates the hash value of a file. This API uses a promise to return the result. |
| [hash](arkts-corefile-fileio-depr--f.md#hash-2) | Calculates the hash value of a file. This API uses an asynchronous callback to return the result. |
| [lchown](arkts-corefile-fileio-depr--f.md#lchown-1) | Changes the file owner (owner of the symbolic link, not the file referred to by the symbolic link) based on the file path. This API uses a promise to return the result. |
| [lchown](arkts-corefile-fileio-depr--f.md#lchown-2) | Changes the file owner (owner of the symbolic link, not the file referred to by the symbolic link) based on a file path. This API uses an asynchronous callback to return the result. |
| [lchownSync](arkts-corefile-fileio-depr--f.md#lchownsync) | Changes the file owner based on a file path and changes the owner of the symbolic link (not the referenced file). This API returns the result synchronously. |
| [lstat](arkts-corefile-fileio-depr--f.md#lstat-1) | Obtains information about a symbolic link that is used to refer to a file or directory. This API uses a promise to return the result. |
| [lstat](arkts-corefile-fileio-depr--f.md#lstat-2) | Obtains information about a symbolic link that is used to refer to a file or directory. This API uses an asynchronous callback to return the result. |
| [lstatSync](arkts-corefile-fileio-depr--f.md#lstatsync) | Obtains information about a symbolic link that is used to refer to a file or directory. This API returns the result synchronously. |
| [mkdir](arkts-corefile-fileio-depr--f.md#mkdir-1) | Creates a directory. This API uses a promise to return the result. |
| [mkdir](arkts-corefile-fileio-depr--f.md#mkdir-2) | Creates a directory. This API uses an asynchronous callback to return the result. |
| [mkdir](arkts-corefile-fileio-depr--f.md#mkdir-3) | Creates a directory. This API uses an asynchronous callback to return the result. |
| [mkdirSync](arkts-corefile-fileio-depr--f.md#mkdirsync) | Creates a directory. This API returns the result synchronously. |
| [mkdtemp](arkts-corefile-fileio-depr--f.md#mkdtemp-1) | Creates a temporary directory. This API uses a promise to return the result. |
| [mkdtemp](arkts-corefile-fileio-depr--f.md#mkdtemp-2) | Creates a temporary directory. This API uses an asynchronous callback to return the result. |
| [mkdtempSync](arkts-corefile-fileio-depr--f.md#mkdtempsync) | Creates a temporary directory. This API returns the result synchronously. |
| [open](arkts-corefile-fileio-depr--f.md#open-1) | Opens a file. This API uses a promise to return the result. |
| [open](arkts-corefile-fileio-depr--f.md#open-2) | Opens a file. This API uses an asynchronous callback to return the result. |
| [open](arkts-corefile-fileio-depr--f.md#open-3) | Opens a file. This API uses an asynchronous callback to return the result. |
| [open](arkts-corefile-fileio-depr--f.md#open-4) | Opens a file. This API uses an asynchronous callback to return the result. |
| [opendir](arkts-corefile-fileio-depr--f.md#opendir-1) | Opens a directory. This API uses a promise to return the result. |
| [opendir](arkts-corefile-fileio-depr--f.md#opendir-2) | Opens a file directory. This API uses an asynchronous callback to return the result. |
| [opendirSync](arkts-corefile-fileio-depr--f.md#opendirsync) | Opens a directory. This API returns the result synchronously. |
| [openSync](arkts-corefile-fileio-depr--f.md#opensync) | Opens a file. This API returns the result synchronously. |
| [read](arkts-corefile-fileio-depr--f.md#read-1) | Reads data from a file. This API uses a promise to return the result. |
| [read](arkts-corefile-fileio-depr--f.md#read-2) | Reads data from a file. This API uses an asynchronous callback to return the result. |
| [read](arkts-corefile-fileio-depr--f.md#read-3) | Reads data from a file. This API uses an asynchronous callback to return the result. |
| [readSync](arkts-corefile-fileio-depr--f.md#readsync-1) | Reads data from a file. This API returns the result synchronously. |
| [readText](arkts-corefile-fileio-depr--f.md#readtext-1) | Reads the text content of a file. This API uses a promise to return the result. |
| [readText](arkts-corefile-fileio-depr--f.md#readtext-2) | Reads the text content of a file. This API uses an asynchronous callback to return the result. |
| [readTextSync](arkts-corefile-fileio-depr--f.md#readtextsync) | Reads the text content of a file. This API returns the result synchronously. |
| [rename](arkts-corefile-fileio-depr--f.md#rename-1) | Renames a file. This API uses a promise to return the result. |
| [rename](arkts-corefile-fileio-depr--f.md#rename-2) | Renames a file. This API uses an asynchronous callback to return the result. |
| [renameSync](arkts-corefile-fileio-depr--f.md#renamesync) | Renames a file. This API returns the result synchronously. |
| [rmdir](arkts-corefile-fileio-depr--f.md#rmdir-1) | Removes a directory. This API uses a promise to return the result. |
| [rmdir](arkts-corefile-fileio-depr--f.md#rmdir-2) | Removes a directory. This API uses an asynchronous callback to return the result. |
| [rmdirSync](arkts-corefile-fileio-depr--f.md#rmdirsync) | Removes a directory. This API returns the result synchronously. |
| [stat](arkts-corefile-fileio-depr--f.md#stat-1) | Obtains file information. This API uses a promise to return the result. |
| [stat](arkts-corefile-fileio-depr--f.md#stat-2) | Obtains file information. This API uses an asynchronous callback to return the result. |
| [statSync](arkts-corefile-fileio-depr--f.md#statsync) | Obtains file information. This API returns the result synchronously. |
| [symlink](arkts-corefile-fileio-depr--f.md#symlink-1) | Creates a symbolic link based on the file path. This API uses a promise to return the result. |
| [symlink](arkts-corefile-fileio-depr--f.md#symlink-2) | Creates a symbolic link based on the file path. This API uses an asynchronous callback to return the result. |
| [symlinkSync](arkts-corefile-fileio-depr--f.md#symlinksync) | Creates a symbolic link based on the file path. This API returns the result synchronously. |
| [truncate](arkts-corefile-fileio-depr--f.md#truncate-1) | Truncates a file based on the file path. This API uses a promise to return the result. |
| [truncate](arkts-corefile-fileio-depr--f.md#truncate-2) | Truncates a file based on the file path. This API uses an asynchronous callback to return the result. |
| [truncate](arkts-corefile-fileio-depr--f.md#truncate-3) | Truncates a file based on the file path. This API uses an asynchronous callback to return the result. |
| [truncateSync](arkts-corefile-fileio-depr--f.md#truncatesync) | Truncates a file based on the file path. This API returns the result synchronously. |
| [unlink](arkts-corefile-fileio-depr--f.md#unlink-1) | Removes a file. This API uses a promise to return the result. |
| [unlink](arkts-corefile-fileio-depr--f.md#unlink-2) | Removes a file. This API uses an asynchronous callback to return the result. |
| [unlinkSync](arkts-corefile-fileio-depr--f.md#unlinksync) | Removes a file. This API returns the result synchronously. |
| [write](arkts-corefile-fileio-depr--f.md#write-1) | Writes data into a file. This API uses a promise to return the result. |
| [write](arkts-corefile-fileio-depr--f.md#write-2) | Writes data to a file. This API uses an asynchronous callback to return the result. |
| [write](arkts-corefile-fileio-depr--f.md#write-3) | Writes data to a file. This API uses an asynchronous callback to return the result. |
| [writeSync](arkts-corefile-fileio-depr--f.md#writesync-1) | Writes data to a file. This API returns the result synchronously. |

### Interfaces

| Name | Description |
| --- | --- |
| [Dir](arkts-corefile-fileio-depr-dir-i.md) | Manages directories. Before calling a method of the **Dir** class, use the **opendir()** method synchronously or asynchronously to create a **Dir** instance. |
| [Dirent](arkts-corefile-fileio-depr-dirent-i.md) | Provides information about files and directories. Before calling an API of the **Dirent** class, use [dir.read()](arkts-corefile-fileio-depr--f.md#read) synchronously or asynchronously to create a **Dirent** instance. |
| [ReadOut](arkts-corefile-fileio-depr-readout-i.md) | Obtains the file read result. This class applies only to the **read()** method. |
| [Stat](arkts-corefile-fileio-depr-stat-i.md) | Provides detailed file information. Before calling a method of the **Stat** class, use the [stat()](arkts-corefile-fileio-depr--f.md#stat) method synchronously or asynchronously to create a **Stat** instance. |
| [Stream](arkts-corefile-fileio-depr-stream-i.md) | Provides a stream for file operations. Before calling any API of the **Stream** class, use **createStream()** to create a **Stream** instance synchronously or asynchronously. |
| [Watcher](arkts-corefile-fileio-depr-watcher-i.md) | Listens for file change. You can call the **Watcher.stop()** method synchronously or asynchronously to stop the listening. |
