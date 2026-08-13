# getBundlesLocalFilePresentStatus（系统接口）

## getBundlesLocalFilePresentStatus

```TypeScript
function getBundlesLocalFilePresentStatus(bundleNames: Array<string>): Promise<Array<LocalFilePresentStatus>>
```

对接入云盘的应用，检测其在云盘存储空间内是否存在未上云文件，支持同时查询多个应用。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-cloudSyncManager-function getBundlesLocalFilePresentStatus(bundleNames: Array<string>): Promise<Array<LocalFilePresentStatus>>--><!--Device-cloudSyncManager-function getBundlesLocalFilePresentStatus(bundleNames: Array<string>): Promise<Array<LocalFilePresentStatus>>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleNames | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[LocalFilePresentStatus](arkts-corefile-cloudsyncmanager-localfilepresentstatus-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 22400005 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900010 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundles: Array<string> = ['com.example.app1', 'com.example.app2'];
cloudSyncManager.getBundlesLocalFilePresentStatus(bundles).then((results: Array<cloudSyncManager.LocalFilePresentStatus>) => {
  results.forEach((item) => {
    console.info(`bundle: ${item.bundleName}, hasLocalUncloudedFiles: ${item.isLocalFilePresent}`);
  });
}).catch((err: BusinessError) => {
  console.error(`getBundlesLocalFilePresentStatus failed, code: ${err.code}, message: ${err.message}`);
});
```
