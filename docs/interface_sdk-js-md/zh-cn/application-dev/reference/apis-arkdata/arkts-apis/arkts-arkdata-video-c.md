# Video

视频类型数据，是[File](arkts-arkdata-file-c.md)的子类，用于描述视频文件。

**继承/实现关系：** Video extends [File](arkts-arkdata-file-c.md)

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

## videoUri

```TypeScript
set videoUri(value: string)
```

本地视频数据uri或网络视频uri，本地视频数据uri可通过[getUriFromPath](@ohos.file.fileuri:fileUri.getUriFromPath)函数获取。

**类型：** string

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本11开始，该接口支持在元服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

