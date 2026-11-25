# offCheckTrigger (System API)

## Modules to Import

```TypeScript
import { cloudSyncManager } from '@kit.CoreFileKit';
```

## offCheckTrigger

```TypeScript
function offCheckTrigger(): void
```

取消订阅云盘校验完成事件。

**Since:** 26.1.0

**Required permissions:** ohos.permission.CLOUDFILE_SYNC_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-cloudSyncManager-function offCheckTrigger(): void--><!--Device-cloudSyncManager-function offCheckTrigger(): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| 13600001 | IPC error. Possible cause: <br>1.IPC failed or timed out. 2.Failed to load the service. |
