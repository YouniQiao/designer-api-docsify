# DowngradeDownload（系统接口）

全量下载：为云盘管理应用提供集中下载云端数据的能力。

云盘全量下载对象，用于支撑云盘管理应用完成云盘文件的全量下载流程。

**起始版本：** 20

<!--Device-cloudSyncManager-class DowngradeDownload--><!--Device-cloudSyncManager-class DowngradeDownload-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**系统接口：** 此接口为系统接口。

## constructor

```TypeScript
constructor(bundleName: string)
```

全量下载对象的构造函数，用于获取指定包名的DowngradeDownload类的实例。

**起始版本：** 20

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-DowngradeDownload-constructor(bundleName: string)--><!--Device-DowngradeDownload-constructor(bundleName: string)-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 22400005 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

获取需要全量下载的应用仅位于本地、仅位于云端或者本地和云端均有的文件大小和个数信息。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-DowngradeDownload-getCloudFileInfo(): Promise<CloudFileInfo>--><!--Device-DowngradeDownload-getCloudFileInfo(): Promise<CloudFileInfo>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;CloudFileInfo&gt; |

**错误码：**

| 错误码ID |
| --- |
| 22400005 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900010 |

## 示例

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

启动指定应用的云文件的全量下载，使用Promise异步回调。使用callback异步回调。

同一应用存在正在执行的全量下载任务的情况下，重复触发会返回错误信息（22400006）。

**起始版本：** 20

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-DowngradeDownload-startDownload(callback: Callback<DownloadProgress>): Promise<void>--><!--Device-DowngradeDownload-startDownload(callback: Callback<DownloadProgress>): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DownloadProgress&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 22400005 |
| 22400006 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900010 |

## 示例

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

将云盘目录下已完成本地下载的文件搬迁至指定目录，过程中通过回调上报搬迁进度。使用callback异步回调。

同一应用存在正在执行的搬迁任务的情况下，重复触发会返回错误信息（22400006）。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DowngradeDownload-startTransfer(targetUri: string, callback: Callback<TransferProgress>): void--><!--Device-DowngradeDownload-startTransfer(targetUri: string, callback: Callback<TransferProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetUri | string | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TransferProgress&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 22400006 |
| 13900001 |
| 13900002 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900010 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let targetPath: string = "file://docs/storage/Users/currentUser/Download/";
try {
    let downgradeMgr = new cloudSyncManager.DowngradeDownload("com.demo");
    downgradeMgr.startTransfer(targetPath, (data: cloudSyncManager.TransferProgress) => {
        console.info(`Transfer progress: successfulCount: ${data.successfulCount}, totalCount: ${data.totalCount}`);
    });
} catch (err) {
    let e = err as BusinessError;
    console.error(`transfer files failed with error message: ${e.message}, error code: ${e.code}`);
}
```

## stopDownload

```TypeScript
stopDownload(): Promise<void>
```

停止由[startDownload](arkts-corefile-cloudsyncmanager-downgradedownload-c-sys.md#startdownload)触发的全量下载任务，使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-DowngradeDownload-stopDownload(): Promise<void>--><!--Device-DowngradeDownload-stopDownload(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| 22400005 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName: string = "com.demo.a";
let downgradeMgr = new cloudSyncManager.DowngradeDownload(bundleName);
downgradeMgr.startDownload((data: cloudSyncManager.DownloadProgress) => {
  console.info(`Downgrade progress: downloadedSize: ${data.downloadedSize}, totalSize: ${data.totalSize}`);
}).then(() => {
  console.info("Downgrade started successfully.");
  let needStop = true;
  if (needStop) {
    downgradeMgr.stopDownload().then(() => {
      console.info("Downgrade stopped successfully.");
    }).catch((err: BusinessError) => {
      console.error(`Failed to stop downgrade, error message: ${err.message}, error code: ${err.code}`);
    });
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to start downgrade, error message: ${err.message}, error code: ${err.code}`);
});
```
