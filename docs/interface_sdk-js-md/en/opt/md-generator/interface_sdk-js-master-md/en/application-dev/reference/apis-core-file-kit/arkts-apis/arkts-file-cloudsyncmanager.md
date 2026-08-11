# @ohos.file.cloudSyncManager

The **cloudSyncManager** module provides APIs for managing device-cloud sync for applications. You can use the APIs to manage the full download state, the reason why the full download stops, and number of local and cloud files.

**Since:** 10

<!--Device-unnamed-declare namespace cloudSyncManager--><!--Device-unnamed-declare namespace cloudSyncManager-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## Modules to Import

```TypeScript
import { cloudSyncManager } from 'kits/@kit.CoreFileKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [changeAppCloudSwitch](arkts-corefile-cloudsyncmanager-changeappcloudswitch-f-sys.md#changeappcloudswitch) |
| [changeAppCloudSwitch](arkts-corefile-cloudsyncmanager-changeappcloudswitch-f-sys.md#changeappcloudswitch-1) |
| [clean](arkts-corefile-cloudsyncmanager-clean-f-sys.md#clean) |
| [clean](arkts-corefile-cloudsyncmanager-clean-f-sys.md#clean-1) |
| [disableCloud](arkts-corefile-cloudsyncmanager-disablecloud-f-sys.md#disablecloud) |
| [disableCloud](arkts-corefile-cloudsyncmanager-disablecloud-f-sys.md#disablecloud-1) |
| [enableCloud](arkts-corefile-cloudsyncmanager-enablecloud-f-sys.md#enablecloud) |
| [enableCloud](arkts-corefile-cloudsyncmanager-enablecloud-f-sys.md#enablecloud-1) |
| [getBundlesLocalFilePresentStatus](arkts-corefile-cloudsyncmanager-getbundleslocalfilepresentstatus-f-sys.md#getbundleslocalfilepresentstatus) |
| [getDowngradeDownloadTaskState](arkts-corefile-cloudsyncmanager-getdowngradedownloadtaskstate-f-sys.md#getdowngradedownloadtaskstate) |
| [notifyDataChange](arkts-corefile-cloudsyncmanager-notifydatachange-f-sys.md#notifydatachange) |
| [notifyDataChange](arkts-corefile-cloudsyncmanager-notifydatachange-f-sys.md#notifydatachange-1) |
| [notifyDataChange](arkts-corefile-cloudsyncmanager-notifydatachange-f-sys.md#notifydatachange-2) |
| [notifyDataChange](arkts-corefile-cloudsyncmanager-notifydatachange-f-sys.md#notifydatachange-3) |
<!--DelEnd-->

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DownloadProgress](arkts-corefile-cloudsyncmanager-downloadprogress-c.md) |

<!--Del-->
### Classes（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DowngradeDownload](arkts-corefile-cloudsyncmanager-downgradedownload-c-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CloudFileInfo](arkts-corefile-cloudsyncmanager-cloudfileinfo-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ExtraData](arkts-corefile-cloudsyncmanager-extradata-i-sys.md) |
| [LocalFilePresentStatus](arkts-corefile-cloudsyncmanager-localfilepresentstatus-i-sys.md) |
| [TransferProgress](arkts-corefile-cloudsyncmanager-transferprogress-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DownloadState](arkts-corefile-cloudsyncmanager-downloadstate-e.md) |
| [DownloadStopReason](arkts-corefile-cloudsyncmanager-downloadstopreason-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Action](arkts-corefile-cloudsyncmanager-action-e-sys.md) |
| [DownloadState](arkts-corefile-cloudsyncmanager-downloadstate-e-sys.md) |
| [TransferState](arkts-corefile-cloudsyncmanager-transferstate-e-sys.md) |
| [TransferStopReason](arkts-corefile-cloudsyncmanager-transferstopreason-e-sys.md) |
<!--DelEnd-->
