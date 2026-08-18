# createPartition (System API)

## Modules to Import

```TypeScript
```

## createPartition

```TypeScript
function createPartition(diskId: string, params: PartitionParams): Promise<void>
```

Creates a partition on a disk. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MOUNT_FORMAT_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-volumeManager-function createPartition(diskId: string, params: PartitionParams): Promise<void>--><!--Device-volumeManager-function createPartition(diskId: string, params: PartitionParams): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| diskId | string | Yes |
| params | [PartitionParams](arkts-corefile-volumemanager-partitionparams-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600010 |
| 13600008 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 13600022 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600005 |
| 13600002 |
| 13600001 |
