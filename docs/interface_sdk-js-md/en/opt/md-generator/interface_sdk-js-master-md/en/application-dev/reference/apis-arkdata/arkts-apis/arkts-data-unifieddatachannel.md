# @ohos.data.unifiedDataChannel

As a part of the Unified Data Management Framework (UDMF), the **unifiedDataChannel** module provides unified data channels and standard data access interfaces for many-to-many data sharing across applications. It also provides definitions for uniform data types, such as text and image, to streamline data interaction between different applications and minimize the workload of data type adaptation. Although the UDMF does not parse user data, you are advised not to transfer sensitive personal data or privacy data due to low-level security of storage path.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace unifiedDataChannel--><!--Device-unnamed-declare namespace unifiedDataChannel-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [convertRecordsToEntries](arkts-arkdata-unifieddatachannel-convertrecordstoentries-f.md#convertrecordstoentries) |
| [deleteData](arkts-arkdata-unifieddatachannel-deletedata-f.md#deletedata) |
| [deleteData](arkts-arkdata-unifieddatachannel-deletedata-f.md#deletedata) |
| [insertData](arkts-arkdata-unifieddatachannel-insertdata-f.md#insertdata) |
| [insertData](arkts-arkdata-unifieddatachannel-insertdata-f.md#insertdata) |
| [queryData](arkts-arkdata-unifieddatachannel-querydata-f.md#querydata) |
| [queryData](arkts-arkdata-unifieddatachannel-querydata-f.md#querydata) |
| [updateData](arkts-arkdata-unifieddatachannel-updatedata-f.md#updatedata) |
| [updateData](arkts-arkdata-unifieddatachannel-updatedata-f.md#updatedata) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [removeAppShareOptions](arkts-arkdata-unifieddatachannel-removeappshareoptions-f-sys.md#removeappshareoptions-system-api) |
| [setAppShareOptions](arkts-arkdata-unifieddatachannel-setappshareoptions-f-sys.md#setappshareoptions-system-api) |
<!--DelEnd-->

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ApplicationDefinedRecord](arkts-arkdata-unifieddatachannel-applicationdefinedrecord-c.md) |
| [Audio](arkts-arkdata-unifieddatachannel-audio-c.md) |
| [File](arkts-arkdata-unifieddatachannel-file-c.md) |
| [Folder](arkts-arkdata-unifieddatachannel-folder-c.md) |
| [HTML](arkts-arkdata-unifieddatachannel-html-c.md) |
| [Hyperlink](arkts-arkdata-unifieddatachannel-hyperlink-c.md) |
| [Image](arkts-arkdata-unifieddatachannel-image-c.md) |
| [PlainText](arkts-arkdata-unifieddatachannel-plaintext-c.md) |
| [Summary](arkts-arkdata-unifieddatachannel-summary-c.md) |
| [SystemDefinedAppItem](arkts-arkdata-unifieddatachannel-systemdefinedappitem-c.md) |
| [SystemDefinedForm](arkts-arkdata-unifieddatachannel-systemdefinedform-c.md) |
| [SystemDefinedPixelMap](arkts-arkdata-unifieddatachannel-systemdefinedpixelmap-c.md) |
| [SystemDefinedRecord](arkts-arkdata-unifieddatachannel-systemdefinedrecord-c.md) |
| [Text](arkts-arkdata-unifieddatachannel-text-c.md) |
| [UnifiedData](arkts-arkdata-unifieddatachannel-unifieddata-c.md) |
| [UnifiedDataProperties](arkts-arkdata-unifieddatachannel-unifieddataproperties-c.md) |
| [UnifiedRecord](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md) |
| [Video](arkts-arkdata-unifieddatachannel-video-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DataLoadInfo](arkts-arkdata-unifieddatachannel-dataloadinfo-i.md) |
| [DataLoadParams](arkts-arkdata-unifieddatachannel-dataloadparams-i.md) |
| [GetDataParams](arkts-arkdata-unifieddatachannel-getdataparams-i.md) |
| [Options](arkts-arkdata-unifieddatachannel-options-i.md) |
| [ProgressInfo](arkts-arkdata-unifieddatachannel-progressinfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FileConflictOptions](arkts-arkdata-unifieddatachannel-fileconflictoptions-e.md) |
| [Intention](arkts-arkdata-unifieddatachannel-intention-e.md) |
| [ListenerStatus](arkts-arkdata-unifieddatachannel-listenerstatus-e.md) |
| [ProgressIndicator](arkts-arkdata-unifieddatachannel-progressindicator-e.md) |
| [ShareOptions](arkts-arkdata-unifieddatachannel-shareoptions-e.md) |
| [UriPermission](arkts-arkdata-unifieddatachannel-uripermission-e.md) |
| [Visibility](arkts-arkdata-unifieddatachannel-visibility-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Intention](arkts-arkdata-unifieddatachannel-intention-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DataLoadHandler](arkts-arkdata-unifieddatachannel-dataloadhandler-t.md) |
| [DataProgressListener](arkts-arkdata-unifieddatachannel-dataprogresslistener-t.md) |
| [DelayedDataLoadHandler](arkts-arkdata-unifieddatachannel-delayeddataloadhandler-t.md) |
| [GetDelayData](arkts-arkdata-unifieddatachannel-getdelaydata-t.md) |
| [ValueType](arkts-arkdata-unifieddatachannel-valuetype-t.md) |
