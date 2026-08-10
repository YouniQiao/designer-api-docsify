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

## defaultRecommendationType

```TypeScript
defaultRecommendationType?: RecommendationType
```

Recommended tag displayed when the picker is opened. This configuration takes effect only after   
**recommendationTypeList** is set.

If the tag exists, the tag page is displayed by default.

If the tag does not exist, the All tag page is displayed by default.

**类型：** [RecommendationType](arkts-medialibrary-photoaccesshelper-recommendationtype-e-sys.md)

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RecommendationOptions-defaultRecommendationType?: RecommendationType--><!--Device-RecommendationOptions-defaultRecommendationType?: RecommendationType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## recommendationTypeList

```TypeScript
recommendationTypeList?: Array<RecommendationType>
```

List of recommendation types. If images of multiple categories need to be recommended based on the enumerated value, set this parameter.

**类型：** Array&lt;RecommendationType&gt;

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RecommendationOptions-recommendationTypeList?: Array<RecommendationType>--><!--Device-RecommendationOptions-recommendationTypeList?: Array<RecommendationType>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

