# fileIo

FileIO

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-declare namespace fileIo--><!--Device-unnamed-declare namespace fileIo-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## Summary

### Namespaces

| Name | Description |
| --- | --- |
| [OpenMode](arkts-corefile-fileio-openmode-n.md) | Enumerates the constants of the **mode** parameter used in **open()**, which specifies the file opening mode, such as **READ_ONLY**, **WRITE_ONLY**, **READ_WRITE**, or **CREATE**. |

### Functions

| Name | Description |
| --- | --- |
| [access](arkts-corefile-fileio-access-f.md#access) | Checks whether a file or directory exists or has the operation permission. This API uses a promise to return the result.  If the read, write, or read and write permission verification fails, the error code 13900012(Permission denied) will be thrown. |
| [access](arkts-corefile-fileio-access-f.md#access-1) | Checks whether a file or directory exists. This API uses an asynchronous callback to return the result. |
| [access](arkts-corefile-fileio-access-f.md#access-2) | Checks whether the file or directory is on the local host or verifies the operation permission. This API uses a promise to return the result.  If the read, write, or read and write permission verification fails, the error code 13900012(Permission denied) will be thrown. |
| [accessSync](arkts-corefile-fileio-accesssync-f.md#accesssync) | Checks whether a file or directory exists or has the operation permission. This API returns the result synchronously.  If the read, write, or read and write permission verification fails, the error code 13900012(Permission denied) will be thrown. |
| [accessSync](arkts-corefile-fileio-accesssync-f.md#accesssync-1) | Checks whether a file or directory is stored locally or has the operation permission. This API returns the result synchronously.  If the read, write, or read and write permission verification fails, the error code 13900012(Permission denied) will be thrown. |
| [close](arkts-corefile-fileio-close-f.md#close) | Closes a file or directory. After the file or directory is closed, the FD becomes invalid and cannot be used for read /write operations. This API uses a promise to return the result. |
| [close](arkts-corefile-fileio-close-f.md#close-1) | Closes a file or directory. After the file or directory is closed, the FD becomes invalid and cannot be used for read /write operations. This API uses an asynchronous callback to return the result. |
| [closeSync](arkts-corefile-fileio-closesync-f.md#closesync) | Closes a file or directory synchronously. After the file or directory is closed, the FD becomes invalid and cannot be used for read/write operations. |
| [copy](arkts-corefile-fileio-copy-f.md#copy) | Copies a file or directory. This API uses a promise to return the result.  File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be the URI of the file or directory.  A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500. |
| [copy](arkts-corefile-fileio-copy-f.md#copy-1) | Copies a file or directory. This API uses an asynchronous callback to return the result.  File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be the URI of the file or directory.  A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500. |
| [copy](arkts-corefile-fileio-copy-f.md#copy-2) | Copies a file or directory. This API uses an asynchronous callback to return the result.  File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be the URI of the file or directory.  A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500. |
| [copyDir](arkts-corefile-fileio-copydir-f.md#copydir) | Copies the source directory and its content to the destination path. You can set the conflict handling mode. This API uses a promise to return the result. |
| [copyDir](arkts-corefile-fileio-copydir-f.md#copydir-1) | Copies the source directory and its content to the destination path. This API uses an asynchronous callback to return the result.  An exception will be thrown if the destination directory contains a directory with the same name as the source directory and there are files with the same name in the conflicting directory. All the non-conflicting files in the source directory will be copied to the destination directory, and the non-conflicting files in the destination directory will be retained. |
| [copyDirWithConflictFiles](arkts-corefile-fileio-copydirwithconflictfiles-f.md#copydirwithconflictfiles) | Copies the source directory to the destination path. This API uses an asynchronous callback to return the result.  An exception will be thrown if the destination directory contains a directory with the same name as the source directory and there are files with the same name in the conflicting directory. All the non-conflicting files in the source directory will be copied to the destination directory, and the non-conflicting files in the destination directory will be retained. The data attribute in the error returned provides information about the conflicting files in the Array&lt;ConflictFiles&gt; format. |
| [copyDir](arkts-corefile-fileio-copydir-f.md#copydir-2) | Copies the source directory and its content to the destination path. You can set the conflict handling mode. This API uses an asynchronous callback to return the result. |
| [copyDirWithConflictFiles](arkts-corefile-fileio-copydirwithconflictfiles-f.md#copydirwithconflictfiles-1) | Copies the source directory to the destination directory. You can set the copy mode.This API uses an asynchronous callback to return the result. |
| [copyDirSync](arkts-corefile-fileio-copydirsync-f.md#copydirsync) | Copies the source directory to the destination path. This API returns the result synchronously. |
| [copyFile](arkts-corefile-fileio-copyfile-f.md#copyfile) | Copies a file. This API uses a promise to return the result. |
| [copyFile](arkts-corefile-fileio-copyfile-f.md#copyfile-1) | Copies a file. This API overwrites the file with the same name in the destination directory and truncates the part that is not overwritten. This API uses an asynchronous callback to return the result. |
| [copyFile](arkts-corefile-fileio-copyfile-f.md#copyfile-2) | Copies a file with the specified mode. This API uses an asynchronous callback to return the result. |
| [copyFileSync](arkts-corefile-fileio-copyfilesync-f.md#copyfilesync) | Copies a file. This API returns the result synchronously. |
| [createStream](arkts-corefile-fileio-createstream-f.md#createstream) | Creates a stream based on a file path. This API uses a promise to return the result. To close the stream, use  **close()** of [Stream](arkts-corefile-fileio-stream-i.md). |
| [createStream](arkts-corefile-fileio-createstream-f.md#createstream-1) | Creates a stream based on a file path. To close the stream, use **close()** of [Stream](arkts-corefile-fileio-stream-i.md). This API uses an asynchronous callback to return the result. |
| [createStreamSync](arkts-corefile-fileio-createstreamsync-f.md#createstreamsync) | Creates a stream based on a file path. This API returns the result synchronously. To close the stream, use  **close()** of [Stream](arkts-corefile-fileio-stream-i.md). |
| [createRandomAccessFile](arkts-corefile-fileio-createrandomaccessfile-f.md#createrandomaccessfile) | Creates a **RandomAccessFile** instance based on a file path or file object. This API uses a promise to return the result. |
| [createRandomAccessFile](arkts-corefile-fileio-createrandomaccessfile-f.md#createrandomaccessfile-1) | Creates a **RandomAccessFile** instance in read-only mode based on a file path or file object. This API uses an asynchronous callback to return the result. |
| [createRandomAccessFile](arkts-corefile-fileio-createrandomaccessfile-f.md#createrandomaccessfile-2) | Creates a **RandomAccessFile** instance based on a file path or file object. This API uses an asynchronous callback to return the result. |
| [createRandomAccessFileSync](arkts-corefile-fileio-createrandomaccessfilesync-f.md#createrandomaccessfilesync) | Creates a **RandomAccessFile** instance based on a file path or file object. |
| [createReadStream](arkts-corefile-fileio-createreadstream-f.md#createreadstream) | Creates a readable stream. This API returns the result synchronously. |
| [createWriteStream](arkts-corefile-fileio-createwritestream-f.md#createwritestream) | Creates a writeable stream. This API returns the result synchronously. |
| [createWatcher](arkts-corefile-fileio-createwatcher-f.md#createwatcher) | Creates a **Watcher** object to listen for file or directory changes such as creating, deleting, and modifying. |
| [dup](arkts-corefile-fileio-dup-f.md#dup) | Duplicates the file descriptor and returns the corresponding **File** object. |
| [fdatasync](arkts-corefile-fileio-fdatasync-f.md#fdatasync) | Synchronizes data in a file. This API uses a promise to return the result. |
| [fdatasync](arkts-corefile-fileio-fdatasync-f.md#fdatasync-1) | Synchronizes data in a file. This API uses an asynchronous callback to return the result. |
| [fdatasyncSync](arkts-corefile-fileio-fdatasyncsync-f.md#fdatasyncsync) | Synchronizes the data of a file. This API returns the result synchronously. |
| [fdopenStream](arkts-corefile-fileio-fdopenstream-f.md#fdopenstream) | Opens a file stream based on the file descriptor. This API uses a promise to return the result.To close the stream, use **close()** of [Stream](arkts-corefile-fileio-stream-i.md). |
| [fdopenStream](arkts-corefile-fileio-fdopenstream-f.md#fdopenstream-1) | Opens a stream based on the file descriptor. To close the stream, use **close()** of [Stream](arkts-corefile-fileio-stream-i.md).This API uses an asynchronous callback to return the result. |
| [fdopenStreamSync](arkts-corefile-fileio-fdopenstreamsync-f.md#fdopenstreamsync) | Opens a stream based on an FD. This API returns the result synchronously. To close the stream, use **close()** of  [Stream](arkts-corefile-fileio-stream-i.md). |
| [fsync](arkts-corefile-fileio-fsync-f.md#fsync) | Synchronizes the cached data of a file to storage. This API uses a promise to return the result. |
| [fsync](arkts-corefile-fileio-fsync-f.md#fsync-1) | Synchronizes the cached data of a file to storage. This API uses an asynchronous callback to return the result. |
| [fsyncSync](arkts-corefile-fileio-fsyncsync-f.md#fsyncsync) | Synchronizes the cached data of a file to storage. This API returns the result synchronously. |
| [listFile](arkts-corefile-fileio-listfile-f.md#listfile) | Lists the names of all files and directories in the current directory. A file name array is returned, which can be filtered by file name or file name extension. This API uses a promise to return the result.  This API supports recursively listing the relative paths of all files by setting **recursion** in  **ListFileOptions**. The relative path starts with a slash (/). |
| [listFile](arkts-corefile-fileio-listfile-f.md#listfile-1) | Lists the names of all files and directories in the current path. A file name array is returned. This API uses an asynchronous callback to return the result. |
| [listFile](arkts-corefile-fileio-listfile-f.md#listfile-2) | Lists the names of all files and directories in the current directory. A file name array is returned, which can be filtered by file name or file name extension. This API uses an asynchronous callback to return the result.  This API supports recursively listing the relative paths of all files by setting **recursion** in  **ListFileOptions**. The relative path starts with a slash (/). |
| [listFileSync](arkts-corefile-fileio-listfilesync-f.md#listfilesync) | Lists the names of all files and directories in the current directory synchronously. A file name array is returned,which can be filtered by file name or file name extension.  This API supports recursively listing the relative paths of all files by setting **recursion** in  **ListFileOptions**. The relative path starts with a slash (/). |
| [listFileExt](arkts-corefile-fileio-listfileext-f.md#listfileext) | Lists all files in a directory. This API supports recursive listing of files and file filtering. This API uses a promise to return the result.  You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The relative path starts with a slash (/). |
| [listFileExtSync](arkts-corefile-fileio-listfileextsync-f.md#listfileextsync) | Lists all files in a directory. This API supports recursive listing of files and file filtering and returns the result synchronously.  You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The relative path starts with a slash (/). |
| [lseek](arkts-corefile-fileio-lseek-f.md#lseek) | Adjusts the position of the file offset pointer. |
| [lstat](arkts-corefile-fileio-lstat-f.md#lstat) | Obtains information about a symbolic link that is used to refer to a file or directory. The attributes of the symbolic link are returned, instead of the attributes of the target file. This API uses a promise to return the result. |
| [lstat](arkts-corefile-fileio-lstat-f.md#lstat-1) | Obtains information about a symbolic link that is used to refer to a file or directory. The attributes of the symbolic link are returned, instead of the attributes of the target file. This API uses an asynchronous callback to return the result. |
| [lstatSync](arkts-corefile-fileio-lstatsync-f.md#lstatsync) | Obtains information about a symbolic link that is used to refer to a file or directory synchronously. The attributes of the symbolic link are returned, instead of the attributes of the target file. |
| [mkdir](arkts-corefile-fileio-mkdir-f.md#mkdir) | Creates a single-level directory. If the parent directory does not exist, an error is reported. This API uses a promise to return the result. |
| [mkdir](arkts-corefile-fileio-mkdir-f.md#mkdir-1) | Creates a directory. This API uses a promise to return the result. The value **true** means to create a directory recursively. |
| [mkdir](arkts-corefile-fileio-mkdir-f.md#mkdir-2) | Creates a single-level directory. If the parent directory does not exist, an error is reported. This API uses an asynchronous callback to return the result. |
| [mkdir](arkts-corefile-fileio-mkdir-f.md#mkdir-3) | Creates a directory. If **recursion** is set to **true**, a directory is created recursively. This API uses an asynchronous callback to return the result. |
| [mkdirSync](arkts-corefile-fileio-mkdirsync-f.md#mkdirsync) | Creates a single-level directory synchronously. If the parent directory does not exist, an error is reported. |
| [mkdirSync](arkts-corefile-fileio-mkdirsync-f.md#mkdirsync-1) | Creates a directory. This API returns the result synchronously. The value **true** means to create a directory recursively. |
| [mkdtemp](arkts-corefile-fileio-mkdtemp-f.md#mkdtemp) | Create a temporary directory. This API uses a promise to return the result. |
| [mkdtemp](arkts-corefile-fileio-mkdtemp-f.md#mkdtemp-1) | Create a temporary directory. This API uses an asynchronous callback to return the result. |
| [mkdtempSync](arkts-corefile-fileio-mkdtempsync-f.md#mkdtempsync) | Creates a temporary directory. This API returns the result synchronously. |
| [mmap](arkts-corefile-fileio-mmap-f.md#mmap) | Creates a file mapping object based on a file descriptor or file object for efficient read and write access to files. This API uses a promise to return the result.  > **NOTE：** >  > 1. Memory mapping can be performed only for regular files. Non-regular files, such as > pipeline, socket, and device > files, are not supported. You can use [statSync()](arkts-corefile-fileio-statsync-f.md#statsync) to obtain file attributes and then call > [Stat.isFile()](arkts-corefile-fileio-stat-i.md#isfile) to check whether the file is a regular file. >  > 2. If the mapping range exceeds the raw file size and the write permission is granted for the file, the mapping > file size will be automatically expanded. >  > 3. For files from external storage or network files, the establishment of mappings and access > to the mapped memory > are not guaranteed due to differences in the underlying file system. This may cause the application to terminate > unexpectedly. You are advised to use other file access APIs such as [read](arkts-corefile-fileio-read-f.md#read), > [write](arkts-corefile-fileio-write-f.md#write), or [Stream](arkts-corefile-fileio-stream-i.md) in this scenario. |
| [mmapSync](arkts-corefile-fileio-mmapsync-f.md#mmapsync) | Creates a file mapping object synchronously based on a file descriptor or file object for efficient read and write access to files.  > **NOTE：** >  > 1. Memory mapping can be performed only for regular files. Non-regular files, such as > pipeline, socket, and device > files, are not supported. You can use [statSync()](arkts-corefile-fileio-statsync-f.md#statsync) to obtain file attributes and then call > [Stat.isFile()](arkts-corefile-fileio-stat-i.md#isfile) to check whether the file is a regular file. >  > 2. If the mapping range exceeds the raw file size and the write permission is granted for the file, the mapping > file size will be automatically expanded. >  > 3. For files from external storage or network files, the establishment of mappings and access > to the mapped memory > are not guaranteed due to differences in the underlying file system. This may cause the application to terminate > unexpectedly. You are advised to use other file access APIs such as [read](arkts-corefile-fileio-read-f.md#read), > [write](arkts-corefile-fileio-write-f.md#write), or [Stream](arkts-corefile-fileio-stream-i.md) in this scenario. |
| [moveDir](arkts-corefile-fileio-movedir-f.md#movedir) | Moves the source directory and its content to the destination path. This API uses a promise to return the result.  > **NOTE：** >  > This API is not supported in a distributed directory. |
| [moveDir](arkts-corefile-fileio-movedir-f.md#movedir-1) | Moves the source directory and its content to the destination path. This API uses an asynchronous callback to return the result.  An exception will be thrown if a directory conflict occurs, that is, the destination directory contains a directory with the same name as the source directory.  > **NOTE：** >  > This API is not supported in a distributed directory. |
| [moveDirWithConflictFiles](arkts-corefile-fileio-movedirwithconflictfiles-f.md#movedirwithconflictfiles) | Moves the source directory and its content to the destination path. This API uses an asynchronous callback to return the result.  An exception will be thrown if a directory conflict occurs, that is, the destination directory contains a directory with the same name as the source directory.  > **NOTE：** >  > This API is not supported in a distributed directory. |
| [moveDir](arkts-corefile-fileio-movedir-f.md#movedir-2) | Moves the source directory and its content to the destination path. You can set the conflict handling mode. This API uses an asynchronous callback to return the result.  > **NOTE：** >  > This API is not supported in a distributed directory. |
| [moveDirWithConflictFiles](arkts-corefile-fileio-movedirwithconflictfiles-f.md#movedirwithconflictfiles-1) | Moves the source directory to the destination directory. You can set the move mode.This API uses an asynchronous callback to return the result. |
| [moveDirSync](arkts-corefile-fileio-movedirsync-f.md#movedirsync) | Moves the source directory and its content to the destination directory. This API returns the result synchronously.  > **NOTE：** >  > This API is not supported in a distributed directory. |
| [moveFile](arkts-corefile-fileio-movefile-f.md#movefile) | Moves a file to the target path. You can set the conflict handling mode. This API uses a promise to return the result.  > **NOTE：** >  > This API is not supported in a distributed directory. |
| [moveFile](arkts-corefile-fileio-movefile-f.md#movefile-1) | Moves a file and forcibly overwrites the file with the same name in the destination directory. This API uses an asynchronous callback to return the result.  > **NOTE：** >  > This API is not supported in a distributed directory. |
| [moveFile](arkts-corefile-fileio-movefile-f.md#movefile-2) | Moves a file to the target path. You can set the conflict handling mode. This API uses an asynchronous callback to return the result.  > **NOTE：** >  > This API is not supported in a distributed directory. |
| [moveFileSync](arkts-corefile-fileio-movefilesync-f.md#movefilesync) | Moves a file to the destination path. This API returns the result synchronously.  > **NOTE：** >  > This API is not supported in a distributed directory. |
| [open](arkts-corefile-fileio-open-f.md#open) | Opens a file or directory. This API supports the use of a URI. This API uses a promise to return the result. |
| [open](arkts-corefile-fileio-open-f.md#open-1) | Opens a file or directory. This API supports the use of a URI. This API uses an asynchronous callback to return the result. |
| [open](arkts-corefile-fileio-open-f.md#open-2) | Opens a file or directory with the specified mode. This API uses an asynchronous callback to return the result.  This API supports the use of a URI. |
| [openSync](arkts-corefile-fileio-opensync-f.md#opensync) | Opens a file or directory. This API returns the result synchronously. This API supports the use of a URI. |
| [read](arkts-corefile-fileio-read-f.md#read) | Reads data from a file and returns the number of bytes read. This API uses a promise to return the result. |
| [read](arkts-corefile-fileio-read-f.md#read-1) | Reads data from a file and returns the number of bytes read. This API uses an asynchronous callback to return the result. |
| [read](arkts-corefile-fileio-read-f.md#read-2) | Reads data from a file. Read options (such as the offset position and length of the data read)can be configured. The number of bytes read is returned. This API uses an asynchronous callback to return the result. |
| [readSync](arkts-corefile-fileio-readsync-f.md#readsync) | Reads data from a file synchronously and returns the number of bytes read. |
| [readLines](arkts-corefile-fileio-readlines-f.md#readlines) | Reads a file text line by line. Only the files in UTF-8 format are supported. This API uses a promise to return the result. |
| [readLines](arkts-corefile-fileio-readlines-f.md#readlines-1) | Reads a file text line by line. Only the files in UTF-8 format are supported. This API uses an asynchronous callback to return the result. |
| [readLines](arkts-corefile-fileio-readlines-f.md#readlines-2) | Reads a file text line by line. Read options can be configured. Only the files in UTF-8 format are supported. This API uses an asynchronous callback to return the result. |
| [readLinesSync](arkts-corefile-fileio-readlinessync-f.md#readlinessync) | Reads a file text line by line synchronously. Only the files in UTF-8 format are supported. |
| [readText](arkts-corefile-fileio-readtext-f.md#readtext) | Reads the text content of a file synchronously. This API returns the result synchronously. This API uses a promise to return the result. |
| [readText](arkts-corefile-fileio-readtext-f.md#readtext-1) | Reads the text of a file. This API uses an asynchronous callback to return the result. |
| [readText](arkts-corefile-fileio-readtext-f.md#readtext-2) | Reads the text of a file. Read options can be configured. This API uses an asynchronous callback to return the result. |
| [readTextSync](arkts-corefile-fileio-readtextsync-f.md#readtextsync) | Reads the text content of a file. This API returns the result synchronously. |
| [rename](arkts-corefile-fileio-rename-f.md#rename) | Renames a file or directory. This API uses a promise to return the result.  > **NOTE：** >  > This API is not supported in a distributed directory. |
| [rename](arkts-corefile-fileio-rename-f.md#rename-1) | Renames a file or directory. This API uses an asynchronous callback to return the result.  > **NOTE：** >  > This API is not supported in a distributed directory. |
| [renameSync](arkts-corefile-fileio-renamesync-f.md#renamesync) | Renames a file or directory. This API returns the result synchronously.  > **NOTE：** >  > This API is not supported in a distributed directory. |
| [rmdir](arkts-corefile-fileio-rmdir-f.md#rmdir) | Deletes a directory and all its subdirectories and files. This API uses a promise to return the result.  > **NOTE：** >  > This API can be used to remove a single file. However, you are advised to use **unlink()** instead. |
| [rmdir](arkts-corefile-fileio-rmdir-f.md#rmdir-1) | Deletes a directory and all its subdirectories and files. This API uses an asynchronous callback to return the result.  > **NOTE：** >  > This API can be used to remove a single file. However, you are advised to use **unlink()** instead. |
| [rmdirSync](arkts-corefile-fileio-rmdirsync-f.md#rmdirsync) | Removes a directory and all its subdirectories and files synchronously.  > **NOTE：** >  > This API can be used to remove a single file. However, you are advised to use **unlinkSync** instead. |
| [stat](arkts-corefile-fileio-stat-f.md#stat) | Obtains detailed attributes of a file or directory. The returned **Stat** object contains attributes such as the file size, permission mode, access time, and modification time. This API uses a promise to return the result. |
| [stat](arkts-corefile-fileio-stat-f.md#stat-1) | Obtains detailed attributes of a file or directory. The returned **Stat** object contains attributes such as the file size, permission mode, access time, and modification time. This API uses an asynchronous callback to return the result. |
| [statSync](arkts-corefile-fileio-statsync-f.md#statsync) | Obtains detailed attributes of a file or directory synchronously. The returned **Stat** object contains attributes such as the file size, permission mode, access time, and modification time. |
| [symlink](arkts-corefile-fileio-symlink-f.md#symlink) | Creates a symbolic link based on a file path. This API uses a promise to return the result. |
| [symlink](arkts-corefile-fileio-symlink-f.md#symlink-1) | Creates a symbolic link based on a file path. This API uses an asynchronous callback to return the result.  > **NOTE：** >  > Since API version 11, this API cannot be used by third-party applications. |
| [symlinkSync](arkts-corefile-fileio-symlinksync-f.md#symlinksync) | Creates a symbolic link based on the file path. This API returns the result synchronously.  > **NOTE：** >  > Since API version 11, this API cannot be used by third-party applications. |
| [truncate](arkts-corefile-fileio-truncate-f.md#truncate) | Truncates a file to the specified length. Excess content will be deleted. This API uses a promise to return the result. |
| [truncate](arkts-corefile-fileio-truncate-f.md#truncate-1) | Truncates a file and deletes its content. This API uses an asynchronous callback to return the result. |
| [truncate](arkts-corefile-fileio-truncate-f.md#truncate-2) | Truncates a file to the specified length. Excess content will be deleted. This API uses an asynchronous callback to return the result. |
| [truncateSync](arkts-corefile-fileio-truncatesync-f.md#truncatesync) | Truncates a file to the specified length synchronously. Excess content will be deleted. |
| [unlink](arkts-corefile-fileio-unlink-f.md#unlink) | Deletes a single file. This method cannot be used to delete a directory. This API uses a promise to return the result. |
| [unlink](arkts-corefile-fileio-unlink-f.md#unlink-1) | Deletes a single file. This method cannot be used to delete a directory. This API uses an asynchronous callback to return the result. |
| [unlinkSync](arkts-corefile-fileio-unlinksync-f.md#unlinksync) | Deletes a single file synchronously. This method cannot be used to delete a directory. |
| [utimes](arkts-corefile-fileio-utimes-f.md#utimes) | Changes the time when the file was last modified. |
| [write](arkts-corefile-fileio-write-f.md#write) | Writes data to a file and returns the number of bytes written. This API uses a promise to return the result. |
| [write](arkts-corefile-fileio-write-f.md#write-1) | Writes data to a file and returns the number of bytes written. This API uses an asynchronous callback to return the result. |
| [write](arkts-corefile-fileio-write-f.md#write-2) | Writes data to a file. Write options (such as the offset position and length of the data written)can be configured.The number of bytes written is returned. This API uses an asynchronous callback to return the result. |
| [writeSync](arkts-corefile-fileio-writesync-f.md#writesync) | Writes data to a file synchronously and returns the number of bytes written. |
| [connectDfs](arkts-corefile-fileio-connectdfs-f.md#connectdfs) | Triggers connection. If the peer device is abnormal, [onStatus](arkts-corefile-fileio-dfslisteners-i.md#onstatus)in DfsListeners will be called to notify the application. |
| [disconnectDfs](arkts-corefile-fileio-disconnectdfs-f.md#disconnectdfs) | Triggers disconnection. |
| [setxattr](arkts-corefile-fileio-setxattr-f.md#setxattr) | Sets an extended attribute of a file or directory. This API uses a promise to return the result. |
| [setxattrSync](arkts-corefile-fileio-setxattrsync-f.md#setxattrsync) | Sets an extended attribute of a file or directory. |
| [getxattr](arkts-corefile-fileio-getxattr-f.md#getxattr) | Obtains an extended attribute of a file or directory. This API uses a promise to return the result. |
| [getxattrSync](arkts-corefile-fileio-getxattrsync-f.md#getxattrsync) | Obtains an extended attribute of a file. This API returns the result synchronously. |

### Classes

| Name | Description |
| --- | --- |
| [TaskSignal](arkts-corefile-fileio-tasksignal-c.md) | Provides APIs for interrupting a copy task. |
| [ReadStream](arkts-corefile-fileio-readstream-c.md) | Defines a readable stream. You need to use [fileIo.createReadStream](arkts-corefile-fileio-createreadstream-f.md#createreadstream) to create a  **ReadStream** instance, which is inherited from [stream.Readable](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md/arkts-arkts-stream-readable-c.md).  The data obtained by **ReadStream** is a decoded string. Currently, only the UTF-8 format is supported. |
| [WriteStream](arkts-corefile-fileio-writestream-c.md) | Defines a writeable stream. You need to use [fileIo.createWriteStream](arkts-corefile-fileio-createwritestream-f.md#createwritestream) to create a  **WriteStream** instance, which is inherited from [stream.Writable](../../apis-arkts/arkts-apis/arkts-arkts-stream-writable-c.md/arkts-arkts-stream-writable-c.md). |
| [AtomicFile](arkts-corefile-fileio-atomicfile-c.md) | AtomicFile is a class used to perform atomic read and write operations on files.A temporary file is written and renamed to the original file location, which ensures file integrity.If the write operation fails, the temporary file is deleted without modifying the original file content.You can call finishWrite() or failWrite() to write or roll back file content. |

### Interfaces

| Name | Description |
| --- | --- |
| [DfsListeners](arkts-corefile-fileio-dfslisteners-i.md) | The listeners of Distributed File System. |
| [Progress](arkts-corefile-fileio-progress-i.md) | Defines the copy progress information. |
| [CopyOptions](arkts-corefile-fileio-copyoptions-i.md) | Defines the callback for listening for the copy progress. |
| [File](arkts-corefile-fileio-file-i.md) | Represents a **File** object opened by **open()**. It contains the FD and provides capabilities such as locking a file and obtaining the parent directory. |
| [FileMapping](arkts-corefile-fileio-filemapping-i.md) | Defines a file mapping object. Before calling the **FileMapping** method,construct a **FileMapping** instance using [mmap()](arkts-corefile-fileio-mmap-f.md#mmap) or [mmapSync()](arkts-corefile-fileio-mmapsync-f.md#mmapsync). |
| [RandomAccessFile](arkts-corefile-fileio-randomaccessfile-i.md) | Provides APIs for randomly reading and writing a stream based on offset pointers. Before invoking any API of  **RandomAccessFile**, you need to use **createRandomAccessFile()** to create a **RandomAccessFile** instance synchronously or asynchronously. |
| [Stat](arkts-corefile-fileio-stat-i.md) | Obtains detailed information of a file, including attributes such as the file size, permission mode,access time, and modification time. Before calling an API of the **Stat** class,use [stat()](arkts-corefile-fileio-stat-f.md#stat) to create a **Stat** instance. |
| [Stream](arkts-corefile-fileio-stream-i.md) | Provides APIs for stream operations, such as reading and writing data streams of files. After using an API of the  **Stream** class, you need to call **close** to close the file stream. Before calling an API of the   **Stream** class, you need to create a **Stream** instance by using   [fileIo.createStream](arkts-corefile-fileio-createstream-f.md#createstream) or [fileIo.fdopenStream](arkts-corefile-fileio-fdopenstream-f.md#fdopenstream). |
| [Watcher](arkts-corefile-fileio-watcher-i.md) | Provides APIs for observing the changes of files or directories.Before using the APIs of Watcher, call createWatcher() to create a Watcher object. |
| [ReaderIterator](arkts-corefile-fileio-readeriterator-i.md) | Provides a **ReaderIterator** object. Before calling APIs of **ReaderIterator**, you need to use **readLines()** to create a **ReaderIterator** instance. |

### Enums

| Name | Description |
| --- | --- |
| [MappingMode](arkts-corefile-fileio-mappingmode-e.md) | Enumerates file memory mapping modes. |
| [WhenceType](arkts-corefile-fileio-whencetype-e.md) | Enumerates the types of the relative offset position used in **lseek()**. |
| [LocationType](arkts-corefile-fileio-locationtype-e.md) | Enumerates the file locations. |
| [AccessModeType](arkts-corefile-fileio-accessmodetype-e.md) | Enumerates the access modes to verify. If this parameter is left blank, the system checks whether the file exists. |
| [AccessFlagType](arkts-corefile-fileio-accessflagtype-e.md) | Enumerates the locations of the file to verify. |

### Types

| Name | Description |
| --- | --- |
| [DfsListenerCallback](arkts-corefile-fileio-dfslistenercallback-t.md) | DfsListener Callback function. |
| [ProgressListener](arkts-corefile-fileio-progresslistener-t.md) | Listener used to observe the copy progress. |

