# mmap

## Modules to Import

```TypeScript
```

## mmap

```TypeScript
function mmap(file: int | File, mode: MappingMode, offset: long, size: int): Promise<FileMapping>
```

Creates a file mapping object based on a file descriptor or file object for efficient read and write access to files. This API uses a promise to return the result. > **NOTE：**> > 1. Memory mapping can be performed only for regular files. Non-regular files, such as > pipeline, socket, and device > files, are not supported. You can use [statSync()](arkts-na-fileio-statsync-f.md#statsync) to obtain file attributes and then call > [Stat.isFile()](arkts-na-fileio-stat-i.md#isfile) to check whether the file is a regular file. > > 2. If the mapping range exceeds the raw file size and the write permission is granted for the file, the mapping > file size will be automatically expanded. > > 3. For files from external storage or network files, the establishment of mappings and access > to the mapped memory > are not guaranteed due to differences in the underlying file system. This may cause the application to terminate > unexpectedly. You are advised to use other file access APIs such as [read](arkts-na-fileio-read-f.md#read), > [write](arkts-na-fileio-write-f.md#write), or [Stream](arkts-na-fileio-stream-i.md#stream) in this scenario.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileIo-function mmap(file: int | File, mode: MappingMode, offset: long, size: int): Promise<FileMapping>--><!--Device-fileIo-function mmap(file: int | File, mode: MappingMode, offset: long, size: int): Promise<FileMapping>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| file | int \| [File](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-file-i.md) | Yes | File** object or FD of the file to close. |
| mode | [MappingMode](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-mappingmode-e.md) | Yes | Option to create a file memory-mapped object. You must specify one of the following options: <br>- **MappingMode.READ_ONLY(0)**: read-only mode. The file mapping area is not writable. An exception is thrown when the file mapping area is modified. <br>- **MappingMode.READ_WRITE(1)**: read/write mode. The modification is written to the file mapping area and then synchronized to the file by the operating system (non-real-time). <br>- **MappingMode.PRIVATE(2)**: private mode. It is a copy-on-write mapping mechanism. Modifications to the mapping area are visible only to the current process and do not affect the raw file. |
| offset | long | Yes | Start position of the file mapping area, in bytes. |
| size | int | Yes | Size of the file mapping area, in bytes. The value ranges from 0 to **INT32_MAX**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[FileMapping](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-filemapping-i.md)&gt; | Promise used to return the file mapping object. Initial state of the returned object: The value of **position** is **0**, and the values of **limit** and **capacity** are equal to the value of **size**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900021 | File table overflow |
| 13900023 | Text file busy |
| 13900017 | No such device |
| 13900050 | Internal resource error |
| 13900024 | File too large |
| 13900056 | Mmap does not support mapping this file |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900038 | Value too large for defined data type |
| 13900001 | Operation not permitted |
| 13900012 | Permission denied |
| 13900015 | File exists |
| 13900008 | Bad file descriptor |
| 13900010 | Try again |
| 13900011 | Out of memory |

