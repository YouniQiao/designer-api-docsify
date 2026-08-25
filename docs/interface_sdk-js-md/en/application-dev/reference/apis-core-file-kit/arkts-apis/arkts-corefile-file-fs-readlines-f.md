# readLines

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## readLines

```TypeScript
declare function readLines(filePath: string, options?: Options): Promise<ReaderIterator>
```

Reads the text content of a file line by line. This API uses a promise to return the result. Only the files in UTF-8 format are supported.

**Since:** 11

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| options | [Options](arkts-corefile-file-fs-options-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900002 |
| 13900012 |
| 13900015 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900033 |
| 13900041 |
| 13900042 |
| 13900044 |


## readLines

```TypeScript
declare function readLines(filePath: string, callback: AsyncCallback<ReaderIterator>): void
```

Reads a file text line by line. This API uses an asynchronous callback to return the result. Only the files in UTF-8 format are supported.

**Since:** 11

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900002 |
| 13900012 |
| 13900015 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900033 |
| 13900041 |
| 13900042 |


## readLines

```TypeScript
declare function readLines(filePath: string, options: Options, callback: AsyncCallback<ReaderIterator>): void
```

Reads a file text line by line. This API uses an asynchronous callback to return the result. Only the files in UTF-8 format are supported.

**Since:** 11

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| options | [Options](arkts-corefile-file-fs-options-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ReaderIterator](arkts-corefile-file-fs-readeriterator-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900002 |
| 13900012 |
| 13900015 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900025 |
| 13900027 |
| 13900030 |
| 13900033 |
| 13900041 |
| 13900042 |
