# DowngradeDownload (System API)

Full download: provides the capability of downloading cloud data for applications. It supports the full download of cloud application files.

**Since:** 23

<!--Device-cloudSyncManager-class DowngradeDownload--><!--Device-cloudSyncManager-class DowngradeDownload-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(bundleName: string)
```

A constructor used to create an instance of the **DowngradeDownload** class with a specified bundle name.

**Since:** 23

**Required permissions:** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-DowngradeDownload-constructor(bundleName: string)--><!--Device-DowngradeDownload-constructor(bundleName: string)-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 22400005 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.demo.a';
try {
  let downgradeMgr = new cloudSyncManager.DowngradeDownload(bundleName);
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to create downgrade manager object, error code: ${error.code}, message: ${error.message}`);
}
```

## getCloudFileInfo

```TypeScript
getCloudFileInfo(): Promise<CloudFileInfo>
```

Obtains the size and count of files for applications requiring full download, including those stored only locally , only in the cloud, or both locally and in the cloud. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-DowngradeDownload-getCloudFileInfo(): Promise<CloudFileInfo>--><!--Device-DowngradeDownload-getCloudFileInfo(): Promise<CloudFileInfo>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CloudFileInfo](arkts-corefile-cloudsyncmanager-cloudfileinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 22400005 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13900010 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName: string = "com.demo.a";
let downgradeMgr = new cloudSyncManager.DowngradeDownload(bundleName);
downgradeMgr.getCloudFileInfo().then((fileInfo: cloudSyncManager.CloudFileInfo) => {
  console.info("cloud file info: " + JSON.stringify(fileInfo));
}).catch((err: BusinessError) => {
  console.error(`Failed to get downgrade info, error message: ${err.message}, error code: ${err.code}`);
});
```

## startDownload

```TypeScript
startDownload(callback: Callback<DownloadProgress>): Promise<void>
```

Starts the full download for the specified application's cloud files. This API uses a promise to return the result. This API uses an asynchronous callback to return the result. Repeated triggering of a full download task will throw an error (22400006).

**Since:** 23

**Required permissions:** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-DowngradeDownload-startDownload(callback: Callback<DownloadProgress>): Promise<void>--><!--Device-DowngradeDownload-startDownload(callback: Callback<DownloadProgress>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DownloadProgress&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 22400005 |
| 22400006 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13900010 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName: string = "com.demo.a";
let downgradeMgr = new cloudSyncManager.DowngradeDownload(bundleName);
let callback = (data: cloudSyncManager.DownloadProgress) => {
  console.info(`Downgrade progress: downloadedSize: ${data.downloadedSize}, totalSize: ${data.totalSize}`);
  if (data.state == cloudSyncManager.DownloadState.COMPLETED) {
    console.info('Downgrade finished.');
  } else if (data.state == cloudSyncManager.DownloadState.STOPPED) {
    console.info(`Downgrade stopped, reason: ${data.stopReason}.`);
  }
};
downgradeMgr.startDownload(callback).then(() => {
  console.info("Downgrade started successfully.");
}).catch((err: BusinessError) => {
  console.error(`Failed to start downgrade, error message: ${err.message}, error code: ${err.code}`);
});
```

## startTransfer

```TypeScript
startTransfer(targetUri: string, callback: Callback<TransferProgress>): void
```

Start to migrate the downloaded full data to the specified public directory of file management.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CLOUDFILE_SYNC_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-DowngradeDownload-startTransfer(targetUri: string, callback: Callback<TransferProgress>): void--><!--Device-DowngradeDownload-startTransfer(targetUri: string, callback: Callback<TransferProgress>): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| targetUri | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TransferProgress](arkts-corefile-cloudsyncmanager-transferprogress-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 22400006 |
| 13900001 |
| 13900002 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900010 |

## stopDownload

```TypeScript
stopDownload(): Promise<void>
```

Stops the full download task triggered by [startDownload](#startdownload) . This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-DowngradeDownload-stopDownload(): Promise<void>--><!--Device-DowngradeDownload-stopDownload(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 22400005 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName: string = "com.demo.a";
let downgradeMgr = new cloudSyncManager.DowngradeDownload(bundleName);
downgradeMgr.startDownload((data: cloudSyncManager.DownloadProgress) => {
  console.info(`Downgrade progress: downloadedSize: ${data.downloadedSize}, totalSize: ${data.totalSize}`);
}).then(() => {
  console.info("Downgrade started successfully.");
}).catch((err: BusinessError) => {
  console.error(`Failed to start downgrade, error message: ${err.message}, error code: ${err.code}`);
});

let needStop = true;
if (needStop) {
  downgradeMgr.stopDownload().then(() => {
    console.info("Downgrade stopped successfully.");
  }).catch((err: BusinessError) => {
    console.error(`Failed to stop downgrade, error message: ${err.message}, error code: ${err.code}`);
  });
}
```
