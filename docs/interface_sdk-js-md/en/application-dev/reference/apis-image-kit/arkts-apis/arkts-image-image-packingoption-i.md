# PackingOption

表示图片编码选项。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-image-interface PackingOption--><!--Device-image-interface PackingOption-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## backgroundColor

```TypeScript
backgroundColor?: int
```

用于指定编码过程中透明区域填充的背景颜色。

当图片像素为RGBA_8888，且编码的目标格式不支持透明度（如"image/jpeg"或"image/heif"）时，透明区域将填充为指定背景颜色（格式：0xRRGGBB），默认值为 0（黑色）。

PNG、WebP等支持透明度的格式会忽略此参数。

颜色范围：0x000000 - 0xFFFFFF

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PackingOption-backgroundColor?: int--><!--Device-PackingOption-backgroundColor?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## bufferSize

```TypeScript
bufferSize?: int
```

接收编码数据的缓冲区大小，单位：字节（Byte）。如果不设置大小，默认为25MB。如果编码图片超过25MB，需要指定大小。bufferSize需大于编码后图片大小。使用  
[packToFile](arkts-image-image-imagepacker-i.md#packtofile)不受此参数限制。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PackingOption-bufferSize?: int--><!--Device-PackingOption-bufferSize?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## desiredDynamicRange

```TypeScript
desiredDynamicRange?: PackingDynamicRange
```

目标动态范围。默认值为SDR。

**Type:** [PackingDynamicRange](arkts-image-image-packingdynamicrange-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PackingOption-desiredDynamicRange?: PackingDynamicRange--><!--Device-PackingOption-desiredDynamicRange?: PackingDynamicRange-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## format

```TypeScript
format: string
```

目标格式。&lt;/br&gt;- 当[输入为ImageSource或PixelMap](../../../media/image/image-encoding.md)时，支持"image/jpeg"、"image/webp"、"image/png"和"image/heic（或者image/heif）"&lt;sup&gt;12+&lt;/sup&gt;、"image/sdr_astc_4x4"&lt;sup&gt;18+&lt;/sup&gt;、"image/sdr_sut_superfast_4x4"&lt;sup&gt;18+&lt;/sup&gt;（不同硬件设备支持情况不同）、"image/hdr_astc_4x4"&lt;sup&gt;20+&lt;/sup&gt;。

- 当[输入为Picture](../../../media/image/image-picture-encoding.md)时，仅支持"image/jpeg"和"image/heic（或者image/heif）"&lt;sup&gt;  
12+&lt;/sup&gt;。  
- gif图片编码需要输入多个PixelMap，并指定format为"image/gif"，使用  
[packToDataFromPixelmapSequence](arkts-image-image-imagepacker-i.md#packtodatafrompixelmapsequence)或  
[packToFileFromPixelmapSequence](arkts-image-image-imagepacker-i.md#packtofilefrompixelmapsequence)接口进行编码。

**说明：** 因为jpeg不支持透明通道，若使用带透明通道的数据编码jpeg格式，透明色将变为黑色。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PackingOption-format: string--><!--Device-PackingOption-format: string-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## maxEmbedThumbnailDimension

```TypeScript
maxEmbedThumbnailDimension?: int
```

用于指定编码过程中生成缩略图的最大边长（宽和高中较大的那一边），较短的一边会根据长边的缩放比例进行缩放。此参数仅在needsPackProperties设置为true时有效。

该值应为整数，默认值为0。

若未指定此参数，或根据该尺寸计算出生成的缩略图宽/高为0，则编码过程中不会生成缩略图。

单位：像素（px）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PackingOption-maxEmbedThumbnailDimension?: int--><!--Device-PackingOption-maxEmbedThumbnailDimension?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## needsPackGPS

```TypeScript
needsPackGPS?: boolean
```

是否在编码过程中保留GPS隐私信息。

true表示保留GPS信息，不进行隐私处理。false表示移除GPS信息（仅在源图像包含EXIF且needsPackProperties设置为true时生效）。默认值为true。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PackingOption-needsPackGPS?: boolean--><!--Device-PackingOption-needsPackGPS?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## needsPackProperties

```TypeScript
needsPackProperties?: boolean
```

是否需要编码图片属性信息，例如EXIF。true表示需要，false表示不需要。默认值为false。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PackingOption-needsPackProperties?: boolean--><!--Device-PackingOption-needsPackProperties?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## quality

```TypeScript
quality: int
```

1. 编码中设定输出图片质量的参数，该参数仅对JPEG图片和HEIF图片生效。取值范围：[0, 100]。0质量最低，100质量最高，质量越高生成图片所占空间越大。WebP、PNG等图片均为无损编码。

2.sdr_astc_4x4编码中，可以设定输出图片质量的参数，可选参数：92、85。

3. sut编码中，设定输出图片质量可选参数：92。4. （API version 20支持）hdr_astc_4x4编码中，可以设定输出图片质量的参数，可选参数：85。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PackingOption-quality: int--><!--Device-PackingOption-quality: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## sizeLimit

```TypeScript
sizeLimit?: PackingSizeLimit
```

用于指定编码输出图像的最大尺寸限制。

当原图宽度或高度超过最大尺寸maxSize的限制时，保持宽高比不变进行等比例缩小，确保输出图像尺寸不超过指定边界。缩放过程由level参数控制采用的缩放算法。

若未指定此参数，或根据最大尺寸计算的输出图宽/高为0，则按原图尺寸编码。

单位：像素（px）。

参数规则：

- maxSize = {0, 0}：不限制最大编码尺寸，按原图尺寸编码  
- maxSize.width > 0而maxSize.height &lt;= 0：限制最大宽度，高度不限（使用原图高度）  
- maxSize.width <= 0而maxSize.height > 0：限制最大高度，宽度不限（使用原图宽度）  
- maxSize.width &gt;&lt;= 0而maxSize.height &gt; 0：限制最大高度，宽度不限（使用原图宽度）  
- maxSize.width > 0且maxSize.height > 0：宽高同时限制，选择较小的缩放比例

默认值：{maxSize: {width: 0, height: 0}, level: AntiAliasingLevel.NONE}

**Type:** [PackingSizeLimit](arkts-image-image-packingsizelimit-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PackingOption-sizeLimit?: PackingSizeLimit--><!--Device-PackingOption-sizeLimit?: PackingSizeLimit-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

## tiffPackingOptions

```TypeScript
tiffPackingOptions?: PackingOptionsForTiff
```

TIFF图像编码选项。

**Type:** [PackingOptionsForTiff](arkts-image-image-packingoptionsfortiff-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PackingOption-tiffPackingOptions?: PackingOptionsForTiff--><!--Device-PackingOption-tiffPackingOptions?: PackingOptionsForTiff-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

