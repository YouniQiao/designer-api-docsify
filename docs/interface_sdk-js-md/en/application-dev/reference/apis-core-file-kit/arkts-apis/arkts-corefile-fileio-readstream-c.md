# ReadStream

文件可读流，需要先通过[fileIo.createReadStream](arkts-corefile-fileio-createreadstream-f.md#createreadstream)方法来构建一个ReadStream实例。ReadStream继承自数据流基类  
[stream.Readable](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md/arkts-arkts-stream-readable-c.md)。

**规格**：ReadStream读到的数据为解码后的字符串，其编码格式当前仅支持'utf-8'。

**Inheritance/Implementation:** ReadStream extends [stream.Readable](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md/arkts-arkts-stream-readable-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-class ReadStream extends stream.Readable--><!--Device-fileIo-class ReadStream extends stream.Readable-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## close

```TypeScript
close(): void
```

关闭可读流。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ReadStream-close(): void--><!--Device-ReadStream-close(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

## constructor

```TypeScript
constructor()
```

The ReadStream constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ReadStream-constructor()--><!--Device-ReadStream-constructor()-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## seek

```TypeScript
seek(offset: long, whence?: WhenceType): long
```

调整可读流偏移指针位置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ReadStream-seek(offset: long, whence?: WhenceType): long--><!--Device-ReadStream-seek(offset: long, whence?: WhenceType): long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | long | Yes | 相对偏移位置，单位为Byte。 |
| whence | [WhenceType](arkts-corefile-fileio-whencetype-e.md) | No | = WhenceType.SEEK_SET] - Where to start the offset. The default value is SEEK_SET, &lt;br&gt;which indicates the beginning of the file. |

**Return value:**

| Type | Description |
| --- | --- |
| long | 当前可读流偏移指针位置（相对于文件头的偏移量，单位为Byte）。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 401 | Parameter error |
| 13900026 | Illegal seek |
| 13900042 | Unknown error |

## bytesRead

```TypeScript
readonly bytesRead: long
```

可读流已经读取的字节数。

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ReadStream-readonly bytesRead: long--><!--Device-ReadStream-readonly bytesRead: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## path

```TypeScript
readonly path: string
```

当前可读流对应的文件路径。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ReadStream-readonly path: string--><!--Device-ReadStream-readonly path: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

