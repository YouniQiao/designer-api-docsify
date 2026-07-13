# Audio

音频类型数据，是[File](arkts-arkdata-file-c.md)的子类，用于描述音频文件。

**继承/实现关系：** Audio extends [File](arkts-arkdata-file-c.md)

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

## audioUri

```TypeScript
set audioUri(value: string)
```

本地音频数据uri或网络音频uri，本地音频数据uri可通过[getUriFromPath](@ohos.file.fileuri:fileUri.getUriFromPath)函数获取。

**类型：** string

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本11开始，该接口支持在元服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

