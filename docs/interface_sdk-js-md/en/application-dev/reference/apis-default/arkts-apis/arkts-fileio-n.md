# fileIo

FileIO

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace fileIo--><!--Device-unnamed-declare namespace fileIo-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
```

## Summary

### Namespaces

| Name | Description |
| --- | --- |
| [OpenMode](arkts-fileio-openmode-n.md) | Enumerates the constants of the **mode** parameter used in **open()**, which specifies the file opening mode, such as **READ_ONLY**, **WRITE_ONLY**, **READ_WRITE**, or **CREATE**. |

### Functions

| Name | Description |
| --- | --- |
| [access](arkts-fileio-access-f.md) | Checks whether a file or directory exists or has the operation permission. This API uses a promise to return the result.If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown. |
| [access](arkts-fileio-access-f.md) | Checks whether a file or directory exists. This API uses an asynchronous callback to return the result. |
| [access](arkts-fileio-access-f.md) | Checks whether the file or directory is on the local host or verifies the operation permission. This API uses a promise to return the result.If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown. |
| [accessSync](arkts-fileio-accesssync-f.md) | Checks whether a file or directory exists or has the operation permission. This API returns the result synchronously.If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown. |
| [accessSync](arkts-fileio-accesssync-f.md) | Checks whether a file or directory is stored locally or has the operation permission. This API returns the result synchronously.If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown. |
| [close](arkts-fileio-close-f.md) | Closes a file or directory. After the file or directory is closed, the FD becomes invalid and cannot be used for read /write operations. This API uses a promise to return the result. |
| [close](arkts-fileio-close-f.md) | Closes a file or directory. After the file or directory is closed, the FD becomes invalid and cannot be used for read /write operations. This API uses an asynchronous callback to return the result. |
| [closeSync](arkts-fileio-closesync-f.md) | Closes a file or directory synchronously. After the file or directory is closed, the FD becomes invalid and cannot be used for read/write operations. |
| [copy](arkts-fileio-copy-f.md) | Copies a file or directory. This API uses a promise to return the result.File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be the URI of the file or directory.A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500. |
| [copy](arkts-fileio-copy-f.md) | Copies a file or directory. This API uses an asynchronous callback to return the result.File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be the URI of the file or directory.A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500. |
| [copy](arkts-fileio-copy-f.md) | Copies a file or directory. This API uses an asynchronous callback to return the result.File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be the URI of the file or directory.A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500. |
| [copyDir](arkts-fileio-copydir-f.md) | Copies the source directory and its content to the destination path. You can set the conflict handling mode. This API uses a promise to return the result. |
| [copyDir](arkts-fileio-copydir-f.md) | Copies the source directory and its content to the destination path. This API uses an asynchronous callback to return the result.An exception will be thrown if the destination directory contains a directory with the same name as the source directory and there are files with the same name in the conflicting directory. All the non-conflicting files in the source directory will be copied to the destination directory, and the non-conflicting files in the destination directory will be retained. |
| [copyDirWithConflictFiles](arkts-fileio-copydirwithconflictfiles-f.md) | Copies the source directory to the destination path. This API uses an asynchronous callback to return the result.An exception will be thrown if the destination directory contains a directory with the same name as the source directory and there are files with the same name in the conflicting directory. All the non-conflicting files in the source directory will be copied to the destination directory, and the non-conflicting files in the destination directory will be retained. The data attribute in the error returned provides information about the conflicting files in the Array&lt;ConflictFiles&gt; format. |
| [copyDir](arkts-fileio-copydir-f.md) | Copies the source directory and its content to the destination path. You can set the conflict handling mode. This API uses an asynchronous callback to return the result. |
| [copyDirWithConflictFiles](arkts-fileio-copydirwithconflictfiles-f.md) | Copies the source directory to the destination directory. You can set the copy mode. This API uses an asynchronous callback to return the result. |
| [copyDirSync](arkts-fileio-copydirsync-f.md) | Copies the source directory to the destination path. This API returns the result synchronously. |
| [copyFile](arkts-fileio-copyfile-f.md) | Copies a file. This API uses a promise to return the result. |
| [copyFile](arkts-fileio-copyfile-f.md) | Copies a file. This API overwrites the file with the same name in the destination directory and truncates the part that is not overwritten. This API uses an asynchronous callback to return the result. |
| [copyFile](arkts-fileio-copyfile-f.md) | Copies a file with the specified mode. This API uses an asynchronous callback to return the result. |
| [copyFileSync](arkts-fileio-copyfilesync-f.md) | Copies a file. This API returns the result synchronously. |
| [createStream](arkts-fileio-createstream-f.md) | Creates a stream based on a file path. This API uses a promise to return the result. To close the stream, use **close()** of [Stream](arkts-fileio-stream-i.md). |
| [createStream](arkts-fileio-createstream-f.md) | Creates a stream based on a file path. To close the stream, use **close()** of [Stream](arkts-fileio-stream-i.md). This API uses an asynchronous callback to return the result. |
| [createStreamSync](arkts-fileio-createstreamsync-f.md) | Creates a stream based on a file path. This API returns the result synchronously. To close the stream, use **close()** of [Stream](arkts-fileio-stream-i.md). |
| [createRandomAccessFile](arkts-fileio-createrandomaccessfile-f.md) | Creates a **RandomAccessFile** instance based on a file path or file object. This API uses a promise to return the result. |
| [createRandomAccessFile](arkts-fileio-createrandomaccessfile-f.md) | Creates a **RandomAccessFile** instance in read-only mode based on a file path or file object. This API uses an asynchronous callback to return the result. |
| [createRandomAccessFile](arkts-fileio-createrandomaccessfile-f.md) | Creates a **RandomAccessFile** instance based on a file path or file object. This API uses an asynchronous callback to return the result. |
| [createRandomAccessFileSync](arkts-fileio-createrandomaccessfilesync-f.md) | Creates a **RandomAccessFile** instance based on a file path or file object. |
| [createReadStream](arkts-fileio-createreadstream-f.md) | Creates a readable stream. This API returns the result synchronously. |
| [createWriteStream](arkts-fileio-createwritestream-f.md) | Creates a writeable stream. This API returns the result synchronously. |
| [createWatcher](arkts-fileio-createwatcher-f.md) | Creates a **Watcher** object to listen for file or directory changes such as creating, deleting, and modifying. |
| [dup](arkts-fileio-dup-f.md) | Duplicates the file descriptor and returns the corresponding **File** object. |
| [fdatasync](arkts-fileio-fdatasync-f.md) | Synchronizes data in a file. This API uses a promise to return the result. |
| [fdatasync](arkts-fileio-fdatasync-f.md) | Synchronizes data in a file. This API uses an asynchronous callback to return the result. |
| [fdatasyncSync](arkts-fileio-fdatasyncsync-f.md) | Synchronizes the data of a file. This API returns the result synchronously. |
| [fdopenStream](arkts-fileio-fdopenstream-f.md) | Opens a file stream based on the file descriptor. This API uses a promise to return the result. To close the stream, use **close()** of [Stream](arkts-fileio-stream-i.md). |
| [fdopenStream](arkts-fileio-fdopenstream-f.md) | Opens a stream based on the file descriptor. To close the stream, use **close()** of [Stream](arkts-fileio-stream-i.md). This API uses an asynchronous callback to return the result. |
| [fdopenStreamSync](arkts-fileio-fdopenstreamsync-f.md) | Opens a stream based on an FD. This API returns the result synchronously. To close the stream, use **close()** of [Stream](arkts-fileio-stream-i.md). |
| [fsync](arkts-fileio-fsync-f.md) | Synchronizes the cached data of a file to storage. This API uses a promise to return the result. |
| [fsync](arkts-fileio-fsync-f.md) | Synchronizes the cached data of a file to storage. This API uses an asynchronous callback to return the result. |
| [fsyncSync](arkts-fileio-fsyncsync-f.md) | Synchronizes the cached data of a file to storage. This API returns the result synchronously. |
| [listFile](arkts-fileio-listfile-f.md) | Lists the names of all files and directories in the current directory. A file name array is returned, which can be filtered by file name or file name extension. This API uses a promise to return the result.This API supports recursively listing the relative paths of all files by setting **recursion** in **ListFileOptions**. The relative path starts with a slash (/). |
| [listFile](arkts-fileio-listfile-f.md) | Lists the names of all files and directories in the current path. A file name array is returned. This API uses an asynchronous callback to return the result. |
| [listFile](arkts-fileio-listfile-f.md) | Lists the names of all files and directories in the current directory. A file name array is returned, which can be filtered by file name or file name extension. This API uses an asynchronous callback to return the result.This API supports recursively listing the relative paths of all files by setting **recursion** in **ListFileOptions**. The relative path starts with a slash (/). |
| [listFileSync](arkts-fileio-listfilesync-f.md) | Lists the names of all files and directories in the current directory synchronously. A file name array is returned, which can be filtered by file name or file name extension.This API supports recursively listing the relative paths of all files by setting **recursion** in **ListFileOptions**. The relative path starts with a slash (/). |
| [listFileExt](arkts-fileio-listfileext-f.md) | Lists all files in a directory. This API supports recursive listing of files and file filtering. This API uses a promise to return the result.You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The relative path starts with a slash (/). |
| [listFileExtSync](arkts-fileio-listfileextsync-f.md) | Lists all files in a directory. This API supports recursive listing of files and file filtering and returns the result synchronously.You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The relative path starts with a slash (/). |
| [lseek](arkts-fileio-lseek-f.md) | Adjusts the position of the file offset pointer. |
| [lstat](arkts-fileio-lstat-f.md) | Obtains information about a symbolic link that is used to refer to a file or directory. The attributes of the symbolic link are returned, instead of the attributes of the target file. This API uses a promise to return the result. |
| [lstat](arkts-fileio-lstat-f.md) | Obtains information about a symbolic link that is used to refer to a file or directory. The attributes of the symbolic link are returned, instead of the attributes of the target file. This API uses an asynchronous callback to return the result. |
| [lstatSync](arkts-fileio-lstatsync-f.md) | Obtains information about a symbolic link that is used to refer to a file or directory synchronously. The attributes of the symbolic link are returned, instead of the attributes of the target file. |
| [mkdir](arkts-fileio-mkdir-f.md) | Creates a single-level directory. If the parent directory does not exist, an error is reported. This API uses a promise to return the result. |
| [mkdir](arkts-fileio-mkdir-f.md) | Creates a directory. This API uses a promise to return the result. The value **true** means to create a directory recursively. |
| [mkdir](arkts-fileio-mkdir-f.md) | Creates a single-level directory. If the parent directory does not exist, an error is reported. This API uses an asynchronous callback to return the result. |
| [mkdir](arkts-fileio-mkdir-f.md) | Creates a directory. If **recursion** is set to **true**, a directory is created recursively. This API uses an asynchronous callback to return the result. |
| [mkdirSync](arkts-fileio-mkdirsync-f.md) | Creates a single-level directory synchronously. If the parent directory does not exist, an error is reported. |
| [mkdirSync](arkts-fileio-mkdirsync-f.md) | Creates a directory. This API returns the result synchronously. The value **true** means to create a directory recursively. |
| [mkdtemp](arkts-fileio-mkdtemp-f.md) | Create a temporary directory. This API uses a promise to return the result. |
| [mkdtemp](arkts-fileio-mkdtemp-f.md) | Create a temporary directory. This API uses an asynchronous callback to return the result. |
| [mkdtempSync](arkts-fileio-mkdtempsync-f.md) | Creates a temporary directory. This API returns the result synchronously. |
| [mmap](arkts-fileio-mmap-f.md) | Creates a file mapping object based on a file descriptor or file object for efficient read and write access to files. This API uses a promise to return the result. |
| [mmapSync](arkts-fileio-mmapsync-f.md) | Creates a file mapping object synchronously based on a file descriptor or file object for efficient read and write access to files. |
| [moveDir](arkts-fileio-movedir-f.md) | Moves the source directory and its content to the destination path. This API uses a promise to return the result. |
| [moveDir](arkts-fileio-movedir-f.md) | Moves the source directory and its content to the destination path. This API uses an asynchronous callback to return the result.An exception will be thrown if a directory conflict occurs, that is, the destination directory contains a directory with the same name as the source directory. |
| [moveDirWithConflictFiles](arkts-fileio-movedirwithconflictfiles-f.md) | Moves the source directory and its content to the destination path. This API uses an asynchronous callback to return the result.An exception will be thrown if a directory conflict occurs, that is, the destination directory contains a directory with the same name as the source directory. |
| [moveDir](arkts-fileio-movedir-f.md) | Moves the source directory and its content to the destination path. You can set the conflict handling mode. This API uses an asynchronous callback to return the result. |
| [moveDirWithConflictFiles](arkts-fileio-movedirwithconflictfiles-f.md) | Moves the source directory to the destination directory. You can set the move mode. This API uses an asynchronous callback to return the result. |
| [moveDirSync](arkts-fileio-movedirsync-f.md) | Moves the source directory and its content to the destination directory. This API returns the result synchronously. |
| [moveFile](arkts-fileio-movefile-f.md) | Moves a file to the target path. You can set the conflict handling mode. This API uses a promise to return the result. |
| [moveFile](arkts-fileio-movefile-f.md) | Moves a file and forcibly overwrites the file with the same name in the destination directory. This API uses an asynchronous callback to return the result. |
| [moveFile](arkts-fileio-movefile-f.md) | Moves a file to the target path. You can set the conflict handling mode. This API uses an asynchronous callback to return the result. |
| [moveFileSync](arkts-fileio-movefilesync-f.md) | Moves a file to the destination path. This API returns the result synchronously. |
| [open](arkts-fileio-open-f.md) | Opens a file or directory. This API supports the use of a URI. This API uses a promise to return the result. |
| [open](arkts-fileio-open-f.md) | Opens a file or directory. This API supports the use of a URI. This API uses an asynchronous callback to return the result. |
| [open](arkts-fileio-open-f.md) | Opens a file or directory with the specified mode. This API uses an asynchronous callback to return the result.This API supports the use of a URI. |
| [openSync](arkts-fileio-opensync-f.md) | Opens a file or directory. This API returns the result synchronously. This API supports the use of a URI. |
| [read](arkts-fileio-read-f.md) | Reads data from a file and returns the number of bytes read. This API uses a promise to return the result. |
| [read](arkts-fileio-read-f.md) | Reads data from a file and returns the number of bytes read. This API uses an asynchronous callback to return the result. |
| [read](arkts-fileio-read-f.md) | Reads data from a file. Read options (such as the offset position and length of the data read) can be configured. The number of bytes read is returned. This API uses an asynchronous callback to return the result. |
| [readSync](arkts-fileio-readsync-f.md) | Reads data from a file synchronously and returns the number of bytes read. |
| [readLines](arkts-fileio-readlines-f.md) | Reads a file text line by line. Only the files in UTF-8 format are supported. This API uses a promise to return the result. |
| [readLines](arkts-fileio-readlines-f.md) | Reads a file text line by line. Only the files in UTF-8 format are supported. This API uses an asynchronous callback to return the result. |
| [readLines](arkts-fileio-readlines-f.md) | Reads a file text line by line. Read options can be configured. Only the files in UTF-8 format are supported. This API uses an asynchronous callback to return the result. |
| [readLinesSync](arkts-fileio-readlinessync-f.md) | Reads a file text line by line synchronously. Only the files in UTF-8 format are supported. |
| [readText](arkts-fileio-readtext-f.md) | Reads the text content of a file synchronously. This API returns the result synchronously. This API uses a promise to return the result. |
| [readText](arkts-fileio-readtext-f.md) | Reads the text of a file. This API uses an asynchronous callback to return the result. |
| [readText](arkts-fileio-readtext-f.md) | Reads the text of a file. Read options can be configured. This API uses an asynchronous callback to return the result. |
| [readTextSync](arkts-fileio-readtextsync-f.md) | Reads the text content of a file. This API returns the result synchronously. |
| [rename](arkts-fileio-rename-f.md) | Renames a file or directory. This API uses a promise to return the result. |
| [rename](arkts-fileio-rename-f.md) | Renames a file or directory. This API uses an asynchronous callback to return the result. |
| [renameSync](arkts-fileio-renamesync-f.md) | Renames a file or directory. This API returns the result synchronously. |
| [rmdir](arkts-fileio-rmdir-f.md) | Deletes a directory and all its subdirectories and files. This API uses a promise to return the result. |
| [rmdir](arkts-fileio-rmdir-f.md) | Deletes a directory and all its subdirectories and files. This API uses an asynchronous callback to return the result. |
| [rmdirSync](arkts-fileio-rmdirsync-f.md) | Removes a directory and all its subdirectories and files synchronously. |
| [stat](arkts-fileio-stat-f.md) | Obtains detailed attributes of a file or directory. The returned **Stat** object contains attributes such as the file size, permission mode, access time, and modification time. This API uses a promise to return the result. |
| [stat](arkts-fileio-stat-f.md) | Obtains detailed attributes of a file or directory. The returned **Stat** object contains attributes such as the file size, permission mode, access time, and modification time. This API uses an asynchronous callback to return the result. |
| [statSync](arkts-fileio-statsync-f.md) | Obtains detailed attributes of a file or directory synchronously. The returned **Stat** object contains attributes such as the file size, permission mode, access time, and modification time. |
| [symlink](arkts-fileio-symlink-f.md) | Creates a symbolic link based on a file path. This API uses a promise to return the result. |
| [symlink](arkts-fileio-symlink-f.md) | Creates a symbolic link based on a file path. This API uses an asynchronous callback to return the result. |
| [symlinkSync](arkts-fileio-symlinksync-f.md) | Creates a symbolic link based on the file path. This API returns the result synchronously. |
| [truncate](arkts-fileio-truncate-f.md) | Truncates a file to the specified length. Excess content will be deleted. This API uses a promise to return the result. |
| [truncate](arkts-fileio-truncate-f.md) | Truncates a file and deletes its content. This API uses an asynchronous callback to return the result. |
| [truncate](arkts-fileio-truncate-f.md) | Truncates a file to the specified length. Excess content will be deleted. This API uses an asynchronous callback to return the result. |
| [truncateSync](arkts-fileio-truncatesync-f.md) | Truncates a file to the specified length synchronously. Excess content will be deleted. |
| [unlink](arkts-fileio-unlink-f.md) | Deletes a single file. This method cannot be used to delete a directory. This API uses a promise to return the result. |
| [unlink](arkts-fileio-unlink-f.md) | Deletes a single file. This method cannot be used to delete a directory. This API uses an asynchronous callback to return the result. |
| [unlinkSync](arkts-fileio-unlinksync-f.md) | Deletes a single file synchronously. This method cannot be used to delete a directory. |
| [utimes](arkts-fileio-utimes-f.md) | Changes the time when the file was last modified. |
| [write](arkts-fileio-write-f.md) | Writes data to a file and returns the number of bytes written. This API uses a promise to return the result. |
| [write](arkts-fileio-write-f.md) | Writes data to a file and returns the number of bytes written. This API uses an asynchronous callback to return the result. |
| [write](arkts-fileio-write-f.md) | Writes data to a file. Write options (such as the offset position and length of the data written) can be configured.The number of bytes written is returned. This API uses an asynchronous callback to return the result. |
| [writeSync](arkts-fileio-writesync-f.md) | Writes data to a file synchronously and returns the number of bytes written. |
| [connectDfs](arkts-fileio-connectdfs-f.md) | Triggers connection. If the peer device is abnormal, [onStatus](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-dfslisteners-i.md#onstatus) in DfsListeners will be called to notify the application. |
| [disconnectDfs](arkts-fileio-disconnectdfs-f.md) | Triggers disconnection. |
| [setxattr](arkts-fileio-setxattr-f.md) | Sets an extended attribute of a file or directory. This API uses a promise to return the result. |
| [setxattrSync](arkts-fileio-setxattrsync-f.md) | Sets an extended attribute of a file or directory. |
| [getxattr](arkts-fileio-getxattr-f.md) | Obtains an extended attribute of a file or directory. This API uses a promise to return the result. |
| [getxattrSync](arkts-fileio-getxattrsync-f.md) | Obtains an extended attribute of a file. This API returns the result synchronously. |

### Classes

| Name | Description |
| --- | --- |
| [TaskSignal](arkts-fileio-tasksignal-c.md) | Provides APIs for interrupting a copy task. |
| [ReadStream](arkts-fileio-readstream-c.md) | Defines a readable stream. You need to use [fileIo.createReadStream](arkts-fileio-createreadstream-f.md) to create a **ReadStream** instance, which is inherited from [stream.Readable](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md).The data obtained by **ReadStream** is a decoded string. Currently, only the UTF-8 format is supported. |
| [WriteStream](arkts-fileio-writestream-c.md) | Defines a writeable stream. You need to use [fileIo.createWriteStream](arkts-fileio-createwritestream-f.md) to create a **WriteStream** instance, which is inherited from [stream.Writable](../../apis-arkts/arkts-apis/arkts-arkts-stream-writable-c.md). |
| [AtomicFile](arkts-fileio-atomicfile-c.md) | AtomicFile is a class used to perform atomic read and write operations on files. A temporary file is written and renamed to the original file location, which ensures file integrity. If the write operation fails, the temporary file is deleted without modifying the original file content. You can call finishWrite() or failWrite() to write or roll back file content. |

### Interfaces

| Name | Description |
| --- | --- |
| [DfsListeners](arkts-fileio-dfslisteners-i.md) | The listeners of Distributed File System. |
| [Progress](arkts-fileio-progress-i.md) | Defines the copy progress information. |
| [CopyOptions](arkts-fileio-copyoptions-i.md) | Defines the callback for listening for the copy progress. |
| [File](arkts-fileio-file-i.md) | Represents a **File** object opened by **open()**. It contains the FD and provides capabilities such as locking a file and obtaining the parent directory. |
| [FileMapping](arkts-fileio-filemapping-i.md) | Defines a file mapping object. Before calling the **FileMapping** method, construct a **FileMapping** instance using [mmap()](arkts-fileio-mmap-f.md) or [mmapSync()](arkts-fileio-mmapsync-f.md). |
| [RandomAccessFile](arkts-fileio-randomaccessfile-i.md) | Provides APIs for randomly reading and writing a stream based on offset pointers. Before invoking any API of **RandomAccessFile**, you need to use **createRandomAccessFile()** to create a **RandomAccessFile** instance synchronously or asynchronously. |
| [Stat](arkts-fileio-stat-i.md) | Obtains detailed information of a file, including attributes such as the file size, permission mode, access time, and modification time. Before calling an API of the **Stat** class, use [stat()](arkts-fileio-stat-f.md) to create a **Stat** instance. |
| [Stream](arkts-fileio-stream-i.md) | Provides APIs for stream operations, such as reading and writing data streams of files. After using an API of the **Stream** class, you need to call **close** to close the file stream. Before calling an API of the **Stream** class, you need to create a **Stream** instance by using [fileIo.createStream](arkts-fileio-createstream-f.md) or [fileIo.fdopenStream](arkts-fileio-fdopenstream-f.md). |
| [Watcher](arkts-fileio-watcher-i.md) | Provides APIs for observing the changes of files or directories. Before using the APIs of Watcher, call createWatcher() to create a Watcher object. |
| [ReaderIterator](arkts-fileio-readeriterator-i.md) | Provides a **ReaderIterator** object. Before calling APIs of **ReaderIterator**, you need to use **readLines()** to create a **ReaderIterator** instance. |

### Enums

| Name | Description |
| --- | --- |
| [MappingMode](arkts-fileio-mappingmode-e.md) | Enumerates file memory mapping modes. |
| [WhenceType](arkts-fileio-whencetype-e.md) | Enumerates the types of the relative offset position used in **lseek()**. |
| [LocationType](arkts-fileio-locationtype-e.md) | Enumerates the file locations. |
| [AccessModeType](arkts-fileio-accessmodetype-e.md) | Enumerates the access modes to verify. If this parameter is left blank, the system checks whether the file exists. |
| [AccessFlagType](arkts-fileio-accessflagtype-e.md) | Enumerates the locations of the file to verify. |

### Types

| Name | Description |
| --- | --- |
| [DfsListenerCallback](arkts-fileio-dfslistenercallback-t.md) | DfsListener Callback function. |
| [ProgressListener](arkts-fileio-progresslistener-t.md) | Listener used to observe the copy progress. |

