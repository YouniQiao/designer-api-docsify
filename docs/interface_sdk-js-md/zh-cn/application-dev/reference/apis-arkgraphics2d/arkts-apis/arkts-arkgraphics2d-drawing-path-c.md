# Path

Path是Drawing模块提供的复合几何路径类，由直线、圆弧、圆锥曲线、二阶贝塞尔、三阶贝塞尔等基本图元组成， 支持路径的构造、变换、布尔运算、SVG路径解析与转换、测量与片段截取等能力。 未设置填充类型时，默认填充类型为WINDING，可通过[setFillType](#setfilltype)修改。

> **说明：**&gt;
> - 本模块使用屏幕物理像素单位px。&gt;
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
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

向路径添加一段圆弧。与[arcTo](#arcto)相比，addArc不会自动添加从路径最后点到弧线起点的连接线段，且通过common2D.Rect对象指定矩形边界。若需要自动连接弧线起点， 请使用arcTo；若仅需添加独立弧线，可使用addArc。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| startAngle | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| sweepAngle | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
const rect: common2D.Rect = {left:100.0, top:100.0, right:500.0, bottom:500.0};
path.addArc(rect, 90.0, 180.0);
```

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

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| radius | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.addCircle(100.0, 200.0, 50.0, drawing.PathDirection.CLOCKWISE);
```

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

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| start | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
const rect: common2D.Rect = {left:100.0, top:100.0, right:500.0, bottom:500.0};
path.addOval(rect, 5, drawing.PathDirection.CLOCKWISE);
```

## addPath

```TypeScript
addPath(path: Path, matrix?: Matrix | null): void
```

对源路径进行矩阵变换后，将其添加到当前路径中。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) \| null | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
let matrix = new drawing.Matrix();
const rect: common2D.Rect = {left:100.0, top:100.0, right:500.0, bottom:500.0};
let roundRect = new drawing.RoundRect(rect, 50.0, 50.0);
path.addRoundRect(roundRect, drawing.PathDirection.CLOCKWISE);
let dstPath = new drawing.Path();
dstPath.addPath(path, matrix);
```

## addPolygon

```TypeScript
addPolygon(points: Array<common2D.Point>, close: boolean): void
```

通过坐标点列表添加多条连续的线段。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| points | Array & lt;common2D.Point & gt; | 是 |
| [close](#close) | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let pointsArray = new Array<common2D.Point>();
const point1: common2D.Point = { x: 200.0, y: 200.0 };
const point2: common2D.Point = { x: 400.0, y: 200.0 };
const point3: common2D.Point = { x: 100.0, y: 400.0 };
const point4: common2D.Point = { x: 300.0, y: 400.0 };
pointsArray.push(point1);
pointsArray.push(point2);
pointsArray.push(point3);
pointsArray.push(point4);
const path = new drawing.Path();
path.addPolygon(pointsArray, false);
```

## addRect

```TypeScript
addRect(rect: common2D.Rect, pathDirection?: PathDirection): void
```

按指定方向，将矩形添加到路径中，添加的路径的起始点为矩形左上角。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
const rect: common2D.Rect = {left:100.0, top:100.0, right:500.0, bottom:500.0};
path.addRect(rect, drawing.PathDirection.CLOCKWISE);
```

## addRoundRect

```TypeScript
addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void
```

按指定方向，向路径添加圆角矩形轮廓。路径添加方向为顺时针时，起始点位于圆角矩形左下方圆角与左边界的交点；路径添加方向为逆时针时，起始点位于圆角矩形左上方圆角与左边界的交点。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| roundRect | [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) | 是 |
| pathDirection | [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
const rect: common2D.Rect = {left:100.0, top:100.0, right:500.0, bottom:500.0};
let roundRect = new drawing.RoundRect(rect, 50.0, 50.0);
path.addRoundRect(roundRect, drawing.PathDirection.CLOCKWISE);
```

## approximate

```TypeScript
approximate(acceptableError: number): Array<number>
```

将当前路径转化为由连续直线段构成的近似路径。

> **说明：**&gt;
> - 当acceptableError为0时，曲线路径被极度细分，会严重影响性能和内存消耗，不建议设置误差值为0。&gt;
> - 当acceptableError远大于路径尺寸时，路径会极度简化，仅保留路径的起止点等少量关键点，可能会丢失原有形状。&gt;
> - 对于椭圆等曲线，当acceptableError过大时，拟合结果通常只包含椭圆的分段贝塞尔曲线的起止点，椭圆形会被极度简化为多边形。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| acceptableError | number | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(100, 100);
path.lineTo(500, 500);
let points: number[] = path.approximate(0.5);
for (let i = 0; i < points.length; i += 3) {
  console.info('PathApproximate Fraction =' + points[i] + ', X =' + points[i + 1] + ', Y =' + points[i + 2] + '\n');
}
```

ArkTS-Sta示例：

```TypeScript
import drawing from "@ohos.graphics.drawing";
import common2D from "@ohos.graphics.common2D";

let path: drawing.Path = new drawing.Path();
path.moveTo(100.0, 100.0);
path.lineTo(500.0, 500.0);
let points: double[] | undefined = path.approximate(0.5);
if (points == undefined) {
  return;
}
for (let i = 0; i < points.length; i += 3) {
  console.info("PathApproximate Fraction =" + points[i] + ", X =" + points[i + 1] + ", Y =" + points[i + 2] + "\n");
}
```

## approximate

```TypeScript
approximate(acceptableError: double): Array<double> | undefined
```

将当前路径转化为由连续直线段构成的近似路径。

> **说明：**&gt;
> - 当acceptableError为0时，曲线路径被极度细分，会严重影响性能和内存消耗，不建议设置误差值为0。&gt;
> - 当acceptableError远大于路径尺寸时，路径会极度简化，仅保留路径的起止点等少量关键点，可能会丢失原有形状。&gt;
> - 对于椭圆等曲线，当acceptableError过大时，拟合结果通常只包含椭圆的分段贝塞尔曲线的起止点，椭圆形会被极度简化为多边形。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| acceptableError | double | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;double & gt; \ | undefined |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |

**示例**

参见 [approximate](#approximate)

## arcTo

ArkTS-Dyn:
```TypeScript
arcTo(x1: number, y1: number, x2: number, y2: number, startDeg: number, sweepDeg: number): void
```

ArkTS-Sta:
```TypeScript
arcTo(x1: double, y1: double, x2: double, y2: double, startDeg: double, sweepDeg: double): void
```

给路径添加一段弧线。绘制弧线的方式为角度弧：首先指定一个矩形边界，取其内切椭圆；然后指定起始角度和扫描度数；最后从起始角度 扫描截取椭圆周长的一部分，即为绘制的弧线。另外会默认添加一条从路径最后点位置（若路径没有内容则默认值为 (0, 0)）到 弧线起始点位置的线段。若不需要自动添加连接线段，请使用[addArc](#addarc)。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x1 | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y1 | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| x2 | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y2 | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| startDeg | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| sweepDeg | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10.0, 10.0);
path.arcTo(10.0, 15.0, 10.0, 10.0, 10.0, 10.0);
```

## buildFromSvgString

```TypeScript
buildFromSvgString(str: string): boolean
```

解析SVG字符串表示的路径。支持标准SVG路径数据命令（如M、L、C、Q、A、Z及其相对坐标形式等），解析失败时返回false。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let svgString: string = "M150 100 L75 300 L225 300 Z";
if (path.buildFromSvgString(svgString)) {
  console.info('buildFromSvgString return true');
} else {
  console.info('buildFromSvgString return false');
}
```

## close

```TypeScript
close(): void
```

闭合路径，会添加一条从路径最后点位置到起始点位置的线段。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10.0, 10.0);
path.cubicTo(10.0, 10.0, 10.0, 10.0, 15.0, 15.0);
path.close();
```

## conicTo

ArkTS-Dyn:
```TypeScript
conicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void
```

ArkTS-Sta:
```TypeScript
conicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void
```

在当前路径上添加一条路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的圆锥曲线，其控制点为 (ctrlX, ctrlY)， 目标点为 (endX, endY)。与[quadTo](#quadto)相比，conicTo通过权重参数可更灵活地控制曲线形状： 权重为1时效果与quadTo相同，权重不为1时可精确表示圆弧、椭圆弧等圆锥曲线段。仅需标准二次贝塞尔 曲线时推荐使用quadTo，需要精确表示圆弧或灵活控制曲线形状时推荐使用conicTo。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ctrlX | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| ctrlY | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| endX | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| endY | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| weight | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.conicTo(200.0, 400.0, 100.0, 200.0, 0.0);
```

## constructor

```TypeScript
constructor()
```

构造一个路径。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
const brushColor: common2D.Color = { alpha: 255, red: 0, green: 255, blue: 0 };
brush.setColor(brushColor);
const newBrush = new drawing.Brush(brush);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
import { image } from '@kit.ImageKit';

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: image.PixelMapFormat.RGBA_8888,
  size: {
    height: 4,
    width: 6
  }
};
image.createPixelMap(color, opts).then((pixelMap) => {
  const canvas = new drawing.Canvas(pixelMap);
});
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
let matrix2 = new drawing.Matrix(matrix);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0.0, 0.0);
path.lineTo(0.0, 700.0);
path.lineTo(700.0, 0.0);
path.close();
let path1: drawing.Path = new drawing.Path(path);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let iter: drawing.PathIterator = new drawing.PathIterator(path);
console.info('PathIterator created successfully');
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
const penColor: common2D.Color = { alpha: 255, red: 0, green: 255, blue: 0 };
pen.setColor(penColor);
pen.setStrokeWidth(10.0);
const newPen = new drawing.Pen(pen);
```

ArkTS-Dyn示例：

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';
class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    pen.setStrokeWidth(10);
    canvas.attachPen(pen);
    let region = new drawing.Region();
    region.setRect(200, 200, 400, 400);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';
class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    pen.setStrokeWidth(10.0);
    canvas.attachPen(pen);
    let region = new drawing.Region();
    region.setRect(200, 200, 400, 400);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';
class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    pen.setStrokeWidth(10);
    canvas.attachPen(pen);
    let region = new drawing.Region();
    region.setRect(200, 200, 400, 400);
    let region2 = new drawing.Region(region);
    canvas.drawRegion(region2);
    canvas.detachPen();
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';
class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    pen.setStrokeWidth(10);
    canvas.attachPen(pen);
    let region = new drawing.Region();
    region.setRect(200, 200, 400, 400);
    let region2 = new drawing.Region(region);
    canvas.drawRegion(region2);
    canvas.detachPen();
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';
class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    pen.setStrokeWidth(10);
    canvas.attachPen(pen);
    let region = new drawing.Region(100, 100, 200, 200);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';
class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    pen.setStrokeWidth(10.0);
    canvas.attachPen(pen);
    let region = new drawing.Region(100, 100, 200, 200);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let rect: common2D.Rect = {left: 100.0, top: 100.0, right: 500.0, bottom: 300.0};
let roundRect = new drawing.RoundRect(rect, 50.0, 50.0);
let roundRect2 = new drawing.RoundRect(roundRect);
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let rect: common2D.Rect = { left: 100.0, top: 100.0, right: 500.0, bottom: 300.0 };
let roundRect = new drawing.RoundRect(rect, 50.0, 50.0);
```

ArkTS-Dyn示例：

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context: DrawContext) {
    let samplingOptions = new drawing.SamplingOptions();
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    let samplingOptions = new drawing.SamplingOptions();
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context: DrawContext) {
    let samplingOptions = new drawing.SamplingOptions(drawing.FilterMode.FILTER_MODE_NEAREST);
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let samplingOptions = new drawing.SamplingOptions(drawing.FilterMode.FILTER_MODE_NEAREST);
  }
}
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
let typefaceArgument = new drawing.TypefaceArguments();
```

## constructor

```TypeScript
constructor(path: Path)
```

构造一个已有路径的副本。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |

**示例**

参见 [constructor](#constructor)

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

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
let rect : common2D.Rect = {left: 50, top: 50, right: 250, bottom: 250};
path.addRect(rect, drawing.PathDirection.CLOCKWISE);
console.info("test contains: " + path.contains(0.0, 0.0));
console.info("test contains: " + path.contains(60.0, 60.0));
```

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10, 10, 20, 20);
let rect2 = drawing.RectUtils.makeLtrb(0, 0, 40, 40);
let isContains = drawing.RectUtils.contains(rect2, rect);
console.info('isContains: ', isContains);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10.0, 10.0, 20.0, 20.0);
let rect2 = drawing.RectUtils.makeLtrb(0.0, 0.0, 40.0, 40.0);
if (rect == undefined || rect2 == undefined) {
    return;
}
let isContains = drawing.RectUtils.contains(rect2, rect);
console.info('isContains: ', isContains);
```

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0, 0, 100, 100);
let isContains = drawing.RectUtils.contains(rect, 10, 20, 30, 40);
console.info('isContains: ', isContains);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0.0, 0.0, 100.0, 100.0);
if (rect == undefined) {
    return;
}
let isContains = drawing.RectUtils.contains(rect, 10.0, 20.0, 30.0, 40.0);
console.info('isContains :', isContains);
```

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0, 0, 100, 100);
let isContains = drawing.RectUtils.contains(rect, 10, 20);
console.info('isContains: ', isContains);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0.0, 0.0, 100.0, 100.0);
if (rect == undefined) {
    return;
}
let isContains = drawing.RectUtils.contains(rect, 10.0, 20.0);
console.info('isContains: ', isContains);
```

## convertToSvgString

```TypeScript
convertToSvgString(): string
```

将路径转换为SVG字符串。输出的字符串遵循SVG路径数据规范映射。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(0, 700);
path.close();
let svgString = path.convertToSvgString();
console.info('svgString: ', svgString);
```

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

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ctrlX1 | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| ctrlY1 | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| ctrlX2 | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| ctrlY2 | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| endX | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| endY | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10.0, 10.0);
path.cubicTo(100.0, 100.0, 80.0, 150.0, 300.0, 150.0);
```

## getBounds

```TypeScript
getBounds(): common2D.Rect
```

获取包含路径的最小矩形边界。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Rect |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let font: drawing.Font = new drawing.Font();
let text: string = 'hello world';
let glyphs: number[] = font.textToGlyphs(text);
let fontBounds: Array<common2D.Rect> = font.getBounds(glyphs);
for (let index = 0; index < fontBounds.length; index++) {
  console.info("get fontWidths[", index, "] left:", fontBounds[index].left, " top:", fontBounds[index].top,
    " right:", fontBounds[index].right, " bottom:", fontBounds[index].bottom);
}
```

ArkTS-Sta示例：

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let font: drawing.Font = new drawing.Font();
let text: string = 'hello world';
let glyphs : int[] | undefined = font.textToGlyphs(text);
if (glyphs != undefined && font.getBounds(glyphs!) != undefined) {
  let fontBounds: Array<common2D.Rect> = font.getBounds(glyphs!)!;
  for (let index = 0; index < fontBounds.length; index++) {
    console.info("get fontWidths[", index, "] left:", fontBounds[index].left, " top:", fontBounds[index].top,
      " right:", fontBounds[index].right, " bottom:", fontBounds[index].bottom);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.lineTo(50, 40);
let rect : common2D.Rect = {left: 0, top: 0, right: 0, bottom: 0};
rect = path.getBounds();
console.info('test rect.left: ' + rect.left);
console.info('test rect.top: ' + rect.top);
console.info('test rect.right: ' + rect.right);
console.info('test rect.bottom: ' + rect.bottom);
```

ArkTS-Sta示例：

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.lineTo(50.0, 40.0)
let rect : common2D.Rect = {left: 0.0, top: 0.0, right: 0.0, bottom: 0.0};
rect = path.getBounds() == undefined ? rect : path.getBounds()!;
console.info("test rect.left: " + rect.left);
console.info("test rect.top: " + rect.top);
console.info("test rect.right: " + rect.right);
console.info("test rect.bottom: " + rect.bottom);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let region = new drawing.Region();
let rect = region.getBounds();
```

## getBounds

```TypeScript
getBounds(): common2D.Rect | undefined
```

获取包含路径的最小矩形边界。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Rect \| undefined |

**示例**

参见 [getBounds](#getbounds)

## getConicWeightData

ArkTS-Dyn:
```TypeScript
getConicWeightData(): Array<number>
```

ArkTS-Sta:
```TypeScript
getConicWeightData(): Array<double>
```

获取路径的圆锥曲线权重数据。在路径（path）图元中，圆锥曲线数据采用有理贝塞尔曲线（Rational Bézier Curve）形式表示，其中每个控制点附带一个权重值（weight）。权重属于曲线定义的几何参数。主要作用如下：形状调控：权重值越大，曲线越靠近对应控制点；权重为1时退化为标准贝塞尔曲线；权重为0时该控制点不起作用。精确表示圆锥曲线：通过组合权重与二次贝塞尔曲线，可以精确表示圆弧、椭圆弧、抛物线等圆锥曲线段，无需使用分段逼近或专用椭圆弧指令。数据组织：权重通常以数组形式与点数据并列，按顺序对应每个控制点，与相应的指令verb（如[conicTo](#conicto)）配合使用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: Array & lt;number & gt;<br>ArkTS-Sta：Array & lt;double & gt; |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.conicTo(100, 100, 200, 0, 0.5);
let conicWeightData: Array<number> = path.getConicWeightData();
console.info('conicWeightData size: ', conicWeightData.length);
console.info('conicWeightData[0]: ', conicWeightData[0]);
```

ArkTS-Sta示例：

```TypeScript
import drawing from "@ohos.graphics.drawing";

let path: drawing.Path = new drawing.Path();
path.moveTo(0.0, 0.0);
path.conicTo(100.0, 100.0, 200.0, 0.0, 0.5);
let conicWeightData: Array<double> = path.getConicWeightData();
if (conicWeightData == undefined) {
  return;
}
console.info("conicWeightData size: ", conicWeightData.length);
console.info("conicWeightData[0]: ", conicWeightData[0]);
```

## getFillType

```TypeScript
getFillType(): PathFillType
```

获取路径的填充类型。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
const path = new drawing.Path();
path.setFillType(drawing.PathFillType.WINDING);
let type = path.getFillType();
console.info('type :' + type);
```

## getFillType

```TypeScript
getFillType(): PathFillType | undefined
```

获取路径的填充类型。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md) \| undefined |

**示例**

参见 [getFillType](#getfilltype)

## getLastPoint

```TypeScript
getLastPoint(): common2D.Point
```

获取路径最后点位置的坐标。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Point |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
const path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(100, 100);
let lastPoint = path.getLastPoint();
console.info('lastPoint.x:', lastPoint?.x);
console.info('lastPoint.y:', lastPoint?.y);
```

## getLastPoint

```TypeScript
getLastPoint(): common2D.Point | undefined
```

获取路径最后点位置的坐标。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Point \| undefined |

**示例**

参见 [getLastPoint](#getlastpoint)

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

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| forceClosed | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：double |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.arcTo(20.0, 20.0, 180.0, 180.0, 180.0, 90.0);
let len = path.getLength(false);
console.info('path length = ' + len);
```

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

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| forceClosed | boolean | 是 |
| distance | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |
| flags | [PathMeasureMatrixFlags](arkts-arkgraphics2d-drawing-pathmeasurematrixflags-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(0, 700);
let matrix = new drawing.Matrix();
if(path.getMatrix(false, 10.0, matrix, drawing.PathMeasureMatrixFlags.GET_TANGENT_MATRIX)) {
  console.info("path.getMatrix return true");
} else {
  console.info('path.getMatrix return false');
}
```

## getPathIterator

```TypeScript
getPathIterator(): PathIterator
```

返回该路径的操作迭代器。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为18。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [PathIterator](arkts-arkgraphics2d-drawing-pathiterator-c.md) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let iter = path.getPathIterator();
```

## getPathIterator

```TypeScript
getPathIterator(): PathIterator | undefined
```

返回该路径的操作迭代器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [PathIterator](arkts-arkgraphics2d-drawing-pathiterator-c.md) \| undefined |

**示例**

参见 [getPathIterator](#getpathiterator)

## getPointData

```TypeScript
getPointData(): Array<common2D.Point>
```

获取路径的点数据。在路径（path）图元中，点数据以数值序列的形式存在，与verb指令一一对应，用来精确指定绘图操作的几何坐标位置。点数据的主要类型包括：终点坐标：与[moveTo](#moveto)、[lineTo](#lineto)等指令配合，定义线段或移动的目标位置。控制点坐标：与曲线指令配合，用于定义贝塞尔曲线的形状（如三次曲线需要两个控制点和一个终点）。闭合点：通常不单独提供坐标，由[close](#close)指令隐式使用路径起点。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array & lt;common2D.Point & gt; |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
import { common2D } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(100, 100);
path.quadTo(150, 150, 200, 100);
let pointData: Array<common2D.Point> = path.getPointData();
console.info('pointData size: ', pointData.length);
console.info('pointData[0].x: ', pointData[0].x);
console.info('pointData[0].y: ', pointData[0].y);
```

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

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| forceClosed | boolean | 是 |
| distance | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| position | common2D.Point | 是 |
| tangent | common2D.Point | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0.0, 0.0);
path.lineTo(0.0, 700.0);
path.lineTo(700.0, 0.0);
let position: common2D.Point = { x: 0.0, y: 0.0 };
let tangent: common2D.Point = { x: 0.0, y: 0.0 };
if (path.getPositionAndTangent(false, 0.1, position, tangent)) {
  console.info('getPositionAndTangent-----position:  ' + position.x);
  console.info('getPositionAndTangent-----position:  ' + position.y);
  console.info('getPositionAndTangent-----tangent:  ' + tangent.x);
  console.info('getPositionAndTangent-----tangent:  ' + tangent.y);
}
```

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

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| forceClosed | boolean | 是 |
| start | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| stop | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| startWithMoveTo | boolean | 是 |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0.0, 0.0);
path.lineTo(0.0, 700.0);
path.lineTo(700.0, 0.0);
let dstPath: drawing.Path = new drawing.Path();
console.info('getSegment-----result:  ' + path.getSegment(true, 10.0, 20.0, true, dstPath));
```

## getVerbData

```TypeScript
getVerbData(): Array<PathIteratorVerb>
```

获取路径的指令数据。在路径（path）图元中，指令数据verb用于描述路径构造过程中的基本绘图动作。指令数据以枚举的形式存在，每个取值对应一种几何操作类型，例如：  
[moveTo](#moveto)：将当前绘图点移至指定坐标，不产生线段。  
[lineTo](#lineto)：从当前点向指定点绘制直线段。  
[close](#close)：将当前点与路径起点相连，形成封闭区域。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array&lt;[PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md)&gt; |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(100, 100);
path.close();
let verbData: Array<drawing.PathIteratorVerb> = path.getVerbData();
console.info('verbData size: ', verbData.length);
console.info('verbData[0]: ', verbData[0]);
console.info('verbData[1]: ', verbData[1]);
```

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

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |
| weight | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| interpolatedPath | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(50, 50);
path.lineTo(100, 100);
path.lineTo(200, 200);
let other: drawing.Path = new drawing.Path();
other.moveTo(80, 80);
other.lineTo(300, 300);
let interpolatedPath: drawing.Path = new drawing.Path();
if (path.interpolate(other, 0.0, interpolatedPath)) {
  console.info('interpolate return true');
} else {
  console.info('interpolate return false');
}
```

## isClosed

```TypeScript
isClosed(): boolean
```

获取路径是否闭合。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0.0, 0.0);
path.lineTo(0.0, 700.0);
if (path.isClosed()) {
  console.info('path is closed.');
} else {
  console.info('path is not closed.');
}
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断路径是否为空。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
let path = new drawing.Path();
path.moveTo(10.0, 10.0);
path.lineTo(20.0, 20.0);
let isEmpty = path.isEmpty();
console.info('isEmpty:', isEmpty);
```

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeEmpty();
let isEmpty = drawing.RectUtils.isEmpty(rect);
console.info('isEmpty:', isEmpty);
let rect2 = drawing.RectUtils.makeLtrb(0, 0, 20, 20);
isEmpty = drawing.RectUtils.isEmpty(rect2);
console.info('isEmpty:', isEmpty);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeEmpty();
if (rect == undefined) {
    return;
}
let isEmpty = drawing.RectUtils.isEmpty(rect);
console.info('isEmpty :', isEmpty);
let rect2 = drawing.RectUtils.makeLtrb(0.0, 0.0, 20.0, 20.0);
if (rect2 == undefined) {
    return;
}
isEmpty = drawing.RectUtils.isEmpty(rect2);
console.info('isEmpty :', isEmpty);
```

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    pen.setStrokeWidth(10);
    canvas.attachPen(pen);
    let region = new drawing.Region();
    let flag: boolean = region.isEmpty();
    console.info('flag: ', flag);
    region.setRect(100, 100, 400, 400);
    flag = region.isEmpty();
    console.info('flag: ', flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

## isEqual

```TypeScript
isEqual(path: Path): boolean
```

判断当前路径与另一条路径是否相等。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix1 = new drawing.Matrix();
matrix1.setMatrix([2, 1, 3, 1, 2, 1, 3, 1, 2]);
let matrix2 = new drawing.Matrix();
matrix2.setMatrix([-2, 1, 3, 1, 0, -1, 3, -1, 2]);
if (matrix1.isEqual(matrix2)) {
  console.info("matrix1 and matrix2 are equal.");
} else {
  console.info("matrix1 and matrix2 are not equal.");
}
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(100, 100);
let other: drawing.Path = new drawing.Path();
other.moveTo(0, 0);
other.lineTo(100, 100);
if (path.isEqual(other)) {
  console.info('isEqual return true');
} else {
  console.info('isEqual return false');
}
```

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10, 20, 20, 30);
let rect2 = drawing.RectUtils.makeEmpty();
let isEqual = drawing.RectUtils.isEqual(rect, rect2);
console.info('isEqual:', isEqual);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10.0, 20.0, 20.0, 30.0);
let rect2 = drawing.RectUtils.makeEmpty();
if (rect == undefined || rect2 == undefined) {
    return;
}
let isEqual = drawing.RectUtils.isEqual(rect, rect2);
console.info('isEqual :', isEqual);
```

ArkTS-Dyn示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
import { RenderNode, DrawContext } from '@kit.ArkUI';
class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    pen.setStrokeWidth(10);
    canvas.attachPen(pen);
    let region = new drawing.Region();
    let other = new drawing.Region();
    region.setRect(100, 100, 400, 400);
    other.setRect(150, 150, 250 ,250);
    let flag: boolean = false;
    flag = region.isEqual(other);
    console.info('flag: ', flag);
    canvas.drawRegion(region);
    canvas.drawRegion(other);
    canvas.detachPen();
  }
}
```

ArkTS-Sta示例：

```TypeScript
import drawing from "@ohos.graphics.drawing";
import common2D from "@ohos.graphics.common2D";
import { RenderNode, DrawContext } from '@ohos.arkui.node';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    pen.setStrokeWidth(10);
    canvas.attachPen(pen);
    let region = new drawing.Region();
    let other = new drawing.Region();
    region.setRect(100, 100, 400, 400);
    other.setRect(150, 150, 250 ,250);
    let flag: boolean = false;
    flag = region.isEqual(other);
    console.info('flag: ', flag);
    canvas.drawRegion(region);
    canvas.drawRegion(other);
    canvas.detachPen();
  }
}
```

## isInterpolate

```TypeScript
isInterpolate(other: Path): boolean
```

判断当前路径与另一条路径在结构和操作顺序上是否完全一致，以确定两条路径是否兼容插值。若路径中包含圆锥曲线（Conic）操作，则对应操作的权重值也必须一致，才能视为兼容插值。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0.0, 0.0);
path.lineTo(100.0, 100.0);
let other: drawing.Path = new drawing.Path();
other.moveTo(0.0, 1.0);
other.lineTo(200.0, 200.0);
if (path.isInterpolate(other)) {
  console.info('isInterpolate return true');
} else {
  console.info('isInterpolate return false');
}
```

## isInverseFillType

```TypeScript
isInverseFillType(): boolean
```

检查当前路径填充类型是否是反向填充类型。例如填充类型WINDING、EVEN_ODD不是反向类型，INVERSE_WINDING、INVERSE_EVEN_ODD是反向类型。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.setFillType(drawing.PathFillType.WINDING);
if (path.isInverseFillType()) {
  console.info("path is inverse FillType.");
} else {
  console.info("path is not inverse FillType.");
}
```

## isRect

```TypeScript
isRect(rect: common2D.Rect | null): boolean
```

判断路径是否构成矩形。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect \| null | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10.0,10.0);
path.lineTo(20.0,10.0);
let isRect = path.isRect(null);
console.info("isRect: ", isRect);
let rect: common2D.Rect = { left : 100.0, top : 100.0, right : 400.0, bottom : 500.0 };
path.lineTo(20.0, 20.0);
path.lineTo(10.0, 20.0);
path.lineTo(10.0, 10.0);
isRect = path.isRect(rect);
console.info('isRect: ', isRect);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
import { RenderNode, DrawContext } from '@kit.ArkUI';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    pen.setStrokeWidth(10);
    canvas.attachPen(pen);
    let region = new drawing.Region();
    let flag: boolean = false;
    flag = region.isRect();
    console.info('flag :', flag);
    region.setRect(100, 100, 200, 200);
    flag = region.isRect();
    console.info('flag :', flag);
    let other = new drawing.Region(220, 200, 280, 280);
    region.op(other, drawing.RegionOp.UNION);
    flag = region.isRect();
    console.info('flag :', flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

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

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10.0, 10.0);
path.lineTo(10.0, 15.0);
```

## moveTo

ArkTS-Dyn:
```TypeScript
moveTo(x: number, y: number): void
```

ArkTS-Sta:
```TypeScript
moveTo(x: double, y: double): void
```

设置自定义路径的起始点位置。与[rMoveTo](#rmoveto)使用相对坐标不同，moveTo使用绝对坐标设置起始点。 当路径起点固定时，推荐使用moveTo；当路径需要基于当前位置动态构建时，推荐使用[rMoveTo](#rmoveto)。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10.0, 10.0);
```

## offset

```TypeScript
offset(dx: number, dy: number): Path
```

将路径沿x轴方向偏移dx距离、沿y轴方向偏移dy距离，并保存在返回的路径对象中。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.moveTo(200, 200);
path.lineTo(300, 300);
const dstPath = path.offset(200, 200);
```

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0, 0, 20, 20);
drawing.RectUtils.offset(rect, 10, 20);
console.info('rect.left: ', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0.0, 0.0, 20.0, 20.0);
if (rect == undefined) {
    return;
}
drawing.RectUtils.offset(rect, 10, 20);
console.info('rect.left:', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';
class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    pen.setStrokeWidth(10.0);
    canvas.attachPen(pen);
    let region = new drawing.Region();
    region.setRect(100, 100, 400, 400);
    region.offset(10, 20);
    canvas.drawPoint(200.0, 200.0);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let roundRect : drawing.RoundRect = new drawing.RoundRect({ left: 0, top: 0, right: 300, bottom: 300 }, 50, 50);
roundRect.offset(100, 100);
```

## offset

```TypeScript
offset(dx: double, dy: double): Path | undefined
```

Offsets this path by specified distances along the X axis and Y axis and stores the resulting path in the Path object returned.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dx | double | 是 |
| dy | double | 是 |

**返回值：**

| 类型 |
| --- |
| Path \| undefined |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

参见 [offset](#offset)

## op

```TypeScript
op(path: Path, pathOp: PathOp): boolean
```

将当前路径与path按照指定的路径操作类型进行合并，并将合并结果保存在当前路径中。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
const path2 = new drawing.Path();
path.addCircle(100.0, 200.0, 100.0, drawing.PathDirection.CLOCKWISE);
console.info("get pathOp: ", path2.op(path, drawing.PathOp.DIFFERENCE));
```

ArkTS-Dyn示例：

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    pen.setStrokeWidth(10);
    canvas.attachPen(pen);
    let region = new drawing.Region();
    region.setRect(200, 200, 400, 400);
    let othregion = new drawing.Region();
    othregion.setRect(110, 110, 240, 240);
    let flag: boolean = false;
    flag = region.op(othregion,drawing.RegionOp.REPLACE);
    console.info("region op : " + flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    pen.setStrokeWidth(10.0);
    canvas.attachPen(pen);
    let region = new drawing.Region();
    region.setRect(200, 200, 400, 400);
    let othregion = new drawing.Region();
    othregion.setRect(110, 110, 240, 240);
    let flag: boolean = false;
    flag = region.op(othregion, drawing.RegionOp.REPLACE);
    console.info("region op : " + flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

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

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ctrlX | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| ctrlY | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| endX | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| endY | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10.0, 10.0);
path.quadTo(10.0, 15.0, 10.0, 10.0);
```

## rConicTo

ArkTS-Dyn:
```TypeScript
rConicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void
```

ArkTS-Sta:
```TypeScript
rConicTo(ctrlX: double, ctrlY: double, endX: double, endY: double, weight: double): void
```

使用相对位置添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的圆锥曲线。 与[conicTo](#conicto)使用绝对坐标不同，rConicTo使用相对于当前路径最后点位置的偏移量在当前路径上添加 圆锥曲线。当路径需要基于当前位置动态构建时，推荐使用相对坐标方法；当路径目标点固定时，推荐使用绝对坐标方法。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ctrlX | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| ctrlY | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| endX | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| endY | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| weight | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.rConicTo(200.0, 400.0, 100.0, 200.0, 0.0);
```

## rCubicTo

ArkTS-Dyn:
```TypeScript
rCubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void
```

ArkTS-Sta:
```TypeScript
rCubicTo(ctrlX1: double, ctrlY1: double, ctrlX2: double, ctrlY2: double, endX: double, endY: double): void
```

使用相对位置添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的三阶贝塞尔曲线。 与[cubicTo](#cubicto)使用绝对坐标不同，rCubicTo使用相对于当前路径最后点位置的偏移量在当前路径上 添加三阶贝塞尔曲线。当路径需要基于当前位置动态构建时，推荐使用相对坐标方法；当路径目标点固定时，推荐使用绝对坐标方法。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ctrlX1 | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| ctrlY1 | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| ctrlX2 | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| ctrlY2 | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| endX | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| endY | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.rCubicTo(200.0, 0.0, 0.0, 200.0, -20.0, 0.0);
```

## reset

```TypeScript
reset(): void
```

重置自定义路径数据。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
brush.reset();
```

ArkTS-Dyn示例：

```TypeScript
import {drawing} from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
matrix.postScale(2, 3, 4, 5);
matrix.reset();
console.info("matrix= "+matrix.getAll().toString());
```

ArkTS-Sta示例：

```TypeScript
import {drawing} from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
matrix.postScale(2.0, 3.0, 4.0, 5.0);
matrix.reset();
if (matrix.getAll() != undefined) {
  console.info("matrix= "+matrix.getAll()!.toString());
}
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
path.moveTo(10.0, 10.0);
path.cubicTo(10.0, 10.0, 10.0, 10.0, 15.0, 15.0);
path.reset();
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
pen.reset();
```

## rewind

```TypeScript
rewind(): void
```

将路径内添加的各类点/线清空，但是保留内存空间。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
let path = new drawing.Path();
path.moveTo(10.0, 10.0);
path.lineTo(20.0, 20.0);
path.rewind();
let empty = path.isEmpty();
console.info('empty : ', empty);
```

## rLineTo

ArkTS-Dyn:
```TypeScript
rLineTo(dx: number, dy: number): void
```

ArkTS-Sta:
```TypeScript
rLineTo(dx: double, dy: double): void
```

使用相对位置添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的线段。 与[lineTo](#lineto)使用绝对坐标不同，rLineTo使用相对于当前路径最后点位置的偏移量来指定目标点。 当路径需要基于当前位置动态构建时，推荐使用相对坐标方法；当目标点位置固定时，推荐使用绝对坐标方法。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dx | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| dy | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.rLineTo(400.0, 200.0);
```

## rMoveTo

ArkTS-Dyn:
```TypeScript
rMoveTo(dx: number, dy: number): void
```

ArkTS-Sta:
```TypeScript
rMoveTo(dx: double, dy: double): void
```

设置一个相对于当前路径最后点位置（若路径没有内容则默认为 (0, 0)）的路径起始点位置。 与[moveTo](#moveto)使用绝对坐标不同，rMoveTo使用相对于当前路径最后点位置的偏移量。 当路径需要基于当前位置动态构建时，推荐使用相对坐标方法（如rMoveTo、rLineTo等）；当路径起点固定时，推荐使用绝对坐标方法。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dx | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| dy | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.rMoveTo(10.0, 10.0);
```

## rQuadTo

ArkTS-Dyn:
```TypeScript
rQuadTo(dx1: number, dy1: number, dx2: number, dy2: number): void
```

ArkTS-Sta:
```TypeScript
rQuadTo(dx1: double, dy1: double, dx2: double, dy2: double): void
```

使用相对位置添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的二阶贝塞尔曲线。 与[quadTo](#quadto)使用绝对坐标不同，rQuadTo使用相对于当前路径最后点位置的偏移量在当前路径上 添加二阶贝塞尔曲线。当路径需要基于当前位置动态构建时，推荐使用相对坐标方法；当路径目标点固定时，推荐使用绝对坐标方法。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dx1 | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| dy1 | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| dx2 | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| dy2 | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.rQuadTo(100.0, 0.0, 0.0, 200.0);
```

## set

```TypeScript
set(src: Path): void
```

使用指定路径替换当前路径的内容，使当前路径与指定路径完全一致。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
let path: drawing.Path = new drawing.Path();
path.moveTo(0.0, 0.0);
path.lineTo(0.0, 700.0);
path.lineTo(700.0, 0.0);
path.close();
let path1: drawing.Path = new drawing.Path();
path1.set(path);
```

## setFillType

```TypeScript
setFillType(pathFillType: PathFillType): void
```

设置路径的填充类型，决定路径内部区域的定义方式。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pathFillType | [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.setFillType(drawing.PathFillType.WINDING);
```

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

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
const path = new drawing.Path();
path.moveTo(0.0, 0.0);
path.lineTo(0.0, 700.0);
let isEmpty = path.isEmpty();
console.info('isEmpty:', isEmpty);
path.reset();
isEmpty = path.isEmpty();
console.info('isEmpty:', isEmpty);
path.setLastPoint(50.0, 50.0);
isEmpty = path.isEmpty();
console.info('isEmpty:', isEmpty);
```

## toggleInverseFillType

```TypeScript
toggleInverseFillType(): void
```

切换路径的填充类型为反向类型。例如，使用WINDING填充类型时，经过取反后填充类型为INVERSE_WINDING，而使用EVEN_ODD填充类型时，经过取反后填充类型为INVERSE_EVEN_ODD，反之亦然。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.setFillType(drawing.PathFillType.WINDING);
path.toggleInverseFillType();
console.info("path fillType = ", path.getFillType());
```

## transform

```TypeScript
transform(matrix: Matrix): void
```

对路径进行矩阵变换。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path = new drawing.Path();
let matrix = new drawing.Matrix();
matrix.setScale(1.5, 1.5, 10.0, 10.0);
const rect: common2D.Rect = {left:100.0, top:100.0, right:500.0, bottom:500.0};
let roundRect = new drawing.RoundRect(rect, 50.0, 50.0);
path.addRoundRect(roundRect, drawing.PathDirection.CLOCKWISE);
path.transform(matrix);
```
