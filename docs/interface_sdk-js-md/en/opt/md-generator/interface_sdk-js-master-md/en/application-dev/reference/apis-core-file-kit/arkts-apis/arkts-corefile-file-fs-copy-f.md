# copy

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## copy

```TypeScript
declare function copy(srcUri: string, destUri: string, options?: CopyOptions): Promise<void>
```

Copies a file or directory. This API uses a promise to return the result.

File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be the URI of the file or directory.

A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500.

**Since:** 11

<!--Device-unnamed-declare function copy(srcUri: string, destUri: string, options?: CopyOptions): Promise<void>--><!--Device-unnamed-declare function copy(srcUri: string, destUri: string, options?: CopyOptions): Promise<void>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900038 |
| 13900034 |
| 13900044 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900021 |
| 13900022 |
| 13900018 |
| 13900019 |
| 13900028 |
| 13900030 |
| 13900031 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900005 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900015 |
| 13900008 |
| 13900010 |
| 13900011 |


## copy

```TypeScript
declare function copy(srcUri: string, destUri: string, callback: AsyncCallback<void>): void
```

Copies a file or directory. This API uses an asynchronous callback to return the result.

File copy across devices is supported. This API forcibly overwrites the file or directory.The input parameter can be the URI of the file or directory. A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500.

**Since:** 11

<!--Device-unnamed-declare function copy(srcUri: string, destUri: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function copy(srcUri: string, destUri: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| srcUri | string | Yes |
| destUri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900038 |
| 13900034 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900021 |
| 13900022 |
| 13900018 |
| 13900019 |
| 13900028 |
| 13900030 |
| 13900031 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900005 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900015 |
| 13900008 |
| 13900010 |
| 13900011 |


## copy

```TypeScript
declare function copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback<void>): void
```

Copies a file or directory. This API uses an asynchronous callback to return the result.

File copy across devices is supported. This API forcibly overwrites the file or directory.The input parameter can be the URI of the file or directory. A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time cannot exceed 500.

**Since:** 11

<!--Device-unnamed-declare function copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| srcUri | string | Yes |
| destUri | string | Yes |
| options | [CopyOptions](arkts-corefile-file-fs-copyoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900038 |
| 13900034 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900021 |
| 13900022 |
| 13900018 |
| 13900019 |
| 13900028 |
| 13900030 |
| 13900031 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900005 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900015 |
| 13900008 |
| 13900010 |
| 13900011 |
