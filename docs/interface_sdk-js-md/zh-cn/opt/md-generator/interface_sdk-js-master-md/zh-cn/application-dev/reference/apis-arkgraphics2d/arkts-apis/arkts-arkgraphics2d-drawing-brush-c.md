# Brush

画刷对象，用于设置图形的填充样式，包括颜色、抗锯齿、混合模式、颜色滤波器、蒙版滤波器、着色器效果、阴影层效果及图像滤波器等，并支持获取颜色、透明度、抗锯齿等属性及重置画刷为初始状态。 画刷需通过Canvas的[attachBrush](arkts-arkgraphics2d-drawing-canvas-c.md#attachbrush)方法绑定到画布后生效，绘制完成后通过 [detachBrush](arkts-arkgraphics2d-drawing-canvas-c.md#detachbrush)方法解绑；画刷用于图形填充，画笔（Pen）用于图形描边，详见[Pen](arkts-arkgraphics2d-drawing-pen-c.md#pen)。 > **说明：** > > - 本模块使用屏幕物理像素单位px。 > > - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 23

<!--Device-drawing-class Brush--><!--Device-drawing-class Brush-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor()
```

构造一个新的画刷对象。默认配置：新建画刷默认抗锯齿关闭、混合模式为SRC_OVER，且未设置颜色滤波器、蒙版滤波器、着色器效果、 阴影层效果和图像滤波器。

**起始版本：** 23

<!--Device-Brush-constructor()--><!--Device-Brush-constructor()-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(brush: Brush)
```

复制构造一个新的画刷对象。

**起始版本：** 23

<!--Device-Brush-constructor(brush: Brush)--><!--Device-Brush-constructor(brush: Brush)-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| brush | [Brush](arkts-arkgraphics2d-drawing-brush-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getAlpha

```TypeScript
getAlpha(): number
```

获取画刷的透明度。

**起始版本：** 23

<!--Device-Brush-getAlpha(): int--><!--Device-Brush-getAlpha(): int-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getColor

```TypeScript
getColor(): common2D.Color
```

获取画刷的颜色。

**起始版本：** 12

<!--Device-Brush-getColor(): common2D.Color--><!--Device-Brush-getColor(): common2D.Color-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Color |

## getColor

```TypeScript
getColor(): common2D.Color | undefined
```

获取画刷的颜色。

**起始版本：** 23

<!--Device-Brush-getColor(): common2D.Color | undefined--><!--Device-Brush-getColor(): common2D.Color | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Color |

## getColor4f

```TypeScript
getColor4f(): common2D.Color4f
```

获取画刷的颜色，与[getColor](#getcolor)的区别是返回值类型为浮点数，适用于需要浮点数类型的场景。

**起始版本：** 20

<!--Device-Brush-getColor4f(): common2D.Color4f--><!--Device-Brush-getColor4f(): common2D.Color4f-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Color4f |

## getColor4f

```TypeScript
getColor4f(): common2D.Color4f | undefined
```

获取画刷的颜色，与[getColor](#getcolor)的区别是返回值类型为浮点数，适用于需要浮点数类型的场景。

**起始版本：** 24

<!--Device-Brush-getColor4f(): common2D.Color4f | undefined--><!--Device-Brush-getColor4f(): common2D.Color4f | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Color4f |

## getColorFilter

```TypeScript
getColorFilter(): ColorFilter
```

获取画刷的颜色滤波器。

**起始版本：** 12

<!--Device-Brush-getColorFilter(): ColorFilter--><!--Device-Brush-getColorFilter(): ColorFilter-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

## getColorFilter

```TypeScript
getColorFilter(): ColorFilter | undefined
```

获取画刷的颜色滤波器。

**起始版本：** 23

<!--Device-Brush-getColorFilter(): ColorFilter | undefined--><!--Device-Brush-getColorFilter(): ColorFilter | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

## getHexColor

```TypeScript
getHexColor(): number
```

获取画刷颜色的16进制ARGB格式值。与[getColor](#getcolor)的区别是返回值类型为16进制ARGB格式的32位无符号整数。

**起始版本：** 23

<!--Device-Brush-getHexColor(): int--><!--Device-Brush-getHexColor(): int-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## isAntiAlias

```TypeScript
isAntiAlias(): boolean
```

获取画刷是否开启抗锯齿属性。

**起始版本：** 23

<!--Device-Brush-isAntiAlias(): boolean--><!--Device-Brush-isAntiAlias(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## reset

```TypeScript
reset(): void
```

重置当前画刷为初始状态，清除已设置的颜色、透明度、抗锯齿、颜色滤波器、蒙版滤波器、着色器效果、阴影层效果、混合模式和图像滤波器等属性。初始状态的具体取值：抗锯齿关闭、混合模式为SRC_OVER，且未设置颜色滤波器、蒙版滤波器、 着色器效果、阴影层效果和图像滤波器。如需使用上述属性，需要重新调用对应的set接口进行设置。

**起始版本：** 23

<!--Device-Brush-reset(): void--><!--Device-Brush-reset(): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## setAlpha

```TypeScript
setAlpha(alpha: number): void
```

设置画刷的透明度。调用setAlpha后，渲染时以setAlpha设置的透明度为准，覆盖setColor中Color对象的alpha通道值。

**起始版本：** 23

<!--Device-Brush-setAlpha(alpha: int): void--><!--Device-Brush-setAlpha(alpha: int): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alpha | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setAntiAlias

```TypeScript
setAntiAlias(aa: boolean): void
```

设置画刷是否开启抗锯齿。开启后，图形边缘显示更平滑。未调用此接口设置时，系统默认关闭抗锯齿。

**起始版本：** 23

<!--Device-Brush-setAntiAlias(aa: boolean): void--><!--Device-Brush-setAntiAlias(aa: boolean): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| aa | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setBlendMode

```TypeScript
setBlendMode(mode: BlendMode): void
```

设置画刷的混合模式。未调用此接口设置时，系统默认的混合模式为SRC_OVER。

**起始版本：** 23

<!--Device-Brush-setBlendMode(mode: BlendMode): void--><!--Device-Brush-setBlendMode(mode: BlendMode): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [BlendMode](../../apis-arkui/arkts-components/arkts-arkui-blendmode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setColor

```TypeScript
setColor(color: common2D.Color): void
```

设置画刷的颜色。设置的颜色将作为图形填充的基础颜色，在未设置ShaderEffect时以该颜色进行渲染填充。

**起始版本：** 23

<!--Device-Brush-setColor(color: common2D.Color): void--><!--Device-Brush-setColor(color: common2D.Color): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | common2D.Color | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setColor

```TypeScript
setColor(alpha: number, red: number, green: number, blue: number): void
```

设置画刷的颜色。性能优于[setColor](#setcolor)接口，推荐使用本接口。

**起始版本：** 23

<!--Device-Brush-setColor(alpha: int, red: int, green: int, blue: int): void--><!--Device-Brush-setColor(alpha: int, red: int, green: int, blue: int): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alpha | number | 是 |
| red | number | 是 |
| green | number | 是 |
| blue | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setColor

```TypeScript
setColor(color: number): void
```

设置画刷的颜色。与[setColor](#setcolor)的区别是支持通过16进制ARGB数值直接设置颜色。

**起始版本：** 23

<!--Device-Brush-setColor(color: int): void--><!--Device-Brush-setColor(color: int): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setColor4f

```TypeScript
setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void
```

设置画刷的颜色以及标准色域。与[setColor](#setcolor)的区别是可以单独设置色域， 适用于需要单独设置色域的场景。

**起始版本：** 24

<!--Device-Brush-setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void--><!--Device-Brush-setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color4f | common2D.Color4f | 是 |
| colorSpace | colorSpaceManager.ColorSpaceManager \| null | 是 |

## setColorFilter

```TypeScript
setColorFilter(filter: ColorFilter | null): void
```

设置画刷的颜色滤波器。

**起始版本：** 23

<!--Device-Brush-setColorFilter(filter: ColorFilter | null): void--><!--Device-Brush-setColorFilter(filter: ColorFilter | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | ColorFilter \| null | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setImageFilter

```TypeScript
setImageFilter(filter: ImageFilter | null): void
```

设置画刷的图像滤波器。

**起始版本：** 23

<!--Device-Brush-setImageFilter(filter: ImageFilter | null): void--><!--Device-Brush-setImageFilter(filter: ImageFilter | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) \| null | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setMaskFilter

```TypeScript
setMaskFilter(filter: MaskFilter | null): void
```

设置画刷的蒙版滤波器。

**起始版本：** 23

<!--Device-Brush-setMaskFilter(filter: MaskFilter | null): void--><!--Device-Brush-setMaskFilter(filter: MaskFilter | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [MaskFilter](arkts-arkgraphics2d-drawing-maskfilter-c.md) \| null | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setShaderEffect

```TypeScript
setShaderEffect(shaderEffect: ShaderEffect | null): void
```

设置画刷的着色器效果。

**起始版本：** 23

<!--Device-Brush-setShaderEffect(shaderEffect: ShaderEffect | null): void--><!--Device-Brush-setShaderEffect(shaderEffect: ShaderEffect | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) \| null | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setShadowLayer

```TypeScript
setShadowLayer(shadowLayer: ShadowLayer | null): void
```

设置画刷的阴影层效果。当前仅在通过Canvas的[drawTextBlob](arkts-arkgraphics2d-drawing-canvas-c.md#drawtextblob)等方法绘制文字时生效。

**起始版本：** 23

<!--Device-Brush-setShadowLayer(shadowLayer: ShadowLayer | null): void--><!--Device-Brush-setShadowLayer(shadowLayer: ShadowLayer | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shadowLayer | [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) \| null | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
