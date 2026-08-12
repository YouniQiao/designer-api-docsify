# getDowngradeDownloadTaskState（系统接口）

## getDowngradeDownloadTaskState

```TypeScript
function getDowngradeDownloadTaskState(bundleNames: Array<string>): Promise<Array<DownloadProgress>>
```

查询接入云盘的应用的全量下载任务状态。使用Promise异步回调。

由于返回的DownloadProgress对象中不包含包名信息，因此在批量查询多个应用时，调用方需自行记录应用包名。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-cloudSyncManager-function getDowngradeDownloadTaskState(bundleNames: Array<string>): Promise<Array<DownloadProgress>>--><!--Device-cloudSyncManager-function getDowngradeDownloadTaskState(bundleNames: Array<string>): Promise<Array<DownloadProgress>>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleNames | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;DownloadProgress & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| 13900010 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundles: Array<string> = ['com.example.app1', 'com.example.app2'];
cloudSyncManager.getDowngradeDownloadTaskState(bundles).then((results: Array<cloudSyncManager.DownloadProgress>) => {
  results.forEach((item) => {
    console.info(`state: ${item.state}, downloadedSize: ${item.downloadedSize}, totalSize: ${item.totalSize}`);
    console.info(`successfulCount: ${item.successfulCount}, failedCount: ${item.failedCount}, totalCount: ${item.totalCount}`);
    if (item.state == cloudSyncManager.DownloadState.STOPPED) {
      console.info(`stopReason: ${item.stopReason}`);
    }
  });
}).catch((err: BusinessError) => {
  console.error(`getDowngradeDownloadTaskState failed, code: ${err.code}, message: ${err.message}`);
});
```
