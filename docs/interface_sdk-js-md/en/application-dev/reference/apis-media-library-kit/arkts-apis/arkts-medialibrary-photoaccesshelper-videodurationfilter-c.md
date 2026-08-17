# VideoDurationFilter

Describes the configuration for video duration filtering.

**Since:** 26.0.0

<!--Device-photoAccessHelper-class VideoDurationFilter--><!--Device-photoAccessHelper-class VideoDurationFilter-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from 'photoAccessHelper';
```

## extraVideoDuration

```TypeScript
extraVideoDuration?: int
```

Maximum video duration in **FilterOperator.BETWEEN** mode. The default value is **-1**. The unit is milliseconds (ms).

**Type:** int

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-VideoDurationFilter-extraVideoDuration?: int--><!--Device-VideoDurationFilter-extraVideoDuration?: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## filterOperator

```TypeScript
filterOperator: FilterOperator
```

Filter operator. For example, files can be filtered based on being greater than or less than a certain file size.

**Type:** [FilterOperator](arkts-medialibrary-photoaccesshelper-filteroperator-e.md)

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-VideoDurationFilter-filterOperator: FilterOperator--><!--Device-VideoDurationFilter-filterOperator: FilterOperator-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## videoDuration

```TypeScript
videoDuration: int
```

Video duration used for filtering. The unit is milliseconds (ms).

**Type:** int

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-VideoDurationFilter-videoDuration: int--><!--Device-VideoDurationFilter-videoDuration: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

