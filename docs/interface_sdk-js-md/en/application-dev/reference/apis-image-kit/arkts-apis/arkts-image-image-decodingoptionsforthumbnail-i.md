# DecodingOptionsForThumbnail

Describes thumbnail decoding parameters.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-image-interface DecodingOptionsForThumbnail--><!--Device-image-interface DecodingOptionsForThumbnail-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## generateThumbnailIfAbsent

```TypeScript
generateThumbnailIfAbsent?: boolean
```

Flag to specify whether the thumbnail should be generated, if the image does not have a thumbnail.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value: true.

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

This parameter is valid only when generateThumbnailIfAbsent is set to true. The width and height of the image cannot exceed the value of this parameter.The value should be an integer.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Unit:px.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Default value:512.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DecodingOptionsForThumbnail-maxGeneratedPixelDimension?: int--><!--Device-DecodingOptionsForThumbnail-maxGeneratedPixelDimension?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

