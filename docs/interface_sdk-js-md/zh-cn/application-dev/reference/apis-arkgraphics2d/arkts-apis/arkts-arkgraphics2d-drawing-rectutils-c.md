# RectUtils

提供处理矩形的工具，支持矩形的快速构建与基本属性获取、边界计算与调整、平移与状态判断、边界规范化等功能。主要的使用场景：
1. 矩形快速构建与获取基本属性，如构造新矩形、拷贝矩形、获取矩形的宽高以及中心点等。
2. 边界计算与调整，如判断包含关系、计算与更新矩形之间交集和并集，更新边界值等。
3. 矩形平移与状态判断，如对矩形进行平移、将矩形平移到指定位置、判断矩形是否为空以及判断两个矩形是否相等。
4. 矩形边界规范化，如对存在反转情况的矩形边界值进行交换排序等。

> **说明：**&gt;
> - 本Class首批接口从API version 20开始支持。&gt;
> - 本模块使用屏幕物理像素单位px。&gt;
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## centerX

ArkTS-Dyn:
```TypeScript
static centerX(rect: common2D.Rect): number
```

ArkTS-Sta:
```TypeScript
static centerX(rect: common2D.Rect): double
```

获取矩形中心的x轴坐标，中心x轴坐标为矩形左边界与右边界之和的一半。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：double |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(20, 30, 30, 40);
let x = drawing.RectUtils.centerX(rect);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(20.0, 30.0, 30.0, 40.0);
if (rect == undefined) {
    return;
}
let x = drawing.RectUtils.centerX(rect);
```

## centerY

ArkTS-Dyn:
```TypeScript
static centerY(rect: common2D.Rect): number
```

ArkTS-Sta:
```TypeScript
static centerY(rect: common2D.Rect): double
```

获取矩形中心的y轴坐标，中心y轴坐标为矩形上边界与下边界之和的一半。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：double |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(20, 30, 30, 40);
let y = drawing.RectUtils.centerY(rect);
```

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(20.0, 30.0, 30.0, 40.0);
if (rect == undefined) {
    return;
}
let x = drawing.RectUtils.centerY(rect);
```

## contains

```TypeScript
static contains(rect: common2D.Rect, other: common2D.Rect): boolean
```

判断一个矩形是否完全包含另外一个矩形。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| other | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

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

## contains

ArkTS-Dyn:
```TypeScript
static contains(rect: common2D.Rect, left: number, top: number, right: number, bottom: number): boolean
```

ArkTS-Sta:
```TypeScript
static contains(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): boolean
```

判断一个矩形是否完全包含另外一个矩形（另一个矩形分别用左上右下坐标表示）。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| left | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| top | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| right | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| bottom | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

参见 [contains](#contains)

## contains

ArkTS-Dyn:
```TypeScript
static contains(rect: common2D.Rect, x: number, y: number): boolean
```

ArkTS-Sta:
```TypeScript
static contains(rect: common2D.Rect, x: double, y: double): boolean
```

判断一个矩形是否完全包含一个点。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

参见 [contains](#contains)

## getHeight

ArkTS-Dyn:
```TypeScript
static getHeight(rect: common2D.Rect): number
```

ArkTS-Sta:
```TypeScript
static getHeight(rect: common2D.Rect): double
```

获取矩形的高度。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：double |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let height = canvas.getHeight();
    console.info('get canvas height:' + height);
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
    let height = canvas.getHeight();
    console.info('get canvas height:' + height);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10, 10, 20, 20);
let height = drawing.RectUtils.getHeight(rect);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10.0, 10.0, 20.0, 20.0);
if (rect == undefined) {
    return;
}
let height = drawing.RectUtils.getHeight(rect);
```

## getWidth

ArkTS-Dyn:
```TypeScript
static getWidth(rect: common2D.Rect): number
```

ArkTS-Sta:
```TypeScript
static getWidth(rect: common2D.Rect): double
```

获取矩形的宽度。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：double |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let width = canvas.getWidth();
    console.info('get canvas width:' + width);
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
    let width = canvas.getWidth();
    console.info('get canvas width:' + width);
  }
}
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
let width = pen.getWidth();
```

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10, 10, 20, 20);
let width = drawing.RectUtils.getWidth(rect);
console.info('width:', width);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10.0, 10.0, 20.0, 20.0);
if (rect == undefined) {
    return;
}
let width = drawing.RectUtils.getWidth(rect);
console.info('width:', width);
```

## inset

ArkTS-Dyn:
```TypeScript
static inset(rect: common2D.Rect, left: number, top: number, right: number, bottom: number): void
```

ArkTS-Sta:
```TypeScript
static inset(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): void
```

将指定矩形的左边界、上边界、右边界和下边界分别和传入的“左上右下”的值相加。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| left | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| top | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| right | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| bottom | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10, 10, 20, 20);
drawing.RectUtils.inset(rect, 10, -20, 30, 60);
console.info('rect.left: ', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10.0, 10.0, 20.0, 20.0);
if (rect == undefined) {
    return;
}
drawing.RectUtils.inset(rect, 10.0, -20.0, 30.0, 60.0);
console.info('rect.left:', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

## intersect

```TypeScript
static intersect(rect: common2D.Rect, other: common2D.Rect): boolean
```

计算两个矩形的交集区域，并将交集结果更新到第一个入参代表的矩形区域。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| other | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0, 0, 20, 20);
let rect2 = drawing.RectUtils.makeLtrb(10, 10, 40, 40);
let isIntersect = drawing.RectUtils.intersect(rect, rect2);
console.info('isIntersect: ', isIntersect);
console.info('rect.left: ', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0.0, 0.0, 20.0, 20.0);
let rect2 = drawing.RectUtils.makeLtrb(10.0, 10.0, 40.0, 40.0);
if (rect == undefined || rect2 == undefined) {
    return;
}
let isIntersect = drawing.RectUtils.intersect(rect, rect2);
console.info('isIntersect :', isIntersect);
console.info('rect.left:', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

## isEmpty

```TypeScript
static isEmpty(rect: common2D.Rect): boolean
```

判断矩形是否为空（左边界大于等于右边界或者上边界大于等于下边界）。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |

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
static isEqual(rect: common2D.Rect, other: common2D.Rect): boolean
```

判断两个矩形是否相等。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| other | common2D.Rect | 是 |

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

## isIntersect

```TypeScript
static isIntersect(rect: common2D.Rect, other: common2D.Rect): boolean
```

判断两个矩形是否相交。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| other | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0, 0, 20, 20);
let rect2 = drawing.RectUtils.makeLtrb(10, 10, 40, 40);
let isIntersect = drawing.RectUtils.isIntersect(rect, rect2);
console.info('isIntersect:', isIntersect);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0.0, 0.0, 20.0, 20.0);
let rect2 = drawing.RectUtils.makeLtrb(10.0, 10.0, 40.0, 40.0);
if (rect == undefined || rect2 == undefined) {
    return;
}
let isIntersect = drawing.RectUtils.isIntersect(rect, rect2);
console.info('isIntersect :', isIntersect);
```

## makeCopy

```TypeScript
static makeCopy(src: common2D.Rect): common2D.Rect
```

拷贝一个矩形。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| common2D.Rect |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10, 10, 20, 20);
let rect2 = drawing.RectUtils.makeCopy(rect);
console.info('rect2.left: ', rect2.left);
console.info('rect2.top: ', rect2.top);
console.info('rect2.right: ', rect2.right);
console.info('rect2.bottom: ', rect2.bottom);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(10.0, 10.0, 20.0, 20.0);
if (rect == undefined) {
    return;
}
let rect2 = drawing.RectUtils.makeCopy(rect);
console.info('rect2.left:', rect2?.left);
console.info('rect2.top: ', rect2?.top);
console.info('rect2.right: ', rect2?.right);
console.info('rect2.bottom: ', rect2?.bottom);
```

## makeCopy

```TypeScript
static makeCopy(src: common2D.Rect): common2D.Rect | undefined
```

拷贝一个矩形。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| common2D.Rect \| undefined |

**示例**

参见 [makeCopy](#makecopy)

## makeEmpty

```TypeScript
static makeEmpty(): common2D.Rect
```

创建一个上下左右边界坐标都是0的矩形。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Rect |

**示例**

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';

let rect = drawing.RectUtils.makeEmpty();
```

## makeEmpty

```TypeScript
static makeEmpty(): common2D.Rect | undefined
```

创建一个上下左右边界坐标都是0的矩形。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Rect \| undefined |

**示例**

参见 [makeEmpty](#makeempty)

## makeLtrb

```TypeScript
static makeLtrb(left: number, top: number, right: number, bottom: number): common2D.Rect
```

创建指定上下左右边界的矩形。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| left | number | 是 |
| top | number | 是 |
| right | number | 是 |
| bottom | number | 是 |

**返回值：**

| 类型 |
| --- |
| common2D.Rect |

**示例**

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';

let rect = drawing.RectUtils.makeLtrb(10.0, 10.0, 20.0, 20.0);
```

## makeLtrb

```TypeScript
static makeLtrb(left: double, top: double, right: double, bottom: double): common2D.Rect | undefined
```

创建指定上下左右边界的矩形。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| left | double | 是 |
| top | double | 是 |
| right | double | 是 |
| bottom | double | 是 |

**返回值：**

| 类型 |
| --- |
| common2D.Rect \| undefined |

**示例**

参见 [makeLtrb](#makeltrb)

## offset

ArkTS-Dyn:
```TypeScript
static offset(rect: common2D.Rect, dx: number, dy: number): void
```

ArkTS-Sta:
```TypeScript
static offset(rect: common2D.Rect, dx: double, dy: double): void
```

对矩形进行平移。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| dx | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| dy | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

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

## offsetTo

ArkTS-Dyn:
```TypeScript
static offsetTo(rect: common2D.Rect, newLeft: number, newTop: number): void
```

ArkTS-Sta:
```TypeScript
static offsetTo(rect: common2D.Rect, newLeft: double, newTop: double): void
```

将矩形平移到指定位置。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| newLeft | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| newTop | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(20, 20, 40, 40);
drawing.RectUtils.offsetTo(rect, 10, 20);
console.info('rect.left: ', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(20.0, 20.0, 40.0, 40.0);
if (rect == undefined) {
    return;
}
drawing.RectUtils.offsetTo(rect, 10.0, 20.0);
console.info('rect.left:', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

## setEmpty

```TypeScript
static setEmpty(rect: common2D.Rect): void
```

将矩形的上下左右边界都设为0。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |

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

## setLtrb

ArkTS-Dyn:
```TypeScript
static setLtrb(rect: common2D.Rect, left: number, top: number, right: number, bottom: number): void
```

ArkTS-Sta:
```TypeScript
static setLtrb(rect: common2D.Rect, left: double, top: double, right: double, bottom: double): void
```

使用传入的“左上右下”的值更新当前矩形的左上右下边界值。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| left | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| top | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| right | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| bottom | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeEmpty();
drawing.RectUtils.setLtrb(rect, 10, 20, 30, 60);
console.info('rect.left: ', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeEmpty();
if (rect == undefined) {
    return;
}
drawing.RectUtils.setLtrb(rect, 10.0, 20.0, 30.0, 60.0);
console.info('rect.left:', rect?.left);
console.info('rect.top: ', rect?.top);
console.info('rect.right: ', rect?.right);
console.info('rect.bottom: ', rect?.bottom);
```

## setRect

```TypeScript
static setRect(rect: common2D.Rect, other: common2D.Rect): void
```

使用另一个矩形对当前矩形进行赋值。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| other | common2D.Rect | 是 |

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

## sort

```TypeScript
static sort(rect: common2D.Rect): void
```

如果矩形存在反转的情况（即左边界大于右边界或上边界大于下边界），则将发生反转的对应边界值进行交换（若左边界大于右边界，交换左右边界值；若上边界大于下边界，交换上下边界值），使得上边界小于下边界（左边界小于右边界）。如果矩形不存在反转的情况（即左边界小于等于右边界且上边界小于等于下边界），不做任何操作。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(20, 40, 30, 30);
drawing.RectUtils.sort(rect);
console.info('rect.left: ', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(20.0, 40.0, 30.0, 30.0);
if (rect == undefined) {
    return;
}
drawing.RectUtils.sort(rect);
console.info('rect.left:', rect?.left);
console.info('rect.top: ', rect?.top);
console.info('rect.right: ', rect?.right);
console.info('rect.bottom: ', rect?.bottom);
```

## union

```TypeScript
static union(rect: common2D.Rect, other: common2D.Rect): void
```

计算两个矩形的并集区域，并将并集结果更新到第一个入参代表的矩形区域。如果第一个入参矩形为空，则将并集结果更新到第二个入参代表的矩形区域；如果第二个入参的矩形为空，则不进行任何操作。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| other | common2D.Rect | 是 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0, 0, 20, 20);
let rect2 = drawing.RectUtils.makeLtrb(10, 10, 40, 40);
drawing.RectUtils.union(rect, rect2);
console.info('rect.left: ', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

ArkTS-Sta示例：

```TypeScript
import { drawing, common2D } from '@kit.ArkGraphics2D';
let rect = drawing.RectUtils.makeLtrb(0.0, 0.0, 20.0, 20.0);
let rect2 = drawing.RectUtils.makeLtrb(10.0, 10.0, 40.0, 40.0);
if (rect == undefined || rect2 == undefined) {
    return;
}
drawing.RectUtils.union(rect, rect2);
console.info('rect.left:', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```
