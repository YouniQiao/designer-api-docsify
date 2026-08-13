# lstat

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## lstat

```TypeScript
declare function lstat(path: string): Promise<Stat>
```

Obtains information about a symbolic link that is used to refer to a file or directory. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** -1

<!--Device-unnamed-declare function lstat(path: string): Promise<Stat>--><!--Device-unnamed-declare function lstat(path: string): Promise<Stat>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Stat](arkts-corefile-file-fs-stat-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900038 |
| 13900033 |
| 13900002 |
| 13900018 |
| 13900012 |
| 13900013 |
| 13900030 |
| 13900008 |
| 13900042 |
| 13900011 |


## lstat

```TypeScript
declare function lstat(path: string, callback: AsyncCallback<Stat>): void
```

Obtains information about a symbolic link that is used to refer to a file or directory. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** -1

<!--Device-unnamed-declare function lstat(path: string, callback: AsyncCallback<Stat>): void--><!--Device-unnamed-declare function lstat(path: string, callback: AsyncCallback<Stat>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Stat](arkts-corefile-file-fs-stat-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900038 |
| 13900033 |
| 13900002 |
| 13900018 |
| 13900012 |
| 13900013 |
| 13900030 |
| 13900008 |
| 13900042 |
| 13900011 |
