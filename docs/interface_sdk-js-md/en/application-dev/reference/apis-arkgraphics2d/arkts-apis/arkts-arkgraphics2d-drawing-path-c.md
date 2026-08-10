# Path

Path是Drawing模块提供的复合几何路径类，由直线、圆弧、圆锥曲线、二阶贝塞尔、三阶贝塞尔等基本图元组成，支持路径的构造、变换、布尔运算、SVG路径解析与转换、测量与片段截取等能力。未设置填充类型时，默认填充类型为WINDING，可通过[setFillType](arkts-arkgraphics2d-drawing-path-c.md#setfilltype)修改。

> **说明：**
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-drawing-class Path--><!--Device-drawing-class Path-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## addArc

ArkTS-Dyn:
```TypeScript
addArc(rect: common2D.Rect, startAngle: number, sweepAngle: number): void
```

ArkTS-Sta:
```TypeScript
addArc(rect: common2D.Rect, startAngle: double, sweepAngle: double): void
```

向路径添加一段圆弧。与[arcTo](arkts-arkgraphics2d-drawing-path-c.md#arcto)相比，addArc不会自动添加从路径最后点到弧线起点的连接线段，且通过common2D.Rect对象指定矩形边界。若需要自动连接弧线起点，请使用arcTo；若仅需添加独立弧线，可使用addArc。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Path-addArc(rect: common2D.Rect, startAngle: double, sweepAngle: double): void--><!--Device-Path-addArc(rect: common2D.Rect, startAngle: double, sweepAngle: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | 包含弧的椭圆的矩形边界。 |
| startAngle | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 弧的起始角度，单位为度，0°为x轴正方向，该参数为浮点数。当对90取余接近于0且sweepAngle不在(-360, 360)区间内时，将添加整个椭圆而非圆弧。 |
| sweepAngle | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 扫描角度，单位为度。正数表示顺时针方向，负数表示逆时针方向。当参数不在(-360, 360)区间内且startAngle对90取余接近于0时，将添加整个椭圆而非圆 弧；其余情况下实际扫描角度为该入参对360取余的结果。该参数为浮点数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## addCircle

ArkTS-Dyn:
```TypeScript
addCircle(x: number, y: number, radius: number, pathDirection?: PathDirection): void
```

ArkTS-Sta:
```TypeScript
addCircle(x: double, y: double, radius: double, pathDirection?: PathDirection): void
```

按指定方向，向路径添加圆形，圆的起点位于(x + radius, y)。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Path-addCircle(x: double, y: double, radius: double, pathDirection?: PathDirection): void--><!--Device-Path-addCircle(x: double, y: double, radius: double, pathDirection?: PathDirection): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 表示圆心的x轴坐标，该参数为浮点数。单位为物理像素px。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 表示圆心的y轴坐标，该参数为浮点数。单位为物理像素px。 |
| radius | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 表示圆形的半径，取值范围>0，该参数为浮点数，小于等于0时不会有任何效果。单位为物理像素px。 |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | No | 表示路径方向。不传入时默认为顺时针方向。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## addOval

ArkTS-Dyn:
```TypeScript
addOval(rect: common2D.Rect, start: number, pathDirection?: PathDirection): void
```

ArkTS-Sta:
```TypeScript
addOval(rect: common2D.Rect, start: int, pathDirection?: PathDirection): void
```

按指定方向，将矩形的内切椭圆添加到路径中。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Path-addOval(rect: common2D.Rect, start: int, pathDirection?: PathDirection): void--><!--Device-Path-addOval(rect: common2D.Rect, start: int, pathDirection?: PathDirection): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | 椭圆的矩形边界。 |
| start | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示椭圆初始点的索引，取值范围为不小于0的整数，0、1、2、3分别对应椭圆的上端点、右端点、下端点、左端点，大于等于4时会对4取余。 |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | No | 表示路径方向。不传入时默认为顺时针方向。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## addPath

```TypeScript
addPath(path: Path, matrix?: Matrix | null): void
```

对源路径进行矩阵变换后，将其添加到当前路径中。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Path-addPath(path: Path, matrix?: Matrix | null): void--><!--Device-Path-addPath(path: Path, matrix?: Matrix | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes | 要添加到当前路径的源路径对象，经过矩阵变换后将被追加到当前路径中。 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | No | 表示矩阵对象，用于对源路径进行变换（如旋转、缩放、平移等）。当需要对源路径进行 几何变换后再添加到当前路径时传入此参数；当仅需原样添加源路径时可不传入，不传入时默认为单位矩阵（即不进行任何变换）。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## addPolygon

```TypeScript
addPolygon(points: Array<common2D.Point>, close: boolean): void
```

通过坐标点列表添加多条连续的线段。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Path-addPolygon(points: Array<common2D.Point>, close: boolean): void--><!--Device-Path-addPolygon(points: Array<common2D.Point>, close: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| points | Array&lt;common2D.Point&gt; | Yes | 多边形各顶点的坐标点数组，按数组顺序依次连接各点形成连续线段。 |
| close | boolean | Yes | 表示是否将路径闭合，即是否添加路径起始点到终点的连线。true表示将路径闭合，false表示不将路径闭合。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## addRect

```TypeScript
addRect(rect: common2D.Rect, pathDirection?: PathDirection): void
```

按指定方向，将矩形添加到路径中，添加的路径的起始点为矩形左上角。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Path-addRect(rect: common2D.Rect, pathDirection?: PathDirection): void--><!--Device-Path-addRect(rect: common2D.Rect, pathDirection?: PathDirection): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | 向路径中添加的矩形轮廓，rect参数需为有效的common2D.Rect对象，left需小于right、top需小于bottom。 |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | No | 表示路径方向。不传入时默认为顺时针方向。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## addRoundRect

```TypeScript
addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void
```

按指定方向，向路径添加圆角矩形轮廓。路径添加方向为顺时针时，起始点位于圆角矩形左下方圆角与左边界的交点；路径添加方向为逆时针时，起始点位于圆角矩形左上方圆角与左边界的交点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Path-addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void--><!--Device-Path-addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| roundRect | [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) | Yes | 向路径中添加的圆角矩形对象，需为有效的RoundRect对象。 |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | No | 表示路径方向。不传入时默认为顺时针方向。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## approximate

```TypeScript
approximate(acceptableError: number): Array<number>
```

将当前路径转化为由连续直线段构成的近似路径。

> **说明：**
> 
> - 当acceptableError为0时，曲线路径被极度细分，会严重影响性能和内存消耗，不建议设置误差值为0。
> 
> - 当acceptableError远大于路径尺寸时，路径会极度简化，仅保留路径的起止点等少量关键点，可能会丢失原有形状。
> 
> - 对于椭圆等曲线，当acceptableError过大时，拟合结果通常只包含椭圆的分段贝塞尔曲线的起止点，椭圆形会被极度简化为多边形。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Path-approximate(acceptableError: number): Array<number>--><!--Device-Path-approximate(acceptableError: number): Array<number>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| acceptableError | number | Yes | 表示路径上每条线段的可接受误差，取值范围≥0，该参数为浮点数，小于0时报错。单位为物理像素px。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;number&gt; | 返回包含近似路径的点的数组，至少包含两个点。每个点由三个值组成： &lt;br&gt;1. 该点所在的位置距离路径起点的长度比例值，范围为[0.0, 1.0]。 &lt;br&gt;2. 点的x坐标。 &lt;br&gt;3. 点的y坐标。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 25900001 | Parameter error. Possible causes: Incorrect parameter range. |

## approximate

```TypeScript
approximate(acceptableError: double): Array<double> | undefined
```

将当前路径转化为由连续直线段构成的近似路径。

> **说明：**
> 
> - 当acceptableError为0时，曲线路径被极度细分，会严重影响性能和内存消耗，不建议设置误差值为0。
> 
> - 当acceptableError远大于路径尺寸时，路径会极度简化，仅保留路径的起止点等少量关键点，可能会丢失原有形状。
> 
> - 对于椭圆等曲线，当acceptableError过大时，拟合结果通常只包含椭圆的分段贝塞尔曲线的起止点，椭圆形会被极度简化为多边形。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-Path-approximate(acceptableError: double): Array<double> | undefined--><!--Device-Path-approximate(acceptableError: double): Array<double> | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| acceptableError | double | Yes | 表示路径上每条线段的可接受误差，取值范围≥0，该参数为浮点数，小于0时报错。单位为物理像素px。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;double&gt; | 返回包含近似路径的点的数组，至少包含两个点。每个点由三个值组成： &lt;br&gt;1. 该点所在的位置距离路径起点的长度比例值，范围为[0.0, 1.0]。 &lt;br&gt;2. 点的x坐标。 &lt;br&gt;3. 点的y坐标。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 25900001 | Parameter error. Possible causes: Incorrect parameter range. |

## arcTo

ArkTS-Dyn:
```TypeScript
arcTo(x1: number, y1: number, x2: number, y2: number, startDeg: number, sweepDeg: number): void
```

ArkTS-Sta:
```TypeScript
arcTo(x1: double, y1: double, x2: double, y2: double, startDeg: double, sweepDeg: double): void
```

给路径添加一段弧线。绘制弧线的方式为角度弧：首先指定一个矩形边界，取其内切椭圆；然后指定起始角度和扫描度数；最后从起始角度扫描截取椭圆周长的一部分，即为绘制的弧线。另外会默认添加一条从路径最后点位置（若路径没有内容则默认值为 (0, 0)）到弧线起始点位置的线段。若不需要自动添加连接线段，请使用[addArc](arkts-arkgraphics2d-drawing-path-c.md#addarc)。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-arcTo(x1: double, y1: double, x2: double, y2: double, startDeg: double, sweepDeg: double): void--><!--Device-Path-arcTo(x1: double, y1: double, x2: double, y2: double, startDeg: double, sweepDeg: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x1 | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 矩形左上角的x坐标，该参数为浮点数。单位为物理像素px。 |
| y1 | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 矩形左上角的y坐标，该参数为浮点数。单位为物理像素px。 |
| x2 | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 矩形右下角的x坐标，该参数为浮点数。单位为物理像素px。 |
| y2 | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 矩形右下角的y坐标，该参数为浮点数。单位为物理像素px。 |
| startDeg | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 起始的角度。角度的起始方向（0°）为x轴正方向。单位为度。 |
| sweepDeg | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 扫描的度数，为正数时顺时针扫描，为负数时逆时针扫描。实际扫描的度数为该入参对360取模的结果。 单位为度。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## buildFromSvgString

```TypeScript
buildFromSvgString(str: string): boolean
```

解析SVG字符串表示的路径。支持标准SVG路径数据命令（如M、L、C、Q、A、Z及其相对坐标形式等），解析失败时返回false。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Path-buildFromSvgString(str: string): boolean--><!--Device-Path-buildFromSvgString(str: string): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| str | string | Yes | SVG路径数据格式的字符串，用于描述绘制路径。支持M/m、L/l、H/h、V/v、C/c、S/s、Q/q、T/t、A/a、Z/z 等SVG路径命令，具体语法请参考SVG路径数据规范。传入不符合SVG路径格式的字符串时，解析失败，接口返回false。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回是否成功解析SVG字符串的结果。true表示解析成功，false表示解析失败。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

## close

```TypeScript
close(): void
```

闭合路径，会添加一条从路径最后点位置到起始点位置的线段。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Path-close(): void--><!--Device-Path-close(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## conicTo

ArkTS-Dyn:
```TypeScript
conicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void
```

ArkTS-Sta:
```TypeScript
conicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void
```

在当前路径上添加一条路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的圆锥曲线，其控制点为 (ctrlX, ctrlY)，目标点为 (endX, endY)。与[quadTo](arkts-arkgraphics2d-drawing-path-c.md#quadto)相比，conicTo通过权重参数可更灵活地控制曲线形状：权重为1时效果与quadTo相同，权重不为1时可精确表示圆弧、椭圆弧等圆锥曲线段。仅需标准二次贝塞尔曲线时推荐使用quadTo，需要精确表示圆弧或灵活控制曲线形状时推荐使用conicTo。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-conicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void--><!--Device-Path-conicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctrlX | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 控制点的x坐标，该参数为浮点数。单位为物理像素px。 |
| ctrlY | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 控制点的y坐标，该参数为浮点数。单位为物理像素px。 |
| endX | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标点的x坐标，该参数为浮点数。单位为物理像素px。 |
| endY | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标点的y坐标，该参数为浮点数。单位为物理像素px。 |
| weight | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 表示曲线权重，决定了曲线的形状。值越大，曲线越接近控制点。 小于等于0时，效果与[lineTo](arkts-arkgraphics2d-drawing-path-c.md#lineto)相同； 值为1时，效果与[quadTo](arkts-arkgraphics2d-drawing-path-c.md#quadto)相同。该参数为浮点数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## constructor

```TypeScript
constructor()
```

构造一个路径。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-constructor()--><!--Device-Path-constructor()-End-->

**System capability:** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(path: Path)
```

构造一个已有路径的副本。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-constructor(path: Path)--><!--Device-Path-constructor(path: Path)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes | 待复制的路径对象。 |

## contains

ArkTS-Dyn:
```TypeScript
contains(x: number, y: number): boolean
```

ArkTS-Sta:
```TypeScript
contains(x: double, y: double): boolean
```

判断指定坐标点是否被路径包含，判定规则参考[PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md)。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Path-contains(x: double, y: double): boolean--><!--Device-Path-contains(x: double, y: double): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | x轴上坐标点，该参数为浮点数。单位为物理像素px。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | y轴上坐标点，该参数为浮点数。单位为物理像素px。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回指定坐标点是否在路径内。true表示点在路径内，false表示点不在路径内。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## convertToSvgString

```TypeScript
convertToSvgString(): string
```

将路径转换为SVG字符串。输出的字符串遵循SVG路径数据规范映射。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path-convertToSvgString(): string--><!--Device-Path-convertToSvgString(): string-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| string | 转换后的SVG字符串，以SVG路径格式描述当前路径的几何形状。 |

## cubicTo

ArkTS-Dyn:
```TypeScript
cubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void
```

ArkTS-Sta:
```TypeScript
cubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void
```

添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的三阶贝塞尔曲线。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-cubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void--><!--Device-Path-cubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctrlX1 | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 第一个控制点的x坐标，该参数为浮点数。单位为物理像素px。 |
| ctrlY1 | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 第一个控制点的y坐标，该参数为浮点数。单位为物理像素px。 |
| ctrlX2 | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 第二个控制点的x坐标，该参数为浮点数。单位为物理像素px。 |
| ctrlY2 | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 第二个控制点的y坐标，该参数为浮点数。单位为物理像素px。 |
| endX | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标点的x坐标，该参数为浮点数。单位为物理像素px。 |
| endY | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标点的y坐标，该参数为浮点数。单位为物理像素px。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## getBounds

```TypeScript
getBounds(): common2D.Rect
```

获取包含路径的最小矩形边界。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-Path-getBounds(): common2D.Rect--><!--Device-Path-getBounds(): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Rect | 包含路径的最小矩形区域。 |

## getBounds

```TypeScript
getBounds(): common2D.Rect | undefined
```

获取包含路径的最小矩形边界。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Path-getBounds(): common2D.Rect | undefined--><!--Device-Path-getBounds(): common2D.Rect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Rect | 包含路径的最小矩形区域。创建失败时返回undefined。 |

## getConicWeightData

ArkTS-Dyn:
```TypeScript
getConicWeightData(): Array<number>
```

ArkTS-Sta:
```TypeScript
getConicWeightData(): Array<double>
```

获取路径的圆锥曲线权重数据。

在路径（path）图元中，圆锥曲线数据采用有理贝塞尔曲线（Rational Bézier Curve）形式表示，其中每个控制点附带一个权重值（weight）。权重属于曲线定义的几何参数。

主要作用如下：

形状调控：权重值越大，曲线越靠近对应控制点；权重为1时退化为标准贝塞尔曲线；权重为0时该控制点不起作用。

精确表示圆锥曲线：通过组合权重与二次贝塞尔曲线，可以精确表示圆弧、椭圆弧、抛物线等圆锥曲线段，无需使用分段逼近或专用椭圆弧指令。

数据组织：权重通常以数组形式与点数据并列，按顺序对应每个控制点，与相应的指令verb（如[conicTo](arkts-arkgraphics2d-drawing-path-c.md#conicto)）配合使用。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path-getConicWeightData(): Array<double>--><!--Device-Path-getConicWeightData(): Array<double>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt; | 类型为浮点数，取值范围≥0。取值为0.0时，该控制点完全无效，曲线不经过此点，曲线实际由其余控制点定义。取值为1.0时，该控制点对应的曲线变为标准贝塞尔曲线，此时权重不产生 额外形变效果。取值大于1时，权重值越大，曲线越靠近该控制点；小于1.0但大于0.0时，曲线则相对远离该控制点。 |

## getFillType

```TypeScript
getFillType(): PathFillType
```

获取路径的填充类型。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Path-getFillType(): PathFillType--><!--Device-Path-getFillType(): PathFillType-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md) | 路径的填充类型，决定路径内部区域的定义方式。 |

## getFillType

```TypeScript
getFillType(): PathFillType | undefined
```

获取路径的填充类型。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-Path-getFillType(): PathFillType | undefined--><!--Device-Path-getFillType(): PathFillType | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md) | 路径的填充类型，决定路径内部区域的定义方式。 |

## getLastPoint

```TypeScript
getLastPoint(): common2D.Point
```

获取路径最后点位置的坐标。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path-getLastPoint(): common2D.Point--><!--Device-Path-getLastPoint(): common2D.Point-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Point | 路径最后点位置坐标。如果路径为空，则返回undefined。 |

## getLastPoint

```TypeScript
getLastPoint(): common2D.Point | undefined
```

获取路径最后点位置的坐标。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path-getLastPoint(): common2D.Point | undefined--><!--Device-Path-getLastPoint(): common2D.Point | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Point | 路径最后点位置坐标。如果路径为空，则返回undefined。 |

## getLength

ArkTS-Dyn:
```TypeScript
getLength(forceClosed: boolean): number
```

ArkTS-Sta:
```TypeScript
getLength(forceClosed: boolean): double
```

获取路径长度。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Path-getLength(forceClosed: boolean): double--><!--Device-Path-getLength(forceClosed: boolean): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| forceClosed | boolean | Yes | 表示是否按照闭合路径测量，true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 路径长度。单位为物理像素px。 |

## getMatrix

ArkTS-Dyn:
```TypeScript
getMatrix(forceClosed: boolean, distance: number, matrix: Matrix, flags: PathMeasureMatrixFlags): boolean
```

ArkTS-Sta:
```TypeScript
getMatrix(forceClosed: boolean, distance: double, matrix: Matrix, flags: PathMeasureMatrixFlags): boolean
```

在路径上距离起始点distance处，获取一个变换矩阵，用于表示该点的坐标和朝向。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Path-getMatrix(forceClosed: boolean, distance: double, matrix: Matrix, flags: PathMeasureMatrixFlags): boolean--><!--Device-Path-getMatrix(forceClosed: boolean, distance: double, matrix: Matrix, flags: PathMeasureMatrixFlags): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| forceClosed | boolean | Yes | 表示是否按照闭合路径测量，true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。 |
| distance | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 表示与路径起始点的距离，小于0时会被视作0，大于路径长度时会被视作路径长度。该参数为浮点数。 单位为物理像素px。 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes | 用于存储获取到的变换矩阵的矩阵对象，该矩阵表示路径上指定距离处的坐标位置和朝向信息。 |
| flags | [PathMeasureMatrixFlags](arkts-arkgraphics2d-drawing-pathmeasurematrixflags-e.md) | Yes | 矩阵信息维度枚举，用于指定获取的矩阵包含哪些维度信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回是否成功获取变换矩阵的结果。true表示成功，false表示失败。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

## getPathIterator

```TypeScript
getPathIterator(): PathIterator
```

返回该路径的操作迭代器。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-Path-getPathIterator(): PathIterator--><!--Device-Path-getPathIterator(): PathIterator-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [PathIterator](arkts-arkgraphics2d-drawing-pathiterator-c.md) | 路径的迭代器对象，用于遍历路径中的绘图指令和点数据，可通过迭代器逐条获取路径的verb指令及对应的坐标点。 |

## getPathIterator

```TypeScript
getPathIterator(): PathIterator | undefined
```

返回该路径的操作迭代器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Path-getPathIterator(): PathIterator | undefined--><!--Device-Path-getPathIterator(): PathIterator | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [PathIterator](arkts-arkgraphics2d-drawing-pathiterator-c.md) | 路径的迭代器对象，用于遍历路径中的绘图指令和点数据，可通过迭代器逐条获取路径的verb指令及对应的坐标点。创建失败时返回undefined。 |

## getPointData

```TypeScript
getPointData(): Array<common2D.Point>
```

获取路径的点数据。

在路径（path）图元中，点数据以数值序列的形式存在，与verb指令一一对应，用来精确指定绘图操作的几何坐标位置。

点数据的主要类型包括：

终点坐标：与[moveTo](arkts-arkgraphics2d-drawing-path-c.md#moveto)、[lineTo](arkts-arkgraphics2d-drawing-path-c.md#lineto)等指令配合，定义线段或移动的目标位置。

控制点坐标：与曲线指令配合，用于定义贝塞尔曲线的形状（如三次曲线需要两个控制点和一个终点）。

闭合点：通常不单独提供坐标，由[close](arkts-arkgraphics2d-drawing-path-c.md#close)指令隐式使用路径起点。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path-getPointData(): Array<common2D.Point>--><!--Device-Path-getPointData(): Array<common2D.Point>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;common2D.Point&gt; | 返回路径的点数据数组，每个元素为common2D.Point对象，其x、y坐标为浮点数。 理论取值范围为全体实数，但实际受限于渲染坐标系的有效范围（如-2^31到2^31-1或屏幕可见区域）；超出范围可能导致图形不可见或裁剪。 |

## getPositionAndTangent

ArkTS-Dyn:
```TypeScript
getPositionAndTangent(forceClosed: boolean, distance: number, position: common2D.Point, tangent: common2D.Point): boolean
```

ArkTS-Sta:
```TypeScript
getPositionAndTangent(forceClosed: boolean, distance: double, position: common2D.Point, tangent: common2D.Point): boolean
```

获取路径起始点指定距离处的坐标点和切线值。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Path-getPositionAndTangent(forceClosed: boolean, distance: double, position: common2D.Point, tangent: common2D.Point): boolean--><!--Device-Path-getPositionAndTangent(forceClosed: boolean, distance: double, position: common2D.Point, tangent: common2D.Point): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| forceClosed | boolean | Yes | 表示是否按照闭合路径测量，true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。 |
| distance | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 表示与路径起始点的距离，小于0时会被视作0，大于路径长度时会被视作路径长度。 该参数为浮点数。单位为物理像素px。 |
| position | common2D.Point | Yes | 存储获取到的距离路径起始点distance处的点的坐标。 |
| tangent | common2D.Point | Yes | 存储获取到的距离路径起始点distance处的点的切线值，tangent.x表示该点切线的余弦值，tangent.y表示该点切线的正弦值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 表示是否成功获取距离路径起始点distance处的点的坐标和切线值的结果。 true表示获取成功，false表示获取失败，position和tangent不会被改变。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## getSegment

ArkTS-Dyn:
```TypeScript
getSegment(forceClosed: boolean, start: number, stop: number, startWithMoveTo: boolean, dst: Path): boolean
```

ArkTS-Sta:
```TypeScript
getSegment(forceClosed: boolean, start: double, stop: double, startWithMoveTo: boolean, dst: Path): boolean
```

截取路径的片段并追加到目标路径上。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-Path-getSegment(forceClosed: boolean, start: double, stop: double, startWithMoveTo: boolean, dst: Path): boolean--><!--Device-Path-getSegment(forceClosed: boolean, start: double, stop: double, startWithMoveTo: boolean, dst: Path): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| forceClosed | boolean | Yes | 表示是否按照闭合路径测量，true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。 |
| start | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 表示与路径起始点的距离，距离路径起始点start距离的位置即为截取路径片段的起始点， 小于0时会被视作0，大于等于stop时会截取失败。该参数为浮点数。单位为物理像素px。 |
| stop | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 表示与路径起始点的距离，距离路径起始点stop距离的位置即为截取路径片段的终点， 小于等于start时会截取失败，大于路径长度时会被视作路径长度。该参数为浮点数。单位为物理像素px。 |
| startWithMoveTo | boolean | Yes | 表示是否在目标路径执行[moveTo](arkts-arkgraphics2d-drawing-path-c.md#moveto) 移动到截取路径片段的起始点位置。true表示执行moveTo；false表示不执行moveTo。 |
| dst | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes | 目标路径，截取成功时会将得到的路径片段追加到目标路径上，截取失败时不做改变。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 表示是否成功截取路径片段。true表示截取成功，false表示截取失败。 |

## getVerbData

```TypeScript
getVerbData(): Array<PathIteratorVerb>
```

获取路径的指令数据。

在路径（path）图元中，指令数据verb用于描述路径构造过程中的基本绘图动作。

指令数据以枚举的形式存在，每个取值对应一种几何操作类型，例如：

[moveTo](arkts-arkgraphics2d-drawing-path-c.md#moveto)：将当前绘图点移至指定坐标，不产生线段。

[lineTo](arkts-arkgraphics2d-drawing-path-c.md#lineto)：从当前点向指定点绘制直线段。

[close](arkts-arkgraphics2d-drawing-path-c.md#close)：将当前点与路径起点相连，形成封闭区域。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path-getVerbData(): Array<PathIteratorVerb>--><!--Device-Path-getVerbData(): Array<PathIteratorVerb>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;PathIteratorVerb&gt; | 返回路径的指令数据数组，每个数组元素对应为路径中的基本绘图动作类型，与点数据一一对应。 |

## interpolate

ArkTS-Dyn:
```TypeScript
interpolate(other: Path, weight: number, interpolatedPath: Path): boolean
```

ArkTS-Sta:
```TypeScript
interpolate(other: Path, weight: double, interpolatedPath: Path): boolean
```

根据给定的权重，在当前路径和另一条路径之间进行插值，并将结果存储在目标路径对象中。两条路径点数相同即可插值成功，目标路径按照当前路径的指令结构进行创建。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-Path-interpolate(other: Path, weight: double, interpolatedPath: Path): boolean--><!--Device-Path-interpolate(other: Path, weight: double, interpolatedPath: Path): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes | 表示另一条路径对象。 |
| weight | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 表示插值权重，取值范围为[0.0, 1.0]。该参数为浮点数。 |
| interpolatedPath | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes | 表示用于存储插值结果的目标路径对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回插值操作是否成功的结果。true表示插值成功，false表示插值失败。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 25900001 | Parameter error. Possible causes: Incorrect parameter range. |

## isClosed

```TypeScript
isClosed(): boolean
```

获取路径是否闭合。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Path-isClosed(): boolean--><!--Device-Path-isClosed(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 表示当前路径是否闭合，true表示闭合，false表示不闭合。 |

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断路径是否为空。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-Path-isEmpty(): boolean--><!--Device-Path-isEmpty(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 路径是否为空。true表示当前路径为空，false表示路径不为空。 |

## isEqual

```TypeScript
isEqual(path: Path): boolean
```

判断当前路径与另一条路径是否相等。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path-isEqual(path: Path): boolean--><!--Device-Path-isEqual(path: Path): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes | 另一条路径对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回当前路径与另一条路径是否相等的结果。true表示路径相等，false表示路径不相等。 |

## isInterpolate

```TypeScript
isInterpolate(other: Path): boolean
```

判断当前路径与另一条路径在结构和操作顺序上是否完全一致，以确定两条路径是否兼容插值。若路径中包含圆锥曲线（Conic）操作，则对应操作的权重值也必须一致，才能视为兼容插值。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-Path-isInterpolate(other: Path): boolean--><!--Device-Path-isInterpolate(other: Path): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes | 表示另一条路径对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回当前路径与另一条路径是否兼容插值的结果。true表示兼容插值，false表示不兼容插值。 |

## isInverseFillType

```TypeScript
isInverseFillType(): boolean
```

检查当前路径填充类型是否是反向填充类型。例如填充类型WINDING、EVEN_ODD不是反向类型，INVERSE_WINDING、INVERSE_EVEN_ODD是反向类型。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Path-isInverseFillType(): boolean--><!--Device-Path-isInverseFillType(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 检查当前路径填充类型是否是反向填充类型。true表示是反向填充类型，false表示不是反向填充类型。 |

## isRect

```TypeScript
isRect(rect: common2D.Rect | null): boolean
```

判断路径是否构成矩形。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Path-isRect(rect: common2D.Rect | null): boolean--><!--Device-Path-isRect(rect: common2D.Rect | null): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect \| null | Yes | 矩形对象，作为出参使用，路径构成矩形时，会被改写为路径表示的矩形，否则不会改变。可以为null，表示无需获取路径表示的矩形。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回路径是否构成矩形。true表示路径构成矩形，false表示路径不构成矩形。 |

## lineTo

ArkTS-Dyn:
```TypeScript
lineTo(x: number, y: number): void
```

ArkTS-Sta:
```TypeScript
lineTo(x: double, y: double): void
```

添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的线段。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-lineTo(x: double, y: double): void--><!--Device-Path-lineTo(x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标点的x轴坐标，该参数为浮点数。单位为物理像素px。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标点的y轴坐标，该参数为浮点数。单位为物理像素px。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## moveTo

ArkTS-Dyn:
```TypeScript
moveTo(x: number, y: number): void
```

ArkTS-Sta:
```TypeScript
moveTo(x: double, y: double): void
```

设置自定义路径的起始点位置。与[rMoveTo](arkts-arkgraphics2d-drawing-path-c.md#rmoveto)使用相对坐标不同，moveTo使用绝对坐标设置起始点。当路径起点固定时，推荐使用moveTo；当路径需要基于当前位置动态构建时，推荐使用[rMoveTo](arkts-arkgraphics2d-drawing-path-c.md#rmoveto)。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-moveTo(x: double, y: double): void--><!--Device-Path-moveTo(x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 起始点的x轴坐标，该参数为浮点数。单位为物理像素px。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 起始点的y轴坐标，该参数为浮点数。单位为物理像素px。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## offset

```TypeScript
offset(dx: number, dy: number): Path
```

将路径沿x轴方向偏移dx距离、沿y轴方向偏移dy距离，并保存在返回的路径对象中。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-Path-offset(dx: number, dy: number): Path--><!--Device-Path-offset(dx: number, dy: number): Path-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | number | Yes | x轴方向偏移量，正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。单位为物理像素px。 |
| dy | number | Yes | y轴方向偏移量，正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。单位为物理像素px。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) | 返回当前路径偏移(dx,dy)后生成的新路径对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## offset

```TypeScript
offset(dx: double, dy: double): Path | undefined
```

Offsets this path by specified distances along the X axis and Y axis and stores the resulting path in the Path object returned.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Path-offset(dx: double, dy: double): Path | undefined--><!--Device-Path-offset(dx: double, dy: double): Path | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | double | Yes | X offset. A positive number indicates an offset towards the positive direction of the X axis, and a negative number indicates an offset towards the negative direction of the X axis. The value is a floating point number. |
| dy | double | Yes | Y offset. A positive number indicates an offset towards the positive direction of the Y axis, and a negative number indicates an offset towards the negative direction of the Y axis. The value is a floating point number. |

**Return value:**

| Type | Description |
| --- | --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) | New path generated. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## op

```TypeScript
op(path: Path, pathOp: PathOp): boolean
```

将当前路径与path按照指定的路径操作类型进行合并，并将合并结果保存在当前路径中。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Path-op(path: Path, pathOp: PathOp): boolean--><!--Device-Path-op(path: Path, pathOp: PathOp): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes | 路径对象，用于与当前路径合并。 |
| pathOp | [PathOp](arkts-arkgraphics2d-drawing-pathop-e.md) | Yes | 路径操作类型枚举，用于指定两条路径的布尔运算方式。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回路径合并是否成功的结果。true表示合并成功，false表示合并失败。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## quadTo

ArkTS-Dyn:
```TypeScript
quadTo(ctrlX: number, ctrlY: number, endX: number, endY: number): void
```

ArkTS-Sta:
```TypeScript
quadTo(ctrlX: double, ctrlY: double, endX: double, endY: double): void
```

添加从路径最后点位置（若路径没有内容则默认值为 (0, 0)）到目标点位置的二阶贝塞尔曲线。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-quadTo(ctrlX: double, ctrlY: double, endX: double, endY: double): void--><!--Device-Path-quadTo(ctrlX: double, ctrlY: double, endX: double, endY: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctrlX | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 控制点的x坐标，该参数为浮点数。单位为物理像素px。 |
| ctrlY | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 控制点的y坐标，该参数为浮点数。单位为物理像素px。 |
| endX | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标点的x坐标，该参数为浮点数。单位为物理像素px。 |
| endY | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标点的y坐标，该参数为浮点数。单位为物理像素px。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## rConicTo

ArkTS-Dyn:
```TypeScript
rConicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void
```

ArkTS-Sta:
```TypeScript
rConicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void
```

使用相对位置添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的圆锥曲线。与[conicTo](arkts-arkgraphics2d-drawing-path-c.md#conicto)使用绝对坐标不同，rConicTo使用相对于当前路径最后点位置的偏移量在当前路径上添加圆锥曲线。当路径需要基于当前位置动态构建时，推荐使用相对坐标方法；当路径目标点固定时，推荐使用绝对坐标方法。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-rConicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void--><!--Device-Path-rConicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctrlX | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 控制点相对于路径最后点位置的x轴偏移量， 正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。单位为物理像素px。 |
| ctrlY | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 控制点相对于路径最后点位置的y轴偏移量， 正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。单位为物理像素px。 |
| endX | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标点相对于路径最后点位置的x轴偏移量， 正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。单位为物理像素px。 |
| endY | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标点相对于路径最后点位置的y轴偏移量， 正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。单位为物理像素px。 |
| weight | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 表示曲线权重，决定了曲线的形状，越大越接近控制点。 若小于等于0则等同于使用[rLineTo](arkts-arkgraphics2d-drawing-path-c.md#rlineto)添加一条到结束点的线段， 若为1则等同于[rQuadTo](arkts-arkgraphics2d-drawing-path-c.md#rquadto)，该参数为浮点数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## rCubicTo

ArkTS-Dyn:
```TypeScript
rCubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void
```

ArkTS-Sta:
```TypeScript
rCubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void
```

使用相对位置添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的三阶贝塞尔曲线。与[cubicTo](arkts-arkgraphics2d-drawing-path-c.md#cubicto)使用绝对坐标不同，rCubicTo使用相对于当前路径最后点位置的偏移量在当前路径上添加三阶贝塞尔曲线。当路径需要基于当前位置动态构建时，推荐使用相对坐标方法；当路径目标点固定时，推荐使用绝对坐标方法。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-rCubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void--><!--Device-Path-rCubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctrlX1 | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 第一个控制点相对于路径最后点位置的x轴偏移量， 正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。单位为物理像素px。 |
| ctrlY1 | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 第一个控制点相对于路径最后点位置的y轴偏移量， 正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。单位为物理像素px。 |
| ctrlX2 | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 第二个控制点相对于路径最后点位置的x轴偏移量， 正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。单位为物理像素px。 |
| ctrlY2 | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 第二个控制点相对于路径最后点位置的y轴偏移量， 正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。单位为物理像素px。 |
| endX | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标点相对于路径最后点位置的x轴偏移量， 正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。单位为物理像素px。 |
| endY | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标点相对于路径最后点位置的y轴偏移量， 正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。单位为物理像素px。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## rLineTo

ArkTS-Dyn:
```TypeScript
rLineTo(dx: number, dy: number): void
```

ArkTS-Sta:
```TypeScript
rLineTo(dx: double, dy: double): void
```

使用相对位置添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的线段。与[lineTo](arkts-arkgraphics2d-drawing-path-c.md#lineto)使用绝对坐标不同，rLineTo使用相对于当前路径最后点位置的偏移量来指定目标点。当路径需要基于当前位置动态构建时，推荐使用相对坐标方法；当目标点位置固定时，推荐使用绝对坐标方法。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-rLineTo(dx: double, dy: double): void--><!--Device-Path-rLineTo(dx: double, dy: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标点相对于当前路径最后点位置的x轴偏移量， 正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。单位为物理像素px。 |
| dy | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标点相对于当前路径最后点位置的y轴偏移量， 正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。单位为物理像素px。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## rMoveTo

ArkTS-Dyn:
```TypeScript
rMoveTo(dx: number, dy: number): void
```

ArkTS-Sta:
```TypeScript
rMoveTo(dx: double, dy: double): void
```

设置一个相对于当前路径最后点位置（若路径没有内容则默认为 (0, 0)）的路径起始点位置。与[moveTo](arkts-arkgraphics2d-drawing-path-c.md#moveto)使用绝对坐标不同，rMoveTo使用相对于当前路径最后点位置的偏移量。当路径需要基于当前位置动态构建时，推荐使用相对坐标方法（如rMoveTo、rLineTo等）；当路径起点固定时，推荐使用绝对坐标方法。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-rMoveTo(dx: double, dy: double): void--><!--Device-Path-rMoveTo(dx: double, dy: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 路径新起始点相对于当前路径最后点位置的x轴偏移量， 正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。单位为物理像素px。 |
| dy | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 路径新起始点相对于当前路径最后点位置的y轴偏移量， 正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。单位为物理像素px。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## rQuadTo

ArkTS-Dyn:
```TypeScript
rQuadTo(dx1: number, dy1: number, dx2: number, dy2: number): void
```

ArkTS-Sta:
```TypeScript
rQuadTo(dx1: double, dy1: double, dx2: double, dy2: double): void
```

使用相对位置添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的二阶贝塞尔曲线。与[quadTo](arkts-arkgraphics2d-drawing-path-c.md#quadto)使用绝对坐标不同，rQuadTo使用相对于当前路径最后点位置的偏移量在当前路径上添加二阶贝塞尔曲线。当路径需要基于当前位置动态构建时，推荐使用相对坐标方法；当路径目标点固定时，推荐使用绝对坐标方法。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-rQuadTo(dx1: double, dy1: double, dx2: double, dy2: double): void--><!--Device-Path-rQuadTo(dx1: double, dy1: double, dx2: double, dy2: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx1 | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 控制点相对于路径最后点位置的x轴偏移量，正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。 单位为物理像素px。 |
| dy1 | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 控制点相对于路径最后点位置的y轴偏移量，正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。 单位为物理像素px。 |
| dx2 | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标点相对于路径最后点位置的x轴偏移量，正数往x轴正方向偏移，负数往x轴负方向偏移，该参数为浮点数。 单位为物理像素px。 |
| dy2 | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标点相对于路径最后点位置的y轴偏移量，正数往y轴正方向偏移，负数往y轴负方向偏移，该参数为浮点数。 单位为物理像素px。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## reset

```TypeScript
reset(): void
```

重置自定义路径数据。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Path-reset(): void--><!--Device-Path-reset(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## rewind

```TypeScript
rewind(): void
```

将路径内添加的各类点/线清空，但是保留内存空间。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-Path-rewind(): void--><!--Device-Path-rewind(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## set

```TypeScript
set(src: Path): void
```

使用指定路径替换当前路径的内容，使当前路径与指定路径完全一致。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Path-set(src: Path): void--><!--Device-Path-set(src: Path): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes | 用于替换当前路径内容的源路径对象。 |

## setFillType

```TypeScript
setFillType(pathFillType: PathFillType): void
```

设置路径的填充类型，决定路径内部区域的定义方式。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Path-setFillType(pathFillType: PathFillType): void--><!--Device-Path-setFillType(pathFillType: PathFillType): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathFillType | [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md) | Yes | 表示路径填充类型，决定路径内部区域的定义方式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## setLastPoint

ArkTS-Dyn:
```TypeScript
setLastPoint(x: number, y: number): void
```

ArkTS-Sta:
```TypeScript
setLastPoint(x: double, y: double): void
```

修改路径最后点位置。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-Path-setLastPoint(x: double, y: double): void--><!--Device-Path-setLastPoint(x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 指定点的x轴坐标，该参数为浮点数。 0表示坐标原点，负数表示位于坐标原点左侧，正数表示位于坐标原点右侧。单位为物理像素px。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 指定点的y轴坐标，该参数为浮点数。 0表示坐标原点，负数表示位于坐标原点上侧，正数表示位于坐标原点下侧。单位为物理像素px。 |

## toggleInverseFillType

```TypeScript
toggleInverseFillType(): void
```

切换路径的填充类型为反向类型。例如，使用WINDING填充类型时，经过取反后填充类型为INVERSE_WINDING，而使用EVEN_ODD填充类型时，经过取反后填充类型为INVERSE_EVEN_ODD，反之亦然。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Path-toggleInverseFillType(): void--><!--Device-Path-toggleInverseFillType(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## transform

```TypeScript
transform(matrix: Matrix): void
```

对路径进行矩阵变换。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Path-transform(matrix: Matrix): void--><!--Device-Path-transform(matrix: Matrix): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | Yes | 表示对路径进行矩阵变换所使用的矩阵对象，该矩阵定义了变换的具体参数 （如缩放比例、旋转角度、平移距离等），路径中的所有点将按照该矩阵进行变换。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

