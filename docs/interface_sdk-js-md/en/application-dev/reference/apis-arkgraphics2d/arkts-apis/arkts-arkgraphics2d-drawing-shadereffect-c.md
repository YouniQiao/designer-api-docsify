# ShaderEffect

着色器，用于在绘图中填充颜色和渐变效果。画刷和画笔设置着色器后，会使用着色器效果而不是颜色属性去绘制，但此时画刷和画笔的透明度属性仍然生效。着色器支持创建单色着色器、线性渐变、径向渐变、扇形渐变、锥形渐变、图片着色器及混合着色器等多种类型。

> **说明：**
> 
> - 本Class首批接口从API version 12开始支持。
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-drawing-class ShaderEffect--><!--Device-drawing-class ShaderEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## createColorShader

```TypeScript
static createColorShader(color: number): ShaderEffect
```

创建具有单一颜色的着色器。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ShaderEffect-static createColorShader(color: number): ShaderEffect--><!--Device-ShaderEffect-static createColorShader(color: number): ShaderEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | number | Yes | 表示着色器的ARGB格式颜色，该参数为32位无符号整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 返回具有单一颜色的着色器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## createColorShader

```TypeScript
static createColorShader(color: int): ShaderEffect | undefined
```

创建具有单一颜色的着色器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ShaderEffect-static createColorShader(color: int): ShaderEffect | undefined--><!--Device-ShaderEffect-static createColorShader(color: int): ShaderEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | int | Yes | 表示着色器的ARGB格式颜色，该参数为32位无符号整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 返回具有单一颜色的着色器对象。创建失败时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## createComposeShader

```TypeScript
static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,
        blendMode: BlendMode): ShaderEffect
```

按照指定的混合模式对两个着色器进行叠加，生成一个新的着色器。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-ShaderEffect-static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,        blendMode: BlendMode): ShaderEffect--><!--Device-ShaderEffect-static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,        blendMode: BlendMode): ShaderEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dstShaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | Yes | 在混合模式中作为目标色的着色器。 |
| srcShaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | Yes | 在混合模式中作为源色的着色器。 |
| blendMode | [BlendMode](../../apis-arkui/arkts-apis/arkts-arkui-common-blendmode-e.md) | Yes | 混合模式，用于指定两个着色器叠加时的颜色混合算法。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 返回叠加后的着色器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 25900001 | Parameter error. Possible causes: Incorrect parameter range. |

## createComposeShader

```TypeScript
static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,
        blendMode: BlendMode): ShaderEffect | undefined
```

Creates an ShaderEffect object that generates a blend ShaderEffect object by two shaders.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ShaderEffect-static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,        blendMode: BlendMode): ShaderEffect | undefined--><!--Device-ShaderEffect-static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,        blendMode: BlendMode): ShaderEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dstShaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | Yes | Indicates a destination ShaderEffect pointer. |
| srcShaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | Yes | Indicates a source ShaderEffect pointer. |
| blendMode | [BlendMode](../../apis-arkui/arkts-apis/arkts-arkui-common-blendmode-e.md) | Yes | BlendMode. |

**Return value:**

| Type | Description |
| --- | --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | Returns a blend ShaderEffect object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 25900001 | Parameter error. Possible causes: Incorrect parameter range. |

## createConicalGradient

```TypeScript
static createConicalGradient(startPt: common2D.Point, startRadius: number, endPt: common2D.Point,
        endRadius: number, colors: Array<number>, mode: TileMode,
        pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect
```

创建着色器，在给定两个圆之间生成锥形渐变。锥形渐变是指颜色在起始圆和结束圆之间，按照一定比例进行插值过渡形成的渐变效果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ShaderEffect-static createConicalGradient(startPt: common2D.Point, startRadius: number, endPt: common2D.Point,        endRadius: number, colors: Array<number>, mode: TileMode,        pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect--><!--Device-ShaderEffect-static createConicalGradient(startPt: common2D.Point, startRadius: number, endPt: common2D.Point,        endRadius: number, colors: Array<number>, mode: TileMode,        pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startPt | common2D.Point | Yes | 表示渐变的起始圆的圆心。 |
| startRadius | number | Yes | 表示渐变的起始圆的半径，小于0时无效。该参数为浮点数。单位为物理像素px。 |
| endPt | common2D.Point | Yes | 表示渐变的结束圆的圆心。 |
| endRadius | number | Yes | 表示渐变的结束圆的半径，小于0时无效。该参数为浮点数。单位为物理像素px。 |
| colors | Array&lt;number&gt; | Yes | 表示在起始圆和结束圆之间分布的颜色数组，数组中的值为32位（ARGB）无符号整数。 |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes | 着色器效果平铺模式。 |
| pos | Array&lt;number&gt; \| null | No | 表示每种对应颜色在颜色数组中的相对位置。数组长度需和colors保持一致， 数组的首个元素应当是0.0，末尾元素应当是1.0，中间的元素应当在0与1之间并且逐下标递增，表示colors中每个对应颜色的相对位置。 当不传该参数，或者pos传入undefined时，默认为null，表示颜色均匀分布在起始角度和结束角度之间。 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No | 矩阵对象，用于对着色器做矩阵变换。当不传该参数，或者matrix传入undefined时，默认为null，表示单位矩阵。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 返回锥形渐变着色器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createConicalGradient

```TypeScript
static createConicalGradient(startPt: common2D.Point, startRadius: double, endPt: common2D.Point,
        endRadius: double, colors: Array<int>, mode: TileMode,
        pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined
```

创建着色器，在给定两个圆之间生成锥形渐变。锥形渐变是指颜色在起始圆和结束圆之间，按照一定比例进行插值过渡形成的渐变效果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ShaderEffect-static createConicalGradient(startPt: common2D.Point, startRadius: double, endPt: common2D.Point,        endRadius: double, colors: Array<int>, mode: TileMode,        pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined--><!--Device-ShaderEffect-static createConicalGradient(startPt: common2D.Point, startRadius: double, endPt: common2D.Point,        endRadius: double, colors: Array<int>, mode: TileMode,        pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startPt | common2D.Point | Yes | 表示渐变的起始圆的圆心。 |
| startRadius | double | Yes | 表示渐变的起始圆的半径，小于0时无效。该参数为浮点数。单位为物理像素px。 |
| endPt | common2D.Point | Yes | 表示渐变的结束圆的圆心。 |
| endRadius | double | Yes | 表示渐变的结束圆的半径，小于0时无效。该参数为浮点数。单位为物理像素px。 |
| colors | Array&lt;int&gt; | Yes | 表示在起始圆和结束圆之间分布的颜色数组，数组中的值为32位（ARGB）无符号整数。 |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes | 着色器效果平铺模式。 |
| pos | Array&lt;double&gt; \| null | No | 表示每种对应颜色在颜色数组中的相对位置。数组长度需和colors保持一致， 数组的首个元素应当是0.0，末尾元素应当是1.0，中间的元素应当在0与1之间并且逐下标递增，表示colors中每个对应颜色的相对位置。 当不传该参数，或者pos传入undefined时，默认为null，表示颜色均匀分布在起始圆和结束圆之间。 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No | 矩阵对象，用于对着色器做矩阵变换。当不传该参数，或者matrix传入undefined时，默认为null，表示单位矩阵。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 返回锥形渐变着色器对象。创建失败时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createImageShader

```TypeScript
static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,
        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect
```

基于图片创建一个着色器。此接口不建议用于录制类型的画布（即用于记录绘制指令而非直接渲染的Canvas对象），会影响性能。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-ShaderEffect-static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect--><!--Device-ShaderEffect-static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixelmap | image.PixelMap | Yes | 进行采样的图片对象。 |
| tileX | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes | 水平方向的平铺模式。 |
| tileY | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes | 竖直方向的平铺模式。 |
| samplingOptions | [SamplingOptions](arkts-arkgraphics2d-drawing-samplingoptions-c.md) | Yes | 图片采样参数，用于指定图像采样时的过滤模式。 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No | 矩阵对象，用于对着色器做矩阵变换。默认为null，表示单位矩阵。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 返回基于图片的着色器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 25900001 | Parameter error. Possible causes: Incorrect parameter range. |

## createImageShader

```TypeScript
static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,
        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect | undefined
```

Creates an ShaderEffect object that generates a shader with single image.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ShaderEffect-static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect | undefined--><!--Device-ShaderEffect-static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixelmap | image.PixelMap | Yes | PixelMap. |
| tileX | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes | Indicates the type of tile mode for horizontal shader effect. |
| tileY | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes | Indicates the type of tile mode for vertical shader effect. |
| samplingOptions | [SamplingOptions](arkts-arkgraphics2d-drawing-samplingoptions-c.md) | Yes | SamplingOptions used to describe the sampling mode. |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No | Indicates the Matrix object. The default value is null. |

**Return value:**

| Type | Description |
| --- | --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | Returns the shader with single image ShaderEffect object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 25900001 | Parameter error. Possible causes: Incorrect parameter range. |

## createLinearGradient

```TypeScript
static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<int>,
        mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect
```

创建着色器，在两个指定点之间生成线性渐变。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ShaderEffect-static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<int>,        mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect--><!--Device-ShaderEffect-static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<int>,        mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startPt | common2D.Point | Yes | 表示渐变的起点。 |
| endPt | common2D.Point | Yes | 表示渐变的终点。 |
| colors | Array&lt;int&gt; | Yes | 表示在两个点之间分布的颜色数组，数组中的值为32位（ARGB）无符号整数。 |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes | 着色器效果平铺模式。 |
| pos | Array&lt;double&gt; \| null | No | 表示每种对应颜色在颜色数组中的相对位置。数组长度需和colors保持一致，数组的首个元素应当是0.0，末尾元素应当是1.0，中间的元素应当在0与1 之间并且逐下标递增，表示colors中每个对应颜色的相对位置。默认为null，表示颜色均匀分布在起点和终点之间。 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No | 矩阵对象，用于对着色器做矩阵变换。默认为null，表示单位矩阵。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 返回线性渐变着色器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createLinearGradient

```TypeScript
static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<int>,
        mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined
```

创建着色器，在两个指定点之间生成线性渐变。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ShaderEffect-static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<int>,        mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined--><!--Device-ShaderEffect-static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<int>,        mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startPt | common2D.Point | Yes | 表示渐变的起点。 |
| endPt | common2D.Point | Yes | 表示渐变的终点。 |
| colors | Array&lt;int&gt; | Yes | 表示在两个点之间分布的颜色数组，数组中的值为32位（ARGB）无符号整数。 |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes | 着色器效果平铺模式。 |
| pos | Array&lt;double&gt; \| null | No | 表示每种对应颜色在颜色数组中的相对位置。数组长度需和colors保持一致， 数组的首个元素应当是0.0，末尾元素应当是1.0，中间的元素应当在0与1之间并且逐下标递增，表示colors中每个对应颜色的相对位置。 当不传该参数，或者pos传入undefined时，默认为null，表示颜色均匀分布在起点和终点之间。 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No | 矩阵对象，用于对着色器做矩阵变换。当不传该参数，或者matrix传入undefined时，默认为null，表示单位矩阵。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 返回线性渐变着色器对象。创建失败时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createRadialGradient

```TypeScript
static createRadialGradient(centerPt: common2D.Point, radius: double, colors: Array<int>,
      mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect
```

创建着色器，使用给定的圆心和半径生成径向渐变。径向渐变是指颜色从圆心逐渐向外扩散形成的渐变。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ShaderEffect-static createRadialGradient(centerPt: common2D.Point, radius: double, colors: Array<int>,      mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect--><!--Device-ShaderEffect-static createRadialGradient(centerPt: common2D.Point, radius: double, colors: Array<int>,      mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| centerPt | common2D.Point | Yes | 表示渐变的圆心。 |
| radius | double | Yes | 表示渐变的半径，小于等于0时无效，该参数为浮点数。单位为物理像素px。 |
| colors | Array&lt;int&gt; | Yes | 表示在圆心和圆边界之间分布的颜色数组，数组中的值为32位（ARGB）无符号整数。 |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes | 着色器效果平铺模式。 |
| pos | Array&lt;double&gt; \| null | No | 表示每种对应颜色在颜色数组中的相对位置。数组长度需和colors保持一致，数组的首个元素应当是0.0，末尾元素应当是1.0，中间的元素应当在0与1 之间并且逐下标递增，表示colors中每个对应颜色的相对位置。默认为null，表示颜色均匀分布在圆心和圆边界之间。 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No | 矩阵对象，用于对着色器做矩阵变换。默认为null，表示单位矩阵。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 返回径向渐变着色器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createRadialGradient

```TypeScript
static createRadialGradient(centerPt: common2D.Point, radius: double, colors: Array<int>,
      mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined
```

创建着色器，使用给定的圆心和半径生成径向渐变。径向渐变是指颜色从圆心逐渐向外扩散形成的渐变。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ShaderEffect-static createRadialGradient(centerPt: common2D.Point, radius: double, colors: Array<int>,      mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined--><!--Device-ShaderEffect-static createRadialGradient(centerPt: common2D.Point, radius: double, colors: Array<int>,      mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| centerPt | common2D.Point | Yes | 表示渐变的圆心。 |
| radius | double | Yes | 表示渐变的半径，小于等于0时无效，该参数为浮点数。单位为物理像素px。 |
| colors | Array&lt;int&gt; | Yes | 表示在圆心和圆边界之间分布的颜色数组，数组中的值为32位（ARGB）无符号整数。 |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes | 着色器效果平铺模式。 |
| pos | Array&lt;double&gt; \| null | No | 表示每种对应颜色在颜色数组中的相对位置。数组长度需和colors保持一致， 数组的首个元素应当是0.0，末尾元素应当是1.0，中间的元素应当在0与1之间并且逐下标递增，表示colors中每个对应颜色的相对位置。 当不传该参数，或者pos传入undefined时，默认为null，表示颜色均匀分布在圆心和圆边界之间。 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No | 矩阵对象，用于对着色器做矩阵变换。当不传该参数，或者matrix传入undefined时，默认为null，表示单位矩阵。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 返回径向渐变着色器对象。创建失败时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createSweepGradient

```TypeScript
static createSweepGradient(centerPt: common2D.Point, colors: Array<number>,
        mode: TileMode, startAngle: number, endAngle: number, pos?: Array<number> | null,
        matrix?: Matrix | null): ShaderEffect
```

创建着色器。该着色器以给定中心点为圆心，在起始角度和结束角度之间沿顺时针或逆时针方向生成颜色扇形渐变。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ShaderEffect-static createSweepGradient(centerPt: common2D.Point, colors: Array<number>,        mode: TileMode, startAngle: number, endAngle: number, pos?: Array<number> | null,        matrix?: Matrix | null): ShaderEffect--><!--Device-ShaderEffect-static createSweepGradient(centerPt: common2D.Point, colors: Array<number>,        mode: TileMode, startAngle: number, endAngle: number, pos?: Array<number> | null,        matrix?: Matrix | null): ShaderEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| centerPt | common2D.Point | Yes | 表示渐变的圆心。 |
| colors | Array&lt;number&gt; | Yes | 表示在起始角度和结束角度之间分布的颜色数组，数组中的值为32位（ARGB）无符号整数。 |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes | 着色器效果平铺模式。 |
| startAngle | number | Yes | 表示扇形渐变的起始角度，单位为度。0度时为x轴正方向，正数往顺时针方向偏移，负数往逆时针方向偏移。该参数为浮点数。 |
| endAngle | number | Yes | 表示扇形渐变的结束角度，单位为度。0度时为x轴正方向，正数往顺时针方向偏移，负数往逆时针方向偏移。小于起始角度时无效。该参数为浮点数。 |
| pos | Array&lt;number&gt; \| null | No | 表示每种对应颜色在颜色数组中的相对位置。数组长度需和colors保持一致，数组的首个元素应当是0.0，末尾元素应当是1.0，中间的元素应当在0与1 之间并且逐下标递增，表示colors中每个对应颜色的相对位置。默认为null，表示颜色均匀分布在起始角度和结束角度之间。 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No | 矩阵对象，用于对着色器做矩阵变换。默认为null，表示单位矩阵。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 返回扇形渐变着色器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createSweepGradient

```TypeScript
static createSweepGradient(centerPt: common2D.Point, colors: Array<int>,
      mode: TileMode, startAngle: double, endAngle: double, pos?: Array<double> | null,
      matrix?: Matrix | null): ShaderEffect | undefined
```

创建着色器。该着色器以给定中心点为圆心，在起始角度和结束角度之间沿顺时针或逆时针方向生成颜色扇形渐变。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ShaderEffect-static createSweepGradient(centerPt: common2D.Point, colors: Array<int>,      mode: TileMode, startAngle: double, endAngle: double, pos?: Array<double> | null,      matrix?: Matrix | null): ShaderEffect | undefined--><!--Device-ShaderEffect-static createSweepGradient(centerPt: common2D.Point, colors: Array<int>,      mode: TileMode, startAngle: double, endAngle: double, pos?: Array<double> | null,      matrix?: Matrix | null): ShaderEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| centerPt | common2D.Point | Yes | 表示渐变的圆心。 |
| colors | Array&lt;int&gt; | Yes | 表示在起始角度和结束角度之间分布的颜色数组，数组中的值为32位（ARGB）无符号整数。 |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes | 着色器效果平铺模式。 |
| startAngle | double | Yes | 表示扇形渐变的起始角度，单位为度。0度时为x轴正方向，正数往顺时针方向偏移，负数往逆时针方向偏移。该参数为浮点数。 |
| endAngle | double | Yes | 表示扇形渐变的结束角度，单位为度。0度时为x轴正方向，正数往顺时针方向偏移，负数往逆时针方向偏移。小于起始角度时无效。该参数为浮点数。 |
| pos | Array&lt;double&gt; \| null | No | 表示每种对应颜色在颜色数组中的相对位置。数组长度需和colors保持一致，数组的首个元素应当是0.0，末尾元素应当是1.0，中间的元素应当在0与1 之间并且逐下标递增，表示colors中每个对应颜色的相对位置。默认为null，表示颜色均匀分布在起始角度和结束角度之间。 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No | 矩阵对象，用于对着色器做矩阵变换。默认为null，表示单位矩阵。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 返回扇形渐变着色器对象。创建失败时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

