# @ohos.data.unifiedDataChannel(标准化数据通路)

本模块为统一数据管理框架（Unified Data Management Framework，UDMF）的组成部分，针对多对多跨应用数据共享的不同业务场景提供了标准化的数据通路，提供了标准化的数据接入与读取接口。同时对文本、图片等数据 类型提供了标准化定义，方便不同应用间进行数据交互，减少数据类型适配的工作量。  
**设计逻辑：** UDMF采用统一数据模型，将不同类型的数据封装为UnifiedData对象，通过Intention标识不同的数据通路类型（如DATA_HUB、DRAG等），实现跨应用数据共享。数据写入时生成唯一标识符key，数据读 取时通过key或intention查询获取。UDMF处理数据时，不会解析用户数据的内容，存储路径安全性较低，不建议传输个人敏感数据和隐私数据。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

## 导入模块

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## 汇总

### 函数

| 名称 |
| --- |
| [convertRecordsToEntries(标准化数据通路)](arkts-arkdata-unifieddatachannel-convertrecordstoentries-f.md) |
| [deleteData(标准化数据通路)](arkts-arkdata-unifieddatachannel-deletedata-f.md) |
| [deleteData(标准化数据通路)](arkts-arkdata-unifieddatachannel-deletedata-f.md) |
| [insertData(标准化数据通路)](arkts-arkdata-unifieddatachannel-insertdata-f.md) |
| [insertData(标准化数据通路)](arkts-arkdata-unifieddatachannel-insertdata-f.md) |
| [queryData(标准化数据通路)](arkts-arkdata-unifieddatachannel-querydata-f.md) |
| [queryData(标准化数据通路)](arkts-arkdata-unifieddatachannel-querydata-f.md) |
| [removeAppShareOptions(标准化数据通路)](arkts-arkdata-unifieddatachannel-removeappshareoptions-f.md) |
| [setAppShareOptions(标准化数据通路)](arkts-arkdata-unifieddatachannel-setappshareoptions-f.md) |
| [updateData(标准化数据通路)](arkts-arkdata-unifieddatachannel-updatedata-f.md) |
| [updateData(标准化数据通路)](arkts-arkdata-unifieddatachannel-updatedata-f.md) |

### 类

| 名称 |
| --- |
| [ApplicationDefinedRecord(标准化数据通路)](arkts-arkdata-unifieddatachannel-applicationdefinedrecord-c.md) |
| [Audio(标准化数据通路)](arkts-arkdata-unifieddatachannel-audio-c.md) |
| [File(标准化数据通路)](arkts-arkdata-unifieddatachannel-file-c.md) |
| [Folder(标准化数据通路)](arkts-arkdata-unifieddatachannel-folder-c.md) |
| [HTML(标准化数据通路)](arkts-arkdata-unifieddatachannel-html-c.md) |
| [Hyperlink(标准化数据通路)](arkts-arkdata-unifieddatachannel-hyperlink-c.md) |
| [Image(标准化数据通路)](arkts-arkdata-unifieddatachannel-image-c.md) |
| [PlainText(标准化数据通路)](arkts-arkdata-unifieddatachannel-plaintext-c.md) |
| [Summary(标准化数据通路)](arkts-arkdata-unifieddatachannel-summary-c.md) |
| [SystemDefinedAppItem(标准化数据通路)](arkts-arkdata-unifieddatachannel-systemdefinedappitem-c.md) |
| [SystemDefinedForm(标准化数据通路)](arkts-arkdata-unifieddatachannel-systemdefinedform-c.md) |
| [SystemDefinedPixelMap(标准化数据通路)](arkts-arkdata-unifieddatachannel-systemdefinedpixelmap-c.md) |
| [SystemDefinedRecord(标准化数据通路)](arkts-arkdata-unifieddatachannel-systemdefinedrecord-c.md) |
| [Text(标准化数据通路)](arkts-arkdata-unifieddatachannel-text-c.md) |
| [UnifiedData(标准化数据通路)](arkts-arkdata-unifieddatachannel-unifieddata-c.md) |
| [UnifiedDataProperties(标准化数据通路)](arkts-arkdata-unifieddatachannel-unifieddataproperties-c.md) |
| [UnifiedRecord(标准化数据通路)](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md) |
| [Video(标准化数据通路)](arkts-arkdata-unifieddatachannel-video-c.md) |

### 接口

| 名称 |
| --- |
| [DataLoadInfo(标准化数据通路)](arkts-arkdata-unifieddatachannel-dataloadinfo-i.md) |
| [DataLoadParams(标准化数据通路)](arkts-arkdata-unifieddatachannel-dataloadparams-i.md) |
| [GetDataParams(标准化数据通路)](arkts-arkdata-unifieddatachannel-getdataparams-i.md) |
| [Options(标准化数据通路)](arkts-arkdata-unifieddatachannel-options-i.md) |
| [ProgressInfo(标准化数据通路)](arkts-arkdata-unifieddatachannel-progressinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [FileConflictOptions(标准化数据通路)](arkts-arkdata-unifieddatachannel-fileconflictoptions-e.md) |
| [Intention(标准化数据通路)](arkts-arkdata-unifieddatachannel-intention-e.md) |
| [ListenerStatus(标准化数据通路)](arkts-arkdata-unifieddatachannel-listenerstatus-e.md) |
| [ProgressIndicator(标准化数据通路)](arkts-arkdata-unifieddatachannel-progressindicator-e.md) |
| [ShareOptions(标准化数据通路)](arkts-arkdata-unifieddatachannel-shareoptions-e.md) |
| [UriPermission(标准化数据通路)](arkts-arkdata-unifieddatachannel-uripermission-e.md) |
| [Visibility(标准化数据通路)](arkts-arkdata-unifieddatachannel-visibility-e.md) |

### 类型

| 名称 |
| --- |
| [DataLoadHandler(标准化数据通路)](arkts-arkdata-unifieddatachannel-dataloadhandler-t.md) |
| [DataProgressListener(标准化数据通路)](arkts-arkdata-unifieddatachannel-dataprogresslistener-t.md) |
| [DelayedDataLoadHandler(标准化数据通路)](arkts-arkdata-unifieddatachannel-delayeddataloadhandler-t.md) |
| [GetDelayData(标准化数据通路)](arkts-arkdata-unifieddatachannel-getdelaydata-t.md) |
| [ValueType(标准化数据通路)](arkts-arkdata-unifieddatachannel-valuetype-t.md) |
