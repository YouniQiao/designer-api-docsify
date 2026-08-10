# SourceOptions

ImageSource的初始化选项。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-image-interface SourceOptions--><!--Device-image-interface SourceOptions-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## sourceDensity

```TypeScript
sourceDensity: int
```

图片资源像素密度。单位：ppi（像素/英寸）。

在解码参数[DecodingOptions](arkts-image-image-decodingoptions-i.md)未设置desiredSize的前提下，当前参数SourceOptions.sourceDensity与DecodingOptions.fitDensity非零时将对解码输出的pixelmap进行缩放。

缩放后宽计算公式如下(高同理)：(width * fitDensity + (sourceDensity >> 1)) / sourceDensity。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-SourceOptions-sourceDensity: int--><!--Device-SourceOptions-sourceDensity: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## sourcePixelFormat

```TypeScript
sourcePixelFormat?: PixelMapFormat
```

图片像素格式，默认值为UNKNOWN。

**Type:** [PixelMapFormat](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-multimedia-movingphotoview-pixelmapformat-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-SourceOptions-sourcePixelFormat?: PixelMapFormat--><!--Device-SourceOptions-sourcePixelFormat?: PixelMapFormat-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## sourceSize

```TypeScript
sourceSize?: Size
```

图像像素大小，默认值为空。

**Type:** [Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-SourceOptions-sourceSize?: Size--><!--Device-SourceOptions-sourceSize?: Size-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

