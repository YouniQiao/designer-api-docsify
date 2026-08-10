# AtomicFile

AtomicFile是一个用于对文件进行原子读写等操作的类。在写操作时，通过写入临时文件，并在写入成功后将其重命名到原始文件位置来确保写入文件的完整性；而在写入失败时删除临时文件，不修改原始文件内容。使用者可以自行调用finishWrite或failWrite来完成文件内容的写入或回滚。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-export class AtomicFile--><!--Device-fileIo-export class AtomicFile-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor(path: string)
```

对于给定路径的文件创建一个AtomicFile类。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AtomicFile-constructor(path: string)--><!--Device-AtomicFile-constructor(path: string)-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 文件的沙箱路径。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |

## delete

```TypeScript
delete(): void
```

删除AtomicFile类，会删除原始文件和临时文件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AtomicFile-delete(): void--><!--Device-AtomicFile-delete(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900042 | Internal error |
| 13900027 | Read-only file system |

## failWrite

```TypeScript
failWrite(): void
```

文件写入失败后调用，将执行文件回滚操作。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AtomicFile-failWrite(): void--><!--Device-AtomicFile-failWrite(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900042 | Internal error |

## finishWrite

```TypeScript
finishWrite(): void
```

在完成对startWrite返回流的写入操作时调用，表示文件写入成功。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AtomicFile-finishWrite(): void--><!--Device-AtomicFile-finishWrite(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900042 | Internal error |

## getBaseFile

```TypeScript
getBaseFile(): File
```

通过AtomicFile对象获取文件对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AtomicFile-getBaseFile(): File--><!--Device-AtomicFile-getBaseFile(): File-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| [File](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-request-file-i.md) | File object opened. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900005 | IO error |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900042 | Internal error |

## openRead

```TypeScript
openRead(): ReadStream
```

创建一个读文件流。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AtomicFile-openRead(): ReadStream--><!--Device-AtomicFile-openRead(): ReadStream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| [ReadStream](arkts-corefile-fileio-readstream-c.md) | ReadStream instance obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900042 | Internal error |

## readFully

```TypeScript
readFully(): ArrayBuffer
```

读取文件全部内容。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AtomicFile-readFully(): ArrayBuffer--><!--Device-AtomicFile-readFully(): ArrayBuffer-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer | Full content of a file. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900005 | I/O error |
| 13900042 | Internal error |

## startWrite

```TypeScript
startWrite(): WriteStream
```

对文件开始新的写入操作。将返回一个WriteStream，用于在其中写入新的文件数据。当文件不存在时新建文件。在写入文件完成后，写入成功需要调用finishWrite()，写入失败需要调用failWrite()。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AtomicFile-startWrite(): WriteStream--><!--Device-AtomicFile-startWrite(): WriteStream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| [WriteStream](arkts-corefile-fileio-writestream-c.md) | Returns the file write stream. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900001 | Operation not permitted |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900042 | Internal error |
| 13900027 | Read-only file system |

