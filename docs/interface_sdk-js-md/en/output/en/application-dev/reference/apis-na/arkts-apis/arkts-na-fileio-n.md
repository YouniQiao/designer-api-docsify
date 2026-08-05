# fileIo

FileIO

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-declare namespace fileIo--><!--Device-unnamed-declare namespace fileIo-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Summary

### Namespaces

| Name | Description |
| --- | --- |
| [OpenMode](arkts-na-fileio-openmode-n.md) | Mode Indicates the open flags. |

### Functions

| Name | Description |
| --- | --- |
| [access](arkts-na-fileio-access-f.md#access) | Checks whether the file or directory exists or has the operation permission. This API uses a promise to return the result. If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown. |
| [access](arkts-na-fileio-access-f.md#access-1) | Checks whether a file or directory exists. This API uses an asynchronous callback to return the result. |
| [access](arkts-na-fileio-access-f.md#access-2) | Checks whether the file or directory is stored locally or has the operation permission. This API uses a promise to return the result. If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown. |
| [accessSync](arkts-na-fileio-accesssync-f.md#accesssync) | Checks whether a file or directory exists or has the operation permission. This API returns the result synchronously. If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown. |
| [accessSync](arkts-na-fileio-accesssync-f.md#accesssync-1) | Checks whether a file or directory is stored locally or has the operation permission. This API returns the result synchronously. If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will be thrown. |
| [close](arkts-na-fileio-close-f.md#close) | Closes a file or directory. This API uses a promise to return the result. |
| [close](arkts-na-fileio-close-f.md#close-1) | Closes a file or directory. This API uses an asynchronous callback to return the result. |
| [closeSync](arkts-na-fileio-closesync-f.md#closesync) | Closes a file or directory. This API returns the result synchronously. |
| [copy](arkts-na-fileio-copy-f.md#copy) | Copies a file or directory. This API uses a promise to return the result. File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be the URI of the file or directory. A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500. |
| [copy](arkts-na-fileio-copy-f.md#copy-1) | Copies a file or directory. This API uses an asynchronous callback to return the result. File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be the URI of the file or directory. A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500. |
| [copy](arkts-na-fileio-copy-f.md#copy-2) | Copies a file or directory. This API uses an asynchronous callback to return the result. File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be the URI of the file or directory. A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500. |
| [copyDir](arkts-na-fileio-copydir-f.md#copydir) | Copies the source directory to the destination directory. This API uses a promise to return the result. |
| [copyDir](arkts-na-fileio-copydir-f.md#copydir-1) | Copies the source directory to the destination directory. This API uses an asynchronous callback to return the result. |
| [copyDirWithConflictFiles](arkts-na-fileio-copydirwithconflictfiles-f.md#copydirwithconflictfiles) | Copies the source directory to the destination directory. This API uses an asynchronous callback to return the result. |
| [copyDir](arkts-na-fileio-copydir-f.md#copydir-2) | Copies the source directory to the destination directory. You can set the copy mode. This API uses an asynchronous callback to return the result. |
| [copyDirWithConflictFiles](arkts-na-fileio-copydirwithconflictfiles-f.md#copydirwithconflictfiles-1) | Copies the source directory to the destination directory. You can set the copy mode. This API uses an asynchronous callback to return the result. |
| [copyDirSync](arkts-na-fileio-copydirsync-f.md#copydirsync) | Copies the source directory to the destination directory. This API returns the result synchronously. |
| [copyFile](arkts-na-fileio-copyfile-f.md#copyfile) | Copies a file. This API uses a promise to return the result. |
| [copyFile](arkts-na-fileio-copyfile-f.md#copyfile-1) | Copies a file. This API overwrites the file with the same name in the destination directory and truncates the part that is not overwritten. This API uses an asynchronous callback to return the result. |
| [copyFile](arkts-na-fileio-copyfile-f.md#copyfile-2) | Copies a file. This API overwrites the file with the same name in the destination directory and truncates the part that is not overwritten. This API uses an asynchronous callback to return the result. |
| [copyFileSync](arkts-na-fileio-copyfilesync-f.md#copyfilesync) | Copies a file. This API returns the result synchronously. |
| [createStream](arkts-na-fileio-createstream-f.md#createstream) | Creates a stream based on a file path. This API uses a promise to return the result. To close the stream, use close() of Stream. |
| [createStream](arkts-na-fileio-createstream-f.md#createstream-1) | Creates a stream based on a file path. This API uses an asynchronous callback to return the result. To close the stream, use close() of Stream. |
| [createStreamSync](arkts-na-fileio-createstreamsync-f.md#createstreamsync) | Creates a stream based on a file path. This API returns the result synchronously. To close the stream, use close() of Stream. |
| [createRandomAccessFile](arkts-na-fileio-createrandomaccessfile-f.md#createrandomaccessfile) | Creates a RandomAccessFile instance based on a file path or file object. This API uses a promise to return the result. |
| [createRandomAccessFile](arkts-na-fileio-createrandomaccessfile-f.md#createrandomaccessfile-1) | Creates a RandomAccessFile object in read-only mode based on a file path or file object. This API uses an asynchronous callback to return the result. |
| [createRandomAccessFile](arkts-na-fileio-createrandomaccessfile-f.md#createrandomaccessfile-2) | Creates a RandomAccessFile instance based on a file path or file object. This API uses an asynchronous callback to return the result. |
| [createRandomAccessFileSync](arkts-na-fileio-createrandomaccessfilesync-f.md#createrandomaccessfilesync) | Creates a RandomAccessFile instance based on a file path or file object. |
| [createReadStream](arkts-na-fileio-createreadstream-f.md#createreadstream) | Creates a readable stream. This API returns the result synchronously. |
| [createWriteStream](arkts-na-fileio-createwritestream-f.md#createwritestream) | Creates a writeable stream. This API returns the result synchronously. |
| [createWatcher](arkts-na-fileio-createwatcher-f.md#createwatcher) | Creates a Watcher object to listen for file or directory changes. |
| [dup](arkts-na-fileio-dup-f.md#dup) | Duplicates the file descriptor and returns the corresponding File object. |
| [fdatasync](arkts-na-fileio-fdatasync-f.md#fdatasync) | Synchronizes the data of a file. This API uses a promise to return the result. |
| [fdatasync](arkts-na-fileio-fdatasync-f.md#fdatasync-1) | Synchronizes the data (excluding the metadata) of a file. This API uses an asynchronous callback to return the result. |
| [fdatasyncSync](arkts-na-fileio-fdatasyncsync-f.md#fdatasyncsync) | Synchronizes the data of a file. This API returns the result synchronously. |
| [fdopenStream](arkts-na-fileio-fdopenstream-f.md#fdopenstream) | Opens a stream based on an FD. This API uses a promise to return the result. To close the stream, use close() of Stream. |
| [fdopenStream](arkts-na-fileio-fdopenstream-f.md#fdopenstream-1) | Opens a stream based on an FD. This API uses an asynchronous callback to return the result. To close the stream, use close() of Stream. |
| [fdopenStreamSync](arkts-na-fileio-fdopenstreamsync-f.md#fdopenstreamsync) | Opens a stream based on an FD. This API returns the result synchronously. To close the stream, use close() of Stream. |
| [fsync](arkts-na-fileio-fsync-f.md#fsync) | Synchronizes the cached data of a file to storage. This API uses a promise to return the result. |
| [fsync](arkts-na-fileio-fsync-f.md#fsync-1) | Synchronizes the cached data of a file to storage. This API uses an asynchronous callback to return the result. |
| [fsyncSync](arkts-na-fileio-fsyncsync-f.md#fsyncsync) | Synchronizes the cached data of a file to storage. This API returns the result synchronously. |
| [listFile](arkts-na-fileio-listfile-f.md#listfile) | Lists all file names in a directory. This API supports recursive listing of all file names and file filtering. The returned result starts with a slash (/) and contains the subdirectory. This API uses a promise to return the result. |
| [listFile](arkts-na-fileio-listfile-f.md#listfile-1) | Lists the names of all files and directories in the current path. This API uses an asynchronous callback to return the result. |
| [listFile](arkts-na-fileio-listfile-f.md#listfile-2) | Lists all file names in a directory. This API supports recursive listing of all file names and file filtering. This API uses an asynchronous callback to return the result. |
| [listFileSync](arkts-na-fileio-listfilesync-f.md#listfilesync) | Lists all file names in a directory. This API returns the result synchronously. This API supports recursive listing of all file names and file filtering. |
| [listFileExt](arkts-na-fileio-listfileext-f.md#listfileext) | Lists all file names in a directory. This API uses a promise to return the result. This API supports recursive listing of all file names and custom file name filtering. The returned result starts with a slash (/) and contains the subdirectory. |
| [listFileExtSync](arkts-na-fileio-listfileextsync-f.md#listfileextsync) | Lists all file names in a directory. This API returns the result synchronously. This API supports recursive listing of all file names and custom file name filtering. The returned result starts with a slash (/) and contains the subdirectory. |
| [lseek](arkts-na-fileio-lseek-f.md#lseek) | Adjusts the position of the file offset pointer. |
| [lstat](arkts-na-fileio-lstat-f.md#lstat) | Obtains information about a symbolic link that is used to refer to a file or directory. This API uses a promise to return the result. |
| [lstat](arkts-na-fileio-lstat-f.md#lstat-1) | Obtains information about a symbolic link that is used to refer to a file or directory. This API uses an asynchronous callback to return the result. |
| [lstatSync](arkts-na-fileio-lstatsync-f.md#lstatsync) | Obtains information about a symbolic link that is used to refer to a file or directory. This API returns the result synchronously. |
| [mkdir](arkts-na-fileio-mkdir-f.md#mkdir) | Creates a directory. This API uses a promise to return the result. |
| [mkdir](arkts-na-fileio-mkdir-f.md#mkdir-1) | Creates a directory. This API uses a promise to return the result. The value true means to create a directory recursively. |
| [mkdir](arkts-na-fileio-mkdir-f.md#mkdir-2) | Creates a directory. This API uses an asynchronous callback to return the result. |
| [mkdir](arkts-na-fileio-mkdir-f.md#mkdir-3) | Creates a directory. This API uses an asynchronous callback to return the result. The value true means to create a directory recursively. |
| [mkdirSync](arkts-na-fileio-mkdirsync-f.md#mkdirsync) | Creates a directory. This API returns the result synchronously. |
| [mkdirSync](arkts-na-fileio-mkdirsync-f.md#mkdirsync-1) | Creates a directory. This API returns the result synchronously. The value true means to create a directory recursively. |
| [mkdtemp](arkts-na-fileio-mkdtemp-f.md#mkdtemp) | Creates a temporary directory. This API uses a promise to return the result. |
| [mkdtemp](arkts-na-fileio-mkdtemp-f.md#mkdtemp-1) | Creates a temporary directory. This API uses an asynchronous callback to return the result. The directory name is created by replacing a string (specified by prefix) with six randomly generated characters. |
| [mkdtempSync](arkts-na-fileio-mkdtempsync-f.md#mkdtempsync) | Creates a temporary directory. This API returns the result synchronously. The directory name is created by replacing a string (specified by prefix) with six randomly generated characters. |
| [mmap](arkts-na-fileio-mmap-f.md#mmap) | Creates a file mapping object based on a file descriptor or file object, using promise asynchronous callback. Maps file contents to memory for efficient read and write access to files. Note: In the read/write mode (MappingMode.READ\_\_\_ESCAPED\_UNDERSCORE\_\_\_WRITE), if the mapping range exceeds the raw file size, the file size will be automatically expanded. |
| [mmapSync](arkts-na-fileio-mmapsync-f.md#mmapsync) | Creates a file mapping object based on a file descriptor or file object by using the synchronization method. Maps file contents to memory for efficient read and write access to files. Note: In the read/write mode (MappingMode.READ\_\_\_ESCAPED\_UNDERSCORE\_\_\_WRITE), if the mapping range exceeds the raw file size, the file size will be automatically expanded. |
| [moveDir](arkts-na-fileio-movedir-f.md#movedir) | Moves the source directory to the destination directory. This API uses a promise to return the result. |
| [moveDir](arkts-na-fileio-movedir-f.md#movedir-1) | Moves the source directory to the destination directory. This API uses an asynchronous callback to return the result. |
| [moveDirWithConflictFiles](arkts-na-fileio-movedirwithconflictfiles-f.md#movedirwithconflictfiles) | Moves the source directory to the destination directory. This API uses an asynchronous callback to return the result. |
| [moveDir](arkts-na-fileio-movedir-f.md#movedir-2) | Moves the source directory to the destination directory. You can set the move mode. This API uses an asynchronous callback to return the result. |
| [moveDirWithConflictFiles](arkts-na-fileio-movedirwithconflictfiles-f.md#movedirwithconflictfiles-1) | Moves the source directory to the destination directory. You can set the move mode. This API uses an asynchronous callback to return the result. |
| [moveDirSync](arkts-na-fileio-movedirsync-f.md#movedirsync) | Moves the source directory to the destination directory. This API returns the result synchronously. |
| [moveFile](arkts-na-fileio-movefile-f.md#movefile) | Moves a file. This API uses a promise to return the result. |
| [moveFile](arkts-na-fileio-movefile-f.md#movefile-1) | Moves a file and forcibly overwrites the file with the same name in the destination directory. This API uses an asynchronous callback to return the result. |
| [moveFile](arkts-na-fileio-movefile-f.md#movefile-2) | Moves a file with the specified mode. This API uses an asynchronous callback to return the result. |
| [moveFileSync](arkts-na-fileio-movefilesync-f.md#movefilesync) | Moves a file. This API returns the result synchronously. |
| [open](arkts-na-fileio-open-f.md#open) | Opens a file or directory. This API uses a promise to return the result. This API supports the use of a URI. |
| [open](arkts-na-fileio-open-f.md#open-1) | Opens a file or directory. This API uses an asynchronous callback to return the result. This API supports the use of a URI. |
| [open](arkts-na-fileio-open-f.md#open-2) | Opens a file or directory with the specified mode. This API uses an asynchronous callback to return the result. This API supports the use of a URI. |
| [openSync](arkts-na-fileio-opensync-f.md#opensync) | Opens a file or directory. This API returns the result synchronously. This API supports the use of a URI. |
| [read](arkts-na-fileio-read-f.md#read) | Reads file data. This API uses a promise to return the result. |
| [read](arkts-na-fileio-read-f.md#read-1) | Reads data from a file. This API uses an asynchronous callback to return the result. |
| [read](arkts-na-fileio-read-f.md#read-2) | Reads data from a file. This API uses an asynchronous callback to return the result. |
| [readSync](arkts-na-fileio-readsync-f.md#readsync) | Reads data from a file. This API returns the result synchronously. |
| [readLines](arkts-na-fileio-readlines-f.md#readlines) | Reads the text content of a file line by line. This API uses a promise to return the result. Only the files in UTF-8 format are supported. |
| [readLines](arkts-na-fileio-readlines-f.md#readlines-1) | Reads a file text line by line. This API uses an asynchronous callback to return the result. Only the files in UTF-8 format are supported. |
| [readLines](arkts-na-fileio-readlines-f.md#readlines-2) | Reads a file text line by line. This API uses an asynchronous callback to return the result. Only the files in UTF-8 format are supported. |
| [readLinesSync](arkts-na-fileio-readlinessync-f.md#readlinessync) | Reads the text content of a file line by line. This API returns the result synchronously. |
| [readText](arkts-na-fileio-readtext-f.md#readtext) | Reads the text content of a file. This API uses a promise to return the result. |
| [readText](arkts-na-fileio-readtext-f.md#readtext-1) | Reads the text content of a file. This API uses an asynchronous callback to return the result. |
| [readText](arkts-na-fileio-readtext-f.md#readtext-2) | Reads the text content of a file. This API uses an asynchronous callback to return the result. |
| [readTextSync](arkts-na-fileio-readtextsync-f.md#readtextsync) | Reads the text of a file. This API returns the result synchronously. |
| [rename](arkts-na-fileio-rename-f.md#rename) | Renames a file or directory. This API uses a promise to return the result. |
| [rename](arkts-na-fileio-rename-f.md#rename-1) | Renames a file or directory. This API uses an asynchronous callback to return the result. |
| [renameSync](arkts-na-fileio-renamesync-f.md#renamesync) | Renames a file or directory. This API returns the result synchronously. |
| [rmdir](arkts-na-fileio-rmdir-f.md#rmdir) | Removes a directory. This API uses a promise to return the result. |
| [rmdir](arkts-na-fileio-rmdir-f.md#rmdir-1) | Removes a directory. This API uses an asynchronous callback to return the result. |
| [rmdirSync](arkts-na-fileio-rmdirsync-f.md#rmdirsync) | Removes a directory. This API returns the result synchronously. |
| [stat](arkts-na-fileio-stat-f.md#stat) | Obtains detailed attribute information of a file or directory. This API uses a promise to return the result. |
| [stat](arkts-na-fileio-stat-f.md#stat-1) | Obtains detailed attribute information of a file or directory. This API uses an asynchronous callback to return the result. |
| [statSync](arkts-na-fileio-statsync-f.md#statsync) | Obtains detailed attribute information of a file or directory. This API returns the result synchronously. |
| [symlink](arkts-na-fileio-symlink-f.md#symlink) | Creates a symbolic link based on a file path. This API uses a promise to return the result. |
| [symlink](arkts-na-fileio-symlink-f.md#symlink-1) | Creates a symbolic link based on a file path. This API uses an asynchronous callback to return the result. |
| [symlinkSync](arkts-na-fileio-symlinksync-f.md#symlinksync) | Creates a symbolic link based on a file path. This API returns the result synchronously. |
| [truncate](arkts-na-fileio-truncate-f.md#truncate) | Truncates a file. This API uses a promise to return the result. |
| [truncate](arkts-na-fileio-truncate-f.md#truncate-1) | Truncates a file. This API uses an asynchronous callback to return the result. |
| [truncate](arkts-na-fileio-truncate-f.md#truncate-2) | Truncates a file. This API uses an asynchronous callback to return the result. |
| [truncateSync](arkts-na-fileio-truncatesync-f.md#truncatesync) | Truncates the file content. This API returns the result synchronously. |
| [unlink](arkts-na-fileio-unlink-f.md#unlink) | Deletes a file. This API uses a promise to return the result. |
| [unlink](arkts-na-fileio-unlink-f.md#unlink-1) | Deletes a file. This API uses an asynchronous callback to return the result. |
| [unlinkSync](arkts-na-fileio-unlinksync-f.md#unlinksync) | Deletes a file. This API returns the result synchronously. |
| [utimes](arkts-na-fileio-utimes-f.md#utimes) | Changes the time when the file was last modified. |
| [write](arkts-na-fileio-write-f.md#write) | Writes data into a file. This API uses a promise to return the result. |
| [write](arkts-na-fileio-write-f.md#write-1) | Writes data to a file. This API uses an asynchronous callback to return the result. |
| [write](arkts-na-fileio-write-f.md#write-2) | Writes data to a file. This API uses an asynchronous callback to return the result. |
| [writeSync](arkts-na-fileio-writesync-f.md#writesync) | Writes data to a file. This API returns the result synchronously. |
| [connectDfs](arkts-na-fileio-connectdfs-f.md#connectdfs) | Triggers connection. If the peer device is abnormal, [onStatus]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ in DfsListeners will be called to notify the application. |
| [disconnectDfs](arkts-na-fileio-disconnectdfs-f.md#disconnectdfs) | Triggers disconnection. |
| [setxattr](arkts-na-fileio-setxattr-f.md#setxattr) | Sets an extended attribute of a file or directory. |
| [setxattrSync](arkts-na-fileio-setxattrsync-f.md#setxattrsync) | Sets an extended attribute of a file or directory. |
| [getxattr](arkts-na-fileio-getxattr-f.md#getxattr) | Obtains an extended attribute of a file or directory. |
| [getxattrSync](arkts-na-fileio-getxattrsync-f.md#getxattrsync) | Obtains an extended attribute of a file. This API returns the result synchronously. |

### Classes

| Name | Description |
| --- | --- |
| [TaskSignal](arkts-na-fileio-tasksignal-c.md) | Provides APIs for interrupting a copy task. |
| [ReadStream](arkts-na-fileio-readstream-c.md) | Defines a readable stream. You need to use fs.createReadStream to create a ReadStream instance, which is inherited from the stream base class. The data obtained by ReadStream is a decoded string. Currently, only the UTF-8 format is supported. |
| [WriteStream](arkts-na-fileio-writestream-c.md) | Defines a writeable stream. You need to use fs.createWriteStream to create a WriteStream instance, which is inherited from the stream base class. |
| [AtomicFile](arkts-na-fileio-atomicfile-c.md) | AtomicFile is a class used to perform atomic read and write operations on files. A temporary file is written and renamed to the original file location, which ensures file integrity. If the write operation fails, the temporary file is deleted without modifying the original file content. You can call finishWrite() or failWrite() to write or roll back file content. |

### Interfaces

| Name | Description |
| --- | --- |
| [DfsListeners](arkts-na-fileio-dfslisteners-i.md) | The listeners of Distributed File System. |
| [Progress](arkts-na-fileio-progress-i.md) | Defines the copy progress information. |
| [CopyOptions](arkts-na-fileio-copyoptions-i.md) | Defines the callback for listening for the copy progress. |
| [File](arkts-na-fileio-file-i.md) | Represents a File object opened by open(). |
| [FileMapping](arkts-na-fileio-filemapping-i.md) | File mapping object. Before invoking the FileMapping method, you need to use the mmap() method (synchronous or asynchronous) to construct a FileMapping instance. |
| [RandomAccessFile](arkts-na-fileio-randomaccessfile-i.md) | Provides APIs for randomly reading and writing a stream. Before invoking any API of RandomAccessFile, you need to use createRandomAccessFile() to create a RandomAccessFile instance synchronously or asynchronously |
| [Stat](arkts-na-fileio-stat-i.md) | Represents detailed file information. Before calling any API of the Stat() class, use stat() to create a Stat instance. |
| [Stream](arkts-na-fileio-stream-i.md) | Provides API for stream operations. Before calling any API of Stream, you need to create a Stream instance by using fs.createStream or fs.fdopenStream. |
| [Watcher](arkts-na-fileio-watcher-i.md) | Provides APIs for observing the changes of files or directories. Before using the APIs of Watcher, call createWatcher() to create a Watcher object. |
| [ReaderIterator](arkts-na-fileio-readeriterator-i.md) | Provides a ReaderIterator object. Before calling APIs of ReaderIterator, you need to use readLines() to create a ReaderIterator instance. |

### Enums

| Name | Description |
| --- | --- |
| [MappingMode](arkts-na-fileio-mappingmode-e.md) | Enumerated type of the file memory mapping mode, which can be used by the mmap API. |
| [WhenceType](arkts-na-fileio-whencetype-e.md) | Enumerates the types of the relative offset position used in lseek(). |
| [LocationType](arkts-na-fileio-locationtype-e.md) | Enumeration of different types of file location. |
| [AccessModeType](arkts-na-fileio-accessmodetype-e.md) | Enumerates the access modes to verify. If this parameter is left blank, the system checks whether the file exists. |
| [AccessFlagType](arkts-na-fileio-accessflagtype-e.md) | Enumerates the locations of the file to verify. |

### Types

| Name | Description |
| --- | --- |
| [DfsListenerCallback](arkts-na-fileio-dfslistenercallback-t.md) | DfsListener Callback function. |
| [ProgressListener](arkts-na-fileio-progresslistener-t.md) | Listener used to observe the copy progress. |

