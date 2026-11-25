# triggerCloudCheck (System API)

## Modules to Import

```TypeScript
import { cloudSyncManager } from '@kit.CoreFileKit';
```

## triggerCloudCheck

```TypeScript
function triggerCloudCheck(userId: number, bundleName: string): Promise<number>
```

触发指定应用的云文件校验。使用Promise异步回调。

**Since:** 26.1.0

**Required permissions:** ohos.permission.CLOUDFILE_SYNC_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-cloudSyncManager-function triggerCloudCheck(userId: int, bundleName: string): Promise<int>--><!--Device-cloudSyncManager-function triggerCloudCheck(userId: int, bundleName: string): Promise<int>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | number | Yes | 用户ID。<br>取值限定为整数。 |
| bundleName | string | Yes | 应用包名 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回API调用状态。值为**0**表示请求已接受；其他值为错误码，错误码对应信息见下方。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| 13600001 | IPC error. Possible cause: <br>1.The cloud sync service is not loaded. <br>2.The IPC connection is broken. |
| 22400001 | Cloud is not ready. |
| 22400002 | Network is not available. |
| 22400003 | Battery is too low to perform sync. |
| 22400005 | Inner service error. |
| 22400006 | Another sync task is running. |
