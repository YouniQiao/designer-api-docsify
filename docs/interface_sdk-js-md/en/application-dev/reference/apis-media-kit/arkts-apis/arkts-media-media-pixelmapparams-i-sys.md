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

## autoFlip

```TypeScript
autoFlip?: boolean
```

Auto flip the thumbnail when video has mirror attribute (Vertical Flip or Horizontal Flip).If the value is false, the returned thumbnail will not be flipped.

**System API**: This is a system API.

**Type:** boolean

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-PixelMapParams-autoFlip?: boolean--><!--Device-PixelMapParams-autoFlip?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**System API:** This is a system API.

## colorFormat

```TypeScript
colorFormat?: PixelFormat
```

Color format of the thumbnail.

**System API**: This is a system API.

**Type:** [PixelFormat](arkts-media-media-pixelformat-e-sys.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PixelMapParams-colorFormat?: PixelFormat--><!--Device-PixelMapParams-colorFormat?: PixelFormat-End-->

**System capability:** SystemCapability.Multimedia.Media.AVImageGenerator

**System API:** This is a system API.

