# ImageFilter

图像滤波器，用于对图像应用各种滤波效果，支持创建模糊、颜色混合、级联组合、偏移、基于着色器等多种图像滤波器。

> **说明：**
> 
> - 本Class首批接口从API version 12开始支持。
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-drawing-class ImageFilter--><!--Device-drawing-class ImageFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## createBlendImageFilter

```TypeScript
static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter
```

按照指定的混合模式对两个滤波器进行叠加，生成一个新的滤波器。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-ImageFilter-static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter--><!--Device-ImageFilter-static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [BlendMode](../../apis-arkui/arkts-apis/arkts-arkui-common-blendmode-e.md) | Yes | 颜色混合模式。 |
| background | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | Yes | 在混合模式中作为目标色的滤波器。 |
| foreground | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | Yes | 在混合模式中作为源色的滤波器。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 返回按照指定混合模式叠加后的图像滤波器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 25900001 | Parameter error. Possible causes: Incorrect parameter range. |

## createBlendImageFilter

```TypeScript
static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter | undefined
```

按照指定的混合模式对两个滤波器进行叠加，生成一个新的滤波器。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ImageFilter-static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter | undefined--><!--Device-ImageFilter-static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [BlendMode](../../apis-arkui/arkts-apis/arkts-arkui-common-blendmode-e.md) | Yes | 颜色混合模式。 |
| background | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | Yes | 在混合模式中作为目标色的滤波器。 |
| foreground | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | Yes | 在混合模式中作为源色的滤波器。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 返回按照指定混合模式叠加后的图像滤波器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 25900001 | Parameter error. Possible causes: Incorrect parameter range. |

## createBlurImageFilter

```TypeScript
static createBlurImageFilter(sigmaX: number, sigmaY: number,
        tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter
```

创建具有模糊效果的图像滤波器。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ImageFilter-static createBlurImageFilter(sigmaX: number, sigmaY: number,        tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter--><!--Device-ImageFilter-static createBlurImageFilter(sigmaX: number, sigmaY: number,        tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sigmaX | number | Yes | 表示沿x轴方向上高斯模糊的标准差，必须大于0，该参数为浮点数。单位为物理像素px。 |
| sigmaY | number | Yes | 表示沿y轴方向上高斯模糊的标准差，必须大于0，该参数为浮点数。单位为物理像素px。 |
| tileMode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes | 表示在边缘处应用的平铺模式。 |
| imageFilter | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) \| null | No | 要与当前图像滤波器叠加的输入滤波器，默认为null，表示直接将当前图像滤波器作用于原始图像。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 返回创建的模糊图像滤波器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createBlurImageFilter

```TypeScript
static createBlurImageFilter(sigmaX: double, sigmaY: double,
        tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter | undefined
```

创建具有模糊效果的图像滤波器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ImageFilter-static createBlurImageFilter(sigmaX: double, sigmaY: double,        tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter | undefined--><!--Device-ImageFilter-static createBlurImageFilter(sigmaX: double, sigmaY: double,        tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sigmaX | double | Yes | 表示沿x轴方向上高斯模糊的标准差，必须大于0，该参数为浮点数。单位为物理像素px。 |
| sigmaY | double | Yes | 表示沿y轴方向上高斯模糊的标准差，必须大于0，该参数为浮点数。单位为物理像素px。 |
| tileMode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes | 表示在边缘处应用的平铺模式。 |
| imageFilter | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) \| null | No | 要与当前图像滤波器叠加的输入滤波器，默认为null，表示直接将当前图像滤波器作用于原始图像。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 返回创建的模糊图像滤波器。创建失败时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createComposeImageFilter

```TypeScript
static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter
```

将两个图像滤波器进行级联，生成新的图像滤波器，级联时会将第一级滤波器的输出作为第二级滤波器的输入，经过第二级滤波器处理后，输出最终的滤波结果。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-ImageFilter-static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter--><!--Device-ImageFilter-static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cOuter | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | Yes | 在级联中，作为第二级的滤波器，处理第一级滤波器的输出。如果第二级滤波器为空，第一级滤波器不为空，最后输出第一级滤波器的结果。两级滤波器不能同时为空。 |
| cInner | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | Yes | 在级联中，作为第一级的滤波器，直接处理图像的原始内容。如果第一级滤波器为空，第二级滤波器不为空，最后输出第二级滤波器的结果。两级滤波器不能同时为空。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 返回级联后的图像滤波器。 |

## createComposeImageFilter

```TypeScript
static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter | undefined
```

将两个图像滤波器进行级联，生成新的图像滤波器，级联时会将第一级滤波器的输出作为第二级滤波器的输入，经过第二级滤波器处理后，输出最终的滤波结果。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ImageFilter-static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter | undefined--><!--Device-ImageFilter-static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cOuter | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | Yes | 在级联中，作为第二级的滤波器，处理第一级滤波器的输出。如果第二级滤波器为空，第一级滤波器不为空，最后输出第一级滤波器的结果。两级滤波器不能同时为空。 |
| cInner | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | Yes | 在级联中，作为第一级的滤波器，直接处理图像的原始内容。如果第一级滤波器为空，第二级滤波器不为空，最后输出第二级滤波器的结果。两级滤波器不能同时为空。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 返回级联后的图像滤波器。 |

## createFromColorFilter

```TypeScript
static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter
```

创建一个图像滤波器，将指定的颜色滤波器应用于输入的图像滤波器。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ImageFilter-static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter--><!--Device-ImageFilter-static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorFilter | [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) | Yes | 表示颜色滤波器。 |
| imageFilter | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) \| null | No | 要与当前图像滤波器叠加的输入滤波器，默认为null，表示直接将当前图像滤波器作用于原始图像。<br>**Since:** 20 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 返回颜色滤波器叠加后的图像滤波器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## createFromColorFilter

```TypeScript
static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter | undefined
```

创建一个图像滤波器，将指定的颜色滤波器应用于输入的图像滤波器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ImageFilter-static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter | undefined--><!--Device-ImageFilter-static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorFilter | [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) | Yes | 表示颜色滤波器。 |
| imageFilter | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) \| null | No | 要与当前图像滤波器叠加的输入滤波器。 当不传该参数，或者imageFilter传入undefined时，默认为null，表示直接将当前图像滤波器作用于原始图像。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 返回颜色滤波器叠加后的图像滤波器。创建失败时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## createFromImage

```TypeScript
static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter
```

基于给定的图像创建一个图像滤波器。此接口不建议用于录制类型的画布（即用于记录绘制指令而非直接渲染的Canvas对象），会影响性能。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-ImageFilter-static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter--><!--Device-ImageFilter-static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixelmap | image.PixelMap | Yes | 图像对象。 |
| srcRect | common2D.Rect \| null | No | 可选参数，默认为null。此滤波器要使用的图像的像素区域，如果为null，则使用pixelmap全部区域。 |
| dstRect | common2D.Rect \| null | No | 可选参数，默认为null。要进行渲染的区域，如果为null，则和srcRect保持一致。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 返回基于图像创建的图像滤波器。 |

## createFromImage

```TypeScript
static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter | undefined
```

基于给定的图像创建一个图像滤波器。此接口不建议用于录制类型的画布（即用于记录绘制指令而非直接渲染的Canvas对象），会影响性能。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ImageFilter-static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter | undefined--><!--Device-ImageFilter-static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixelmap | image.PixelMap | Yes | 图像对象。 |
| srcRect | common2D.Rect \| null | No | 可选参数，默认为null。此滤波器要使用的图像的像素区域，如果为null，则使用pixelmap全部区域。 |
| dstRect | common2D.Rect \| null | No | 可选参数，默认为null。要进行渲染的区域，如果为null，则和srcRect保持一致。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 返回基于图像创建的图像滤波器。 |

## createFromShaderEffect

```TypeScript
static createFromShaderEffect(shader: ShaderEffect): ImageFilter
```

基于着色器创建一个图像滤波器。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-ImageFilter-static createFromShaderEffect(shader: ShaderEffect): ImageFilter--><!--Device-ImageFilter-static createFromShaderEffect(shader: ShaderEffect): ImageFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| shader | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | Yes | 表示应用于图像的着色器效果。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 返回基于着色器创建的图像滤波器。 |

## createFromShaderEffect

```TypeScript
static createFromShaderEffect(shader: ShaderEffect): ImageFilter | undefined
```

基于着色器创建一个图像滤波器。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ImageFilter-static createFromShaderEffect(shader: ShaderEffect): ImageFilter | undefined--><!--Device-ImageFilter-static createFromShaderEffect(shader: ShaderEffect): ImageFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| shader | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | Yes | 表示应用于图像的着色器效果。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 返回基于着色器创建的图像滤波器。 |

## createOffsetImageFilter

```TypeScript
static createOffsetImageFilter(dx: number, dy: number, input?: ImageFilter | null): ImageFilter
```

创建一个偏移滤波器，将输入的滤波器按照指定向量进行平移。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-ImageFilter-static createOffsetImageFilter(dx: number, dy: number, input?: ImageFilter | null): ImageFilter--><!--Device-ImageFilter-static createOffsetImageFilter(dx: number, dy: number, input?: ImageFilter | null): ImageFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | number | Yes | 水平方向的平移距离，该参数为浮点数。单位为物理像素px。 |
| dy | number | Yes | 竖直方向的平移距离，该参数为浮点数。单位为物理像素px。 |
| input | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) \| null | No | 需要进行平移的滤波器。默认为null，如果为null，则将无滤波效果的绘制结果进行平移。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 返回偏移后的图像滤波器。 |

## createOffsetImageFilter

```TypeScript
static createOffsetImageFilter(dx: double, dy: double, input?: ImageFilter | null): ImageFilter | undefined
```

创建一个偏移滤波器，将输入的滤波器按照指定向量进行平移。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ImageFilter-static createOffsetImageFilter(dx: double, dy: double, input?: ImageFilter | null): ImageFilter | undefined--><!--Device-ImageFilter-static createOffsetImageFilter(dx: double, dy: double, input?: ImageFilter | null): ImageFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | double | Yes | 水平方向的平移距离，该参数为浮点数。单位为物理像素px。 |
| dy | double | Yes | 竖直方向的平移距离，该参数为浮点数。单位为物理像素px。 |
| input | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) \| null | No | 需要进行平移的滤波器。默认为null，如果为null，则将无滤波效果的绘制结果进行平移。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 返回偏移后的图像滤波器。 |

