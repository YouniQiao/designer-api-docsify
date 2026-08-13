# rename

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## rename

```TypeScript
declare function rename(oldPath: string, newPath: string): Promise<void>
```

Renames a file or directory. This API uses a promise to return the result. > **NOTE：**> > This API is not supported in a distributed directory.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function rename(oldPath: string, newPath: string): Promise<void>--><!--Device-unnamed-declare function rename(oldPath: string, newPath: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| oldPath | string | Yes |
| newPath | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900016 |
| 13900018 |
| 13900019 |
| 13900028 |
| 13900025 |
| 13900027 |
| 13900032 |
| 13900001 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |


## rename

```TypeScript
declare function rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void
```

Renames a file or directory. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is not supported in a distributed directory.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| oldPath | string | Yes |
| newPath | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900016 |
| 13900018 |
| 13900019 |
| 13900028 |
| 13900025 |
| 13900027 |
| 13900032 |
| 13900001 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |
