# mmap

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## mmap

```TypeScript
function mmap(file: int | File, mode: MappingMode, offset: long, size: int): Promise<FileMapping>
```

基于文件描述符或文件对象创建文件映射对象，实现文件的高效读写访问。使用Promise异步回调。

> **说明：**&gt;
> 1. 仅支持对常规文件（regular file）进行内存映射，不支持管道、socket、设备文件等非常规文件类型。可通过[statSync](arkts-corefile-fileio-statsync-f.md)获取文件属性后调用
> [Stat.isFile()](arkts-corefile-fileio-stat-i.md#isfile)判断文件是否为常规文件。&gt;
> 2. 若映射范围超过原始文件大小且文件具有写权限，将自动扩展映射文件大小。&gt;
> 3. 对于外部存储或网络文件等，由于底层文件系统的差异，映射的建立及对映射内存的访问行为不做保证，可能导致应用异常终止。建议此类场景优先使用[read](arkts-corefile-fileio-read-f.md)、
> [write](arkts-corefile-fileio-write-f.md)或[Stream](arkts-corefile-fileio-stream-i.md)等其他文件访问接口。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [file](arkts-corefile-storagestatistics-storagestats-i-sys.md) | int \| [File](arkts-corefile-file-fs-file-i.md) | 是 |
| mode | [MappingMode](arkts-corefile-file-fs-mappingmode-e.md) | 是 |
| offset | long | 是 |
| size | int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[FileMapping](arkts-corefile-file-fs-filemapping-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900011 |
| 13900012 |
| 13900015 |
| 13900017 |
| 13900020 |
| 13900021 |
| 13900023 |
| 13900024 |
| 13900038 |
| 13900050 |
| 13900056 |
