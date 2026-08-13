# PixelMapParams

Defines the format parameters of the video thumbnail to be obtained.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-media-interface PixelMapParams--><!--Device-media-interface PixelMapParams-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## height

```TypeScript
height?: int
```

Height of the thumbnail. Unit: px. The value must be greater than 0 and less than or equal to the height of the original video. Otherwise, the returned thumbnail will not be scaled.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-PixelMapParams-height?: int--><!--Device-PixelMapParams-height?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

## width

```TypeScript
width?: int
```

Width of the thumbnail. Unit: px. The value must be greater than 0 and less than or equal to the width of the original video. Otherwise, the returned thumbnail will not be scaled.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-PixelMapParams-width?: int--><!--Device-PixelMapParams-width?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

