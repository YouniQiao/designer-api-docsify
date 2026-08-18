# formatPartition (System API)

## Modules to Import

```TypeScript
```

## formatPartition

```TypeScript
function formatPartition(diskId: string, partitionNum: number, params: FormatParams): Promise<void>
```

Formats a partition on a disk. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MOUNT_FORMAT_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-volumeManager-function formatPartition(diskId: string, partitionNum: int, params: FormatParams): Promise<void>--><!--Device-volumeManager-function formatPartition(diskId: string, partitionNum: int, params: FormatParams): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| diskId | string | Yes |
| partitionNum | number | Yes |
| params | [FormatParams](arkts-corefile-volumemanager-formatparams-i-sys.md) | Yes |

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600005 |
| 13600002 |
| 13600001 |
| 13600032 |
