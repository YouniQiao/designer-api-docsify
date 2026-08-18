# getDowngradeDownloadTaskState (System API)

## Modules to Import

```TypeScript
```

## getDowngradeDownloadTaskState

```TypeScript
function getDowngradeDownloadTaskState(bundleNames: Array<string>): Promise<Array<DownloadProgress>>
```

Supports querying the execution status of full data download tasks for integrated cloud drive applications.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CLOUDFILE_SYNC_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-cloudSyncManager-function getDowngradeDownloadTaskState(bundleNames: Array<string>): Promise<Array<DownloadProgress>>--><!--Device-cloudSyncManager-function getDowngradeDownloadTaskState(bundleNames: Array<string>): Promise<Array<DownloadProgress>>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleNames | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;DownloadProgress & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900010 |
