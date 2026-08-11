# close

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## close

```TypeScript
declare function close(file: number | File): Promise<void>
```

Closes a file or directory. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function close(file: number | File): Promise<void>--><!--Device-unnamed-declare function close(file: number | File): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| file | number \| [File](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-request-file-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |


## close

```TypeScript
declare function close(file: number | File, callback: AsyncCallback<void>): void
```

Closes a file or directory. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function close(file: number | File, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function close(file: number | File, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| file | number \| [File](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-request-file-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |
