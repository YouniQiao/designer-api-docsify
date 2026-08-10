# mmap

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## mmap

```TypeScript
function mmap(file: int | File, mode: MappingMode, offset: long, size: int): Promise<FileMapping>
```

基于文件描述符或文件对象创建文件映射对象，实现文件的高效读写访问。使用Promise异步回调。

> **说明：**
> 
> 1. 仅支持对常规文件（regular file）进行内存映射，不支持管道、socket、设备文件等非常规文件类型。可通过[statSync](arkts-corefile-fileio-statsync-f.md#statsync)获取文件属性后调用
> [Stat.isFile()](arkts-corefile-fileio-stat-i.md#isfile)判断文件是否为常规文件。
> 
> 2. 若映射范围超过原始文件大小且文件具有写权限，将自动扩展映射文件大小。
> 
> 3. 对于外部存储或网络文件等，由于底层文件系统的差异，映射的建立及对映射内存的访问行为不做保证，可能导致应用异常终止。建议此类场景优先使用[read](arkts-corefile-fileio-read-f.md#read)、
> [write](arkts-corefile-fileio-write-f.md#write)或[Stream](arkts-corefile-fileio-stream-i.md)等其他文件访问接口。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileIo-function mmap(file: int | File, mode: MappingMode, offset: long, size: int): Promise<FileMapping>--><!--Device-fileIo-function mmap(file: int | File, mode: MappingMode, offset: long, size: int): Promise<FileMapping>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| file | int \| File | Yes | 已打开的File对象或已打开的文件描述符fd。 |
| mode | [MappingMode](arkts-corefile-file-fs-mappingmode-e.md) | Yes | 创建文件内存映射对象的选项，必须指定如下选项中的一个：&lt;br/&gt; - MappingMode.READ_ONLY(0)：只读映射模式。文件映射区不可写，修改会抛出异常。&lt;br/&gt; - MappingMode.READ_WRITE(1)：读写映射模式。修改会写入文件映射区，后续由操作系统同步到文件（非实时）。&lt;br/&gt; - MappingMode.PRIVATE(2)：私有映射模式。是一种写时复制的映射机制，对映射区的修改仅对当前进程可见，不会影响原始文件。 |
| offset | long | Yes | 文件映射区的起始位置，单位为Byte。 |
| size | int | Yes | 文件映射区的大小，取值范围(0, INT32_MAX]，单位为Byte。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;FileMapping&gt; | Promise对象，返回文件映射对象。返回的对象初始状态：position为0，limit和capacity均等于size。 |

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

