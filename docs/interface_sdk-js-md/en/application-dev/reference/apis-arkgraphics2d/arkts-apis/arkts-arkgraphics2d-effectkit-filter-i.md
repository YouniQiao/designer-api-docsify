# Filter

An image effect class used to add a specified effect to the effect chain through chained calls. It is suitable for scenarios such as image filter processing, visual effect enhancement, and image beautification. Before calling the methods of Filter, you need to create a Filter instance via createEffect. After adding effects, you need to call getEffectPixelMap to obtain the processed image.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { effectKit } from 'kits/@kit.ArkGraphics2D';
```

## blur

```TypeScript
blur(radius: number): Filter
```

Adds the blur effect to the effect chain and returns the instance of the chain. The shader tile mode uses DECAL. To specify the tile mode, use the blur(radius: number, tileMode: TileMode) API. It is commonly used in scenarios such as background blurring, privacy information masking, frosted glass background effect, and pop-up window background blur.

> **NOTE：**&gt;
> This API provides the blur effect for static images. To provide the real-time blur effect for components, use dynamic blur.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| radius | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

## blur

```TypeScript
blur(radius: number, tileMode: TileMode): Filter
```

Adds the blur effect to the effect chain and returns the instance of the chain. It supports selecting the shader effect tile mode. It is commonly used in scenarios such as background blurring, privacy information masking, frosted glass background effect, and pop-up window background blur.

> **NOTE：**&gt;
> This API provides the blur effect for static images. To provide the real-time blur effect for components, use dynamic blur.

**Since:** 14

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| radius | number | Yes |
| tileMode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

## brightness

```TypeScript
brightness(bright: number): Filter
```

Adds the brightness effect to the effect chain and returns the instance of the chain. This method achieves a brightness effect by adjusting the image brightness. It is commonly used in scenarios such as dark image brightening, image preview brightness enhancement, and night mode image adaptation.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bright | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

## getEffectPixelMap

```TypeScript
getEffectPixelMap(): Promise<image.PixelMap>
```

Obtains image.PixelMap of the source image to which the effect chain has been added. CPU rendering is used by default. This API uses a promise to return the result. To specify the rendering mode, use the getEffectPixelMap(useCpuRender: boolean) API. It is commonly used in scenarios where the processed image needs to be saved or displayed.

> **NOTE：**&gt;
> This method uses CPU rendering by default. The shader tile mode supports only DECAL, and other modes (CLAMP, REPEAT, MIRROR) are not supported. To use GPU rendering or learn about the impact of rendering modes on TileMode, see TileMode and getEffectPixelMap(useCpuRender: boolean).

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

## getEffectPixelMap

```TypeScript
getEffectPixelMap(useCpuRender : boolean): Promise<image.PixelMap>
```

Obtains image.PixelMap of the source image with the linked list effect. The rendering mode (CPU rendering or GPU rendering) can be specified. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| useCpuRender | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

## getPixelMap

```TypeScript
getPixelMap(): image.PixelMap
```

Obtains image.PixelMap of the source image to which the effect chain has been added. It is commonly used in scenarios where the processed image needs to be saved or displayed.

> **NOTE：**&gt;
> This API is supported since API version 9 and deprecated since API version 11. Use getEffectPixelMap instead.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [getEffectPixelMap](#geteffectpixelmap)

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| image.PixelMap |

## grayscale

```TypeScript
grayscale(): Filter
```

Adds the grayscale effect to the effect chain and returns the instance of the chain. This method converts a color image into a grayscale image by calculating the grayscale value through weighted RGB values. It is commonly used in scenarios such as black-and-white style photo generation, image preprocessing decolorization, and grayscale icon creation.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

## invert

```TypeScript
invert(): Filter
```

Adds the invert effect to the effect chain and returns the instance of the chain. This method inverts the RGB color values of the image. It is commonly used in scenarios such as negative film effect, image artistic processing, and night mode adaptation.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

## setColorMatrix

```TypeScript
setColorMatrix(colorMatrix: Array<number>): Filter
```

Performs color transformation on the image using a custom color matrix, adds the effect to the effect chain, and returns the instance of the chain. It is commonly used in scenarios such as implementing custom color effects not supported by preset filters, such as vintage tones and warm/cool tone adjustments.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorMatrix | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
