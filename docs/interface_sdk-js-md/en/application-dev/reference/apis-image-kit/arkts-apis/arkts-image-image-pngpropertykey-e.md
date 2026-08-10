# PngPropertyKey

表示PNG图片信息的枚举。

> **说明：**
> 
> 返回字段类型具体参考[PngMetadata](../../../reference/apis-image-kit/arkts-apis-image-PngMetadata.md)。
> | 名称 | 值 | 说明 |
> | ---- | -- | ---- |
> | X_PIXELS_PER_METER | 'PngXPixelsPerMeter' | PNG图像X方向每米像素数。 |
> | MODIFICATION_TIME | 'PngModificationTime' | PNG图像的最后一次修改的时间。 |
> | SOFTWARE | 'PngSoftware' | 用于生成PNG图像的软件名称和版本。 |
> | COPYRIGHT | 'PngCopyright' | PNG图像的版权信息。 |
> | CREATION_TIME | 'PngCreationTime' | PNG图像的创建时间。 |
> | SRGB_INTENT | 'PngSRGBIntent' | PNG图像的sRGB（standard Red Green Blue，标准红绿蓝）渲染意图。

- 0表示感知意图。  
- 1表示相对比色意图。  
- 2表示饱和度意图。  
- 3绝对色度意图。 |  
| AUTHOR | 'PngAuthor' | PNG图像的作者。 |  
| INTERLACE_TYPE | 'PngInterlaceType' | PNG图像的交错模式。  
- 0表示无交错模式（图像按照从上到下、从左到右的顺序加载）。  
- 1表示交错模式（通过多次扫描逐步显示图像，图像在加载过程中逐渐清晰）。 |  
| WARNING | 'PngWarning' | PNG图像的警告信息。 |  
| Y_PIXELS_PER_METER | 'PngYPixelsPerMeter' | PNG图像Y方向每米像素数。 |  
| GAMMA | 'PngGamma' | PNG图像的系数伽马的值。 |  
| CHROMATICITIES | 'PngChromaticities' | PNG图像的原色与白点色度坐标cHRM（primary chromaticities and white point）。该信息可用于与设备无关的色彩校正。 |  
| DESCRIPTION | 'PngDescription' | PNG图像的描述。 |  
| TITLE | 'PngTitle' | PNG图像的标题。 |  
| COMMENT | 'PngComment' | PNG图像的注释。 |  
| DISCLAIMER | 'PngDisclaimer' | PNG图像的免责声明。 |

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-image-enum PngPropertyKey--><!--Device-image-enum PngPropertyKey-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## X_PIXELS_PER_METER

```TypeScript
X_PIXELS_PER_METER = 'PngXPixelsPerMeter'
```

PNG x pixels per meter.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PngPropertyKey-X_PIXELS_PER_METER = 'PngXPixelsPerMeter'--><!--Device-PngPropertyKey-X_PIXELS_PER_METER = 'PngXPixelsPerMeter'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Y_PIXELS_PER_METER

```TypeScript
Y_PIXELS_PER_METER = 'PngYPixelsPerMeter'
```

PNG y pixels per meter.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PngPropertyKey-Y_PIXELS_PER_METER = 'PngYPixelsPerMeter'--><!--Device-PngPropertyKey-Y_PIXELS_PER_METER = 'PngYPixelsPerMeter'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## GAMMA

```TypeScript
GAMMA = 'PngGamma'
```

PNG gamma.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PngPropertyKey-GAMMA = 'PngGamma'--><!--Device-PngPropertyKey-GAMMA = 'PngGamma'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## INTERLACE_TYPE

```TypeScript
INTERLACE_TYPE = 'PngInterlaceType'
```

PNG interlacing mode.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PngPropertyKey-INTERLACE_TYPE = 'PngInterlaceType'--><!--Device-PngPropertyKey-INTERLACE_TYPE = 'PngInterlaceType'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## SRGB_INTENT

```TypeScript
SRGB_INTENT = 'PngSRGBIntent'
```

PNG sRGB rendering intent.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PngPropertyKey-SRGB_INTENT = 'PngSRGBIntent'--><!--Device-PngPropertyKey-SRGB_INTENT = 'PngSRGBIntent'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## CHROMATICITIES

```TypeScript
CHROMATICITIES = 'PngChromaticities'
```

PNG color primary/white-point coordinates.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PngPropertyKey-CHROMATICITIES = 'PngChromaticities'--><!--Device-PngPropertyKey-CHROMATICITIES = 'PngChromaticities'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## TITLE

```TypeScript
TITLE = 'PngTitle'
```

PNG title.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PngPropertyKey-TITLE = 'PngTitle'--><!--Device-PngPropertyKey-TITLE = 'PngTitle'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## DESCRIPTION

```TypeScript
DESCRIPTION = 'PngDescription'
```

PNG description.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PngPropertyKey-DESCRIPTION = 'PngDescription'--><!--Device-PngPropertyKey-DESCRIPTION = 'PngDescription'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## COMMENT

```TypeScript
COMMENT = 'PngComment'
```

PNG comment.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PngPropertyKey-COMMENT = 'PngComment'--><!--Device-PngPropertyKey-COMMENT = 'PngComment'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## DISCLAIMER

```TypeScript
DISCLAIMER = 'PngDisclaimer'
```

PNG disclaimer.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PngPropertyKey-DISCLAIMER = 'PngDisclaimer'--><!--Device-PngPropertyKey-DISCLAIMER = 'PngDisclaimer'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## WARNING

```TypeScript
WARNING = 'PngWarning'
```

PNG warning.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PngPropertyKey-WARNING = 'PngWarning'--><!--Device-PngPropertyKey-WARNING = 'PngWarning'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## AUTHOR

```TypeScript
AUTHOR = 'PngAuthor'
```

PNG author.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PngPropertyKey-AUTHOR = 'PngAuthor'--><!--Device-PngPropertyKey-AUTHOR = 'PngAuthor'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## COPYRIGHT

```TypeScript
COPYRIGHT = 'PngCopyright'
```

PNG copyright.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PngPropertyKey-COPYRIGHT = 'PngCopyright'--><!--Device-PngPropertyKey-COPYRIGHT = 'PngCopyright'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## CREATION_TIME

```TypeScript
CREATION_TIME = 'PngCreationTime'
```

PNG creation time.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PngPropertyKey-CREATION_TIME = 'PngCreationTime'--><!--Device-PngPropertyKey-CREATION_TIME = 'PngCreationTime'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## MODIFICATION_TIME

```TypeScript
MODIFICATION_TIME = 'PngModificationTime'
```

PNG modification time.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PngPropertyKey-MODIFICATION_TIME = 'PngModificationTime'--><!--Device-PngPropertyKey-MODIFICATION_TIME = 'PngModificationTime'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## SOFTWARE

```TypeScript
SOFTWARE = 'PngSoftware'
```

PNG software.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PngPropertyKey-SOFTWARE = 'PngSoftware'--><!--Device-PngPropertyKey-SOFTWARE = 'PngSoftware'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

