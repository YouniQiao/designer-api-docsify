# ShaderEffect

着色器，用于在绘图中填充颜色和渐变效果。画刷和画笔设置着色器后，会使用着色器效果而不是颜色属性去绘制，但此时画刷和画笔的透明度属性仍然生效。 着色器支持创建单色着色器、线性渐变、径向渐变、扇形渐变、锥形渐变、图片着色器及混合着色器等多种类型。 > **说明：** > > - 本Class首批接口从API version 12开始支持。 > > - 本模块使用屏幕物理像素单位px。 > > - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 23

**废弃版本：** -1

<!--Device-drawing-class ShaderEffect--><!--Device-drawing-class ShaderEffect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## createColorShader

```TypeScript
static createColorShader(color: number): ShaderEffect
```

创建具有单一颜色的着色器。

**起始版本：** 12

**废弃版本：** -1

<!--Device-ShaderEffect-static createColorShader(color: number): ShaderEffect--><!--Device-ShaderEffect-static createColorShader(color: number): ShaderEffect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## createColorShader

```TypeScript
static createColorShader(color: number): ShaderEffect | undefined
```

创建具有单一颜色的着色器。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ShaderEffect-static createColorShader(color: int): ShaderEffect | undefined--><!--Device-ShaderEffect-static createColorShader(color: int): ShaderEffect | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## createComposeShader

```TypeScript
static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,
        blendMode: BlendMode): ShaderEffect
```

按照指定的混合模式对两个着色器进行叠加，生成一个新的着色器。

**起始版本：** 20

**废弃版本：** -1

<!--Device-ShaderEffect-static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,        blendMode: BlendMode): ShaderEffect--><!--Device-ShaderEffect-static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,        blendMode: BlendMode): ShaderEffect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dstShaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 是 |
| srcShaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 是 |
| blendMode | [BlendMode](../../apis-arkui/arkts-components/arkts-arkui-blendmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |

## createComposeShader

```TypeScript
static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,
        blendMode: BlendMode): ShaderEffect | undefined
```

按照指定的混合模式对两个着色器进行叠加，生成一个新的着色器。

**起始版本：** 24

**废弃版本：** -1

<!--Device-ShaderEffect-static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,        blendMode: BlendMode): ShaderEffect | undefined--><!--Device-ShaderEffect-static createComposeShader(dstShaderEffect: ShaderEffect, srcShaderEffect: ShaderEffect,        blendMode: BlendMode): ShaderEffect | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dstShaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 是 |
| srcShaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 是 |
| blendMode | [BlendMode](../../apis-arkui/arkts-components/arkts-arkui-blendmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |

## createConicalGradient

```TypeScript
static createConicalGradient(startPt: common2D.Point, startRadius: number, endPt: common2D.Point,
        endRadius: number, colors: Array<number>, mode: TileMode,
        pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect
```

创建着色器，在给定两个圆之间生成锥形渐变。锥形渐变是指颜色在起始圆和结束圆之间，按照一定比例进行插值过渡形成的渐变效果。

**起始版本：** 12

**废弃版本：** -1

<!--Device-ShaderEffect-static createConicalGradient(startPt: common2D.Point, startRadius: number, endPt: common2D.Point,        endRadius: number, colors: Array<number>, mode: TileMode,        pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect--><!--Device-ShaderEffect-static createConicalGradient(startPt: common2D.Point, startRadius: number, endPt: common2D.Point,        endRadius: number, colors: Array<number>, mode: TileMode,        pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startPt | common2D.Point | 是 |
| startRadius | number | 是 |
| endPt | common2D.Point | 是 |
| endRadius | number | 是 |
| colors | Array & lt;number & gt; | 是 |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | 是 |
| pos | Array & lt;number & gt; \ | null | 否 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | 否 |

**返回值：**

| 类型 |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## createConicalGradient

```TypeScript
static createConicalGradient(startPt: common2D.Point, startRadius: number, endPt: common2D.Point,
        endRadius: number, colors: Array<number>, mode: TileMode,
        pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect | undefined
```

创建着色器，在给定两个圆之间生成锥形渐变。锥形渐变是指颜色在起始圆和结束圆之间，按照一定比例进行插值过渡形成的渐变效果。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ShaderEffect-static createConicalGradient(startPt: common2D.Point, startRadius: double, endPt: common2D.Point,        endRadius: double, colors: Array<int>, mode: TileMode,        pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined--><!--Device-ShaderEffect-static createConicalGradient(startPt: common2D.Point, startRadius: double, endPt: common2D.Point,        endRadius: double, colors: Array<int>, mode: TileMode,        pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startPt | common2D.Point | 是 |
| startRadius | number | 是 |
| endPt | common2D.Point | 是 |
| endRadius | number | 是 |
| colors | Array & lt;number & gt; | 是 |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | 是 |
| pos | Array & lt;number & gt; \ | null | 否 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | 否 |

**返回值：**

| 类型 |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## createImageShader

```TypeScript
static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,
        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect
```

基于图片创建一个着色器。此接口不建议用于录制类型的画布（即用于记录绘制指令而非直接渲染的Canvas对象），会影响性能。

**起始版本：** 20

**废弃版本：** -1

<!--Device-ShaderEffect-static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect--><!--Device-ShaderEffect-static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmap | image.PixelMap | 是 |
| tileX | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | 是 |
| tileY | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | 是 |
| samplingOptions | [SamplingOptions](arkts-arkgraphics2d-drawing-samplingoptions-c.md) | 是 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | 否 |

**返回值：**

| 类型 |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |

## createImageShader

```TypeScript
static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,
        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect | undefined
```

基于图片创建一个着色器。此接口不建议用于录制类型的画布（即用于记录绘制指令而非直接渲染的Canvas对象），会影响性能。

**起始版本：** 24

**废弃版本：** -1

<!--Device-ShaderEffect-static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect | undefined--><!--Device-ShaderEffect-static createImageShader(pixelmap: image.PixelMap, tileX: TileMode, tileY: TileMode,        samplingOptions: SamplingOptions, matrix?: Matrix | null): ShaderEffect | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmap | image.PixelMap | 是 |
| tileX | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | 是 |
| tileY | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | 是 |
| samplingOptions | [SamplingOptions](arkts-arkgraphics2d-drawing-samplingoptions-c.md) | 是 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | 否 |

**返回值：**

| 类型 |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |

## createLinearGradient

```TypeScript
static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<number>,
        mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect
```

创建着色器，在两个指定点之间生成线性渐变。

**起始版本：** 12

**废弃版本：** -1

<!--Device-ShaderEffect-static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<int>,        mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect--><!--Device-ShaderEffect-static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<int>,        mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startPt | common2D.Point | 是 |
| endPt | common2D.Point | 是 |
| colors | Array & lt;number & gt; | 是 |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | 是 |
| pos | Array & lt;number & gt; \ | null | 否 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | 否 |

**返回值：**

| 类型 |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## createLinearGradient

```TypeScript
static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<number>,
        mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect | undefined
```

创建着色器，在两个指定点之间生成线性渐变。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ShaderEffect-static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<int>,        mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined--><!--Device-ShaderEffect-static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<int>,        mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startPt | common2D.Point | 是 |
| endPt | common2D.Point | 是 |
| colors | Array & lt;number & gt; | 是 |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | 是 |
| pos | Array & lt;number & gt; \ | null | 否 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | 否 |

**返回值：**

| 类型 |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## createRadialGradient

```TypeScript
static createRadialGradient(centerPt: common2D.Point, radius: number, colors: Array<number>,
      mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect
```

创建着色器，使用给定的圆心和半径生成径向渐变。径向渐变是指颜色从圆心逐渐向外扩散形成的渐变。

**起始版本：** 12

**废弃版本：** -1

<!--Device-ShaderEffect-static createRadialGradient(centerPt: common2D.Point, radius: double, colors: Array<int>,      mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect--><!--Device-ShaderEffect-static createRadialGradient(centerPt: common2D.Point, radius: double, colors: Array<int>,      mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| centerPt | common2D.Point | 是 |
| radius | number | 是 |
| colors | Array & lt;number & gt; | 是 |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | 是 |
| pos | Array & lt;number & gt; \ | null | 否 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | 否 |

**返回值：**

| 类型 |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## createRadialGradient

```TypeScript
static createRadialGradient(centerPt: common2D.Point, radius: number, colors: Array<number>,
      mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect | undefined
```

创建着色器，使用给定的圆心和半径生成径向渐变。径向渐变是指颜色从圆心逐渐向外扩散形成的渐变。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ShaderEffect-static createRadialGradient(centerPt: common2D.Point, radius: double, colors: Array<int>,      mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined--><!--Device-ShaderEffect-static createRadialGradient(centerPt: common2D.Point, radius: double, colors: Array<int>,      mode: TileMode, pos?: Array<double> | null, matrix?: Matrix | null): ShaderEffect | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| centerPt | common2D.Point | 是 |
| radius | number | 是 |
| colors | Array & lt;number & gt; | 是 |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | 是 |
| pos | Array & lt;number & gt; \ | null | 否 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | 否 |

**返回值：**

| 类型 |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## createSweepGradient

```TypeScript
static createSweepGradient(centerPt: common2D.Point, colors: Array<number>,
        mode: TileMode, startAngle: number, endAngle: number, pos?: Array<number> | null,
        matrix?: Matrix | null): ShaderEffect
```

创建着色器。该着色器以给定中心点为圆心，在起始角度和结束角度之间沿顺时针或逆时针方向生成颜色扇形渐变。

**起始版本：** 12

**废弃版本：** -1

<!--Device-ShaderEffect-static createSweepGradient(centerPt: common2D.Point, colors: Array<number>,        mode: TileMode, startAngle: number, endAngle: number, pos?: Array<number> | null,        matrix?: Matrix | null): ShaderEffect--><!--Device-ShaderEffect-static createSweepGradient(centerPt: common2D.Point, colors: Array<number>,        mode: TileMode, startAngle: number, endAngle: number, pos?: Array<number> | null,        matrix?: Matrix | null): ShaderEffect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| centerPt | common2D.Point | 是 |
| colors | Array & lt;number & gt; | 是 |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | 是 |
| startAngle | number | 是 |
| endAngle | number | 是 |
| pos | Array & lt;number & gt; \ | null | 否 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | 否 |

**返回值：**

| 类型 |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## createSweepGradient

```TypeScript
static createSweepGradient(centerPt: common2D.Point, colors: Array<number>,
      mode: TileMode, startAngle: number, endAngle: number, pos?: Array<number> | null,
      matrix?: Matrix | null): ShaderEffect | undefined
```

创建着色器。该着色器以给定中心点为圆心，在起始角度和结束角度之间沿顺时针或逆时针方向生成颜色扇形渐变。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ShaderEffect-static createSweepGradient(centerPt: common2D.Point, colors: Array<int>,      mode: TileMode, startAngle: double, endAngle: double, pos?: Array<double> | null,      matrix?: Matrix | null): ShaderEffect | undefined--><!--Device-ShaderEffect-static createSweepGradient(centerPt: common2D.Point, colors: Array<int>,      mode: TileMode, startAngle: double, endAngle: double, pos?: Array<double> | null,      matrix?: Matrix | null): ShaderEffect | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| centerPt | common2D.Point | 是 |
| colors | Array & lt;number & gt; | 是 |
| mode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | 是 |
| startAngle | number | 是 |
| endAngle | number | 是 |
| pos | Array & lt;number & gt; \ | null | 否 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | 否 |

**返回值：**

| 类型 |
| --- |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
