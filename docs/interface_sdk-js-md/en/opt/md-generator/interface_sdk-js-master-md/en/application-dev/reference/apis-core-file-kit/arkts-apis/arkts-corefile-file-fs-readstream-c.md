# ReadStream

Defines a readable stream. You need to use  
[fileIo.createReadStream](../../../reference/apis-core-file-kit/js-apis-file-fs.md#fileiocreatereadstream12) to create a **ReadStream** instance, which is inherited from  
[stream.Readable](../../apis-arkts/arkts-apis/arkts-arkts-stream-readableoptions-i.md#ReadableOptions).

The data obtained by **ReadStream** is a decoded string. Currently, only the UTF-8 format is supported.

**Inheritance/Implementation:** ReadStream extends [stream.Readable](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md#Readable)

**Since:** 12

<!--Device-unnamed-declare class ReadStream extends stream.Readable--><!--Device-unnamed-declare class ReadStream extends stream.Readable-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## close

```TypeScript
close(): void
```

Closes this readable stream.

**Since:** 12

<!--Device-ReadStream-close(): void--><!--Device-ReadStream-close(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |

## Examples

```TypeScript
const filePath = pathDir + "/test.txt";
const rs = fileIo.createReadStream(filePath);
rs.close();
```

## constructor

```TypeScript
constructor()
```

The ReadStream constructor.

**Since:** 12

<!--Device-ReadStream-constructor()--><!--Device-ReadStream-constructor()-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## seek

```TypeScript
seek(offset: number, whence?: WhenceType): number
```

Adjusts the position of the readable stream offset pointer.

**Since:** 12

<!--Device-ReadStream-seek(offset: number, whence?: WhenceType): number--><!--Device-ReadStream-seek(offset: number, whence?: WhenceType): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |
| whence | [WhenceType](arkts-corefile-file-fs-whencetype-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900026 |
| 13900042 |

## Examples

```TypeScript
const filePath = pathDir + "/test.txt";
const rs = fileIo.createReadStream(filePath);
const curOff = rs.seek(5, fileIo.WhenceType.SEEK_SET);
console.info(`Succeeded in seeking, current offset is ${curOff}`);
rs.close();
```

## bytesRead

```TypeScript
readonly bytesRead: number
```

Number of bytes read by the readable stream.

**Type:** number

**Since:** 12

<!--Device-ReadStream-readonly bytesRead: number--><!--Device-ReadStream-readonly bytesRead: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## path

```TypeScript
readonly path: string
```

Path of the file corresponding to the readable stream.

**Type:** string

**Since:** 12

<!--Device-ReadStream-readonly path: string--><!--Device-ReadStream-readonly path: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO
