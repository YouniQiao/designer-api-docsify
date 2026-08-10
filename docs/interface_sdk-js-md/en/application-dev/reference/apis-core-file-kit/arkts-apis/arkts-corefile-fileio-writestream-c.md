# WriteStream

文件可写流，需要先通过[fileIo.createWriteStream](arkts-corefile-fileio-createwritestream-f.md#createwritestream)方法来构建一个WriteStream实例。WriteStream继承自数据流基类  
[stream.Writable](../../apis-arkts/arkts-apis/arkts-arkts-stream-writable-c.md/arkts-arkts-stream-writable-c.md)。

**Inheritance/Implementation:** WriteStream extends [stream.Writable](../../apis-arkts/arkts-apis/arkts-arkts-stream-writable-c.md/arkts-arkts-stream-writable-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-class WriteStream extends stream.Writable--><!--Device-fileIo-class WriteStream extends stream.Writable-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## close

```TypeScript
close(): void
```

关闭可写流。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WriteStream-close(): void--><!--Device-WriteStream-close(): void-End-->

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

The WriteStream constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WriteStream-constructor()--><!--Device-WriteStream-constructor()-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## seek

```TypeScript
seek(offset: long, whence?: WhenceType): long
```

调整可写流的偏移指针位置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WriteStream-seek(offset: long, whence?: WhenceType): long--><!--Device-WriteStream-seek(offset: long, whence?: WhenceType): long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | long | Yes | 相对偏移位置，单位为Byte。 |
| whence | [WhenceType](arkts-corefile-fileio-whencetype-e.md) | No | = WhenceType.SEEK_SET] - Where to start the offset. &lt;br&gt;The default value is SEEK_SET, which indicates the beginning of the file. |

**Return value:**

| Type | Description |
| --- | --- |
| long | 当前可写流偏移指针位置（相对于文件头的偏移量，单位为Byte）。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 401 | Parameter error |
| 13900026 | Illegal seek |
| 13900042 | Unknown error |

## bytesWritten

```TypeScript
readonly bytesWritten: long
```

可写流已经写入的字节数。

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WriteStream-readonly bytesWritten: long--><!--Device-WriteStream-readonly bytesWritten: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## path

```TypeScript
readonly path: string
```

当前可写流对应的文件路径。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WriteStream-readonly path: string--><!--Device-WriteStream-readonly path: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

