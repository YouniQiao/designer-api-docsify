# ShaderEffect

Implements the shader effect. After a shader effect is set for a pen or brush, the shader effect instead of the color attribute is used for drawing. In this case, the alpha value set for the pen or brush still takes effect. > **NOTE：**> > - The initial APIs of this class are supported since API version 12. > > - This module uses the physical pixel unit, px. > > - This module operates under a single-threaded model. The caller needs to manage thread safety and context state > transitions.

**Since:** 23

<!--Device-drawing-class ShaderEffect--><!--Device-drawing-class ShaderEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
```

## createColorShader

```TypeScript
static createColorShader(color: number): ShaderEffect
```

Creates a **ShaderEffect** object with a single color.

**Since:** 12

<!--Device-ShaderEffect-static createColorShader(color: number): ShaderEffect--><!--Device-ShaderEffect-static createColorShader(color: number): ShaderEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createColorShader

```TypeScript
static createColorShader(color: number): ShaderEffect | undefined
```

Creates a ShaderEffect object with a single color.

**Since:** 23

<!--Device-ShaderEffect-static createColorShader(color: int): ShaderEffect | undefined--><!--Device-ShaderEffect-static createColorShader(color: int): ShaderEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createComposeShader

```TypeScript
static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,
        blendMode: BlendMode): ShaderEffect
```

Creates a shader by blending two existing shaders in a certain way.

**Since:** 20

<!--Device-ShaderEffect-static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,        blendMode: BlendMode): ShaderEffect--><!--Device-ShaderEffect-static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,        blendMode: BlendMode): ShaderEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dstShaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | Yes |
| srcShaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | Yes |
| blendMode | [BlendMode](../../apis-na/arkts-apis/arkts-na-common-blendmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |

## createComposeShader

```TypeScript
static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,
        blendMode: BlendMode): ShaderEffect | undefined
```

Creates an ShaderEffect object that generates a blend ShaderEffect object by two shaders.

**Since:** 24

<!--Device-ShaderEffect-static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,        blendMode: BlendMode): ShaderEffect | undefined--><!--Device-ShaderEffect-static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,        blendMode: BlendMode): ShaderEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dstShaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | Yes |
| srcShaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | Yes |
| blendMode | [BlendMode](../../apis-na/arkts-apis/arkts-na-common-blendmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |

## createConicalGradient

```TypeScript
static createConicalGradient(startPt: common2D.Point, startRadius: number, endPt: common2D.Point,
        endRadius: number, colors: Array<number>, mode: TileMode,
        pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect
```

Creates a **ShaderEffect** object that generates a conical gradient between two given circles.

**Since:** 12

<!--Device-ShaderEffect-static createConicalGradient(startPt: common2D.Point, startRadius: number, endPt: common2D.Point,        endRadius: number, colors: Array<number>, mode: TileMode,        pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect--><!--Device-ShaderEffect-static createConicalGradient(startPt: common2D.Point, startRadius: number, endPt: common2D.Point,        endRadius: number, colors: Array<number>, mode: TileMode,        pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startPt | common2D.Point | Yes |
| startRadius | number | Yes |
| endPt | common2D.Point | Yes |
| endRadius | number | Yes |
| colors | Array & lt;number & gt; | Yes |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes |
| pos | Array & lt;number & gt; \ | null | No |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createConicalGradient

```TypeScript
static createConicalGradient(startPt: common2D.Point, startRadius: number, endPt: common2D.Point,
        endRadius: number, colors: Array<number>, mode: TileMode,
        pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect | undefined
```

Creates a ShaderEffect object that generates a conical gradient between two given circles.

**Since:** 23

<!--Device-ShaderEffect-static createConicalGradient(startPt: common2D.Point, startRadius: double, endPt: common2D.Point,        endRadius: double, colors: Array<int>, mode: TileMode,        pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined--><!--Device-ShaderEffect-static createConicalGradient(startPt: common2D.Point, startRadius: double, endPt: common2D.Point,        endRadius: double, colors: Array<int>, mode: TileMode,        pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startPt | common2D.Point | Yes |
| startRadius | number | Yes |
| endPt | common2D.Point | Yes |
| endRadius | number | Yes |
| colors | Array & lt;number & gt; | Yes |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes |
| pos | Array & lt;number & gt; \ | null | No |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createImageShader

```TypeScript
static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,
        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect
```

Creates a shader based on an image. You are advised not to use the function for the canvas of the capture type because it affects the performance.

**Since:** 20

<!--Device-ShaderEffect-static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect--><!--Device-ShaderEffect-static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelmap | image.PixelMap | Yes |
| tileX | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes |
| tileY | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes |
| samplingOptions | [SamplingOptions](arkts-arkgraphics2d-drawing-samplingoptions-c.md) | Yes |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |

## createImageShader

```TypeScript
static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,
        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect | undefined
```

Creates an ShaderEffect object that generates a shader with single image.

**Since:** 24

<!--Device-ShaderEffect-static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect | undefined--><!--Device-ShaderEffect-static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelmap | image.PixelMap | Yes |
| tileX | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes |
| tileY | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes |
| samplingOptions | [SamplingOptions](arkts-arkgraphics2d-drawing-samplingoptions-c.md) | Yes |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |

## createLinearGradient

```TypeScript
static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<number>,
        mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect
```

Creates a **ShaderEffect** object that generates a linear gradient between two points.

**Since:** 12

<!--Device-ShaderEffect-static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<int>,        mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect--><!--Device-ShaderEffect-static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<int>,        mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startPt | common2D.Point | Yes |
| endPt | common2D.Point | Yes |
| colors | Array & lt;number & gt; | Yes |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes |
| pos | Array & lt;number & gt; \ | null | No |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createLinearGradient

```TypeScript
static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<number>,
        mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect | undefined
```

Creates a ShaderEffect object that generates a linear gradient between two points.

**Since:** 23

<!--Device-ShaderEffect-static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<int>,        mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined--><!--Device-ShaderEffect-static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<int>,        mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startPt | common2D.Point | Yes |
| endPt | common2D.Point | Yes |
| colors | Array & lt;number & gt; | Yes |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes |
| pos | Array & lt;number & gt; \ | null | No |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createRadialGradient

```TypeScript
static createRadialGradient(centerPt: common2D.Point, radius: number, colors: Array<number>,
      mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect
```

Creates a **ShaderEffect** object that generates a radial gradient based on the center and radius of a circle. A radial gradient refers to the color transition that spreads out gradually from the center of a circle.

**Since:** 12

<!--Device-ShaderEffect-static createRadialGradient(centerPt: common2D.Point, radius: double, colors: Array<int>,      mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect--><!--Device-ShaderEffect-static createRadialGradient(centerPt: common2D.Point, radius: double, colors: Array<int>,      mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| centerPt | common2D.Point | Yes |
| radius | number | Yes |
| colors | Array & lt;number & gt; | Yes |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes |
| pos | Array & lt;number & gt; \ | null | No |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createRadialGradient

```TypeScript
static createRadialGradient(centerPt: common2D.Point, radius: number, colors: Array<number>,
      mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect | undefined
```

Creates a ShaderEffect object that generates a radial gradient based on the center and radius of a circle. A radial gradient refers to the color transition that spreads out gradually from the center of a circle.

**Since:** 23

<!--Device-ShaderEffect-static createRadialGradient(centerPt: common2D.Point, radius: double, colors: Array<int>,      mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined--><!--Device-ShaderEffect-static createRadialGradient(centerPt: common2D.Point, radius: double, colors: Array<int>,      mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| centerPt | common2D.Point | Yes |
| radius | number | Yes |
| colors | Array & lt;number & gt; | Yes |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes |
| pos | Array & lt;number & gt; \ | null | No |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createSweepGradient

```TypeScript
static createSweepGradient(centerPt: common2D.Point, colors: Array<number>,
        mode: TileMode, startAngle: number, endAngle: number, pos?: Array<number> | null,
        matrix?: Matrix | null): ShaderEffect
```

Creates a **ShaderEffect** object that generates a color sweep gradient around a given center point, either in a clockwise or counterclockwise direction.

**Since:** 12

<!--Device-ShaderEffect-static createSweepGradient(centerPt: common2D.Point, colors: Array<number>,        mode: TileMode, startAngle: number, endAngle: number, pos?: Array<number> | null,        matrix?: Matrix | null): ShaderEffect--><!--Device-ShaderEffect-static createSweepGradient(centerPt: common2D.Point, colors: Array<number>,        mode: TileMode, startAngle: number, endAngle: number, pos?: Array<number> | null,        matrix?: Matrix | null): ShaderEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| centerPt | common2D.Point | Yes |
| colors | Array & lt;number & gt; | Yes |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes |
| startAngle | number | Yes |
| endAngle | number | Yes |
| pos | Array & lt;number & gt; \ | null | No |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createSweepGradient

```TypeScript
static createSweepGradient(centerPt: common2D.Point, colors: Array<number>,
      mode: TileMode, startAngle: number, endAngle: number, pos?: Array<number> | null,
      matrix?: Matrix | null): ShaderEffect | undefined
```

Creates a ShaderEffect object that generates a color sweep gradient around a given center point, either in a clockwise or counterclockwise direction.

**Since:** 23

<!--Device-ShaderEffect-static createSweepGradient(centerPt: common2D.Point, colors: Array<int>,      mode: TileMode, startAngle: double, endAngle: double, pos?: Array<double> | null,      matrix?: Matrix | null): ShaderEffect | undefined--><!--Device-ShaderEffect-static createSweepGradient(centerPt: common2D.Point, colors: Array<int>,      mode: TileMode, startAngle: double, endAngle: double, pos?: Array<double> | null,      matrix?: Matrix | null): ShaderEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| centerPt | common2D.Point | Yes |
| colors | Array & lt;number & gt; | Yes |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes |
| startAngle | number | Yes |
| endAngle | number | Yes |
| pos | Array & lt;number & gt; \ | null | No |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
