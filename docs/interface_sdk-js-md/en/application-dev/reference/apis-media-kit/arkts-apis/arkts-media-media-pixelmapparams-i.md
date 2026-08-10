# PixelMapParams

Defines the format parameters of the video thumbnail to be obtained.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-media-interface PixelMapParams--><!--Device-media-interface PixelMapParams-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## height

```TypeScript
height?: int
```

Height of the thumbnail. Unit: px.The value must be greater than 0 and less than or equal to the height of the original video.Otherwise, the returned thumbnail will not be scaled.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PixelMapParams-height?: int--><!--Device-PixelMapParams-height?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

## width

```TypeScript
width?: int
```

Width of the thumbnail. Unit: px.The value must be greater than 0 and less than or equal to the width of the original video.Otherwise, the returned thumbnail will not be scaled.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PixelMapParams-width?: int--><!--Device-PixelMapParams-width?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

