# Image

图片类型数据，是[File](arkts-arkdata-file-c.md)的子类，用于描述图片文件。

**继承/实现关系：** Image extends [File](arkts-arkdata-file-c.md)

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

## imageUri

```TypeScript
set imageUri(value: string)
```

本地图片数据uri或网络图片uri，本地图片数据uri可通过[getUriFromPath](@ohos.file.fileuri:fileUri.getUriFromPath)函数获取。

**类型：** string

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本11开始，该接口支持在元服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

