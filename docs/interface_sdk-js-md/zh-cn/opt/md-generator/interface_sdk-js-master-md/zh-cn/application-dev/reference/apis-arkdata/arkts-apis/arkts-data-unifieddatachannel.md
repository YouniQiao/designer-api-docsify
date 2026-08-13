# @ohos.data.unifiedDataChannel

本模块为统一数据管理框架（Unified Data Management Framework，UDMF）的组成部分，针对多对多跨应用数据共享的不同业务场景提供了标准化的数据通路，提供了标准化的数据接入与读取接口。同时对文本、图片等数据 类型提供了标准化定义，方便不同应用间进行数据交互，减少数据类型适配的工作量。 **设计逻辑：** UDMF采用统一数据模型，将不同类型的数据封装为UnifiedData对象，通过Intention标识不同的数据通路类型（如DATA_HUB、DRAG等），实现跨应用数据共享。数据写入时生成唯一标识符key，数据读 取时通过key或intention查询获取。 UDMF处理数据时，不会解析用户数据的内容，存储路径安全性较低，不建议传输个人敏感数据和隐私数据。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace unifiedDataChannel--><!--Device-unnamed-declare namespace unifiedDataChannel-End-->

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

## 汇总

### 函数

| 名称 |
| --- |
| [convertRecordsToEntries](arkts-arkdata-unifieddatachannel-convertrecordstoentries-f.md#convertRecordsToEntries) |
| [deleteData](arkts-arkdata-unifieddatachannel-deletedata-f.md#deleteData) |
| [deleteData](arkts-arkdata-unifieddatachannel-deletedata-f.md#deleteData) |
| [insertData](arkts-arkdata-unifieddatachannel-insertdata-f.md#insertData) |
| [insertData](arkts-arkdata-unifieddatachannel-insertdata-f.md#insertData) |
| [queryData](arkts-arkdata-unifieddatachannel-querydata-f.md#queryData) |
| [queryData](arkts-arkdata-unifieddatachannel-querydata-f.md#queryData) |
| [updateData](arkts-arkdata-unifieddatachannel-updatedata-f.md#updateData) |
| [updateData](arkts-arkdata-unifieddatachannel-updatedata-f.md#updateData) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [removeAppShareOptions](arkts-arkdata-unifieddatachannel-removeappshareoptions-f-sys.md#removeAppShareOptions（系统接口）) |
| [setAppShareOptions](arkts-arkdata-unifieddatachannel-setappshareoptions-f-sys.md#setAppShareOptions（系统接口）) |
<!--DelEnd-->

### 类

| 名称 |
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

### 接口

| 名称 |
| --- |
| [DataLoadInfo](arkts-arkdata-unifieddatachannel-dataloadinfo-i.md) |
| [DataLoadParams](arkts-arkdata-unifieddatachannel-dataloadparams-i.md) |
| [GetDataParams](arkts-arkdata-unifieddatachannel-getdataparams-i.md) |
| [Options](arkts-arkdata-unifieddatachannel-options-i.md) |
| [ProgressInfo](arkts-arkdata-unifieddatachannel-progressinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [FileConflictOptions](arkts-arkdata-unifieddatachannel-fileconflictoptions-e.md) |
| [Intention](arkts-arkdata-unifieddatachannel-intention-e.md) |
| [ListenerStatus](arkts-arkdata-unifieddatachannel-listenerstatus-e.md) |
| [ProgressIndicator](arkts-arkdata-unifieddatachannel-progressindicator-e.md) |
| [ShareOptions](arkts-arkdata-unifieddatachannel-shareoptions-e.md) |
| [UriPermission](arkts-arkdata-unifieddatachannel-uripermission-e.md) |
| [Visibility](arkts-arkdata-unifieddatachannel-visibility-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [Intention](arkts-arkdata-unifieddatachannel-intention-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [DataLoadHandler](arkts-arkdata-unifieddatachannel-dataloadhandler-t.md) |
| [DataProgressListener](arkts-arkdata-unifieddatachannel-dataprogresslistener-t.md) |
| [DelayedDataLoadHandler](arkts-arkdata-unifieddatachannel-delayeddataloadhandler-t.md) |
| [GetDelayData](arkts-arkdata-unifieddatachannel-getdelaydata-t.md) |
| [ValueType](arkts-arkdata-unifieddatachannel-valuetype-t.md) |
