# AuxiliaryPictureInfo

表示辅助图的图像信息。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-image-interface AuxiliaryPictureInfo--><!--Device-image-interface AuxiliaryPictureInfo-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## auxiliaryPictureType

```TypeScript
auxiliaryPictureType: AuxiliaryPictureType
```

辅助图的图像类型。

**Type:** [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md)

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-AuxiliaryPictureInfo-auxiliaryPictureType: AuxiliaryPictureType--><!--Device-AuxiliaryPictureInfo-auxiliaryPictureType: AuxiliaryPictureType-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## colorSpace

```TypeScript
colorSpace: colorSpaceManager.ColorSpaceManager
```

目标色彩空间。

**Type:** colorSpaceManager.ColorSpaceManager

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-AuxiliaryPictureInfo-colorSpace: colorSpaceManager.ColorSpaceManager--><!--Device-AuxiliaryPictureInfo-colorSpace: colorSpaceManager.ColorSpaceManager-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## pixelFormat

```TypeScript
pixelFormat: PixelMapFormat
```

像素格式。

**Type:** [PixelMapFormat](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-multimedia-movingphotoview-pixelmapformat-e.md)

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-AuxiliaryPictureInfo-pixelFormat: PixelMapFormat--><!--Device-AuxiliaryPictureInfo-pixelFormat: PixelMapFormat-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## rowStride

```TypeScript
rowStride: int
```

行跨距。单位：字节（Byte）。应大于或等于图像每行像素数据所占的字节数，不满足时数据读取异常。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-AuxiliaryPictureInfo-rowStride: int--><!--Device-AuxiliaryPictureInfo-rowStride: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## size

```TypeScript
size: Size
```

图片大小。

**Type:** [Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md)

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-AuxiliaryPictureInfo-size: Size--><!--Device-AuxiliaryPictureInfo-size: Size-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

