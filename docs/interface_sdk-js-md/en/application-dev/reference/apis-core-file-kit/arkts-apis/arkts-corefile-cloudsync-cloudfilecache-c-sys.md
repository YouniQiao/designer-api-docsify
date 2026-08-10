# CloudFileCache

云盘文件缓存对象，用来支撑文件管理应用原文件下载流程。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cloudSync-class CloudFileCache--><!--Device-cloudSync-class CloudFileCache-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## Modules to Import

```TypeScript
import { cloudSync } from 'kits/@kit.CoreFileKit';
```

## cleanCache

```TypeScript
cleanCache(uri: string): void
```

同步方法删除文件缓存。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-CloudFileCache-cleanCache(uri: string): void--><!--Device-CloudFileCache-cleanCache(uri: string): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 待删除缓存文件的uri。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 13900002 | No such file or directory. |
| 14000002 | Invalid uri. |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 13600001 | IPC error. |

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CloudFileCache-constructor(bundleName: string)--><!--Device-CloudFileCache-constructor(bundleName: string)-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Name of the bundle that need to start download task and subscribes download progress. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | The caller is not a system application. |

## getDownloadList

```TypeScript
getDownloadList(uris: Array<string>): Promise<Array<DownloadProgress>>
```

获取文件下载进度列表。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

**Model restriction:** This API can be used only in the stage model.

<!--Device-CloudFileCache-getDownloadList(uris: Array<string>): Promise<Array<DownloadProgress>>--><!--Device-CloudFileCache-getDownloadList(uris: Array<string>): Promise<Array<DownloadProgress>>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uris | Array&lt;string&gt; | Yes | 待查询下载进度的文件URI数组，数组长度取值范围[1,100]。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;DownloadProgress&gt;&gt; | Promise对象，返回文件下载进度列表的结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument. Possible causes: &lt;br&gt;1.Mandatory parameters are left unspecified. 2.The length of the input parameter exceeds the upper limit. &lt;br&gt;3.The input parameter contains an invalid uri. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13900010 | Try again. |

