# Path

Path是Drawing模块提供的复合几何路径类，由直线、圆弧、圆锥曲线、二阶贝塞尔、三阶贝塞尔等基本图元组成，支持路径的构造、变换、布尔运算、SVG路径解析与转换、测量与片段截取等能力。未设置填充类型时，默认填充类型为WINDING，可通过[setFillType](arkts-arkgraphics2d-drawing-path-c.md#setfilltype)修改。

> **说明：**
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 11

<!--Device-drawing-class Path--><!--Device-drawing-class Path-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## addArc

```TypeScript
addArc(rect: common2D.Rect, startAngle: number, sweepAngle: number): void
```

向路径添加一段圆弧。与[arcTo](arkts-arkgraphics2d-drawing-path-c.md#arcto)相比，addArc不会自动添加从路径最后点到弧线起点的连接线段，且通过common2D.Rect对象指定矩形边界。若需要自动连接弧线起点，请使用arcTo；若仅需添加独立弧线，可使用addArc。

**起始版本：** 12

<!--Device-Path-addArc(rect: common2D.Rect, startAngle: double, sweepAngle: double): void--><!--Device-Path-addArc(rect: common2D.Rect, startAngle: double, sweepAngle: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| startAngle | number | 是 |
| sweepAngle | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## addCircle

```TypeScript
addCircle(x: number, y: number, radius: number, pathDirection?: PathDirection): void
```

按指定方向，向路径添加圆形，圆的起点位于(x + radius, y)。

**起始版本：** 12

<!--Device-Path-addCircle(x: double, y: double, radius: double, pathDirection?: PathDirection): void--><!--Device-Path-addCircle(x: double, y: double, radius: double, pathDirection?: PathDirection): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| radius | number | 是 |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## addOval

```TypeScript
addOval(rect: common2D.Rect, start: number, pathDirection?: PathDirection): void
```

按指定方向，将矩形的内切椭圆添加到路径中。

**起始版本：** 12

<!--Device-Path-addOval(rect: common2D.Rect, start: int, pathDirection?: PathDirection): void--><!--Device-Path-addOval(rect: common2D.Rect, start: int, pathDirection?: PathDirection): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| start | number | 是 |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## addPath

```TypeScript
addPath(path: Path, matrix?: Matrix | null): void
```

对源路径进行矩阵变换后，将其添加到当前路径中。

**起始版本：** 12

<!--Device-Path-addPath(path: Path, matrix?: Matrix | null): void--><!--Device-Path-addPath(path: Path, matrix?: Matrix | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## addPolygon

```TypeScript
addPolygon(points: Array<common2D.Point>, close: boolean): void
```

通过坐标点列表添加多条连续的线段。

**起始版本：** 12

<!--Device-Path-addPolygon(points: Array<common2D.Point>, close: boolean): void--><!--Device-Path-addPolygon(points: Array<common2D.Point>, close: boolean): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| points | Array&lt;common2D.Point&gt; | 是 |
| [close](#close) | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## addRect

```TypeScript
addRect(rect: common2D.Rect, pathDirection?: PathDirection): void
```

按指定方向，将矩形添加到路径中，添加的路径的起始点为矩形左上角。

**起始版本：** 12

<!--Device-Path-addRect(rect: common2D.Rect, pathDirection?: PathDirection): void--><!--Device-Path-addRect(rect: common2D.Rect, pathDirection?: PathDirection): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## addRoundRect

```TypeScript
addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void
```

按指定方向，向路径添加圆角矩形轮廓。路径添加方向为顺时针时，起始点位于圆角矩形左下方圆角与左边界的交点；路径添加方向为逆时针时，起始点位于圆角矩形左上方圆角与左边界的交点。

**起始版本：** 12

<!--Device-Path-addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void--><!--Device-Path-addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| roundRect | [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) | 是 |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

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

**起始版本：** 20

<!--Device-Path-approximate(acceptableError: number): Array<number>--><!--Device-Path-approximate(acceptableError: number): Array<number>-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| acceptableError | number | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |

## arcTo

```TypeScript
arcTo(x1: number, y1: number, x2: number, y2: number, startDeg: number, sweepDeg: number): void
```

给路径添加一段弧线。绘制弧线的方式为角度弧：首先指定一个矩形边界，取其内切椭圆；然后指定起始角度和扫描度数；最后从起始角度扫描截取椭圆周长的一部分，即为绘制的弧线。另外会默认添加一条从路径最后点位置（若路径没有内容则默认值为 (0, 0)）到弧线起始点位置的线段。若不需要自动添加连接线段，请使用[addArc](arkts-arkgraphics2d-drawing-path-c.md#addarc)。

**起始版本：** 11

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Path-arcTo(x1: double, y1: double, x2: double, y2: double, startDeg: double, sweepDeg: double): void--><!--Device-Path-arcTo(x1: double, y1: double, x2: double, y2: double, startDeg: double, sweepDeg: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x1 | number | 是 |
| y1 | number | 是 |
| x2 | number | 是 |
| y2 | number | 是 |
| startDeg | number | 是 |
| sweepDeg | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## buildFromSvgString

```TypeScript
buildFromSvgString(str: string): boolean
```

解析SVG字符串表示的路径。支持标准SVG路径数据命令（如M、L、C、Q、A、Z及其相对坐标形式等），解析失败时返回false。

**起始版本：** 12

<!--Device-Path-buildFromSvgString(str: string): boolean--><!--Device-Path-buildFromSvgString(str: string): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| str | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## close

```TypeScript
close(): void
```

闭合路径，会添加一条从路径最后点位置到起始点位置的线段。

**起始版本：** 11

<!--Device-Path-close(): void--><!--Device-Path-close(): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## conicTo

```TypeScript
conicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void
```

在当前路径上添加一条路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的圆锥曲线，其控制点为 (ctrlX, ctrlY)，目标点为 (endX, endY)。与[quadTo](arkts-arkgraphics2d-drawing-path-c.md#quadto)相比，conicTo通过权重参数可更灵活地控制曲线形状：权重为1时效果与quadTo相同，权重不为1时可精确表示圆弧、椭圆弧等圆锥曲线段。仅需标准二次贝塞尔曲线时推荐使用quadTo，需要精确表示圆弧或灵活控制曲线形状时推荐使用conicTo。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Path-conicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void--><!--Device-Path-conicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ctrlX | number | 是 |
| ctrlY | number | 是 |
| endX | number | 是 |
| endY | number | 是 |
| weight | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## constructor

```TypeScript
constructor()
```

构造一个路径。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Path-constructor()--><!--Device-Path-constructor()-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(path: Path)
```

构造一个已有路径的副本。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Path-constructor(path: Path)--><!--Device-Path-constructor(path: Path)-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |

## contains

```TypeScript
contains(x: number, y: number): boolean
```

判断指定坐标点是否被路径包含，判定规则参考[PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md)。

**起始版本：** 12

<!--Device-Path-contains(x: double, y: double): boolean--><!--Device-Path-contains(x: double, y: double): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## convertToSvgString

```TypeScript
convertToSvgString(): string
```

将路径转换为SVG字符串。输出的字符串遵循SVG路径数据规范映射。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Path-convertToSvgString(): string--><!--Device-Path-convertToSvgString(): string-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| string |

## cubicTo

```TypeScript
cubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void
```

添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的三阶贝塞尔曲线。

**起始版本：** 11

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Path-cubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void--><!--Device-Path-cubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ctrlX1 | number | 是 |
| ctrlY1 | number | 是 |
| ctrlX2 | number | 是 |
| ctrlY2 | number | 是 |
| endX | number | 是 |
| endY | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## getBounds

```TypeScript
getBounds(): common2D.Rect
```

获取包含路径的最小矩形边界。

**起始版本：** 12

<!--Device-Path-getBounds(): common2D.Rect--><!--Device-Path-getBounds(): common2D.Rect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Rect |

## getConicWeightData

```TypeScript
getConicWeightData(): Array<number>
```

获取路径的圆锥曲线权重数据。

在路径（path）图元中，圆锥曲线数据采用有理贝塞尔曲线（Rational Bézier Curve）形式表示，其中每个控制点附带一个权重值（weight）。权重属于曲线定义的几何参数。

主要作用如下：

形状调控：权重值越大，曲线越靠近对应控制点；权重为1时退化为标准贝塞尔曲线；权重为0时该控制点不起作用。

精确表示圆锥曲线：通过组合权重与二次贝塞尔曲线，可以精确表示圆弧、椭圆弧、抛物线等圆锥曲线段，无需使用分段逼近或专用椭圆弧指令。

数据组织：权重通常以数组形式与点数据并列，按顺序对应每个控制点，与相应的指令verb（如[conicTo](arkts-arkgraphics2d-drawing-path-c.md#conicto)）配合使用。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Path-getConicWeightData(): Array<double>--><!--Device-Path-getConicWeightData(): Array<double>-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array&lt;number&gt; |

## getFillType

```TypeScript
getFillType(): PathFillType
```

获取路径的填充类型。

**起始版本：** 20

<!--Device-Path-getFillType(): PathFillType--><!--Device-Path-getFillType(): PathFillType-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md) |

## getLastPoint

```TypeScript
getLastPoint(): common2D.Point
```

获取路径最后点位置的坐标。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Path-getLastPoint(): common2D.Point--><!--Device-Path-getLastPoint(): common2D.Point-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Point |

## getLength

```TypeScript
getLength(forceClosed: boolean): number
```

获取路径长度。

**起始版本：** 12

<!--Device-Path-getLength(forceClosed: boolean): double--><!--Device-Path-getLength(forceClosed: boolean): double-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| forceClosed | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getMatrix

```TypeScript
getMatrix(forceClosed: boolean, distance: number, matrix: Matrix, flags: PathMeasureMatrixFlags): boolean
```

在路径上距离起始点distance处，获取一个变换矩阵，用于表示该点的坐标和朝向。

**起始版本：** 12

<!--Device-Path-getMatrix(forceClosed: boolean, distance: double, matrix: Matrix, flags: PathMeasureMatrixFlags): boolean--><!--Device-Path-getMatrix(forceClosed: boolean, distance: double, matrix: Matrix, flags: PathMeasureMatrixFlags): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| forceClosed | boolean | 是 |
| distance | number | 是 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |
| flags | [PathMeasureMatrixFlags](arkts-arkgraphics2d-drawing-pathmeasurematrixflags-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## getPathIterator

```TypeScript
getPathIterator(): PathIterator
```

返回该路径的操作迭代器。

**起始版本：** 18

<!--Device-Path-getPathIterator(): PathIterator--><!--Device-Path-getPathIterator(): PathIterator-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [PathIterator](arkts-arkgraphics2d-drawing-pathiterator-c.md) |

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

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Path-getPointData(): Array<common2D.Point>--><!--Device-Path-getPointData(): Array<common2D.Point>-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array&lt;common2D.Point&gt; |

## getPositionAndTangent

```TypeScript
getPositionAndTangent(forceClosed: boolean, distance: number, position: common2D.Point, tangent: common2D.Point): boolean
```

获取路径起始点指定距离处的坐标点和切线值。

**起始版本：** 12

<!--Device-Path-getPositionAndTangent(forceClosed: boolean, distance: double, position: common2D.Point, tangent: common2D.Point): boolean--><!--Device-Path-getPositionAndTangent(forceClosed: boolean, distance: double, position: common2D.Point, tangent: common2D.Point): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| forceClosed | boolean | 是 |
| distance | number | 是 |
| position | common2D.Point | 是 |
| tangent | common2D.Point | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## getSegment

```TypeScript
getSegment(forceClosed: boolean, start: number, stop: number, startWithMoveTo: boolean, dst: Path): boolean
```

截取路径的片段并追加到目标路径上。

**起始版本：** 18

<!--Device-Path-getSegment(forceClosed: boolean, start: double, stop: double, startWithMoveTo: boolean, dst: Path): boolean--><!--Device-Path-getSegment(forceClosed: boolean, start: double, stop: double, startWithMoveTo: boolean, dst: Path): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| forceClosed | boolean | 是 |
| start | number | 是 |
| stop | number | 是 |
| startWithMoveTo | boolean | 是 |
| dst | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

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

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Path-getVerbData(): Array<PathIteratorVerb>--><!--Device-Path-getVerbData(): Array<PathIteratorVerb>-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array&lt;PathIteratorVerb&gt; |

## interpolate

```TypeScript
interpolate(other: Path, weight: number, interpolatedPath: Path): boolean
```

根据给定的权重，在当前路径和另一条路径之间进行插值，并将结果存储在目标路径对象中。两条路径点数相同即可插值成功，目标路径按照当前路径的指令结构进行创建。

**起始版本：** 20

<!--Device-Path-interpolate(other: Path, weight: double, interpolatedPath: Path): boolean--><!--Device-Path-interpolate(other: Path, weight: double, interpolatedPath: Path): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |
| weight | number | 是 |
| interpolatedPath | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |

## isClosed

```TypeScript
isClosed(): boolean
```

获取路径是否闭合。

**起始版本：** 12

<!--Device-Path-isClosed(): boolean--><!--Device-Path-isClosed(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断路径是否为空。

**起始版本：** 20

<!--Device-Path-isEmpty(): boolean--><!--Device-Path-isEmpty(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## isEqual

```TypeScript
isEqual(path: Path): boolean
```

判断当前路径与另一条路径是否相等。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Path-isEqual(path: Path): boolean--><!--Device-Path-isEqual(path: Path): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isInterpolate

```TypeScript
isInterpolate(other: Path): boolean
```

判断当前路径与另一条路径在结构和操作顺序上是否完全一致，以确定两条路径是否兼容插值。若路径中包含圆锥曲线（Conic）操作，则对应操作的权重值也必须一致，才能视为兼容插值。

**起始版本：** 20

<!--Device-Path-isInterpolate(other: Path): boolean--><!--Device-Path-isInterpolate(other: Path): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isInverseFillType

```TypeScript
isInverseFillType(): boolean
```

检查当前路径填充类型是否是反向填充类型。例如填充类型WINDING、EVEN_ODD不是反向类型，INVERSE_WINDING、INVERSE_EVEN_ODD是反向类型。

**起始版本：** 23

<!--Device-Path-isInverseFillType(): boolean--><!--Device-Path-isInverseFillType(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## isRect

```TypeScript
isRect(rect: common2D.Rect | null): boolean
```

判断路径是否构成矩形。

**起始版本：** 20

<!--Device-Path-isRect(rect: common2D.Rect | null): boolean--><!--Device-Path-isRect(rect: common2D.Rect | null): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect \| null | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## lineTo

```TypeScript
lineTo(x: number, y: number): void
```

添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的线段。

**起始版本：** 11

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Path-lineTo(x: double, y: double): void--><!--Device-Path-lineTo(x: double, y: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## moveTo

```TypeScript
moveTo(x: number, y: number): void
```

设置自定义路径的起始点位置。与[rMoveTo](arkts-arkgraphics2d-drawing-path-c.md#rmoveto)使用相对坐标不同，moveTo使用绝对坐标设置起始点。当路径起点固定时，推荐使用moveTo；当路径需要基于当前位置动态构建时，推荐使用[rMoveTo](arkts-arkgraphics2d-drawing-path-c.md#rmoveto)。

**起始版本：** 11

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Path-moveTo(x: double, y: double): void--><!--Device-Path-moveTo(x: double, y: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## offset

```TypeScript
offset(dx: number, dy: number): Path
```

将路径沿x轴方向偏移dx距离、沿y轴方向偏移dy距离，并保存在返回的路径对象中。

**起始版本：** 12

<!--Device-Path-offset(dx: number, dy: number): Path--><!--Device-Path-offset(dx: number, dy: number): Path-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dx | number | 是 |
| dy | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## op

```TypeScript
op(path: Path, pathOp: PathOp): boolean
```

将当前路径与path按照指定的路径操作类型进行合并，并将合并结果保存在当前路径中。

**起始版本：** 12

<!--Device-Path-op(path: Path, pathOp: PathOp): boolean--><!--Device-Path-op(path: Path, pathOp: PathOp): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |
| pathOp | [PathOp](arkts-arkgraphics2d-drawing-pathop-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## quadTo

```TypeScript
quadTo(ctrlX: number, ctrlY: number, endX: number, endY: number): void
```

添加从路径最后点位置（若路径没有内容则默认值为 (0, 0)）到目标点位置的二阶贝塞尔曲线。

**起始版本：** 11

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Path-quadTo(ctrlX: double, ctrlY: double, endX: double, endY: double): void--><!--Device-Path-quadTo(ctrlX: double, ctrlY: double, endX: double, endY: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ctrlX | number | 是 |
| ctrlY | number | 是 |
| endX | number | 是 |
| endY | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## rConicTo

```TypeScript
rConicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void
```

使用相对位置添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的圆锥曲线。与[conicTo](arkts-arkgraphics2d-drawing-path-c.md#conicto)使用绝对坐标不同，rConicTo使用相对于当前路径最后点位置的偏移量在当前路径上添加圆锥曲线。当路径需要基于当前位置动态构建时，推荐使用相对坐标方法；当路径目标点固定时，推荐使用绝对坐标方法。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Path-rConicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void--><!--Device-Path-rConicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ctrlX | number | 是 |
| ctrlY | number | 是 |
| endX | number | 是 |
| endY | number | 是 |
| weight | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## rCubicTo

```TypeScript
rCubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void
```

使用相对位置添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的三阶贝塞尔曲线。与[cubicTo](arkts-arkgraphics2d-drawing-path-c.md#cubicto)使用绝对坐标不同，rCubicTo使用相对于当前路径最后点位置的偏移量在当前路径上添加三阶贝塞尔曲线。当路径需要基于当前位置动态构建时，推荐使用相对坐标方法；当路径目标点固定时，推荐使用绝对坐标方法。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Path-rCubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void--><!--Device-Path-rCubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ctrlX1 | number | 是 |
| ctrlY1 | number | 是 |
| ctrlX2 | number | 是 |
| ctrlY2 | number | 是 |
| endX | number | 是 |
| endY | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## rLineTo

```TypeScript
rLineTo(dx: number, dy: number): void
```

使用相对位置添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的线段。与[lineTo](arkts-arkgraphics2d-drawing-path-c.md#lineto)使用绝对坐标不同，rLineTo使用相对于当前路径最后点位置的偏移量来指定目标点。当路径需要基于当前位置动态构建时，推荐使用相对坐标方法；当目标点位置固定时，推荐使用绝对坐标方法。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Path-rLineTo(dx: double, dy: double): void--><!--Device-Path-rLineTo(dx: double, dy: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dx | number | 是 |
| dy | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## rMoveTo

```TypeScript
rMoveTo(dx: number, dy: number): void
```

设置一个相对于当前路径最后点位置（若路径没有内容则默认为 (0, 0)）的路径起始点位置。与[moveTo](arkts-arkgraphics2d-drawing-path-c.md#moveto)使用绝对坐标不同，rMoveTo使用相对于当前路径最后点位置的偏移量。当路径需要基于当前位置动态构建时，推荐使用相对坐标方法（如rMoveTo、rLineTo等）；当路径起点固定时，推荐使用绝对坐标方法。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Path-rMoveTo(dx: double, dy: double): void--><!--Device-Path-rMoveTo(dx: double, dy: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dx | number | 是 |
| dy | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## rQuadTo

```TypeScript
rQuadTo(dx1: number, dy1: number, dx2: number, dy2: number): void
```

使用相对位置添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的二阶贝塞尔曲线。与[quadTo](arkts-arkgraphics2d-drawing-path-c.md#quadto)使用绝对坐标不同，rQuadTo使用相对于当前路径最后点位置的偏移量在当前路径上添加二阶贝塞尔曲线。当路径需要基于当前位置动态构建时，推荐使用相对坐标方法；当路径目标点固定时，推荐使用绝对坐标方法。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Path-rQuadTo(dx1: double, dy1: double, dx2: double, dy2: double): void--><!--Device-Path-rQuadTo(dx1: double, dy1: double, dx2: double, dy2: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dx1 | number | 是 |
| dy1 | number | 是 |
| dx2 | number | 是 |
| dy2 | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## reset

```TypeScript
reset(): void
```

重置自定义路径数据。

**起始版本：** 11

<!--Device-Path-reset(): void--><!--Device-Path-reset(): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## rewind

```TypeScript
rewind(): void
```

将路径内添加的各类点/线清空，但是保留内存空间。

**起始版本：** 20

<!--Device-Path-rewind(): void--><!--Device-Path-rewind(): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## set

```TypeScript
set(src: Path): void
```

使用指定路径替换当前路径的内容，使当前路径与指定路径完全一致。

**起始版本：** 20

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Path-set(src: Path): void--><!--Device-Path-set(src: Path): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |

## setFillType

```TypeScript
setFillType(pathFillType: PathFillType): void
```

设置路径的填充类型，决定路径内部区域的定义方式。

**起始版本：** 12

<!--Device-Path-setFillType(pathFillType: PathFillType): void--><!--Device-Path-setFillType(pathFillType: PathFillType): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pathFillType | [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## setLastPoint

```TypeScript
setLastPoint(x: number, y: number): void
```

修改路径最后点位置。

**起始版本：** 20

<!--Device-Path-setLastPoint(x: double, y: double): void--><!--Device-Path-setLastPoint(x: double, y: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

## toggleInverseFillType

```TypeScript
toggleInverseFillType(): void
```

切换路径的填充类型为反向类型。例如，使用WINDING填充类型时，经过取反后填充类型为INVERSE_WINDING，而使用EVEN_ODD填充类型时，经过取反后填充类型为INVERSE_EVEN_ODD，反之亦然。

**起始版本：** 23

<!--Device-Path-toggleInverseFillType(): void--><!--Device-Path-toggleInverseFillType(): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## transform

```TypeScript
transform(matrix: Matrix): void
```

对路径进行矩阵变换。

**起始版本：** 12

<!--Device-Path-transform(matrix: Matrix): void--><!--Device-Path-transform(matrix: Matrix): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
