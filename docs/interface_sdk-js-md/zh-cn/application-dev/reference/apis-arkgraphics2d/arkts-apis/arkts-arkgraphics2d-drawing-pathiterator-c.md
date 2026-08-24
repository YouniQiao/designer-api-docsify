# PathIterator

表示路径操作迭代器，可通过遍历迭代器逐段读取路径的操作指令。 迭代器按顺序遍历路径中的操作指令，便于实现对路径的细粒度分析与自定义处理。

> **说明：**&gt;
> - 本Class首批接口从API version 18开始支持。&gt;
> - 本模块使用屏幕物理像素单位px。&gt;
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 23

<!--Device-drawing-class PathIterator--><!--Device-drawing-class PathIterator-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor(path: Path)
```

构造迭代器并绑定路径。

**起始版本：** 23

<!--Device-PathIterator-constructor(path: Path)--><!--Device-PathIterator-constructor(path: Path)-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | Path | 是 | 迭代器绑定的路径对象，绑定后迭代器将遍历该路径中的操作指令， 可通过next、peek、hasNext等方法读取路径的操作类型和坐标数据。 |

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

## hasNext

```TypeScript
hasNext(): boolean
```

判断迭代器中是否还有下一个操作。通常与next()或peek()方法配合使用实现路径遍历。

**起始版本：** 23

<!--Device-PathIterator-hasNext(): boolean--><!--Device-PathIterator-hasNext(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 迭代器是否还有下一个操作可遍历。true表示还有后续路径操作可读取，false表示已遍历至路径末尾，无更多操作。 |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let iter: drawing.PathIterator = new drawing.PathIterator(path);
let res = iter.hasNext();
```

## next

```TypeScript
next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb
```

返回当前路径的下一个操作，并将迭代器推进至该操作，同时将路径坐标点数据按操作类型写入传入的points数组。 若仅需预览下一个操作而不改变迭代器状态，请使用[peek](#peek)。 通常与[hasNext](#hasnext)方法配合使用实现路径遍历。

**起始版本：** 18

<!--Device-PathIterator-next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb--><!--Device-PathIterator-next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| points | Array&lt;common2D.Point&gt; | 是 | 坐标点数组，长度必须至少为偏移量加4，以确保能容纳所有类型的路径数据。操作执行后，该数组会被覆盖。填入的坐标点数量取决于操作类型，其中， MOVE填入1个坐标点，LINE填入2个坐标点，QUAD填入3个坐标点，CONIC填入3个坐标点 + 1个权重值（共3.5组），CUBIC填入4个坐标点，CLOSE和DONE不填入任何点。 |
| offset | number | 否 | 数组中写入位置相对起始点的偏移量，默认为0，取值范围为[0, size-4]，size是指坐标点数组长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) | 当前路径段的操作类型。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(10, 20);
let iter: drawing.PathIterator = new drawing.PathIterator(path);
let verbStr: Array<string> = ['MOVE', 'LINE', 'QUAD', 'CONIC', 'CUBIC', 'CLOSE', 'DONE'];
let pointCount: Array<number> = [1, 2, 3, 4, 4, 0, 0];
let points: Array<common2D.Point> = [{x: 0, y: 0}, {x: 0, y: 0}, {x: 0, y: 0}, {x: 0, y: 0}];
let offset = 0;
let verb = iter.next(points, offset);
let outputMessage: string = 'pathIteratorNext: ';
outputMessage += 'verb =' + verbStr[verb] + '; has ' + pointCount[verb] + ' pairs: ';
for (let j = 0; j < pointCount[verb] + offset; j++) {
  outputMessage += '[' + points[j].x + ', ' + points[j].y + ']';
}
console.info(outputMessage);
```

ArkTS-Sta示例：

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(10.0, 20.0);
let iter: drawing.PathIterator = new drawing.PathIterator(path);
let verbStr: Array<string> = ["MOVE", "LINE", "QUAD", "CONIC", "CUBIC", "CLOSE", "DONE"];
let pointCount: Array<int> = [1,2,3,4,4,0,0]; // 1,2,3,4,4,0,0
let points: Array<common2D.Point> = [{x: 0.0, y: 0.0}, {x: 0.0, y: 0.0}, {x: 0.0, y: 0.0}, {x: 0.0, y: 0.0}];
let offset = 0;
let verb = iter.next(points, offset);
if (verb != undefined) {
  let outputMessage: string = "pathIteratorNext: ";
  outputMessage += "verb =" + verbStr[verb!] + "; has " + pointCount[verb!] + " pairs: ";
  for (let j = 0; j < pointCount[verb!] + offset; j++) {
    outputMessage += "[" + points[j].x + ", " + points[j].y + "]";
  }
  console.info(outputMessage);
}
```

## next

```TypeScript
next(points: Array<common2D.Point>, offset?: int): PathIteratorVerb | undefined
```

返回当前路径的下一个操作，并将迭代器推进至该操作，同时将路径坐标点数据按操作类型写入传入的points数组。 若仅需预览下一个操作而不改变迭代器状态，请使用[peek](#peek)。 通常与[hasNext](#hasnext)方法配合使用实现路径遍历。

**起始版本：** 23

<!--Device-PathIterator-next(points: Array<common2D.Point>, offset?: int): PathIteratorVerb | undefined--><!--Device-PathIterator-next(points: Array<common2D.Point>, offset?: int): PathIteratorVerb | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| points | Array&lt;common2D.Point&gt; | 是 | 坐标点数组，长度必须至少为偏移量加4，以确保能容纳所有类型的路径数据。操作执行后，该数组会被覆盖。填入的坐标点数量取决于操作类型，其中， MOVE填入1个坐标点，LINE填入2个坐标点，QUAD填入3个坐标点，CONIC填入3个坐标点 + 1个权重值（共3.5组），CUBIC填入4个坐标点，CLOSE和DONE不填入任何点。 |
| offset | int | 否 | 数组中写入位置相对起始点的偏移量，默认为0，取值范围为[0, size-4]，size是指坐标点数组长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) \| undefined | 当前路径段的操作类型。创建失败时返回undefined。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**

参见 [next](#next)

## peek

```TypeScript
peek(): PathIteratorVerb
```

返回当前路径的下一个操作，迭代器保持在原操作。与next不同，peek不会推进迭代器位置。

**起始版本：** 18

<!--Device-PathIterator-peek(): PathIteratorVerb--><!--Device-PathIterator-peek(): PathIteratorVerb-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) | 当前路径段的操作类型。 |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let iter: drawing.PathIterator = new drawing.PathIterator(path);
let res = iter.peek();
```

## peek

```TypeScript
peek(): PathIteratorVerb | undefined
```

返回当前路径的下一个操作，迭代器保持在原操作。与next不同，peek不会推进迭代器位置。

**起始版本：** 23

<!--Device-PathIterator-peek(): PathIteratorVerb | undefined--><!--Device-PathIterator-peek(): PathIteratorVerb | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) \| undefined | 当前路径段的操作类型。创建失败时返回undefined。 |

**示例**

参见 [peek](#peek)

