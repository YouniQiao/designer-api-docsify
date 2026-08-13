# RecommendationOptions

Defines the image recommendation options. The image recommendation feature depends on the image data analysis capability, which varies with devices.

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-photoAccessHelper-class RecommendationOptions--><!--Device-photoAccessHelper-class RecommendationOptions-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## recommendationType

```TypeScript
recommendationType?: RecommendationType
```

Type of the recommended image.

**Type:** [RecommendationType](arkts-medialibrary-photoaccesshelper-recommendationtype-e.md)

**Since:** 26.0.0

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RecommendationOptions-recommendationType?: RecommendationType--><!--Device-RecommendationOptions-recommendationType?: RecommendationType-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## textContextInfo

```TypeScript
textContextInfo?: TextContextInfo
```

Text based on which images are recommended. If both **recommendationType** and **textContextInfo** are set, **textContextInfo** takes precedence over **recommendationType**.

**Type:** [TextContextInfo](arkts-medialibrary-photoaccesshelper-textcontextinfo-i.md)

**Since:** 26.0.0

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RecommendationOptions-textContextInfo?: TextContextInfo--><!--Device-RecommendationOptions-textContextInfo?: TextContextInfo-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core
