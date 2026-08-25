# ColorPicker

A color picker class used to obtain the main color from image data. It is suitable for scenarios such as UI theme color extraction, image color scheme analysis, and intelligent color scheme recommendation, helping developers dynamically generate harmonious color schemes based on image content. Before calling the methods of ColorPicker, you need to create a ColorPicker instance via createColorPicker.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { effectKit } from 'kits/@kit.ArkGraphics2D';
```

## getAverageColor

```TypeScript
getAverageColor(): Color
```

Reads the average color value from the image and writes the result to a Color instance. This API returns the result synchronously. It is commonly used in scenarios such as obtaining the overall tone of an image, such as image tone statistics and adaptive background color.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) |

## getHighestSaturationColor

```TypeScript
getHighestSaturationColor(): Color
```

Reads the color value with the highest saturation from the image and writes the result to a Color instance. This API returns the result synchronously. It is commonly used in scenarios such as extracting the most vivid color in an image, such as UI theme accent color extraction and icon highlight color selection.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) |

## getLargestProportionColor

```TypeScript
getLargestProportionColor(): Color
```

Reads the color value with the largest proportion in the image and writes the result to a Color instance. This API returns the result synchronously. This API uses the median cut algorithm to partition the color space and obtains the average color of the color space with the largest proportion. It is commonly used in scenarios such as identifying the largest color area in an image, such as icon background color extraction and image content analysis.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) |

## getMainColor

```TypeScript
getMainColor(): Promise<Color>
```

Reads the color value of the main color from the image and writes the result to a Color instance. This API uses a promise to return the result. This API uses the image scaling algorithm to calculate the weighted value of surrounding pixels and reduce the original image to one pixel to obtain the main color. It is commonly used in scenarios such as automatic app theme color extraction, automatic UI color matching based on images, and dynamic background color adjustment of music players based on album covers.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Color & gt; |

## getMainColorSync

```TypeScript
getMainColorSync(): Color
```

Reads the color value of the main color from the image and writes the result to a Color instance. This API returns the result synchronously. This API uses the image scaling algorithm to calculate the weighted value of surrounding pixels and reduces the original image to one pixel to obtain the main color. It is commonly used in scenarios such as automatic app theme color extraction, automatic UI color matching based on images, and dynamic background color adjustment of music players based on album covers.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) |

## getTopProportionColors

```TypeScript
getTopProportionColors(colorCount: number): Array<Color | null>
```

Reads the top proportion colors from the image, with the number specified by colorCount, and writes the results to an array of Color instances. This API returns the result synchronously. It is commonly used in scenarios such as extracting the top multiple colors by proportion in an image, such as multi-tone color scheme generation and image color distribution analysis.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorCount | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;Color \ | null & gt; |

## isBlackOrWhiteOrGrayColor

```TypeScript
isBlackOrWhiteOrGrayColor(color: number): boolean
```

Determines whether the specified color value is a black, white, or gray color, and returns true or false. It is commonly used in scenarios such as determining whether a color belongs to the achromatic color system, such as intelligent color scheme filtering and image color classification.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
