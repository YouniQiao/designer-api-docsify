# ColorPicker

A color picker class used to obtain the main color from image data. It is suitable for scenarios such as UI theme color extraction, image color scheme analysis, and intelligent color scheme recommendation, helping developers dynamically generate harmonious color schemes based on image content. Before calling the methods of ColorPicker, you need to create a ColorPicker instance via createColorPicker.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { effectKit } from 'kits/@kit.ArkGraphics2D';
```

## discriminatePictureLightDegree

```TypeScript
discriminatePictureLightDegree(): PictureLightDegree
```

Discriminates the light and dark degree of the picture. When the light and dark degree cannot be determined, UNKNOWN_LIGHT_COLOR_DEGREE_PICTURE is returned.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PictureLightDegree](arkts-arkgraphics2d-effectkit-picturelightdegree-e-sys.md) |

## getAlphaZeroTransparentProportion

```TypeScript
getAlphaZeroTransparentProportion(): number
```

Obtains the proportion of fully transparent pixels with alpha=0 in the image.

**Since:** 23

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getComplexityDegree

```TypeScript
getComplexityDegree(): PictureComplexityDegree
```

Obtains the complexity degree of the image. When the complexity degree cannot be determined, the default value UNKNOWN_COMPLEXITY_DEGREE_PICTURE is returned.

**Since:** 22

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PictureComplexityDegree](arkts-arkgraphics2d-effectkit-picturecomplexitydegree-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getDeepenImmersionColor

```TypeScript
getDeepenImmersionColor(): Color
```

Generates a stronger immersion color that merges with the background color and is deeper than the background color, and writes the result to a Color instance. This API uses a color mixing algorithm to create a color that is both harmonious with the background color and has a stronger immersive effect.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) |

## getImmersiveBackgroundColor

```TypeScript
getImmersiveBackgroundColor(): Color
```

Generates an immersive background color that creates an immersive visual effect, and writes the result to a Color instance. This API generates a color value suitable for use as an immersive background based on the dominant color.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) |

## getImmersiveForegroundColor

```TypeScript
getImmersiveForegroundColor(): Color
```

Generates an immersive foreground color that creates an immersive visual effect for text and content, and writes the result to a Color instance. This API generates a color value suitable for use as an immersive foreground based on the dominant color.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) |

## getMorandiShadowColor

```TypeScript
getMorandiShadowColor(): Color
```

Obtains the Morandi shadow color from the dominant color of the image and writes the result to a Color instance. This API uses a specific color conversion algorithm to convert the dominant color into a Morandi style shadow tone.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) |

## getReverseColor

```TypeScript
getReverseColor(): Color
```

Generates a reverse color based on the image brightness discrimination result, and writes the result to a Color instance. Based on the image light degree type obtained from the discriminatePictureLightDegree API, a reverse color is generated. Only the extremely light color picture (EXTREMELY_LIGHT_COLOR_PICTURE) type returns black; other types return white. It is used for UI themes or contrast calculations.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) |

## getShadeDegree

```TypeScript
getShadeDegree(): PictureShadeDegree
```

Obtains the shade degree of the image. When the shade degree cannot be determined, the default value UNKNOWN_SHADE_DEGREE_PICTURE is returned.

**Since:** 22

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PictureShadeDegree](arkts-arkgraphics2d-effectkit-pictureshadedegree-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getTopProportionColorsAndPercentage

```TypeScript
getTopProportionColorsAndPercentage(colorCount: number): Map<Color | null, number | null>
```

Synchronously returns the top proportion colors and their corresponding percentages from the image, with the number specified by colorCount.

**Since:** 22

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorCount | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Map & lt;Color \ | null, number \| null & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
