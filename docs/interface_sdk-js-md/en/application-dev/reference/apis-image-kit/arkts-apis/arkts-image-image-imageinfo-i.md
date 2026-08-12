# ImageInfo

Describes image information.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-image-interface ImageInfo--><!--Device-image-interface ImageInfo-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## alphaType

```TypeScript
alphaType: AlphaType
```

Alpha type.

**Type:** [AlphaType](arkts-image-image-alphatype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageInfo-alphaType: AlphaType--><!--Device-ImageInfo-alphaType: AlphaType-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## density

```TypeScript
density: int
```

Pixel density, in ppi.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageInfo-density: int--><!--Device-ImageInfo-density: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## isHdr

```TypeScript
isHdr: boolean
```

Whether the image is an HDR image. The value **true** means an HDR image, and **false** means an SDR image. For   
[ImageSource](arkts-image-image-imagesource-i.md#ImageSource), this parameter specifies whether the source image is in HDR format. For [PixelMap](arkts-image-image-pixelmap-i.md#PixelMap), this parameter specifies whether the decoded PixelMap is in HDR format.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ImageInfo-isHdr: boolean--><!--Device-ImageInfo-isHdr: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## mimeType

```TypeScript
mimeType: string
```

Actual image format (MIME type).

The supported formats for image decoding and image encoding are different. Do not directly use the actual image format obtained after decoding as the value of **format** in [PackingOption](arkts-image-image-packingoption-i.md#PackingOption) during image encoding.

You can use the **supportedFormats** property of   
[ImageSource](@ohos.multimedia.image: image.ImageSource#supportedFormats) and   
[ImagePacker](@ohos.multimedia.image: image.ImagePacker#supportedFormats) to view the supported formats for decoding and encoding.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ImageInfo-mimeType: string--><!--Device-ImageInfo-mimeType: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## pixelFormat

```TypeScript
pixelFormat: PixelMapFormat
```

Pixel format.

**Type:** PixelMapFormat

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageInfo-pixelFormat: PixelMapFormat--><!--Device-ImageInfo-pixelFormat: PixelMapFormat-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## size

```TypeScript
size: Size
```

Image size.

**Type:** Size

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageInfo-size: Size--><!--Device-ImageInfo-size: Size-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## stride

```TypeScript
stride: int
```

Number of bytes from one row of pixels in memory to the next row of pixels in memory.stride >= region.size.width*4

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageInfo-stride: int--><!--Device-ImageInfo-stride: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

