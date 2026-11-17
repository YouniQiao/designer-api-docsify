# getDiskPowerCycleCount

## Modules to Import

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
```

## getDiskPowerCycleCount

```TypeScript
function getDiskPowerCycleCount(sysPath: string): Promise<number>
```

Obtains the complete power cycle count of a specified disk since it was shipped. This API uses a promise to return the result. If the ioctl read fails (for example, the SATA HDD does not support it), **0** is returned.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_DISK

**Model restriction:** This API can be used only in the stage model.

<!--Device-volumeManager-function getDiskPowerCycleCount(sysPath: string): Promise<int>--><!--Device-volumeManager-function getDiskPowerCycleCount(sysPath: string): Promise<int>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sysPath | string | Yes | Physical path of the disk device node, such as **\/sys/block/nvme0n1**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the power cycle count of the disk. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| 13600001 | IPC error. |
| 13600002 | The file system is not supported. |
| 13600008 | The object does not exist. |
