# moveDir

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## moveDir

```TypeScript
declare function moveDir(src: string, dest: string, mode?: number): Promise<void>
```

Moves the source directory to the destination directory. This API uses a promise to return the result. > **NOTE：**> > This API is not supported in a distributed directory.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare function moveDir(src: string, dest: string, mode?: number): Promise<void>--><!--Device-unnamed-declare function moveDir(src: string, dest: string, mode?: number): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | string | Yes |
| dest | string | Yes |
| mode | number | No |

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


## moveDir

```TypeScript
declare function moveDir(src: string, dest: string, callback: AsyncCallback<void>): void
```

Moves the source directory to the destination directory. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare function moveDir(src: string, dest: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function moveDir(src: string, dest: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | string | Yes |
| dest | string | Yes |
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
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |


## moveDir

```TypeScript
declare function moveDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void
```

Moves the source directory to the destination directory. This API uses an asynchronous callback to return the result. An exception will be thrown if a directory conflict occurs, that is, the destination directory contains a directory with the same name as the source directory. > **NOTE：**> > This API is not supported in a distributed directory.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare function moveDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void--><!--Device-unnamed-declare function moveDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | string | Yes |
| dest | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void, Array&lt;[ConflictFiles](arkts-corefile-file-fs-conflictfiles-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900015 |


## moveDir

```TypeScript
declare function moveDir(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void
```

Moves the source directory to the destination directory. You can set the move mode. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare function moveDir(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function moveDir(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | string | Yes |
| dest | string | Yes |
| mode | number | Yes |
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
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |


## moveDir

```TypeScript
declare function moveDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void
```

Moves the source directory to the destination directory. You can set the move mode. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is not supported in a distributed directory.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare function moveDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void--><!--Device-unnamed-declare function moveDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | string | Yes |
| dest | string | Yes |
| mode | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void, Array&lt;[ConflictFiles](arkts-corefile-file-fs-conflictfiles-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900015 |
