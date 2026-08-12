# Video

视频类型数据，是[File](arkts-arkdata-unifieddatachannel-file-c.md#File)的子类，用于描述视频文件。

**继承/实现关系：** Video extends [File](arkts-arkdata-unifieddatachannel-file-c.md#File)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-unifiedDataChannel-class Video extends File--><!--Device-unifiedDataChannel-class Video extends File-End-->

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

## videoUri

```TypeScript
set videoUri(value: string)
```

本地视频数据uri或网络视频uri，本地视频数据uri可通过[getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md#getUriFromPath)函数获取。

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Video-set videoUri(value: string)--><!--Device-Video-set videoUri(value: string)-End-->

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

