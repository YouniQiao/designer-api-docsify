# getAllDisks (System API)

## Modules to Import

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
```

## getAllDisks

```TypeScript
function getAllDisks(): Promise<Array<Disk>>
```

Querying Information About All Disks.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MOUNT_UNMOUNT_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-volumeManager-function getAllDisks(): Promise<Array<Disk>>--><!--Device-volumeManager-function getAllDisks(): Promise<Array<Disk>>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Disk](arkts-corefile-volumemanager-disk-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
