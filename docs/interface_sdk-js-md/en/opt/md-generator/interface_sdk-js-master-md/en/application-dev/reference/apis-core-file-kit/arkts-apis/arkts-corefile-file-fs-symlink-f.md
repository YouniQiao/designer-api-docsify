# symlink

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## symlink

```TypeScript
declare function symlink(target: string, srcPath: string): Promise<void>
```

Creates a symbolic link based on a file path. This API uses a promise to return the result.

> **NOTE：**
> 
> Since API version 11, this API cannot be used by third-party applications.

**Since:** 9

<!--Device-unnamed-declare function symlink(target: string, srcPath: string): Promise<void>--><!--Device-unnamed-declare function symlink(target: string, srcPath: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | string | Yes |
| srcPath | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900018 |
| 13900030 |
| 13900025 |
| 13900027 |
| 13900005 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |


## symlink

```TypeScript
declare function symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void
```

Creates a symbolic link based on the file path. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Since API version 11, this API cannot be used by third-party applications.

**Since:** 9

<!--Device-unnamed-declare function symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | string | Yes |
| srcPath | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900018 |
| 13900030 |
| 13900025 |
| 13900027 |
| 13900005 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |
