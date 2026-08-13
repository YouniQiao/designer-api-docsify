# CloudFileCache

Provides APIs for the file manager application to download files from the Drive Kit to a local device.

**Since:** 23

**Deprecated since:** -1

<!--Device-cloudSync-class CloudFileCache--><!--Device-cloudSync-class CloudFileCache-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## Modules to Import

```TypeScript
import { cloudSync } from '@kit.CoreFileKit';
```

## cleanCache

```TypeScript
cleanCache(uri: string): void
```

Deletes a cache file. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-CloudFileCache-cleanCache(uri: string): void--><!--Device-CloudFileCache-cleanCache(uri: string): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13900002 |
| 14000002 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

try {
  fileCache.cleanCache(uri);
} catch (err) {
  let error:BusinessError = err as BusinessError;
  console.error("clean cache failed with error message: " + err.message + ", error code: " + err.code);
}
```

## constructor

```TypeScript
constructor(bundleName: string)
```

A constructor used to create a CloudFileCache object.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CloudFileCache-constructor(bundleName: string)--><!--Device-CloudFileCache-constructor(bundleName: string)-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getDownloadList

```TypeScript
getDownloadList(uris: Array<string>): Promise<Array<DownloadProgress>>
```

Query the download state of the cloud file list.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

**Model restriction:** This API can be used only in the stage model.

<!--Device-CloudFileCache-getDownloadList(uris: Array<string>): Promise<Array<DownloadProgress>>--><!--Device-CloudFileCache-getDownloadList(uris: Array<string>): Promise<Array<DownloadProgress>>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uris | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;DownloadProgress & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900010 |
