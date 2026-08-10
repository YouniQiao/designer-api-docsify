# HdrDecomposeOptions (System API)

HDR PixelMap分解为Picture的配置选项，分解后的Picture包含一张SDR主图和一张增益图（GainMap）。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-image-interface HdrDecomposeOptions--><!--Device-image-interface HdrDecomposeOptions-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## desiredPixelFormat

```TypeScript
desiredPixelFormat?: PixelMapFormat
```

分解后SDR PixelMap和增益图的像素格式。支持RGBA_8888、NV12、NV21。默认值为RGBA_8888。

**Type:** [PixelMapFormat](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-multimedia-movingphotoview-pixelmapformat-e-sys.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-HdrDecomposeOptions-desiredPixelFormat?: PixelMapFormat--><!--Device-HdrDecomposeOptions-desiredPixelFormat?: PixelMapFormat-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

## isFullSizeGainmap

```TypeScript
isFullSizeGainmap?: boolean
```

是否生成全尺寸增益图。

true表示生成全尺寸增益图，增益图尺寸和主图一致；false表示不生成全尺寸增益图，增益图尺寸是主图的一半。默认值为false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-HdrDecomposeOptions-isFullSizeGainmap?: boolean--><!--Device-HdrDecomposeOptions-isFullSizeGainmap?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

