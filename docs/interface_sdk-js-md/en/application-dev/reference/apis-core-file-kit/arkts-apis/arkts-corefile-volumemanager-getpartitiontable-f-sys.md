# getPartitionTable (System API)

## Modules to Import

```TypeScript
import { volumeManager } from 'kits/@kit.CoreFileKit';
```

## getPartitionTable

```TypeScript
function getPartitionTable(diskId: string): Promise<PartitionTableInfo>
```

Obtains partition table information based on the disk ID. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.MOUNT_FORMAT_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-volumeManager-function getPartitionTable(diskId: string): Promise<PartitionTableInfo>--><!--Device-volumeManager-function getPartitionTable(diskId: string): Promise<PartitionTableInfo>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| diskId | string | Yes | Disk ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PartitionTableInfo&gt; | Promise used to return the partition table information of the current disk ID. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13600010 | The input parameter is invalid. |
| 13600008 | No such object. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| 13600021 | Get partition table failed. |
| 13600001 | IPC error. |

