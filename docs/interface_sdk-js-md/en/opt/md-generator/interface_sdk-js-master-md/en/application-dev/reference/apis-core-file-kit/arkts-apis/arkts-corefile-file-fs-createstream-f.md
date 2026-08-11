# createStream

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## createStream

```TypeScript
declare function createStream(path: string, mode: string): Promise<Stream>
```

Creates a stream based on a file path. This API uses a promise to return the result. To close the stream, use  
**close()** of [Stream](arkts-corefile-file-fs-stream-i.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-unnamed-declare function createStream(path: string, mode: string): Promise<Stream>--><!--Device-unnamed-declare function createStream(path: string, mode: string): Promise<Stream>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| mode | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Stream&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900038 |
| 13900033 |
| 13900034 |
| 13900044 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900029 |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900006 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900008 |
| 13900011 |


## createStream

```TypeScript
declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void
```

Creates a stream based on a file path. This API uses an asynchronous callback to return the result. To close the stream, use **close()** of [Stream](arkts-corefile-file-fs-stream-i.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-unnamed-declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void--><!--Device-unnamed-declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| mode | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Stream&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900038 |
| 13900033 |
| 13900034 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900029 |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900006 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900008 |
| 13900011 |
