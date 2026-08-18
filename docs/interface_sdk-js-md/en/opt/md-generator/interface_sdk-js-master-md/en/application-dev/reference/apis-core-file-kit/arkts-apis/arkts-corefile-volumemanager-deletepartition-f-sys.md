# deletePartition (System API)

## Modules to Import

```TypeScript
```

## deletePartition

```TypeScript
function deletePartition(diskId: string, partitionNum: number): Promise<void>
```

Deletes a partition on a disk. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MOUNT_FORMAT_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-volumeManager-function deletePartition(diskId: string, partitionNum: int): Promise<void>--><!--Device-volumeManager-function deletePartition(diskId: string, partitionNum: int): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| diskId | string | Yes |
| partitionNum | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600010 |
| 13600008 |
| 13600023 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600005 |
| 13600001 |
