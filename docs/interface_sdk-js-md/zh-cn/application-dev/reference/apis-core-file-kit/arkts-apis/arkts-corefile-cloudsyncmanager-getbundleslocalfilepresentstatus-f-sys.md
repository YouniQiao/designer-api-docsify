# getBundlesLocalFilePresentStatus（系统接口）

## 导入模块

```TypeScript
import { cloudSyncManager } from 'kits/@kit.CoreFileKit';
```

## getBundlesLocalFilePresentStatus

```TypeScript
function getBundlesLocalFilePresentStatus(bundleNames: Array<string>): Promise<Array<LocalFilePresentStatus>>
```

对接入云盘的应用，检测其在云盘存储空间内是否存在未上云文件，支持同时查询多个应用。使用Promise异步回调。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-cloudSyncManager-function getBundlesLocalFilePresentStatus(bundleNames: Array<string>): Promise<Array<LocalFilePresentStatus>>--><!--Device-cloudSyncManager-function getBundlesLocalFilePresentStatus(bundleNames: Array<string>): Promise<Array<LocalFilePresentStatus>>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleNames | Array&lt;string&gt; | 是 | 需要检测的应用包名数组。每个元素为应用的包名字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;LocalFilePresentStatus&gt;&gt; | Promise对象，返回对象数组，数组内每个对象包含指定检测的应用包名及其本地文件存在状态。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. Possible causes: &lt;br&gt;1.Mandatory parameter are left unspecified. 2.The length of the input parameter exceeds the upper limit. &lt;br&gt;3.The input parameter contains an invalid bundleName. |
| 22400005 | Inner error. Possible causes: &lt;br&gt;1.Failed to access the database or execute the SQL statement. &lt;br&gt;2.System error, such as a null pointer, insufficient memory or a JS engine exception. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600001 | IPC error. Possible causes: &lt;br&gt;1.IPC failed or timed out. 2.Failed to load the service. |
| 13900010 | Try again. |

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

