# Canvas

承载绘制内容与绘制状态的载体。Canvas提供矩形、圆形、椭圆、弧线、路径、文字、图片等多种图形的绘制能力，支持通过画笔和画刷设置绘制样式，支持画布裁剪、矩阵变换、画布状态保存与恢复等功能。

> **说明：**&gt;
> - 本模块使用屏幕物理像素单位px。&gt;
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。
> 
> **说明：**&gt;
> 画布自带一个默认画刷，该画刷为黑色，具备抗锯齿，不具备其他任何样式效果。当画布中没有主动设置画刷和画笔时，该默认画刷生效。

**起始版本：** 11

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## attachBrush

```TypeScript
attachBrush(brush: Brush): void
```

绑定画刷到画布上，在画布上进行绘制时，将使用画刷的样式对绘制图形形状的内部进行填充。调用本方法后，画刷将持续生效于后续所有绘制操作，直至调用 [detachBrush](#detachbrush)解除绑定。

> **说明：**&gt;
> 执行该方法后，若brush的效果发生改变并且开发者希望该变化在接下来的绘制动作中生效，需要再次调用本方法。

**起始版本：** 11

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| brush | [Brush](arkts-arkgraphics2d-drawing-brush-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## attachPen

```TypeScript
attachPen(pen: Pen): void
```

绑定画笔到画布上，在画布上进行绘制时，将使用画笔的样式去绘制图形形状的轮廓。调用本方法后，画笔将持续生效于后续所有绘制操作， 直至调用[detachPen](#detachpen)解除绑定。

> **说明：**&gt;
> 执行该方法后，若pen的效果发生改变并且开发者希望该变化在接下来的绘制动作中生效，需要再次调用本方法。

**起始版本：** 11

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pen | [Pen](arkts-arkgraphics2d-drawing-pen-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## clear

```TypeScript
clear(color: common2D.Color): void
```

使用指定颜色填充画布上的裁剪区域。效果等同于[drawColor](#drawcolor)。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | common2D.Color | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## clear

```TypeScript
clear(color: common2D.Color | number): void
```

使用指定颜色填充画布上的裁剪区域。效果等同于[drawColor](#drawcolor)。

**起始版本：** 18

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | common2D.Color \| number | 是 |

## clipPath

```TypeScript
clipPath(path: Path, clipOp?: ClipOp, doAntiAlias?: boolean): void
```

使用自定义路径对画布进行裁剪。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |
| clipOp | [ClipOp](arkts-arkgraphics2d-drawing-clipop-e.md) | 否 |
| doAntiAlias | boolean | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## clipRect

```TypeScript
clipRect(rect: common2D.Rect, clipOp?: ClipOp, doAntiAlias?: boolean): void
```

使用矩形对画布进行裁剪。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| clipOp | [ClipOp](arkts-arkgraphics2d-drawing-clipop-e.md) | 否 |
| doAntiAlias | boolean | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## clipRegion

```TypeScript
clipRegion(region: Region, clipOp?: ClipOp): void
```

在画布上裁剪一个区域。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](../../apis-image-kit/arkts-apis/arkts-image-image-region-i.md) | 是 |
| clipOp | [ClipOp](arkts-arkgraphics2d-drawing-clipop-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## clipRoundRect

```TypeScript
clipRoundRect(roundRect: RoundRect, clipOp?: ClipOp, doAntiAlias?: boolean): void
```

在画布上裁剪一个圆角矩形。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [roundRect](../../apis-arkui/arkts-apis/arkts-arkui-canvaspath-c.md) | [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) | 是 |
| clipOp | [ClipOp](arkts-arkgraphics2d-drawing-clipop-e.md) | 否 |
| doAntiAlias | boolean | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## concatMatrix

```TypeScript
concatMatrix(matrix: Matrix): void
```

画布现有矩阵左乘传入矩阵，不影响之前的绘制操作，后续绘制操作和裁剪操作的形状和位置都会受到该矩阵的影响。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## constructor

```TypeScript
constructor(pixelmap: image.PixelMap)
```

创建一个以PixelMap作为绘制目标的Canvas对象。

**起始版本：** 11

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmap | image.PixelMap | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## detachBrush

```TypeScript
detachBrush(): void
```

将画刷与画布解绑，在画布上进行绘制时，不会再使用画刷对绘制图形形状的内部进行填充。本方法与[attachBrush](#attachbrush)配合使用，用于在完成绘制后解除画刷绑定。

**起始版本：** 11

**系统能力：** SystemCapability.Graphics.Drawing

## detachPen

```TypeScript
detachPen(): void
```

将画笔与画布解绑，在画布上进行绘制时，不会再使用画笔去绘制图形形状的轮廓。本方法与[attachPen](#attachpen)配合使用，用于在完成绘制后解除画笔绑定。

**起始版本：** 11

**系统能力：** SystemCapability.Graphics.Drawing

## drawArc

```TypeScript
drawArc(arc: common2D.Rect, startAngle: number, sweepAngle: number): void
```

在画布上绘制圆弧，默认使用黑色填充内容。该方法允许指定起始角度、扫描角度。当扫描角度的绝对值大于360度时，则绘制椭圆。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [arc](../../apis-arkui/arkts-apis/arkts-arkui-canvaspath-c.md) | common2D.Rect | 是 |
| startAngle | number | 是 |
| sweepAngle | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawArcWithCenter

```TypeScript
drawArcWithCenter(arc: common2D.Rect, startAngle: number, sweepAngle: number, useCenter: boolean): void
```

在画布上绘制圆弧。与[drawArc](#drawarc)相比，本接口增加了useCenter参数，用于控制圆弧的起点和终点是否连接圆弧的中心点。该方法允许指定圆弧的起始角度和扫描角度。

**起始版本：** 18

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [arc](../../apis-arkui/arkts-apis/arkts-arkui-canvaspath-c.md) | common2D.Rect | 是 |
| startAngle | number | 是 |
| sweepAngle | number | 是 |
| useCenter | boolean | 是 |

## drawBackground

```TypeScript
drawBackground(brush: Brush): void
```

使用画刷填充画布的裁剪区域。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| brush | [Brush](arkts-arkgraphics2d-drawing-brush-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawCircle

```TypeScript
drawCircle(x: number, y: number, radius: number): void
```

绘制一个圆形。如果半径小于等于零，则不绘制。默认使用黑色填充内容。

**起始版本：** 11

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| radius | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawColor

```TypeScript
drawColor(color: common2D.Color, blendMode?: BlendMode): void
```

使用指定颜色并按照指定的[BlendMode](arkts-arkgraphics2d-drawing-blendmode-e.md)对画布当前裁剪区域进行填充。

**起始版本：** 11

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | common2D.Color | 是 |
| [blendMode](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md) | [BlendMode](../../apis-arkui/arkts-components/arkts-arkui-blendmode-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawColor

```TypeScript
drawColor(alpha: number, red: number, green: number, blue: number, blendMode?: BlendMode): void
```

使用指定颜色并按照指定的[BlendMode](arkts-arkgraphics2d-drawing-blendmode-e.md)对画布当前裁剪区域进行填充。性能优于 [drawColor](#drawcolor)接口，推荐使用本接口。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alpha | number | 是 |
| red | number | 是 |
| green | number | 是 |
| blue | number | 是 |
| [blendMode](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md) | [BlendMode](../../apis-arkui/arkts-components/arkts-arkui-blendmode-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawColor

```TypeScript
drawColor(color: number, blendMode?: BlendMode): void
```

使用指定颜色并按照指定的[BlendMode](arkts-arkgraphics2d-drawing-blendmode-e.md)对画布当前裁剪区域进行填充。

**起始版本：** 18

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | number | 是 |
| [blendMode](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md) | [BlendMode](../../apis-arkui/arkts-components/arkts-arkui-blendmode-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawGlyphs

```TypeScript
drawGlyphs(glyphIds: Array<number>, glyphIdOffset: number, positions: Array<common2D.Point>,
      positionOffset: number, glyphCount: number, font: Font): void
```

绘制具有指定字体的字形数组。如果字形计数小于或等于0，则不绘制任何内容。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| glyphIds | Array & lt;number & gt; | 是 |
| glyphIdOffset | number | 是 |
| positions | Array & lt;common2D.Point & gt; | 是 |
| positionOffset | number | 是 |
| glyphCount | number | 是 |
| font | [Font](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-font-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |

## drawImage

```TypeScript
drawImage(pixelmap: image.PixelMap, left: number, top: number, samplingOptions?: SamplingOptions): void
```

绘制一张图片，图片的左上角坐标为(left, top)。

**起始版本：** 11

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmap | image.PixelMap | 是 |
| left | number | 是 |
| top | number | 是 |
| samplingOptions | [SamplingOptions](arkts-arkgraphics2d-drawing-samplingoptions-c.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawImageLattice

```TypeScript
drawImageLattice(pixelmap: image.PixelMap, lattice: Lattice, dstRect: common2D.Rect,
      filterMode: FilterMode): void
```

将图像按照矩形网格对象的设置划分为多个网格，并把图像的每个部分按照网格对象的设置绘制到画布上的目标矩形区域。与[drawImageNine](#drawimagenine)固定将图像分割 为9个部分不同，本接口通过Lattice对象支持自定义网格分割。使用此接口时，设置开启抗锯齿无效。偶数行和列（起始计数为0）的每个交叉点对应的网格区域保持原始尺寸不缩放，若固定网格区域的尺寸不超过目标矩形，则会在不缩放的情况下被绘制在目标矩形，反之则会按比例缩放绘制在目标矩形；在角落区域绘制后，若目标矩形中仍有未被覆盖的区 域，则剩下的区域会通过拉伸或压缩来绘制，以便完全覆盖目标矩形。

**起始版本：** 18

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmap | image.PixelMap | 是 |
| [lattice](../../apis-arkui/arkts-components/arkts-arkui-resizableoptions-i.md) | [Lattice](arkts-arkgraphics2d-drawing-lattice-c.md) | 是 |
| dstRect | common2D.Rect | 是 |
| filterMode | [FilterMode](arkts-arkgraphics2d-drawing-filtermode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawImageNine

```TypeScript
drawImageNine(pixelmap: image.PixelMap, center: common2D.Rect, dstRect: common2D.Rect,
      filterMode: FilterMode): void
```

通过绘制两条水平线和两条垂直线将图像分割成9个部分：四个边、四个角和中心。使用此接口时，设置开启抗锯齿无效。若角落的4个区域尺寸不超过目标矩形，则会在不缩放的情况下被绘制在目标矩形，反之则会按比例缩放绘制在目标矩形；在角落区域绘制后，若目标矩形中仍有未被覆盖的区域，则剩下的5个区域会通过拉伸或压缩来绘制，以便完全覆盖目标矩形。

**起始版本：** 18

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmap | image.PixelMap | 是 |
| center | common2D.Rect | 是 |
| dstRect | common2D.Rect | 是 |
| filterMode | [FilterMode](arkts-arkgraphics2d-drawing-filtermode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawImageRect

```TypeScript
drawImageRect(pixelmap: image.PixelMap, dstRect: common2D.Rect, samplingOptions?: SamplingOptions): void
```

将图片绘制到画布的指定区域上。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmap | image.PixelMap | 是 |
| dstRect | common2D.Rect | 是 |
| samplingOptions | [SamplingOptions](arkts-arkgraphics2d-drawing-samplingoptions-c.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawImageRectWithSrc

```TypeScript
drawImageRectWithSrc(pixelmap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect,
      samplingOptions?: SamplingOptions, constraint?: SrcRectConstraint): void
```

将图片的指定区域绘制到画布的指定区域。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmap | image.PixelMap | 是 |
| srcRect | common2D.Rect | 是 |
| dstRect | common2D.Rect | 是 |
| samplingOptions | [SamplingOptions](arkts-arkgraphics2d-drawing-samplingoptions-c.md) | 否 |
| constraint | [SrcRectConstraint](arkts-arkgraphics2d-drawing-srcrectconstraint-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawLine

```TypeScript
drawLine(x0: number, y0: number, x1: number, y1: number): void
```

绘制一条直线段，从指定的起点到终点。如果直线段的起点和终点是同一个点，无法绘制。

**起始版本：** 11

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x0 | number | 是 |
| y0 | number | 是 |
| x1 | number | 是 |
| y1 | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawNestedRoundRect

```TypeScript
drawNestedRoundRect(outer: RoundRect, inner: RoundRect): void
```

绘制两个嵌套的圆角矩形，外部矩形边界必须完全包围内部矩形边界（即内部矩形必须完全位于外部矩形之内），否则无绘制效果。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| outer | [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) | 是 |
| inner | [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawOval

```TypeScript
drawOval(oval: common2D.Rect): void
```

在画布上绘制一个椭圆，椭圆的形状和位置由椭圆的外切矩形给出。默认使用黑色填充内容。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| oval | common2D.Rect | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawPath

```TypeScript
drawPath(path: Path): void
```

绘制一个自定义路径，默认使用黑色填充内容。该路径包含了一组路径轮廓，每个路径轮廓可以是开放的或封闭的。

**起始版本：** 11

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawPixelMapMesh

```TypeScript
drawPixelMapMesh(pixelmap: image.PixelMap, meshWidth: number, meshHeight: number,
      vertices: Array<number>, vertOffset: number, colors: Array<number> | null, colorOffset: number): void
```

在网格上绘制像素图，网格均匀分布在像素图上。（只支持画刷，使用画笔没有绘制效果。）

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmap | image.PixelMap | 是 |
| meshWidth | number | 是 |
| meshHeight | number | 是 |
| [vertices](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-customgeometry-c.md) | Array & lt;number & gt; | 是 |
| vertOffset | number | 是 |
| colors | Array & lt;number & gt; \ | null | 是 |
| colorOffset | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawPoint

```TypeScript
drawPoint(x: number, y: number): void
```

绘制一个点。

**起始版本：** 11

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawPoints

```TypeScript
drawPoints(points: Array<common2D.Point>, mode?: PointMode): void
```

在画布上绘制一组点、线段或多边形。通过指定点的数组和绘制模式来决定绘制方式。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| points | Array & lt;common2D.Point & gt; | 是 |
| mode | [PointMode](arkts-arkgraphics2d-drawing-pointmode-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawRect

```TypeScript
drawRect(rect: common2D.Rect): void
```

绘制一个矩形，默认使用黑色填充。

**起始版本：** 11

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawRect

```TypeScript
drawRect(left: number, top: number, right: number, bottom: number): void
```

绘制一个矩形，默认使用黑色填充。性能优于[drawRect](#drawrect)接口，推荐使用本接口。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| left | number | 是 |
| top | number | 是 |
| right | number | 是 |
| bottom | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawRegion

```TypeScript
drawRegion(region: Region): void
```

绘制一个区域，默认使用黑色填充内容。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](../../apis-image-kit/arkts-apis/arkts-image-image-region-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawRoundRect

```TypeScript
drawRoundRect(roundRect: RoundRect): void
```

绘制一个圆角矩形，默认使用黑色填充内容。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [roundRect](../../apis-arkui/arkts-apis/arkts-arkui-canvaspath-c.md) | [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawShadow

```TypeScript
drawShadow(path: Path, planeParams: common2D.Point3d, devLightPos: common2D.Point3d, lightRadius: number,
      ambientColor: common2D.Color, spotColor: common2D.Color, flag: ShadowFlag) : void
```

绘制射灯类型阴影，使用路径描述环境光阴影的轮廓。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |
| planeParams | common2D.Point3d | 是 |
| devLightPos | common2D.Point3d | 是 |
| lightRadius | number | 是 |
| ambientColor | common2D.Color | 是 |
| spotColor | common2D.Color | 是 |
| flag | [ShadowFlag](arkts-arkgraphics2d-drawing-shadowflag-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawShadow

```TypeScript
drawShadow(path: Path, planeParams: common2D.Point3d, devLightPos: common2D.Point3d, lightRadius: number,
      ambientColor: common2D.Color | number, spotColor: common2D.Color | number, flag: ShadowFlag) : void
```

绘制射灯类型阴影，使用路径描述环境光阴影的轮廓。

**起始版本：** 18

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |
| planeParams | common2D.Point3d | 是 |
| devLightPos | common2D.Point3d | 是 |
| lightRadius | number | 是 |
| ambientColor | common2D.Color \| number | 是 |
| spotColor | common2D.Color \| number | 是 |
| flag | [ShadowFlag](arkts-arkgraphics2d-drawing-shadowflag-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawSingleCharacter

```TypeScript
drawSingleCharacter(text: string, font: Font, x: number, y: number): void
```

绘制单个字符。当前字体不支持待绘制字符时，退化到使用系统字体绘制字符。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| font | [Font](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-font-c.md) | 是 |
| x | number | 是 |
| y | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawSingleCharacterWithFeatures

```TypeScript
drawSingleCharacterWithFeatures(text: string, font: Font, x: number, y: number, features: Array<FontFeature>): void
```

绘制单个字符，字符带有字体特征。当前字体不支持待绘制字符时，退化到使用系统字体绘制字符。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| font | [Font](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-font-c.md) | 是 |
| x | number | 是 |
| y | number | 是 |
| features | Array & lt;FontFeature & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |

## drawTextBlob

```TypeScript
drawTextBlob(blob: TextBlob, x: number, y: number): void
```

绘制一段文字。若构造blob的字体不支持待绘制字符，则该部分字符无法绘制。

**起始版本：** 11

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| blob | [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) | 是 |
| x | number | 是 |
| y | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## drawVertices

```TypeScript
drawVertices(vertexMode: VertexMode, vertexCount: number, positions: Array<common2D.Point>,
      texs: Array<common2D.Point> | null, colors: Array<number> | null, indexCount: number,
      indices: Array<number> | null, mode: BlendMode): void
```

绘制顶点数组描述的三角网格。

**起始版本：** 23

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| vertexMode | [VertexMode](arkts-arkgraphics2d-drawing-vertexmode-e.md) | 是 |
| vertexCount | number | 是 |
| positions | Array & lt;common2D.Point & gt; | 是 |
| texs | Array & lt;common2D.Point & gt; \ | null | 是 |
| colors | Array & lt;number & gt; \ | null | 是 |
| indexCount | number | 是 |
| [indices](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-customgeometry-c.md) | Array & lt;number & gt; \ | null | 是 |
| mode | [BlendMode](../../apis-arkui/arkts-components/arkts-arkui-blendmode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |

## getHeight

```TypeScript
getHeight(): number
```

获取画布的高度。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getLocalClipBounds

```TypeScript
getLocalClipBounds(): common2D.Rect
```

获取画布裁剪区域的边界。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Rect |

## getSaveCount

```TypeScript
getSaveCount(): number
```

获取栈中保存的画布状态（画布矩阵和裁剪区域）的数量。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getTotalMatrix

```TypeScript
getTotalMatrix(): Matrix
```

获取画布矩阵。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) |

## getWidth

```TypeScript
getWidth(): number
```

获取画布的宽度。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## isClipEmpty

```TypeScript
isClipEmpty(): boolean
```

判断画布的裁剪区域是否为空。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## isOpaque

```TypeScript
isOpaque(): boolean
```

检查当前Canvas绘制目标的图层是否不透明。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## quickRejectPath

```TypeScript
quickRejectPath(path: Path): boolean
```

判断路径与画布区域是否不相交。画布区域包含边界。

**起始版本：** 18

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## quickRejectRect

```TypeScript
quickRejectRect(rect: common2D.Rect): boolean
```

判断矩形和画布区域是否不相交。画布区域包含边界。

**起始版本：** 18

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## resetClip

```TypeScript
resetClip(): void
```

将当前画布的裁剪状态重置为初始状态。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

## resetMatrix

```TypeScript
resetMatrix(): void
```

将当前画布的矩阵重置为单位矩阵。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

## restore

```TypeScript
restore(): void
```

恢复保存在栈顶的画布状态（画布矩阵和裁剪区域）。需要与保存接口[save](#save)或[saveLayer](#savelayer)配合使用。 若栈顶状态由saveLayer保存，恢复时还会将saveLayer分配的位图绘制到画布上；若栈为空（无已保存状态），则不执行恢复操作。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

## restoreToCount

```TypeScript
restoreToCount(count: number): void
```

恢复到指定深度的画布状态（画布矩阵和裁剪区域）。需要先调用[save](#save)或[saveLayer](#savelayer)保存画布状态后 才能使用本接口恢复。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| count | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## rotate

```TypeScript
rotate(degrees: number, sx: number, sy: number) : void
```

在当前画布矩阵（默认是单位矩阵）的基础上再叠加一个旋转矩阵，后续绘制操作和裁剪操作的形状和位置都会自动叠加一个旋转效果。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| degrees | number | 是 |
| sx | number | 是 |
| sy | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## save

```TypeScript
save(): number
```

保存当前画布状态（画布矩阵和裁剪区域）到栈顶。需要与恢复接口[restore](#restore)配合使用。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## saveLayer

```TypeScript
saveLayer(rect?: common2D.Rect | null, brush?: Brush | null): number
```

保存当前画布的矩阵和裁剪区域，并为后续绘制分配位图。需要与恢复接口[restore](#restore)配合使用，调用restore将会舍弃对矩阵和裁剪区域做的更改，并绘制位图。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect \| null | 否 |
| brush | [Brush](arkts-arkgraphics2d-drawing-brush-c.md) \| null | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## scale

```TypeScript
scale(sx: number, sy: number): void
```

在当前画布矩阵（默认是单位矩阵）的基础上再叠加一个缩放矩阵，后续绘制操作和裁剪操作的形状和位置都会自动叠加一个缩放效果。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sx | number | 是 |
| sy | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setMatrix

```TypeScript
setMatrix(matrix: Matrix): void
```

设置画布的矩阵，后续绘制操作和裁剪操作的形状和位置都会受到该矩阵的影响。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## skew

```TypeScript
skew(sx: number, sy: number) : void
```

在当前画布矩阵（默认是单位矩阵）的基础上再叠加一个倾斜矩阵，后续绘制操作和裁剪操作的形状和位置都会自动叠加一个倾斜效果。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sx | number | 是 |
| sy | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## translate

```TypeScript
translate(dx: number, dy: number): void
```

在当前画布矩阵（默认是单位矩阵）的基础上再叠加一个平移矩阵，后续绘制操作和裁剪操作的形状和位置都会自动叠加一个平移效果。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dx](../../apis-arkui/arkts-apis/arkts-arkui-actionsheetoffset-i.md) | number | 是 |
| [dy](../../apis-arkui/arkts-apis/arkts-arkui-actionsheetoffset-i.md) | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
