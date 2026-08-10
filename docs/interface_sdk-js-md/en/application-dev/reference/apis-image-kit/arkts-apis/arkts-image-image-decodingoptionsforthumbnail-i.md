# DecodingOptionsForThumbnail

缩略图解码参数选项。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-image-interface DecodingOptionsForThumbnail--><!--Device-image-interface DecodingOptionsForThumbnail-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## generateThumbnailIfAbsent

```TypeScript
generateThumbnailIfAbsent?: boolean
```

指定图像无缩略图时是否生成缩略图。true表示生成，false表示不生成。默认值为true。

当图片文件中无缩略图且generateThumbnailIfAbsent为false时，返回undefined（抛出错误码  
[7700303 图片不包含缩略图数据](../../../reference/apis-image-kit/errorcode-image.md#7700303-图片不包含缩略图数据)）。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DecodingOptionsForThumbnail-generateThumbnailIfAbsent?: boolean--><!--Device-DecodingOptionsForThumbnail-generateThumbnailIfAbsent?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## maxGeneratedPixelDimension

```TypeScript
maxGeneratedPixelDimension?: int
```

用于指定生成缩略图的最大边长（宽和高中较大的那一边），较短的一边会根据长边的缩放比例进行缩放。此参数仅在generateThumbnailIfAbsent设置为true时生效。

该值应为整数，默认值为512。生成后的缩略图，宽和高都会限制在maxGeneratedPixelDimension以内。

若按该参数计算后，缩略图的宽或高小于1像素（取整后为0），则不会生成缩略图。

单位：像素（px）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DecodingOptionsForThumbnail-maxGeneratedPixelDimension?: int--><!--Device-DecodingOptionsForThumbnail-maxGeneratedPixelDimension?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

