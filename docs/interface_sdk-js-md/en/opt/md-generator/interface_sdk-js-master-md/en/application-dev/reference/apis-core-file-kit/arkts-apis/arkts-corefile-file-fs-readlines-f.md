# readLines

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## readLines

```TypeScript
declare function readLines(filePath: string, options?: Options): Promise<ReaderIterator>
```

Reads the text content of a file line by line. This API uses a promise to return the result. Only the files in UTF-8format are supported.

**Since:** 11

<!--Device-unnamed-declare function readLines(filePath: string, options?: Options): Promise<ReaderIterator>--><!--Device-unnamed-declare function readLines(filePath: string, options?: Options): Promise<ReaderIterator>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ReaderIterator&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900022 |
| 13900019 |
| 13900030 |
| 13900025 |
| 13900027 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900044 |
| 13900015 |
| 13900041 |
| 13900042 |


## readLines

```TypeScript
declare function readLines(filePath: string, callback: AsyncCallback<ReaderIterator>): void
```

Reads a file text line by line. This API uses an asynchronous callback to return the result. Only the files in UTF-8format are supported.

**Since:** 11

<!--Device-unnamed-declare function readLines(filePath: string, callback: AsyncCallback<ReaderIterator>): void--><!--Device-unnamed-declare function readLines(filePath: string, callback: AsyncCallback<ReaderIterator>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ReaderIterator&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900022 |
| 13900033 |
| 13900002 |
| 13900019 |
| 13900012 |
| 13900030 |
| 13900015 |
| 13900025 |
| 13900041 |
| 13900042 |
| 13900027 |


## readLines

```TypeScript
declare function readLines(filePath: string, options: Options, callback: AsyncCallback<ReaderIterator>): void
```

Reads a file text line by line. This API uses an asynchronous callback to return the result. Only the files in UTF-8format are supported.

**Since:** 11

<!--Device-unnamed-declare function readLines(filePath: string, options: Options, callback: AsyncCallback<ReaderIterator>): void--><!--Device-unnamed-declare function readLines(filePath: string, options: Options, callback: AsyncCallback<ReaderIterator>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ReaderIterator&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900022 |
| 13900033 |
| 13900002 |
| 13900019 |
| 13900012 |
| 13900030 |
| 13900015 |
| 13900025 |
| 13900041 |
| 13900042 |
| 13900027 |
