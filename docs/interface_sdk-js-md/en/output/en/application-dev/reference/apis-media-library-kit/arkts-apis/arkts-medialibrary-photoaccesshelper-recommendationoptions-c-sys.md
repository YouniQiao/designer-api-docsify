# RecommendationOptions

Defines the image recommendation options. The image recommendation feature depends on the image data analysis capability, which varies with devices.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 26.0.0.

<!--Device-photoAccessHelper-class RecommendationOptions--><!--Device-photoAccessHelper-class RecommendationOptions-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## defaultRecommendationType

```TypeScript
defaultRecommendationType?: RecommendationType
```

Recommended tag displayed when the picker is opened. This configuration takes effect only after **recommendationTypeList** is set. If the tag exists, the tag page is displayed by default. If the tag does not exist, the All tag page is displayed by default.

**Type:** RecommendationType

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 24; ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RecommendationOptions-defaultRecommendationType?: RecommendationType--><!--Device-RecommendationOptions-defaultRecommendationType?: RecommendationType-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## recommendationTypeList

```TypeScript
recommendationTypeList?: Array<RecommendationType>
```

List of recommendation types. If images of multiple categories need to be recommended based on the enumerated value, set this parameter.

**Type:** Array&lt;RecommendationType&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 23; ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RecommendationOptions-recommendationTypeList?: Array<RecommendationType>--><!--Device-RecommendationOptions-recommendationTypeList?: Array<RecommendationType>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

