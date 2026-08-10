# readLinesSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## readLinesSync

```TypeScript
declare function readLinesSync(filePath: string, options?: Options): ReaderIterator
```

以同步方式逐行读取文件的文本内容。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare function readLinesSync(filePath: string, options?: Options): ReaderIterator--><!--Device-unnamed-declare function readLinesSync(filePath: string, options?: Options): ReaderIterator-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | 文件的应用沙箱路径。 |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No | 可选项。支持以下选项：&lt;br/&gt;- encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认'utf-8'，仅支持'utf-8' 。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md) | 返回文件读取迭代器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900022 | Too many open files |
| 13900019 | Is a directory |
| 13900030 | File name too long |
| 13900025 | No space left on device |
| 13900027 | Read-only file system |
| 13900033 | Too many symbolic links encountered |
| 13900002 | No such file or directory |
| 13900012 | Permission denied |
| 13900044 | Network is unreachable<br>**Applicable version:** 12 and later |
| 13900015 | File exists |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

