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

**Required permissions:** ohos.permission.MOUNT_FORMAT_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| diskId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PartitionTableInfo](arkts-corefile-volumemanager-partitiontableinfo-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13600008 |
| 13600010 |
| 13600021 |
