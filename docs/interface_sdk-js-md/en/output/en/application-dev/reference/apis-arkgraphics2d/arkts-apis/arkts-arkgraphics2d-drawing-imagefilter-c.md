# ImageFilter

Implements an image filter. > **NOTE** > > - The initial APIs of this class are supported since API version 12. > > - This module uses the physical pixel unit, px. > > - This module operates under a single-threaded model. The caller needs to manage thread safety and context state > transitions.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-drawing-class ImageFilter--><!--Device-drawing-class ImageFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

## createBlendImageFilter

```TypeScript
static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter
```

Creates a filter by blending two existing filters in a certain way.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-ImageFilter-static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter--><!--Device-ImageFilter-static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Blend mode. |
| background | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Filter that serves as the destination color in blend mode. |
| foreground | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Filter that serves as the source color in blend mode. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Image filter created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) | Parameter error. Possible causes: Incorrect parameter range. |

## createBlendImageFilter

```TypeScript
static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter | undefined
```

Makes an ImageFilter object that applies the blend to the input.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ImageFilter-static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter | undefined--><!--Device-ImageFilter-static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Blendmode. |
| background | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the input background filter. |
| foreground | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the input foreground filter. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | ImageFilter object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) | Parameter error. Possible causes: Incorrect parameter range. |

## createBlurImageFilter

```TypeScript
static createBlurImageFilter(sigmaX: number, sigmaY: number,
        tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter
```

Creates an image filter with a given blur effect.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ImageFilter-static createBlurImageFilter(sigmaX: number, sigmaY: number,        tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter--><!--Device-ImageFilter-static createBlurImageFilter(sigmaX: number, sigmaY: number,        tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sigmaX | number | Yes | Standard deviation of the Gaussian blur along the X axis. The value must be a floating point number greater than 0. |
| sigmaY | number | Yes | Standard deviation of the Gaussian blur along the Y axis. The value must be a floating point number greater than 0. |
| tileMode | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Tile mode to apply to the edges. |
| imageFilter | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| null | No | Filter to which the image filter will be applied. The default value is null, indicating that the image filter is directly applied to the original image. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Image filter created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types; 3. Parameter verification failed. |

## createBlurImageFilter

```TypeScript
static createBlurImageFilter(sigmaX: double, sigmaY: double,
        tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter | undefined
```

Creates an image filter with a given blur effect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ImageFilter-static createBlurImageFilter(sigmaX: double, sigmaY: double,        tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter | undefined--><!--Device-ImageFilter-static createBlurImageFilter(sigmaX: double, sigmaY: double,        tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sigmaX | double | Yes | Standard deviation of the Gaussian blur along the X axis.The value must be a floating point number greater than 0. |
| sigmaY | double | Yes | Standard deviation of the Gaussian blur along the Y axis.The value must be a floating point number greater than 0. |
| tileMode | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Tile mode to apply to the edges. |
| imageFilter | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| null | No | Filter to which the image filter will be applied.The default value is null, indicating that the image filter is directly applied to the original image. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | ImageFilter object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types; 3. Parameter verification failed. |

## createComposeImageFilter

```TypeScript
static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter
```

Cascades two image filters to create a new image filter. The first filter's output becomes the second filter's input. The second filter then processes this input to produce the final result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-ImageFilter-static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter--><!--Device-ImageFilter-static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cOuter | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The second filter in the cascade, which processes the first filter's output. If the second filter is empty and the first filter is not empty, the final result is the first filter's output.The two filters cannot be empty at the same time. |
| cInner | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The first filter in the cascade, which directly processes the original image content. If the first filter is empty and the second filter is not empty, the final result is the second filter's output. The two filters cannot be empty at the same time. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Image filter created. |

## createComposeImageFilter

```TypeScript
static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter | undefined
```

Makes an ImageFilter object that combines the "inner" and "outer" filters, allowing the output of the "inner" filter to serve as the input source bitmap for the "outer" filter.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ImageFilter-static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter | undefined--><!--Device-ImageFilter-static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cOuter | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the instance to apply its effects to the output of the 'inner'filter. |
| cInner | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the output as input for "outer" filters. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | ImageFilter object. |

## createFromColorFilter

```TypeScript
static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter
```

Creates an image filter object with a given color filter effect.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ImageFilter-static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter--><!--Device-ImageFilter-static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorFilter | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Color filter. |
| imageFilter | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| null | No | Filter to which the image filter will be applied. The default value is null, indicating that the image filter is directly applied to the original image.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 20 |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Image filter created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types. |

## createFromColorFilter

```TypeScript
static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter | undefined
```

Creates an image filter object with a given color filter effect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ImageFilter-static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter | undefined--><!--Device-ImageFilter-static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorFilter | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Color filter. |
| imageFilter | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| null | No | Filter to which the image filter will be applied.The default value is null, indicating that the image filter is directly applied to the original image. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | ImageFilter object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types. |

## createFromImage

```TypeScript
static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter
```

Creates an image filter from a given image. You are advised not to use the function for the canvas of the capture type because it affects the performance.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-ImageFilter-static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter--><!--Device-ImageFilter-static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixelmap | image.PixelMap | Yes | Image object. |
| srcRect | common2D.Rect \| null | No | (Optional) Pixel area of the image to be applied to the filter. This parameter is left empty by default, which means that the entire **PixelMap** area is applied. |
| dstRect | common2D.Rect \| null | No | (Optional) Area to be rendered. This parameter is left empty by default, which means that the value is the same as that of **srcRect**. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Image filter created. |

## createFromImage

```TypeScript
static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter | undefined
```

Makes an ImageFilter object that applies the bitmap to the input.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ImageFilter-static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter | undefined--><!--Device-ImageFilter-static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixelmap | image.PixelMap | Yes | The source input image. |
| srcRect | common2D.Rect \| null | No | Indicates the input srcRect, or uses the source bitmap if this is null. |
| dstRect | common2D.Rect \| null | No | Indicates the input dstRect, or uses the source bitmap if this is null. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | ImageFilter object. |

## createFromShaderEffect

```TypeScript
static createFromShaderEffect(shader: ShaderEffect): ImageFilter
```

Creates an **ImageFilter** object based on a shader.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-ImageFilter-static createFromShaderEffect(shader: ShaderEffect): ImageFilter--><!--Device-ImageFilter-static createFromShaderEffect(shader: ShaderEffect): ImageFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| shader | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Shader effect to be applied to the image. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Image filter created. |

## createFromShaderEffect

```TypeScript
static createFromShaderEffect(shader: ShaderEffect): ImageFilter | undefined
```

Makes an ImageFilter object that renders the contents of the input Shader.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ImageFilter-static createFromShaderEffect(shader: ShaderEffect): ImageFilter | undefined--><!--Device-ImageFilter-static createFromShaderEffect(shader: ShaderEffect): ImageFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| shader | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the shader effect to be applied to the image. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | ImageFilter object. |

## createOffsetImageFilter

```TypeScript
static createOffsetImageFilter(dx: number, dy: number, input?: ImageFilter | null): ImageFilter
```

Creates an offset filter to translate the input filter based on the specified vector.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-ImageFilter-static createOffsetImageFilter(dx: number, dy: number, input?: ImageFilter | null): ImageFilter--><!--Device-ImageFilter-static createOffsetImageFilter(dx: number, dy: number, input?: ImageFilter | null): ImageFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | number | Yes | Horizontal translation distance. The value is a floating point number. |
| dy | number | Yes | Vertical translation distance. The value is a floating point number. |
| input | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| null | No | Filter to be translated. This parameter is left empty by default, which means that the drawing result without the filtering effect is translated. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Image filter created. |

## createOffsetImageFilter

```TypeScript
static createOffsetImageFilter(dx: double, dy: double, input?: ImageFilter | null): ImageFilter | undefined
```

Makes an ImageFilter object that instance with the provided x and y offset.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ImageFilter-static createOffsetImageFilter(dx: double, dy: double, input?: ImageFilter | null): ImageFilter | undefined--><!--Device-ImageFilter-static createOffsetImageFilter(dx: double, dy: double, input?: ImageFilter | null): ImageFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | double | Yes | Indicates the offset in the X direction. |
| dy | double | Yes | Indicates the offset in the Y direction. |
| input | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| null | No | Indicates the input image filter used to generate offset effects, or uses the source bitmap if this is null. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | ImageFilter object. |

