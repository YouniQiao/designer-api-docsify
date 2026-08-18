# Pen

画笔对象，用于描述所绘制图形形状的轮廓信息，支持设置颜色、线宽、抗锯齿、透明度、混合模式、转角样式、线帽样式，以及颜色滤波器、蒙版滤波器、路径效果、着色器、阴影层等绘制效果。 > **说明：** > > - 本模块使用屏幕物理像素单位px。 > > - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 23

<!--Device-drawing-class Pen--><!--Device-drawing-class Pen-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor()
```

构造一个新的画笔对象。

**起始版本：** 23

<!--Device-Pen-constructor()--><!--Device-Pen-constructor()-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(pen: Pen)
```

复制构造一个新的画笔对象。

**起始版本：** 23

<!--Device-Pen-constructor(pen: Pen)--><!--Device-Pen-constructor(pen: Pen)-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pen | [Pen](arkts-arkgraphics2d-drawing-pen-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getAlpha

```TypeScript
getAlpha(): number
```

获取画笔的透明度。

**起始版本：** 23

<!--Device-Pen-getAlpha(): int--><!--Device-Pen-getAlpha(): int-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getCapStyle

```TypeScript
getCapStyle(): CapStyle
```

获取画笔的线帽样式。

**起始版本：** 23

<!--Device-Pen-getCapStyle(): CapStyle--><!--Device-Pen-getCapStyle(): CapStyle-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [CapStyle](arkts-arkgraphics2d-drawing-capstyle-e.md) |

## getColor

```TypeScript
getColor(): common2D.Color
```

获取画笔的颜色。

**起始版本：** 12

<!--Device-Pen-getColor(): common2D.Color--><!--Device-Pen-getColor(): common2D.Color-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Color |

## getColor

```TypeScript
getColor(): common2D.Color | undefined
```

获取画笔的颜色。

**起始版本：** 23

<!--Device-Pen-getColor(): common2D.Color | undefined--><!--Device-Pen-getColor(): common2D.Color | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Color |

## getColor4f

```TypeScript
getColor4f(): common2D.Color4f
```

获取画笔的颜色，与[getColor](#getcolor)的区别在于返回值类型为 [common2D.Color4f](arkts-arkgraphics2d-common2d-color4f-i.md#color4f)，颜色通道值为浮点数，适用于需要浮点数类型的场景。

**起始版本：** 20

<!--Device-Pen-getColor4f(): common2D.Color4f--><!--Device-Pen-getColor4f(): common2D.Color4f-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Color4f |

## getColor4f

```TypeScript
getColor4f(): common2D.Color4f | undefined
```

获取画笔的颜色，与[getColor](#getcolor)的区别在于返回值类型为 [common2D.Color4f](arkts-arkgraphics2d-common2d-color4f-i.md#color4f)，颜色通道值为浮点数，适用于需要浮点数类型的场景。

**起始版本：** 24

<!--Device-Pen-getColor4f(): common2D.Color4f | undefined--><!--Device-Pen-getColor4f(): common2D.Color4f | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Color4f |

## getColorFilter

```TypeScript
getColorFilter(): ColorFilter
```

获取画笔的颜色滤波器。

**起始版本：** 12

<!--Device-Pen-getColorFilter(): ColorFilter--><!--Device-Pen-getColorFilter(): ColorFilter-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

## getColorFilter

```TypeScript
getColorFilter(): ColorFilter | undefined
```

获取画笔的颜色滤波器。

**起始版本：** 23

<!--Device-Pen-getColorFilter(): ColorFilter | undefined--><!--Device-Pen-getColorFilter(): ColorFilter | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

## getFillPath

```TypeScript
getFillPath(src: Path, dst: Path): boolean
```

获取使用画笔绘制的源路径轮廓，并用目标路径表示。

**起始版本：** 23

<!--Device-Pen-getFillPath(src: Path, dst: Path): boolean--><!--Device-Pen-getFillPath(src: Path, dst: Path): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getHexColor

```TypeScript
getHexColor(): number
```

获取画笔的颜色。

**起始版本：** 23

<!--Device-Pen-getHexColor(): int--><!--Device-Pen-getHexColor(): int-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getJoinStyle

```TypeScript
getJoinStyle(): JoinStyle
```

获取画笔绘制转角的样式。

**起始版本：** 23

<!--Device-Pen-getJoinStyle(): JoinStyle--><!--Device-Pen-getJoinStyle(): JoinStyle-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [JoinStyle](arkts-arkgraphics2d-drawing-joinstyle-e.md) |

## getMiterLimit

```TypeScript
getMiterLimit(): number
```

获取折线尖角长度与线宽的最大比值。

**起始版本：** 23

<!--Device-Pen-getMiterLimit(): double--><!--Device-Pen-getMiterLimit(): double-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getWidth

```TypeScript
getWidth(): number
```

获取画笔的线宽属性，线宽描述了画笔绘制图形轮廓的宽度。

**起始版本：** 23

<!--Device-Pen-getWidth(): double--><!--Device-Pen-getWidth(): double-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## isAntiAlias

```TypeScript
isAntiAlias(): boolean
```

获取画笔是否开启抗锯齿属性。

**起始版本：** 23

<!--Device-Pen-isAntiAlias(): boolean--><!--Device-Pen-isAntiAlias(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## reset

```TypeScript
reset(): void
```

重置当前画笔为初始状态。

**起始版本：** 23

<!--Device-Pen-reset(): void--><!--Device-Pen-reset(): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## setAlpha

```TypeScript
setAlpha(alpha: number): void
```

设置画笔的透明度。

**起始版本：** 23

<!--Device-Pen-setAlpha(alpha: int): void--><!--Device-Pen-setAlpha(alpha: int): void-End-->

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

设置画笔是否开启抗锯齿。开启后，使图形边缘在显示时更平滑。未调用此接口设置时，系统默认关闭抗锯齿。

**起始版本：** 23

<!--Device-Pen-setAntiAlias(aa: boolean): void--><!--Device-Pen-setAntiAlias(aa: boolean): void-End-->

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

设置画笔的混合模式。

**起始版本：** 23

<!--Device-Pen-setBlendMode(mode: BlendMode): void--><!--Device-Pen-setBlendMode(mode: BlendMode): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [BlendMode](../../apis-arkui/arkts-components/arkts-arkui-blendmode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setCapStyle

```TypeScript
setCapStyle(style: CapStyle): void
```

设置画笔的线帽样式。未调用此接口设置时，系统默认的线帽样式为FLAT_CAP。

**起始版本：** 23

<!--Device-Pen-setCapStyle(style: CapStyle): void--><!--Device-Pen-setCapStyle(style: CapStyle): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CapStyle](arkts-arkgraphics2d-drawing-capstyle-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setColor

```TypeScript
setColor(color: common2D.Color): void
```

设置画笔的颜色。

**起始版本：** 23

<!--Device-Pen-setColor(color: common2D.Color): void--><!--Device-Pen-setColor(color: common2D.Color): void-End-->

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

设置画笔的颜色。性能优于[setColor](#setcolor)接口，推荐使用本接口。

**起始版本：** 23

<!--Device-Pen-setColor(alpha: int, red: int, green: int, blue: int): void--><!--Device-Pen-setColor(alpha: int, red: int, green: int, blue: int): void-End-->

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

设置画笔的颜色。

**起始版本：** 23

<!--Device-Pen-setColor(color: int): void--><!--Device-Pen-setColor(color: int): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | number | 是 |

## setColor4f

```TypeScript
setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void
```

设置画笔的颜色以及标准色域，与[setColor](#setcolor)的区别在于可以单独设置色域。

**起始版本：** 24

<!--Device-Pen-setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void--><!--Device-Pen-setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void-End-->

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

给画笔添加额外的颜色滤波器。

**起始版本：** 23

<!--Device-Pen-setColorFilter(filter: ColorFilter | null): void--><!--Device-Pen-setColorFilter(filter: ColorFilter | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | ColorFilter \| null | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setDither

```TypeScript
setDither(dither: boolean): void
```

设置画笔是否开启抖动绘制效果。抖动绘制使颜色更真实。

**起始版本：** 23

<!--Device-Pen-setDither(dither: boolean): void--><!--Device-Pen-setDither(dither: boolean): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dither | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setImageFilter

```TypeScript
setImageFilter(filter: ImageFilter | null): void
```

设置画笔的图像滤波器。

**起始版本：** 23

<!--Device-Pen-setImageFilter(filter: ImageFilter | null): void--><!--Device-Pen-setImageFilter(filter: ImageFilter | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) \| null | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setJoinStyle

```TypeScript
setJoinStyle(style: JoinStyle): void
```

设置画笔绘制转角的样式。未调用此接口设置时，系统默认的转角样式为MITER_JOIN。

**起始版本：** 23

<!--Device-Pen-setJoinStyle(style: JoinStyle): void--><!--Device-Pen-setJoinStyle(style: JoinStyle): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [JoinStyle](arkts-arkgraphics2d-drawing-joinstyle-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setMaskFilter

```TypeScript
setMaskFilter(filter: MaskFilter | null): void
```

给画笔添加额外的蒙版滤镜。

**起始版本：** 23

<!--Device-Pen-setMaskFilter(filter: MaskFilter | null): void--><!--Device-Pen-setMaskFilter(filter: MaskFilter | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [MaskFilter](arkts-arkgraphics2d-drawing-maskfilter-c.md) \| null | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setMiterLimit

```TypeScript
setMiterLimit(miter: number): void
```

设置折线尖角长度与线宽的最大比值。当画笔绘制一条折线，并且[JoinStyle](arkts-arkgraphics2d-drawing-joinstyle-e.md#joinstyle)为MITER_JOIN时，若尖角长度与线宽的比值大于该最大比值，则该转角使用BEVEL_JOIN 绘制。

**起始版本：** 23

<!--Device-Pen-setMiterLimit(miter: double): void--><!--Device-Pen-setMiterLimit(miter: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| miter | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setPathEffect

```TypeScript
setPathEffect(effect: PathEffect | null): void
```

设置画笔路径效果。

**起始版本：** 23

<!--Device-Pen-setPathEffect(effect: PathEffect | null): void--><!--Device-Pen-setPathEffect(effect: PathEffect | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effect | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) \| null | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setShaderEffect

```TypeScript
setShaderEffect(shaderEffect: ShaderEffect | null): void
```

设置画笔着色器效果。

**起始版本：** 23

<!--Device-Pen-setShaderEffect(shaderEffect: ShaderEffect | null): void--><!--Device-Pen-setShaderEffect(shaderEffect: ShaderEffect | null): void-End-->

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

设置画笔阴影层效果。当前仅在绘制文字时生效。

**起始版本：** 23

<!--Device-Pen-setShadowLayer(shadowLayer: ShadowLayer | null): void--><!--Device-Pen-setShadowLayer(shadowLayer: ShadowLayer | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shadowLayer | [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) \| null | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setStrokeWidth

```TypeScript
setStrokeWidth(width: number): void
```

设置画笔的线宽。0线宽被视作特殊的极细线宽，在绘制时始终会被绘制为1像素，不随画布的缩放而改变；负数线宽在实际绘制时会被视作0线宽。

**起始版本：** 23

<!--Device-Pen-setStrokeWidth(width: double): void--><!--Device-Pen-setStrokeWidth(width: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
