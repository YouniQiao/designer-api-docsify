# getLocalDiskInfos

## Modules to Import

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
```

## getLocalDiskInfos

```TypeScript
function getLocalDiskInfos(): Promise<Array<LocalDiskInfo>>
```

Obtains hardware information about all local disks. This API uses a promise to return the result.

**Since:** 26.1.0

**Required permissions:** ohos.permission.GET_STORAGE_VOLUME_INFO

**Model restriction:** This API can be used only in the stage model.

<!--Device-volumeManager-function getLocalDiskInfos(): Promise<Array<LocalDiskInfo>>--><!--Device-volumeManager-function getLocalDiskInfos(): Promise<Array<LocalDiskInfo>>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[LocalDiskInfo](arkts-corefile-volumemanager-localdiskinfo-i.md)&gt;&gt; | Promise used to return the local disk hardware information list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| 13600001 | IPC error. |
