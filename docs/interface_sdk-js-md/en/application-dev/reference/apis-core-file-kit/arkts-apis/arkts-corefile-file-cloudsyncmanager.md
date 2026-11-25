# @ohos.file.cloudSyncManager(Device-Cloud Sync Management)

The **cloudSyncManager** module provides APIs for managing device-cloud sync for applications. You can use the APIs to manage the full download state, the reason why the full download stops, and number of local and cloud files.

**Since:** 10

<!--Device-unnamed-declare namespace cloudSyncManager--><!--Device-unnamed-declare namespace cloudSyncManager-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## Modules to Import

```TypeScript
import { cloudSyncManager } from '@kit.CoreFileKit';
```

## Summary

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [changeAppCloudSwitch](arkts-corefile-cloudsyncmanager-changeappcloudswitch-f-sys.md#changeappcloudswitch-1) | Changes the device-cloud file sync switch for an application. This API uses a promise to return the result. |
| [changeAppCloudSwitch](arkts-corefile-cloudsyncmanager-changeappcloudswitch-f-sys.md#changeappcloudswitch-2) | Changes the device-cloud file sync switch for an application. This API uses an asynchronous callback to return the result. |
| [clean](arkts-corefile-cloudsyncmanager-clean-f-sys.md#clean-1) | Callback used to clear the cloud data locally. This API uses a promise to return the result. |
| [clean](arkts-corefile-cloudsyncmanager-clean-f-sys.md#clean-2) | Callback used to clear the cloud data locally. This API uses an asynchronous callback to return the result. |
| [disableCloud](arkts-corefile-cloudsyncmanager-disablecloud-f-sys.md#disablecloud-1) | Disables device-cloud sync. This API uses a promise to return the result. |
| [disableCloud](arkts-corefile-cloudsyncmanager-disablecloud-f-sys.md#disablecloud-2) | Disables device-cloud sync. This API uses an asynchronous callback to return the result. |
| [enableCloud](arkts-corefile-cloudsyncmanager-enablecloud-f-sys.md#enablecloud-1) | Enables device-cloud sync. This API uses a promise to return the result. |
| [enableCloud](arkts-corefile-cloudsyncmanager-enablecloud-f-sys.md#enablecloud-2) | Enables device-cloud sync. This API uses an asynchronous callback to return the result. |
| [getBundlesLocalFilePresentStatus](arkts-corefile-cloudsyncmanager-getbundleslocalfilepresentstatus-f-sys.md#getbundleslocalfilepresentstatus-1) | Obtains the existence status of local files for multiple applications and checks whether there are files that have not been uploaded to the cloud in the cloud storage space. This API uses a promise to return the result. |
| [getDowngradeDownloadTaskState](arkts-corefile-cloudsyncmanager-getdowngradedownloadtaskstate-f-sys.md#getdowngradedownloadtaskstate-1) | Supports querying the execution status of full data download tasks for integrated cloud drive applications. |
| [notifyDataChange](arkts-corefile-cloudsyncmanager-notifydatachange-f-sys.md#notifydatachange-1) | Notifies the device-cloud service that the cloud data of a specific application under a specified account has been changed. This API uses a promise to return the result. |
| [notifyDataChange](arkts-corefile-cloudsyncmanager-notifydatachange-f-sys.md#notifydatachange-2) | Notifies the device-cloud service that the cloud data of a specific application under a specified account has been changed. This API uses an asynchronous callback to return the result. |
| [notifyDataChange](arkts-corefile-cloudsyncmanager-notifydatachange-f-sys.md#notifydatachange-3) | Notifies the device-cloud service of the cloud data change information of a specified user. This API uses a promise to return the result. |
| [notifyDataChange](arkts-corefile-cloudsyncmanager-notifydatachange-f-sys.md#notifydatachange-4) | Notifies the device-cloud service of the cloud data change information of a specified user. This API uses an asynchronous callback to return the result. |
| [offCheckTrigger](arkts-corefile-cloudsyncmanager-offchecktrigger-f-sys.md#offchecktrigger-1) | 取消订阅云盘校验完成事件。 |
| [onCheckTrigger](arkts-corefile-cloudsyncmanager-onchecktrigger-f-sys.md#onchecktrigger-1) | 订阅校验完成事件，使用callback异步回调。 |
| [triggerCloudCheck](arkts-corefile-cloudsyncmanager-triggercloudcheck-f-sys.md#triggercloudcheck-1) | 触发指定应用的云文件校验。使用Promise异步回调。 |
<!--DelEnd-->

### Classes

| Name | Description |
| --- | --- |
| [DownloadProgress](arkts-corefile-cloudsyncmanager-downloadprogress-c.md) | Describes the full download progress. |

<!--Del-->
### Classes(System API)

| Name | Description |
| --- | --- |
| [DowngradeDownload](arkts-corefile-cloudsyncmanager-downgradedownload-c-sys.md) | Full download: provides the capability of downloading cloud data for applications. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [CloudFileInfo](arkts-corefile-cloudsyncmanager-cloudfileinfo-i.md) | Represents the number and size of local and cloud files of an application. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [CheckTriggerInfo](arkts-corefile-cloudsyncmanager-checktriggerinfo-i-sys.md) | 表示已完成的云盘校验的触发者及触发原因。 |
| [ExtraData](arkts-corefile-cloudsyncmanager-extradata-i-sys.md) | Represents the cloud data change information. |
| [LocalFilePresentStatus](arkts-corefile-cloudsyncmanager-localfilepresentstatus-i-sys.md) | Specifies a result object that contains the application bundle name and the status information about whether there are files that have not been uploaded to the cloud in the cloud storage space. |
| [TransferProgress](arkts-corefile-cloudsyncmanager-transferprogress-i-sys.md) | Defines the TransferProgress data structure. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [DownloadState](arkts-corefile-cloudsyncmanager-downloadstate-e.md) | Enumerates the full download states. |
| [DownloadStopReason](arkts-corefile-cloudsyncmanager-downloadstopreason-e.md) | Enumerates the reasons why the full download stops. The default value is **NO_STOP**. |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [Action](arkts-corefile-cloudsyncmanager-action-e-sys.md) | Enumerates the actions that can be taken to clear local cloud data. |
| [CheckTriggerReason](arkts-corefile-cloudsyncmanager-checktriggerreason-e-sys.md) | 云盘校验触发原因的枚举值。 |
| [DownloadState](arkts-corefile-cloudsyncmanager-downloadstate-e-sys.md) | Enumerates the full download states. |
| [TransferState](arkts-corefile-cloudsyncmanager-transferstate-e-sys.md) | Describes the state type of transfer task. |
| [TransferStopReason](arkts-corefile-cloudsyncmanager-transferstopreason-e-sys.md) | Describes the state type of transfer stop reason. |
<!--DelEnd-->
