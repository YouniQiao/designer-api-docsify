# Matrix

矩阵对象，用于图形的坐标变换，支持平移、旋转、缩放和倾斜等变换操作。通过矩阵变换可实现不同坐标系之间的映射。表示为3×3的矩阵，如下图所示：矩阵中的元素从左到右，从上到下分别表示水平缩放因子、水平倾斜系数、水平位移系数、垂直倾斜系数、垂直缩放因子、垂直位移系数、x轴透视系数、y轴透视系数、透视缩放因子。设(x&lt;sub&gt;1&lt;/sub&gt;, y&lt;sub&gt;1&lt;/sub&gt;)为源坐标点，(x&lt;sub&gt;2&lt;/sub&gt;, y&lt;sub&gt;2&lt;/sub&gt;)为源坐标点通过矩阵变换后的坐标点，则两个坐标点的关系如下：

> **说明：**&gt;
> - 本Class首批接口从API version 12开始支持。&gt;
> - 本模块使用屏幕物理像素单位px。&gt;
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor()
```

构造一个矩阵对象。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

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
constructor(matrix: Matrix)
```

拷贝一个矩阵。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

**示例**

参见 [constructor](#constructor)

## getAll

```TypeScript
getAll(): Array<number>
```

获取矩阵的所有元素值。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array & lt;number & gt; |

**示例**

```TypeScript
import {drawing} from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
console.info("matrix "+ matrix.getAll());
```

## getAll

```TypeScript
getAll(): Array<double> | undefined
```

获取矩阵的所有元素值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array & lt;double & gt; \ | undefined |

**示例**

参见 [getAll](#getall)

## getValue

ArkTS-Dyn:
```TypeScript
getValue(index: number): number
```

ArkTS-Sta:
```TypeScript
getValue(index: int): double
```

获取矩阵给定索引位的值。索引范围0-8。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：double |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import {drawing} from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
for (let i = 0; i < 9; i++) {
    console.info("matrix "+matrix.getValue(i).toString());
}
```

## invert

```TypeScript
invert(matrix: Matrix): boolean
```

将矩阵matrix设置为当前矩阵的逆矩阵，并返回是否设置成功的结果。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

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

let matrix1 = new drawing.Matrix();
matrix1.setMatrix([2, 1, 3, 1, 2, 1, 3, 1, 2]);
let matrix2 = new drawing.Matrix();
matrix2.setMatrix([-2, 1, 3, 1, 0, -1, 3, -1, 2]);
if (matrix1.invert(matrix2)) {
  console.info("matrix1 is invertible and matrix2 is set as an inverse matrix of the matrix1.");
} else {
  console.info("matrix1 is not invertible and matrix2 is not changed.");
}
```

## isAffine

```TypeScript
isAffine(): boolean
```

判断当前矩阵是否为仿射矩阵。仿射矩阵是一种包括平移、旋转、缩放等变换的矩阵。

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

let matrix = new drawing.Matrix();
matrix.setMatrix([1.0, 0.5, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0]);
let isAffine = matrix.isAffine();
console.info('isAffine :', isAffine);
```

## isEqual

```TypeScript
isEqual(matrix: Matrix): boolean
```

判断两个矩阵是否相等。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

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

## isIdentity

```TypeScript
isIdentity(): boolean
```

判断矩阵是否是单位矩阵。

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

let matrix = new drawing.Matrix();
if (matrix.isIdentity()) {
  console.info("matrix is identity.");
} else {
  console.info("matrix is not identity.");
}
```

## mapPoints

```TypeScript
mapPoints(src: Array<common2D.Point>): Array<common2D.Point>
```

通过矩阵变换将源点数组映射到目标点数组。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Array & lt;common2D.Point & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;common2D.Point & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import {drawing,common2D} from "@kit.ArkGraphics2D";

let src: Array<common2D.Point> = [];
src.push({x: 15, y: 20});
src.push({x: 20, y: 15});
src.push({x: 30, y: 10});
let matrix = new drawing.Matrix();
let dst: Array<common2D.Point> = matrix.mapPoints(src);
console.info("matrix= src: "+JSON.stringify(src));
console.info("matrix= dst: "+JSON.stringify(dst));
```

ArkTS-Sta示例：

```TypeScript
import {drawing,common2D} from "@kit.ArkGraphics2D";

let src: Array<common2D.Point> = [];
src.push({x: 15, y: 20});
src.push({x: 20, y: 15});
src.push({x: 30, y: 10});
let matrix = new drawing.Matrix();
  let dst: Array<common2D.Point> | undefined = matrix!.mapPoints(src);
console.info("matrix= src: "+JSON.stringify(src));
console.info("matrix= dst: "+JSON.stringify(dst));
```

## mapPoints

```TypeScript
mapPoints(src: Array<common2D.Point>): Array<common2D.Point> | undefined
```

通过矩阵变换将源点数组映射到目标点数组。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Array & lt;common2D.Point & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;common2D.Point & gt; \ | undefined |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

参见 [mapPoints](#mappoints)

## mapRadius

ArkTS-Dyn:
```TypeScript
mapRadius(radius: number): number
```

ArkTS-Sta:
```TypeScript
mapRadius(radius: double): double
```

返回半径为radius的圆经过当前矩阵映射形成的椭圆的平均半径。平均半径的平方为椭圆长轴长度和短轴长度的乘积。若当前矩阵包含透视变换，则该结果无意义。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：double |

**示例**

```TypeScript
import { drawing } from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
matrix.setMatrix([2.0, 1.0, 3.0, 1.0, 2.0, 1.0, 3.0, 1.0, 2.0]);
let radius = matrix.mapRadius(10.0);
console.info('radius', radius);
```

## mapRect

```TypeScript
mapRect(dst: common2D.Rect, src: common2D.Rect): boolean
```

将目标矩形设置为源矩形通过矩阵变换后的图形的外接矩形。如下图所示，蓝色矩形为源矩形，假设黄色矩形为源矩形通过矩阵变换形成的图形，此时黄色矩形的边不与坐标轴平行，无法使用矩形对象表示，因此，将目标矩形设置为黄色矩形的外接矩形，即 黑色矩形。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | common2D.Rect | 是 |
| src | common2D.Rect | 是 |

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
import {drawing,common2D} from "@kit.ArkGraphics2D";

let dst: common2D.Rect = { left: 100.0, top: 20.0, right: 130.0, bottom: 60.0 };
let src: common2D.Rect = { left: 100.0, top: 80.0, right: 130.0, bottom: 120.0 };
let matrix = new drawing.Matrix();
if (matrix.mapRect(dst, src)) {
    console.info("matrix= dst "+JSON.stringify(dst));
}
```

## postConcat

```TypeScript
postConcat(matrix: Matrix): void
```

将一个矩阵乘在当前矩阵的左侧，即新的变换在当前矩阵的变换之后应用。如果需要在当前矩阵的变换之前应用新变换，使用preConcat方法。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
if (matrix.isIdentity()) {
  console.info("matrix is identity.");
} else {
  console.info("matrix is not identity.");
}
let matrix1 = new drawing.Matrix();
matrix1.setMatrix([2.0, 1.0, 3.0, 1.0, 2.0, 1.0, 3.0, 1.0, 2.0]);
let matrix2 = new drawing.Matrix();
matrix2.setMatrix([-2.0, 1.0, 3.0, 1.0, 0.0, -1.0, 3.0, -1.0, 2.0]);
matrix1.postConcat(matrix2);
```

## postRotate

ArkTS-Dyn:
```TypeScript
postRotate(degree: number, px: number, py: number): void
```

ArkTS-Sta:
```TypeScript
postRotate(degree: double, px: double, py: double): void
```

将矩阵设置为矩阵右乘围绕旋转中心点旋转degree角度的单位矩阵后得到的矩阵，即新的旋转变换在当前矩阵的变换之后应用。如果需要在当前矩阵的变换之前应用旋转变换，使用preRotate方法。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| degree | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| py | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import {drawing} from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let degree: number = 2;
let px: number = 3;
let py: number = 4;
matrix.postRotate(degree, px, py);
console.info("matrix= "+matrix.getAll().toString());
```

ArkTS-Sta示例：

```TypeScript
import {drawing} from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let degree: double = 2.0;
let px: double = 3.0;
let py: double = 4.0;
matrix.postRotate(degree, px, py);
if (matrix.getAll() != undefined) {
  console.info("matrix= "+matrix.getAll()!.toString());
}
```

## postScale

ArkTS-Dyn:
```TypeScript
postScale(sx: number, sy: number, px: number, py: number): void
```

ArkTS-Sta:
```TypeScript
postScale(sx: double, sy: double, px: double, py: double): void
```

将矩阵设置为矩阵右乘围绕缩放中心点按sx和sy缩放系数缩放后的单位矩阵后得到的矩阵，即新的缩放变换在当前矩阵的变换之后应用。如果需要在当前矩阵的变换之前应用缩放变换，使用preScale方法。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sx | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| sy | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| py | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import {drawing} from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let sx: number = 2;
let sy: number = 0.5;
let px: number = 1;
let py: number = 1;
matrix.postScale(sx, sy, px, py);
console.info("matrix= "+matrix.getAll().toString());
```

ArkTS-Sta示例：

```TypeScript
import {drawing} from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let sx: double = 2.0;
let sy: double = 0.5;
let px: double = 1.0;
let py: double = 1.0;
matrix.postScale(sx, sy, px, py);
if (matrix.getAll() != undefined) {
  console.info("matrix= "+matrix.getAll()!.toString());
}
```

## postSkew

ArkTS-Dyn:
```TypeScript
postSkew(kx: number, ky: number, px: number, py: number): void
```

ArkTS-Sta:
```TypeScript
postSkew(kx: double, ky: double, px: double, py: double): void
```

当前矩阵右乘一个倾斜变换矩阵。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| kx | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| ky | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| py | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**示例**

```TypeScript
import { drawing } from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
matrix.postSkew(2.0, 1.0, 2.0, 1.0);
```

## postTranslate

ArkTS-Dyn:
```TypeScript
postTranslate(dx: number, dy: number): void
```

ArkTS-Sta:
```TypeScript
postTranslate(dx: double, dy: double): void
```

将矩阵设置为矩阵右乘平移dx和dy距离后的单位矩阵后得到的矩阵，即新的平移变换在当前矩阵的变换之后应用。如果需要在当前矩阵的变换之前应用平移变换，使用preTranslate方法。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

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

ArkTS-Dyn示例：

```TypeScript
import {drawing} from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let dx: number = 3;
let dy: number = 4;
matrix.postTranslate(dx, dy);
console.info("matrix= "+matrix.getAll().toString());
```

ArkTS-Sta示例：

```TypeScript
import {drawing} from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let dx: double = 3.0;
let dy: double = 4.0;
matrix.postTranslate(dx, dy);
if (matrix.getAll() != undefined) {
  console.info("matrix= "+matrix.getAll()!.toString());
}
```

## preConcat

```TypeScript
preConcat(matrix: Matrix): void
```

将一个矩阵乘在当前矩阵的右侧，即新的变换在当前矩阵的变换之前应用。如果需要在当前矩阵的变换之后应用新变换，使用postConcat方法。

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
import { drawing } from '@kit.ArkGraphics2D';

let matrix1 = new drawing.Matrix();
matrix1.setMatrix([2.0, 1.0, 3.0, 1.0, 2.0, 1.0, 3.0, 1.0, 2.0]);
let matrix2 = new drawing.Matrix();
matrix2.setMatrix([-2.0, 1.0, 3.0, 1.0, 0.0, -1.0, 3.0, -1.0, 2.0]);
matrix1.preConcat(matrix2);
```

## preRotate

ArkTS-Dyn:
```TypeScript
preRotate(degree: number, px: number, py: number): void
```

ArkTS-Sta:
```TypeScript
preRotate(degree: double, px: double, py: double): void
```

将矩阵设置为矩阵左乘围绕旋转中心点旋转degree角度的单位矩阵后得到的矩阵，即新的旋转变换在当前矩阵的变换之前应用。如果需要在当前矩阵的变换之后应用旋转变换，使用postRotate方法。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| degree | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| py | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import {drawing} from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let degree: number = 2;
let px: number = 3;
let py: number = 4;
matrix.preRotate(degree, px, py);
console.info("matrix= "+matrix.getAll().toString());
```

ArkTS-Sta示例：

```TypeScript
import {drawing} from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let degree: double = 2.0;
let px: double = 3.0;
let py: double = 4.0;
matrix.preRotate(degree, px, py);
if (matrix.getAll() != undefined) {
  console.info("matrix= "+matrix.getAll()!.toString());
}
```

## preScale

ArkTS-Dyn:
```TypeScript
preScale(sx: number, sy: number, px: number, py: number): void
```

ArkTS-Sta:
```TypeScript
preScale(sx: double, sy: double, px: double, py: double): void
```

将矩阵设置为矩阵左乘围绕缩放中心点按sx和sy缩放系数缩放后的单位矩阵后得到的矩阵，即新的缩放变换在当前矩阵的变换之前应用。如果需要在当前矩阵的变换之后应用缩放变换，使用postScale方法。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sx | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| sy | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| py | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import {drawing} from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let sx: number = 2;
let sy: number = 0.5;
let px: number = 1;
let py: number = 1;
matrix.preScale(sx, sy, px, py);
console.info("matrix"+matrix.getAll().toString());
```

ArkTS-Sta示例：

```TypeScript
import {drawing} from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let sx: double = 2.0;
let sy: double = 0.5;
let px: double = 1.0;
let py: double = 1.0;
matrix.preScale(sx, sy, px, py);
if (matrix.getAll() != undefined) {
  console.info("matrix= "+matrix.getAll()!.toString());
}
```

## preSkew

ArkTS-Dyn:
```TypeScript
preSkew(kx: number, ky: number, px: number, py: number): void
```

ArkTS-Sta:
```TypeScript
preSkew(kx: double, ky: double, px: double, py: double): void
```

当前矩阵左乘一个倾斜变换矩阵。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| kx | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| ky | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| py | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**示例**

```TypeScript
import { drawing } from "@kit.ArkGraphics2D";
let matrix = new drawing.Matrix();
matrix.preSkew(2.0, 1.0, 2.0, 1.0);
```

## preTranslate

ArkTS-Dyn:
```TypeScript
preTranslate(dx: number, dy: number): void
```

ArkTS-Sta:
```TypeScript
preTranslate(dx: double, dy: double): void
```

将矩阵设置为矩阵左乘平移dx和dy距离后的单位矩阵后得到的矩阵，即新的平移变换在当前矩阵的变换之前应用。如果需要在当前矩阵的变换之后应用平移变换，使用postTranslate方法。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

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

ArkTS-Dyn示例：

```TypeScript
import {drawing} from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let dx: number = 3;
let dy: number = 4;
matrix.preTranslate(dx, dy);
console.info("matrix"+matrix.getAll().toString());
```

ArkTS-Sta示例：

```TypeScript
import {drawing} from "@kit.ArkGraphics2D";

let matrix = new drawing.Matrix();
let dx: double = 3.0;
let dy: double = 4.0;
matrix.preTranslate(dx, dy);
if (matrix.getAll() != undefined) {
  console.info("matrix= "+matrix.getAll()!.toString());
}
```

## rectStaysRect

```TypeScript
rectStaysRect(): boolean
```

判断经过该矩阵映射后的矩形的形状是否仍为矩形。

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

let matrix = new drawing.Matrix();
matrix.setMatrix([1.0, 0.5, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0]);
let matrix2 = new drawing.Matrix(matrix);
let isRect = matrix2.rectStaysRect();
console.info('isRect :', isRect);
```

## reset

```TypeScript
reset(): void
```

重置当前矩阵为单位矩阵。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

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

## setConcat

```TypeScript
setConcat(matrixA: Matrix, matrixB: Matrix): void
```

用两个矩阵的乘积更新当前矩阵，即当前矩阵 = matrixA × matrixB。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrixA | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |
| matrixB | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix1 = new drawing.Matrix();
matrix1.setMatrix([2.0, 1.0, 3.0, 1.0, 2.0, 1.0, 3.0, 1.0, 2.0]);
let matrix2 = new drawing.Matrix();
matrix2.setMatrix([-2.0, 1.0, 3.0, 1.0, 0.0, -1.0, 3.0, -1.0, 2.0]);
matrix1.setConcat(matrix2, matrix1);
```

## setMatrix

ArkTS-Dyn:
```TypeScript
setMatrix(values: Array<number>): void
```

ArkTS-Sta:
```TypeScript
setMatrix(values: Array<double>): void
```

设置矩阵对象的各项参数。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| values | ArkTS-Dyn: Array & lt;number & gt;<br>ArkTS-Sta：Array & lt;double & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let matrix = new drawing.Matrix();
    matrix.setMatrix([5, 0, 0, 0, 1, 1, 0, 0, 1]);
    canvas.setMatrix(matrix);
    canvas.drawRect({left: 10, right: 200, top: 100, bottom: 500});
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
    let matrix = new drawing.Matrix()
    matrix.setMatrix([5.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0]);
    canvas.setMatrix(matrix);
    canvas.drawRect({left: 10.0, right: 200.0, top: 100.0, bottom: 500.0});
  }
}
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
let value: Array<double> = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0];
matrix.setMatrix(value);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix1 = new drawing.Matrix();
matrix1.setMatrix([2.0, 1.0, 3.0, 1.0, 2.0, 1.0, 3.0, 1.0, 2.0]);
let matrix2 = new drawing.Matrix();
matrix1.setMatrix(matrix2);
```

## setMatrix

ArkTS-Dyn:
```TypeScript
setMatrix(matrix: Array<number> | Matrix): void
```

ArkTS-Sta:
```TypeScript
setMatrix(matrix: Array<double> | Matrix): void
```

用一个矩阵对当前矩阵进行更新。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | ArkTS-Dyn: Array & lt;number & gt; \ | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md)  <br>ArkTS-Sta：Array&lt;double&gt; \| [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

**示例**

参见 [setMatrix](#setmatrix)

## setPolyToPoly

ArkTS-Dyn:
```TypeScript
setPolyToPoly(src: Array<common2D.Point>, dst: Array<common2D.Point>, count: number): boolean
```

ArkTS-Sta:
```TypeScript
setPolyToPoly(src: Array<common2D.Point>, dst: Array<common2D.Point>, count: int): boolean
```

将当前矩阵设置为能够将源点数组映射到目标点数组的变换矩阵。源点和目标点的个数必须大于等于0，小于等于4。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Array & lt;common2D.Point & gt; | 是 |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | Array & lt;common2D.Point & gt; | 是 |
| count | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import {drawing,common2D} from "@kit.ArkGraphics2D";

let srcPoints: Array<common2D.Point> = [ {x: 10, y: 20}, {x: 200, y: 150} ];
let dstPoints: Array<common2D.Point> = [{ x:0, y: 10 }, { x:300, y: 600 }];
let matrix = new drawing.Matrix();
if (matrix.setPolyToPoly(srcPoints, dstPoints, 2)) {
    console.info("matrix"+matrix.getAll().toString());
}
```

ArkTS-Sta示例：

```TypeScript
import {drawing,common2D} from "@kit.ArkGraphics2D";

let srcPoints: Array<common2D.Point> = [ {x: 10.0, y: 20.0}, {x: 200.0, y: 150.0} ];
let dstPoints: Array<common2D.Point> = [{ x:0.0, y: 10.0 }, { x:300.0, y: 600.0 }];
let matrix = new drawing.Matrix();
if (matrix.setPolyToPoly(srcPoints, dstPoints, 2) && matrix.getAll() != undefined) {
  console.info("matrix"+matrix.getAll()!.toString());
}
```

## setRectToRect

```TypeScript
setRectToRect(src: common2D.Rect, dst: common2D.Rect, scaleToFit: ScaleToFit): boolean
```

将当前矩阵设置为能使源矩形映射到目标矩形的变换矩阵。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | common2D.Rect | 是 |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | common2D.Rect | 是 |
| scaleToFit | [ScaleToFit](arkts-arkgraphics2d-drawing-scaletofit-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import {drawing,common2D} from "@kit.ArkGraphics2D";

let src: common2D.Rect = { left: 100, top: 100, right: 300, bottom: 300 };
let dst: common2D.Rect = { left: 200, top: 200, right: 600, bottom: 600 };
let scaleToFit: drawing.ScaleToFit = drawing.ScaleToFit.FILL_SCALE_TO_FIT;
let matrix = new drawing.Matrix();
if (matrix.setRectToRect(src, dst, scaleToFit)) {
    console.info("matrix"+matrix.getAll().toString());
}
```

ArkTS-Sta示例：

```TypeScript
import {drawing,common2D} from "@kit.ArkGraphics2D";

let src: common2D.Rect = { left: 100.0, top: 100.0, right: 300.0, bottom: 300.0 };
let dst: common2D.Rect = { left: 200.0, top: 200.0, right: 600.0, bottom: 600.0 };
let scaleToFit: drawing.ScaleToFit = drawing.ScaleToFit.FILL_SCALE_TO_FIT
let matrix = new drawing.Matrix();
if (matrix.setRectToRect(src, dst, scaleToFit) && matrix.getAll() != undefined) {
  console.info("matrix"+matrix.getAll()!.toString());
}
```

## setRotation

ArkTS-Dyn:
```TypeScript
setRotation(degree: number, px: number, py: number): void
```

ArkTS-Sta:
```TypeScript
setRotation(degree: double, px: double, py: double): void
```

设置矩阵为单位矩阵，并围绕旋转中心点(px, py)进行旋转。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| degree | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| py | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
matrix.setRotation(90.0, 100.0, 100.0);
```

## setScale

ArkTS-Dyn:
```TypeScript
setScale(sx: number, sy: number, px: number, py: number): void
```

ArkTS-Sta:
```TypeScript
setScale(sx: double, sy: double, px: double, py: double): void
```

设置矩阵为单位矩阵，并围绕缩放中心点(px, py)按sx和sy进行缩放。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sx | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| sy | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| py | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
matrix.setScale(100.0, 100.0, 150.0, 150.0);
```

## setSinCos

ArkTS-Dyn:
```TypeScript
setSinCos(sinValue: number, cosValue: number, px: number, py: number): void
```

ArkTS-Sta:
```TypeScript
setSinCos(sinValue: double, cosValue: double, px: double, py: double): void
```

设置矩阵为单位矩阵，使其围绕旋转中心点(px, py)以指定的正弦值和余弦值旋转。与[setRotation](#setrotation)功能类似，但setRotation直接传入角度 值，而本方法传入正弦值和余弦值。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sinValue | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| cosValue | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| py | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
matrix.setMatrix([1.0, 0.5, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0]);
matrix.setSinCos(0.0, 1.0, 1.0, 0.0);
```

## setSkew

ArkTS-Dyn:
```TypeScript
setSkew(kx: number, ky: number, px: number, py: number): void
```

ArkTS-Sta:
```TypeScript
setSkew(kx: double, ky: double, px: double, py: double): void
```

设置矩阵为单位矩阵，并围绕倾斜中心点(px, py)按(kx, ky)进行倾斜变换。与[setRotation](#setrotation)、 [setScale](#setscale)、[setTranslation](#settranslation)类似，均为重置矩阵后施加单一变换。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| kx | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| ky | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| [px](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| py | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
matrix.setMatrix([1.0, 0.5, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0]);
matrix.setSkew(2.0, 0.5, 0.5, 2.0);
```

## setTranslation

ArkTS-Dyn:
```TypeScript
setTranslation(dx: number, dy: number): void
```

ArkTS-Sta:
```TypeScript
setTranslation(dx: double, dy: double): void
```

设置矩阵为单位矩阵，并平移(dx, dy)。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

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

let matrix = new drawing.Matrix();
matrix.setTranslation(100.0, 100.0);
```
