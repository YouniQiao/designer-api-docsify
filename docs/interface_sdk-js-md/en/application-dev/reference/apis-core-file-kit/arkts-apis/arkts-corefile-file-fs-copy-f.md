# copy

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## copy

```TypeScript
declare function copy(srcUri: string, destUri: string, options?: CopyOptions): Promise<void>
```

Copies a file or directory. This API uses a promise to return the result.File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be the URI of the file or directory.A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500.

**Since:** 11

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| srcUri | string | Yes |
| destUri | string | Yes |
| options | [CopyOptions](arkts-corefile-file-fs-copyoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900011 |
| 13900012 |
| 13900015 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900021 |
| 13900022 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900028 |
| 13900030 |
| 13900031 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 13900044 |


## copy

```TypeScript
declare function copy(srcUri: string, destUri: string, callback: AsyncCallback<void>): void
```

Copies a file or directory. This API uses an asynchronous callback to return the result.File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be the URI of the file or directory. A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500.

**Since:** 11

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| srcUri | string | Yes |
| destUri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900011 |
| 13900012 |
| 13900015 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900021 |
| 13900022 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900028 |
| 13900030 |
| 13900031 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |


## copy

```TypeScript
declare function copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback<void>): void
```

Copies a file or directory. This API uses an asynchronous callback to return the result.File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be the URI of the file or directory. A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500.

**Since:** 11

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| srcUri | string | Yes |
| destUri | string | Yes |
| options | [CopyOptions](arkts-corefile-file-fs-copyoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900011 |
| 13900012 |
| 13900015 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900021 |
| 13900022 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900028 |
| 13900030 |
| 13900031 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
