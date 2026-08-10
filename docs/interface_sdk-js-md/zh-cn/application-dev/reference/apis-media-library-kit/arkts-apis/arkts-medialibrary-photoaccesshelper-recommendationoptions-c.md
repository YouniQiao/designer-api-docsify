# RecommendationOptions

Defines the image recommendation options. The image recommendation feature depends on the image data analysis capability, which varies with devices.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为26.0.0。

<!--Device-photoAccessHelper-class RecommendationOptions--><!--Device-photoAccessHelper-class RecommendationOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## recommendationType

```TypeScript
recommendationType?: RecommendationType
```

Type of the recommended image.

**类型：** [RecommendationType](arkts-medialibrary-photoaccesshelper-recommendationtype-e.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-RecommendationOptions-recommendationType?: RecommendationType--><!--Device-RecommendationOptions-recommendationType?: RecommendationType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## textContextInfo

```TypeScript
textContextInfo?: TextContextInfo
```

Text based on which images are recommended. If both **recommendationType** and **textContextInfo** are set,   
**textContextInfo** takes precedence over **recommendationType**.

**类型：** [TextContextInfo](arkts-medialibrary-photoaccesshelper-textcontextinfo-i.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RecommendationOptions-textContextInfo?: TextContextInfo--><!--Device-RecommendationOptions-textContextInfo?: TextContextInfo-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

