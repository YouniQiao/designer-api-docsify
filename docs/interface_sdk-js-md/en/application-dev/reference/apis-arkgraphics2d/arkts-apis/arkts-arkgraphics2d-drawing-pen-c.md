# Pen

画笔对象，用于描述所绘制图形形状的轮廓信息，支持设置颜色、线宽、抗锯齿、透明度、混合模式、转角样式、线帽样式，以及颜色滤波器、蒙版滤波器、路径效果、着色器、阴影层等绘制效果。

> **说明：**
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-drawing-class Pen--><!--Device-drawing-class Pen-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor()
```

构造一个新的画笔对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-constructor()--><!--Device-Pen-constructor()-End-->

**System capability:** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(pen: Pen)
```

复制构造一个新的画笔对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-constructor(pen: Pen)--><!--Device-Pen-constructor(pen: Pen)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pen | [Pen](arkts-arkgraphics2d-drawing-pen-c.md) | Yes | 待复制的画笔对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## getAlpha

ArkTS-Dyn:
```TypeScript
getAlpha(): number
```

ArkTS-Sta:
```TypeScript
getAlpha(): int
```

获取画笔的透明度。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-getAlpha(): int--><!--Device-Pen-getAlpha(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 返回画笔的透明度，该返回值为0到255之间的整数。 |

## getCapStyle

```TypeScript
getCapStyle(): CapStyle
```

获取画笔的线帽样式。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-getCapStyle(): CapStyle--><!--Device-Pen-getCapStyle(): CapStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [CapStyle](arkts-arkgraphics2d-drawing-capstyle-e.md) | 返回画笔的线帽样式。 |

## getColor

```TypeScript
getColor(): common2D.Color
```

获取画笔的颜色。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-Pen-getColor(): common2D.Color--><!--Device-Pen-getColor(): common2D.Color-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Color | 返回画笔当前设置的颜色。 |

## getColor

```TypeScript
getColor(): common2D.Color | undefined
```

获取画笔的颜色。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Pen-getColor(): common2D.Color | undefined--><!--Device-Pen-getColor(): common2D.Color | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Color | 返回画笔当前设置的颜色。获取失败时返回undefined。 |

## getColor4f

```TypeScript
getColor4f(): common2D.Color4f
```

获取画笔的颜色，与[getColor](arkts-arkgraphics2d-drawing-pen-c.md#getcolor)的区别在于返回值类型为  
[common2D.Color4f](arkts-arkgraphics2d-common2d-color4f-i.md)，颜色通道值为浮点数，适用于需要浮点数类型的场景。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Pen-getColor4f(): common2D.Color4f--><!--Device-Pen-getColor4f(): common2D.Color4f-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Color4f | 返回画笔当前设置的颜色，为ARGB格式的浮点数表示，每个颜色通道的取值范围为[0.0, 1.0]。 |

## getColor4f

```TypeScript
getColor4f(): common2D.Color4f | undefined
```

获取画笔的颜色，与[getColor](arkts-arkgraphics2d-drawing-pen-c.md#getcolor)的区别在于返回值类型为  
[common2D.Color4f](arkts-arkgraphics2d-common2d-color4f-i.md)，颜色通道值为浮点数，适用于需要浮点数类型的场景。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-Pen-getColor4f(): common2D.Color4f | undefined--><!--Device-Pen-getColor4f(): common2D.Color4f | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Color4f | 返回画笔当前设置的颜色，为ARGB格式的浮点数表示，每个颜色通道的取值范围为[0.0, 1.0]。获取失败时返回undefined。 |

## getColorFilter

```TypeScript
getColorFilter(): ColorFilter
```

获取画笔的颜色滤波器。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-Pen-getColorFilter(): ColorFilter--><!--Device-Pen-getColorFilter(): ColorFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) | 返回画笔当前设置的颜色滤波器，可用于查询当前画笔的颜色过滤效果。 |

## getColorFilter

```TypeScript
getColorFilter(): ColorFilter | undefined
```

获取画笔的颜色滤波器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Pen-getColorFilter(): ColorFilter | undefined--><!--Device-Pen-getColorFilter(): ColorFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) | 返回画笔当前设置的颜色滤波器，可用于查询当前画笔的颜色过滤效果。获取失败时返回undefined。 |

## getFillPath

```TypeScript
getFillPath(src: Path, dst: Path): boolean
```

获取使用画笔绘制的源路径轮廓，并用目标路径表示。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-getFillPath(src: Path, dst: Path): boolean--><!--Device-Pen-getFillPath(src: Path, dst: Path): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes | 待提取轮廓的源路径对象。 |
| dst | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes | 目标路径对象，用于存储根据画笔属性从src路径计算得到的轮廓结果。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回获取源路径轮廓是否成功，true表示成功，false表示失败。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## getHexColor

ArkTS-Dyn:
```TypeScript
getHexColor(): number
```

ArkTS-Sta:
```TypeScript
getHexColor(): int
```

获取画笔的颜色。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-Pen-getHexColor(): int--><!--Device-Pen-getHexColor(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 返回画笔的颜色，以16进制ARGB格式的32位无符号整数表示。 |

## getJoinStyle

```TypeScript
getJoinStyle(): JoinStyle
```

获取画笔绘制转角的样式。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-getJoinStyle(): JoinStyle--><!--Device-Pen-getJoinStyle(): JoinStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [JoinStyle](arkts-arkgraphics2d-drawing-joinstyle-e.md) | 返回折线转角的样式。 |

## getMiterLimit

ArkTS-Dyn:
```TypeScript
getMiterLimit(): number
```

ArkTS-Sta:
```TypeScript
getMiterLimit(): double
```

获取折线尖角长度与线宽的最大比值。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-getMiterLimit(): double--><!--Device-Pen-getMiterLimit(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 返回折线尖角长度与线宽的最大比值。 |

## getWidth

ArkTS-Dyn:
```TypeScript
getWidth(): number
```

ArkTS-Sta:
```TypeScript
getWidth(): double
```

获取画笔的线宽属性，线宽描述了画笔绘制图形轮廓的宽度。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-getWidth(): double--><!--Device-Pen-getWidth(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 返回画笔的线宽，单位为物理像素px。 |

## isAntiAlias

```TypeScript
isAntiAlias(): boolean
```

获取画笔是否开启抗锯齿属性。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-isAntiAlias(): boolean--><!--Device-Pen-isAntiAlias(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回画笔是否开启抗锯齿属性，true表示开启，false表示关闭。 |

## reset

```TypeScript
reset(): void
```

重置当前画笔为初始状态。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-reset(): void--><!--Device-Pen-reset(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## setAlpha

ArkTS-Dyn:
```TypeScript
setAlpha(alpha: number): void
```

ArkTS-Sta:
```TypeScript
setAlpha(alpha: int): void
```

设置画笔的透明度。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Pen-setAlpha(alpha: int): void--><!--Device-Pen-setAlpha(alpha: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| alpha | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示透明度，取值范围为[0, 255]，传入浮点类型时向下取整。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## setAntiAlias

```TypeScript
setAntiAlias(aa: boolean): void
```

设置画笔是否开启抗锯齿。开启后，使图形边缘在显示时更平滑。未调用此接口设置时，系统默认关闭抗锯齿。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Pen-setAntiAlias(aa: boolean): void--><!--Device-Pen-setAntiAlias(aa: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| aa | boolean | Yes | 表示是否开启抗锯齿。true表示开启，false表示关闭。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## setBlendMode

```TypeScript
setBlendMode(mode: BlendMode): void
```

设置画笔的混合模式。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Pen-setBlendMode(mode: BlendMode): void--><!--Device-Pen-setBlendMode(mode: BlendMode): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [BlendMode](../../apis-arkui/arkts-apis/arkts-arkui-common-blendmode-e.md) | Yes | 颜色的混合模式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## setCapStyle

```TypeScript
setCapStyle(style: CapStyle): void
```

设置画笔的线帽样式。未调用此接口设置时，系统默认的线帽样式为FLAT_CAP。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-setCapStyle(style: CapStyle): void--><!--Device-Pen-setCapStyle(style: CapStyle): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CapStyle](arkts-arkgraphics2d-drawing-capstyle-e.md) | Yes | 描述画笔的线帽样式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## setColor

```TypeScript
setColor(color: common2D.Color): void
```

设置画笔的颜色。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Pen-setColor(color: common2D.Color): void--><!--Device-Pen-setColor(color: common2D.Color): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | common2D.Color | Yes | ARGB格式的颜色，每个颜色通道的值是0到255之间的整数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## setColor

ArkTS-Dyn:
```TypeScript
setColor(alpha: number, red: number, green: number, blue: number): void
```

ArkTS-Sta:
```TypeScript
setColor(alpha: int, red: int, green: int, blue: int): void
```

设置画笔的颜色。性能优于[setColor](arkts-arkgraphics2d-drawing-pen-c.md#setcolor)接口，推荐使用本接口。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-setColor(alpha: int, red: int, green: int, blue: int): void--><!--Device-Pen-setColor(alpha: int, red: int, green: int, blue: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| alpha | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ARGB格式颜色的透明度通道值，该参数取值范围是[0, 255]，传入范围内的浮点数会向下取整，超出范围的值会被截断到0或255。 |
| red | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ARGB格式颜色的红色通道值，该参数取值范围是[0, 255]，传入范围内的浮点数会向下取整，超出范围的值会被截断到0或255。 |
| green | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ARGB格式颜色的绿色通道值，该参数取值范围是[0, 255]，传入范围内的浮点数会向下取整，超出范围的值会被截断到0或255。 |
| blue | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ARGB格式颜色的蓝色通道值，该参数取值范围是[0, 255]，传入范围内的浮点数会向下取整，超出范围的值会被截断到0或255。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## setColor

ArkTS-Dyn:
```TypeScript
setColor(color: number): void
```

ArkTS-Sta:
```TypeScript
setColor(color: int): void
```

设置画笔的颜色。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-Pen-setColor(color: int): void--><!--Device-Pen-setColor(color: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 16进制ARGB格式的颜色，格式为0xAARRGGBB，其中AA表示透明度通道，RR表示红色通道，GG表示绿色通道，BB表示蓝色通道，各通道取值范围为00-FF，取值范围为 [0x00000000, 0xFFFFFFFF]。超出有效范围的值会被截断处理。 |

## setColor4f

```TypeScript
setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void
```

设置画笔的颜色以及标准色域，与[setColor](arkts-arkgraphics2d-drawing-pen-c.md#setcolor)的区别在于可以单独设置色域。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-Pen-setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void--><!--Device-Pen-setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color4f | common2D.Color4f | Yes | ARGB格式的颜色，浮点数，每个颜色通道值的范围为[0.0, 1.0]，超出范围的值会被截断到0.0或1.0。 |
| colorSpace | colorSpaceManager.ColorSpaceManager \| null | Yes | 标准色域对象，null表示使用SRGB色域。 |

## setColorFilter

```TypeScript
setColorFilter(filter: ColorFilter | null): void
```

给画笔添加额外的颜色滤波器。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Pen-setColorFilter(filter: ColorFilter | null): void--><!--Device-Pen-setColorFilter(filter: ColorFilter | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) \| null | Yes | 颜色滤波器。null表示清空颜色滤波器。<br>**Since:** 20 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## setDither

```TypeScript
setDither(dither: boolean): void
```

设置画笔是否开启抖动绘制效果。抖动绘制使颜色更真实。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Pen-setDither(dither: boolean): void--><!--Device-Pen-setDither(dither: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dither | boolean | Yes | 是否开启画笔的抖动绘制效果。true表示开启，false表示关闭。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## setImageFilter

```TypeScript
setImageFilter(filter: ImageFilter | null): void
```

设置画笔的图像滤波器。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-setImageFilter(filter: ImageFilter | null): void--><!--Device-Pen-setImageFilter(filter: ImageFilter | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) \| null | Yes | 图像滤波器，null表示清空画笔的图像滤波器效果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## setJoinStyle

```TypeScript
setJoinStyle(style: JoinStyle): void
```

设置画笔绘制转角的样式。未调用此接口设置时，系统默认的转角样式为MITER_JOIN。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-setJoinStyle(style: JoinStyle): void--><!--Device-Pen-setJoinStyle(style: JoinStyle): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [JoinStyle](arkts-arkgraphics2d-drawing-joinstyle-e.md) | Yes | 折线转角样式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## setMaskFilter

```TypeScript
setMaskFilter(filter: MaskFilter | null): void
```

给画笔添加额外的蒙版滤镜。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-setMaskFilter(filter: MaskFilter | null): void--><!--Device-Pen-setMaskFilter(filter: MaskFilter | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [MaskFilter](arkts-arkgraphics2d-drawing-maskfilter-c.md) \| null | Yes | 蒙版滤镜。null表示清空蒙版滤镜。<br>**Since:** 20 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## setMiterLimit

ArkTS-Dyn:
```TypeScript
setMiterLimit(miter: number): void
```

ArkTS-Sta:
```TypeScript
setMiterLimit(miter: double): void
```

设置折线尖角长度与线宽的最大比值。当画笔绘制一条折线，并且[JoinStyle](arkts-arkgraphics2d-drawing-joinstyle-e.md)为MITER_JOIN时，若尖角长度与线宽的比值大于该最大比值，则该转角使用BEVEL_JOIN绘制。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-setMiterLimit(miter: double): void--><!--Device-Pen-setMiterLimit(miter: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| miter | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 折线尖角长度与线宽的最大比值，负数在绘制时会被视作4.0处理，非负数按实际传入值生效，该参数为浮点数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## setPathEffect

```TypeScript
setPathEffect(effect: PathEffect | null): void
```

设置画笔路径效果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-setPathEffect(effect: PathEffect | null): void--><!--Device-Pen-setPathEffect(effect: PathEffect | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| effect | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) \| null | Yes | 路径效果对象，用于设置虚线、转角等路径绘制样式。null表示清空路径效果。<br>**Since:** 20 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## setShaderEffect

```TypeScript
setShaderEffect(shaderEffect: ShaderEffect | null): void
```

设置画笔着色器效果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-setShaderEffect(shaderEffect: ShaderEffect | null): void--><!--Device-Pen-setShaderEffect(shaderEffect: ShaderEffect | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| shaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) \| null | Yes | 着色器效果对象。null表示清空着色器效果。<br>**Since:** 20 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## setShadowLayer

```TypeScript
setShadowLayer(shadowLayer: ShadowLayer | null): void
```

设置画笔阴影层效果。当前仅在绘制文字时生效。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Pen-setShadowLayer(shadowLayer: ShadowLayer | null): void--><!--Device-Pen-setShadowLayer(shadowLayer: ShadowLayer | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| shadowLayer | [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) \| null | Yes | 阴影层对象。null表示清空阴影层效果。<br>**Since:** 20 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## setStrokeWidth

ArkTS-Dyn:
```TypeScript
setStrokeWidth(width: number): void
```

ArkTS-Sta:
```TypeScript
setStrokeWidth(width: double): void
```

设置画笔的线宽。0线宽被视作特殊的极细线宽，在绘制时始终会被绘制为1像素，不随画布的缩放而改变；负数线宽在实际绘制时会被视作0线宽。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Pen-setStrokeWidth(width: double): void--><!--Device-Pen-setStrokeWidth(width: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 表示线宽，该参数为浮点数，单位为物理像素px。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

