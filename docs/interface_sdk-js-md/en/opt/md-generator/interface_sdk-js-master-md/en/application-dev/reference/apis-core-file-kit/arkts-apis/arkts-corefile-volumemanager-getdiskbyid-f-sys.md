# getDiskById (System API)

## Modules to Import

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
```

## getDiskById

```TypeScript
function getDiskById(diskId: string): Promise<Disk>
```

Querying disk information based on the disk ID.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MOUNT_UNMOUNT_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-volumeManager-function getDiskById(diskId: string): Promise<Disk>--><!--Device-volumeManager-function getDiskById(diskId: string): Promise<Disk>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| diskId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Disk](arkts-corefile-volumemanager-disk-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600010 |
| 13600008 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
