# ImageInfo

表示图片信息。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-image-interface ImageInfo--><!--Device-image-interface ImageInfo-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## alphaType

```TypeScript
alphaType: AlphaType
```

透明度。

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

像素密度。单位：ppi（像素/英寸）。

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

true表示图片为高动态范围（HDR），false表示图片非高动态范围（SDR）。对于[ImageSource](arkts-image-image-imagesource-i.md)，代表源图片是否为HDR；对于  
[PixelMap](arkts-image-image-pixelmap-i.md)，代表解码后的PixelMap是否为HDR。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ImageInfo-isHdr: boolean--><!--Device-ImageInfo-isHdr: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## mimeType

```TypeScript
mimeType: string
```

图片真实格式（MIME type）。

图片解码和图片编码支持格式的范围不同，请避免直接将解码得到的图片真实格式作为图片编码时[PackingOption](arkts-image-image-packingoption-i.md)的format。

可以使用ImageSource[属性](../../../reference/apis-image-kit/arkts-apis-image-ImageSource.md#属性)中的supportedFormats和ImagePacker[属性](../../../reference/apis-image-kit/arkts-apis-image-ImagePacker.md#属性)中的supportedFormats查看解码和编码支持的格式范围。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ImageInfo-mimeType: string--><!--Device-ImageInfo-mimeType: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## pixelFormat

```TypeScript
pixelFormat: PixelMapFormat
```

像素格式。

**Type:** [PixelMapFormat](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-multimedia-movingphotoview-pixelmapformat-e.md)

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

图片大小。

**Type:** [Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md)

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

跨距，内存中每行像素所占的空间。单位：字节（Byte）。stride >= size.width * 4，不满足时数据读取异常。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageInfo-stride: int--><!--Device-ImageInfo-stride: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

