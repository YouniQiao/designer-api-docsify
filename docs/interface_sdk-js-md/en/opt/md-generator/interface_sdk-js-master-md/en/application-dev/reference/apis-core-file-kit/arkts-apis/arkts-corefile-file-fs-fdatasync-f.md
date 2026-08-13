# fdatasync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## fdatasync

```TypeScript
declare function fdatasync(fd: number): Promise<void>
```

Synchronizes the data of a file. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** -1

<!--Device-unnamed-declare function fdatasync(fd: number): Promise<void>--><!--Device-unnamed-declare function fdatasync(fd: number): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |
| 13900027 |


## fdatasync

```TypeScript
declare function fdatasync(fd: number, callback: AsyncCallback<void>): void
```

Synchronizes the data of a file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** -1

<!--Device-unnamed-declare function fdatasync(fd: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function fdatasync(fd: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |
| 13900027 |
