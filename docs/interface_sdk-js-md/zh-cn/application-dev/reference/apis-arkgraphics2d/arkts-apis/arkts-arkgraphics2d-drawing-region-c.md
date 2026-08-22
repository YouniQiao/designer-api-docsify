# Region

区域对象，用于描述所绘制图形的区域信息。Region支持设置矩形区域和路径区域，提供区域间的合并运算、相交判断、平移、边界获取等操作。

> **说明：**
> 
> - 本Class首批接口从API version 12开始支持。
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 23

<!--Device-drawing-class Region--><!--Device-drawing-class Region-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor()
```

构造一个区域对象。

**起始版本：** 23

<!--Device-Region-constructor()--><!--Device-Region-constructor()-End-->

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
constructor(region: Region)
```

拷贝一个区域对象。

**起始版本：** 23

<!--Device-Region-constructor(region: Region)--><!--Device-Region-constructor(region: Region)-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | Region | 是 | 用于拷贝的区域。 |

**示例**

参见 [constructor](#constructor)

## constructor

```TypeScript
constructor(left: int, top: int, right: int, bottom: int)
```

构造矩形区域。

**起始版本：** 23

<!--Device-Region-constructor(left: int, top: int, right: int, bottom: int)--><!--Device-Region-constructor(left: int, top: int, right: int, bottom: int)-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| left | int | 是 | 矩形区域的左侧位置（矩形左上角横坐标）。该参数必须为整数。0表示坐标原点，负数表示位于坐标原点左侧，正数表示位于坐标原点右侧。单位为物理像素px。 |
| top | int | 是 | 矩形区域的顶部位置（矩形左上角纵坐标）。该参数必须为整数。0表示坐标原点，负数表示位于坐标原点上侧，正数表示位于坐标原点下侧。单位为物理像素px。 |
| right | int | 是 | 矩形区域的右侧位置（矩形右下角横坐标）。该参数必须为整数。0表示坐标原点，负数表示位于坐标原点左侧，正数表示位于坐标原点右侧。单位为物理像素px。 |
| bottom | int | 是 | 矩形区域的底部位置（矩形右下角纵坐标）。该参数必须为整数。0表示坐标原点，负数表示位于坐标原点上侧，正数表示位于坐标原点下侧。单位为物理像素px。 |

**示例**

参见 [constructor](#constructor)

## getBoundaryPath

```TypeScript
getBoundaryPath(): Path
```

返回一个新路径，该路径取自当前区域的边界。

**起始版本：** 20

<!--Device-Region-getBoundaryPath(): Path--><!--Device-Region-getBoundaryPath(): Path-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Path | 返回当前区域边界的路径。 |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
let region = new drawing.Region();
let path = region.getBoundaryPath();
```

## getBoundaryPath

```TypeScript
getBoundaryPath(): Path | undefined
```

返回一个新路径，该路径取自当前区域的边界。

**起始版本：** 24

<!--Device-Region-getBoundaryPath(): Path | undefined--><!--Device-Region-getBoundaryPath(): Path | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Path \| undefined | 返回当前区域边界的路径。 |

**示例**

参见 [getBoundaryPath](#getboundarypath)

## getBounds

```TypeScript
getBounds(): common2D.Rect
```

获取区域的边界。

**起始版本：** 20

<!--Device-Region-getBounds(): common2D.Rect--><!--Device-Region-getBounds(): common2D.Rect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common2D.Rect | 返回当前区域的边界矩形。 |

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

获取区域的边界。

**起始版本：** 24

<!--Device-Region-getBounds(): common2D.Rect | undefined--><!--Device-Region-getBounds(): common2D.Rect | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common2D.Rect \| undefined | 返回当前区域的边界矩形。 |

**示例**

参见 [getBounds](#getbounds)

## isComplex

```TypeScript
isComplex(): boolean
```

判断当前区域是否包含多个矩形。

**起始版本：** 24

<!--Device-Region-isComplex(): boolean--><!--Device-Region-isComplex(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回当前区域是否包含多个矩形的结果。true表示当前区域包含多个矩形，false表示当前区域不包含多个矩形。 |

**示例**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';
import { RenderNode, DrawContext } from '@kit.ArkUI';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    pen.setStrokeWidth(10);
    canvas.attachPen(pen);
    let region = new drawing.Region();
    region.setRect(100, 100, 200, 200);
    region.op(new drawing.Region(220, 200, 280, 280), drawing.RegionOp.UNION);
    let flag: boolean = false;
    flag = region.isComplex();
    console.info('flag :', flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断当前区域是否为空。

**起始版本：** 24

<!--Device-Region-isEmpty(): boolean--><!--Device-Region-isEmpty(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回当前区域是否为空的结果。true表示当前区域为空，false表示当前区域不为空。 |

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
isEqual(other: Region): boolean
```

判断指定区域是否与当前区域相等。

**起始版本：** 24

<!--Device-Region-isEqual(other: Region): boolean--><!--Device-Region-isEqual(other: Region): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Region | 是 | 用于与当前区域进行比较的其他区域对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回其他区域是否与当前区域相等的结果。true表示相等，false表示不相等。 |

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

## isPointContained

```TypeScript
isPointContained(x: int, y:int): boolean
```

判断测试点是否在区域内。

**起始版本：** 23

<!--Device-Region-isPointContained(x: int, y:int): boolean--><!--Device-Region-isPointContained(x: int, y:int): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | int | 是 | 测试点的x轴坐标。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| y | int | 是 | 测试点的y轴坐标。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回测试点是否在区域内的结果。true表示测试点在区域内，false表示测试点不在区域内。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**示例**

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
    region.setRect(100, 100, 400, 400);
    let flag: boolean = false;
    flag = region.isPointContained(200,200);
    console.info("region isPointContained : " + flag);
    canvas.drawPoint(200,200);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

## isRect

```TypeScript
isRect(): boolean
```

判断当前区域是否等同于单个矩形。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Region-isRect(): boolean--><!--Device-Region-isRect(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回当前区域是否等同于单个矩形的结果。true表示当前区域等同于单个矩形，false表示当前区域不等同于单个矩形。 |

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

## isRegionContained

```TypeScript
isRegionContained(other: Region): boolean
```

判断其他区域是否在当前区域内。

**起始版本：** 23

<!--Device-Region-isRegionContained(other: Region): boolean--><!--Device-Region-isRegionContained(other: Region): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Region | 是 | 用于判断是否在当前区域内的其他区域对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回其他区域是否在当前区域内的结果。true表示其他区域在当前区域内，false表示其他区域不在当前区域内。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**示例**

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
    let other = new drawing.Region();
    region.setRect(100, 100, 400, 400);
    other.setRect(150, 150, 250 ,250);
    let flag: boolean = false;
    flag = region.isRegionContained(other);
    console.info("region isRegionContained : " + flag);
    canvas.drawRegion(region);
    canvas.drawRegion(other);
    canvas.detachPen();
  }
}
```

## offset

```TypeScript
offset(dx: int, dy: int): void
```

对区域进行平移。

**起始版本：** 24

<!--Device-Region-offset(dx: int, dy: int): void--><!--Device-Region-offset(dx: int, dy: int): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dx | int | 是 | x轴方向平移量，正数往x轴正方向平移，负数往x轴负方向平移，该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| dy | int | 是 | y轴方向平移量，正数往y轴正方向平移，负数往y轴负方向平移，该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |

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

## op

```TypeScript
op(region: Region, regionOp: RegionOp): boolean
```

将当前区域与指定区域进行运算，并替换为运算结果。

**起始版本：** 23

<!--Device-Region-op(region: Region, regionOp: RegionOp): boolean--><!--Device-Region-op(region: Region, regionOp: RegionOp): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | Region | 是 | 用于与当前区域进行运算的指定区域对象。 |
| regionOp | [RegionOp](arkts-arkgraphics2d-drawing-regionop-e.md) | 是 | 区域运算操作类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回区域运算结果是否成功替换当前区域的结果。true表示区域运算结果替换当前区域成功，false表示区域运算结果替换当前区域失败。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

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

## quickContains

```TypeScript
quickContains(left: int, top: int, right: int, bottom: int): boolean
```

判断当前区域是否等同于单个矩形并且包含指定矩形。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Region-quickContains(left: int, top: int, right: int, bottom: int): boolean--><!--Device-Region-quickContains(left: int, top: int, right: int, bottom: int): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| left | int | 是 | 矩形区域的左侧位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| top | int | 是 | 矩形区域的顶部位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| right | int | 是 | 矩形区域的右侧位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| bottom | int | 是 | 矩形区域的底部位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回判断结果。true表示当前区域等同于单个矩形且包含指定矩形，false表示当前区域不等同于单个矩形或不包含指定矩形。 |

**示例**

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
    flag = region.quickContains(10, 10, 100, 100);
    console.info('flag :', flag);
    let other = new drawing.Region();
    other.setRect(100, 100, 200, 200);
    flag = other.quickContains(10, 10, 100, 100);
    console.info('flag :', flag);
    canvas.drawRegion(region);
    canvas.drawRegion(other);
    canvas.detachPen();
  }
}
```

## quickReject

```TypeScript
quickReject(left: int, top: int, right: int, bottom: int): boolean
```

快速判断矩形和区域是否不相交。实际上比较的是矩形和区域的外接矩形是否不相交，因此当外接矩形相交但实际区域不相交时，会返回false（即误判为相交）。

**起始版本：** 23

<!--Device-Region-quickReject(left: int, top: int, right: int, bottom: int): boolean--><!--Device-Region-quickReject(left: int, top: int, right: int, bottom: int): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| left | int | 是 | 矩形区域的左侧位置（矩形左上角横坐标）。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| top | int | 是 | 矩形区域的顶部位置（矩形左上角纵坐标）。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| right | int | 是 | 矩形区域的右侧位置（矩形右下角横坐标）。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| bottom | int | 是 | 矩形区域的底部位置（矩形右下角纵坐标）。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回矩形是否与区域不相交的结果。true表示矩形与区域不相交，false表示矩形与区域相交。当矩形与区域仅点或边相交时，也返回true。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**示例**

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
    region.setRect(100, 100, 400, 400);
    let flag: boolean = false;
    flag = region.quickReject(50, 50, 70, 70);
    console.info("region quickReject : " + flag);
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
    region.setRect(100, 100, 400, 400);
    let flag: boolean = false;
    flag = region.quickReject(50, 50, 70, 70);
    console.info("region quickReject : " + flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

## quickRejectRegion

```TypeScript
quickRejectRegion(region: Region): boolean
```

判断当前区域是否与指定区域不相交。实际上比较的是两个区域的外接矩形是否不相交，因此当外接矩形相交但实际区域不相交时，会返回false（即误判为相交）。

**起始版本：** 24

<!--Device-Region-quickRejectRegion(region: Region): boolean--><!--Device-Region-quickRejectRegion(region: Region): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | Region | 是 | 用于判断是否与当前区域不相交的指定区域对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回当前区域与另一个区域是否不相交的结果。true表示不相交，false表示相交。当两个区域仅点或边相交时，也返回true。 |

**示例**

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
    let region2 = new drawing.Region();
    region2.setRect(100, 100, 400, 400);
    let flag: boolean = false;
    flag = region.quickRejectRegion(region2);
    console.info("region quickRejectRegion: " + flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

## setEmpty

```TypeScript
setEmpty(): void
```

设置当前区域为空。

**起始版本：** 23

<!--Device-Region-setEmpty(): void--><!--Device-Region-setEmpty(): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10, 20, 20, 30);
drawing.RectUtils.setEmpty(rect);
console.info('rect.left: ', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10.0, 20.0, 20.0, 30.0);
if (rect == undefined) {
    return;
}
drawing.RectUtils.setEmpty(rect)
console.info('rect.left:', rect?.left);
console.info('rect.top: ', rect?.top);
console.info('rect.right: ', rect?.right);
console.info('rect.bottom: ', rect?.bottom);
```

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    let region = new drawing.Region();
    region.setRect(100, 100, 200, 200);
    let isEmpty = region.isEmpty();
    console.info("isEmpty :" + isEmpty);
    region.setEmpty();
    isEmpty = region.isEmpty();
    console.info("isEmpty :" + isEmpty);
  }
}
```

## setPath

```TypeScript
setPath(path: Path, clip: Region): boolean
```

设置一个与裁剪区域内路径轮廓相匹配的区域。

**起始版本：** 23

<!--Device-Region-setPath(path: Path, clip: Region): boolean--><!--Device-Region-setPath(path: Path, clip: Region): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | Path | 是 | 用于设置区域轮廓的路径对象。 |
| clip | Region | 是 | 裁剪区域对象，用于限定路径轮廓的有效范围，仅路径在裁剪区域内的部分会被用于设置区域。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回设置区域是否成功的结果。true表示设置成功，false表示设置失败。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**示例**

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
    let path = new drawing.Path();
    region.setRect(100, 100, 400, 400);
    path.arcTo(50, 50, 300, 300, 0, 359);
    let flag: boolean = false;
    flag = region.setPath(path,region);
    console.info("region setPath : " + flag);
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
    let path = new drawing.Path();
    region.setRect(100, 100, 400, 400);
    path.arcTo(50.0, 50.0, 300.0, 300.0, 0.0, 359.0);
    let flag: boolean = false;
    flag = region.setPath(path,region);
    console.info("region setPath : " + flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

## setRect

```TypeScript
setRect(left: int, top: int, right: int, bottom: int): boolean
```

设置一个矩形区域。

**起始版本：** 23

<!--Device-Region-setRect(left: int, top: int, right: int, bottom: int): boolean--><!--Device-Region-setRect(left: int, top: int, right: int, bottom: int): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| left | int | 是 | 矩形区域的左侧位置（矩形左上角横坐标）。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| top | int | 是 | 矩形区域的顶部位置（矩形左上角纵坐标）。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| right | int | 是 | 矩形区域的右侧位置（矩形右下角横坐标）。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| bottom | int | 是 | 矩形区域的底部位置（矩形右下角纵坐标）。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回设置矩形区域是否成功的结果。true表示设置矩形区域成功，false表示设置矩形区域失败。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10, 20, 30, 40);
let rect2 = drawing.RectUtils.makeEmpty();
drawing.RectUtils.setRect(rect2, rect);
console.info('rect2.left: ', rect2.left);
console.info('rect2.top: ', rect2.top);
console.info('rect2.right: ', rect2.right);
console.info('rect2.bottom: ', rect2.bottom);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10.0, 20.0, 30.0, 40.0);
let rect2 = drawing.RectUtils.makeEmpty();
if (rect == undefined || rect2 == undefined) {
    return;
}
drawing.RectUtils.setRect(rect2, rect);
console.info('rect2.left:', rect2.left);
console.info('rect2.top: ', rect2.top);
console.info('rect2.right: ', rect2.right);
console.info('rect2.bottom: ', rect2.bottom);
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
    let flag: boolean = false;
    flag = region.setRect(50, 50, 300, 300);
    console.info("region setRect : " + flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { RenderNode, DrawContext } from '@ohos.arkui.node';
import drawing from "@ohos.graphics.drawing";
import common2D from "@ohos.graphics.common2D";

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    pen.setStrokeWidth(10.0);
    canvas.attachPen(pen);
    let region = new drawing.Region();
    let flag: boolean = false;
    flag = region.setRect(50, 50, 300, 300);
    console.info("region setRect : " + flag);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

## setRegion

```TypeScript
setRegion(region: Region): void
```

设置当前区域为指定区域。

**起始版本：** 24

<!--Device-Region-setRegion(region: Region): void--><!--Device-Region-setRegion(region: Region): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| region | Region | 是 | 用于设置当前区域内容的源区域对象。 |

**示例**

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
    region.setRect(100, 100, 200, 200);
    let region2 = new drawing.Region();
    region2.setRegion(region);
    canvas.drawRegion(region2);
    canvas.detachPen();
  }
}
```

