# HdrComposeOptions

Picture合成HDR时可配置的参数选项。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-image-interface HdrComposeOptions--><!--Device-image-interface HdrComposeOptions-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## desiredPixelFormat

```TypeScript
desiredPixelFormat?: PixelMapFormat
```

用于合成图像的像素格式，支持RGBA_1010102、YCBCR_P010和YCRCB_P010格式。

**Type:** [PixelMapFormat](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-multimedia-movingphotoview-pixelmapformat-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-HdrComposeOptions-desiredPixelFormat?: PixelMapFormat--><!--Device-HdrComposeOptions-desiredPixelFormat?: PixelMapFormat-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

