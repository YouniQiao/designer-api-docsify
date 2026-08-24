# Brush

画刷对象，用于设置图形的填充样式，包括颜色、抗锯齿、混合模式、颜色滤波器、蒙版滤波器、着色器效果、阴影层效果及图像滤波器等，并支持获取颜色、透明度、抗锯齿等属性及重置画刷为初始状态。画刷需通过Canvas的[attachBrush](arkts-arkgraphics2d-drawing-canvas-c.md#attachbrush)方法绑定到画布后生效，绘制完成后通过 [detachBrush](arkts-arkgraphics2d-drawing-canvas-c.md#detachbrush)方法解绑；画刷用于图形填充，画笔（Pen）用于图形描边，详见[Pen](arkts-arkgraphics2d-drawing-pen-c.md)。

> **说明：**&gt;
> - 本模块使用屏幕物理像素单位px。&gt;
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 23

<!--Device-drawing-class Brush--><!--Device-drawing-class Brush-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor()
```

构造一个新的画刷对象。默认配置：新建画刷默认抗锯齿关闭、混合模式为SRC_OVER，且未设置颜色滤波器、蒙版滤波器、着色器效果、 阴影层效果和图像滤波器。

**起始版本：** 23

<!--Device-Brush-constructor()--><!--Device-Brush-constructor()-End-->

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
constructor(brush: Brush)
```

复制构造一个新的画刷对象。

**起始版本：** 23

<!--Device-Brush-constructor(brush: Brush)--><!--Device-Brush-constructor(brush: Brush)-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brush | [Brush](arkts-arkgraphics2d-drawing-brush-c.md) | 是 | 待复制的画刷对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**示例**

参见 [constructor](#constructor)

## getAlpha

```TypeScript
getAlpha(): int
```

获取画刷的透明度。

**起始版本：** 23

<!--Device-Brush-getAlpha(): int--><!--Device-Brush-getAlpha(): int-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 返回画刷的透明度，取值范围为[0, 255]的整数。 |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
let alpha = brush.getAlpha();
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
let alpha = pen.getAlpha();
```

## getColor

```TypeScript
getColor(): common2D.Color
```

获取画刷的颜色。

**起始版本：** 12

<!--Device-Brush-getColor(): common2D.Color--><!--Device-Brush-getColor(): common2D.Color-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common2D.Color | 返回画刷的颜色，为ARGB格式的颜色对象，包含alpha、red、green、blue四个通道值，每个通道取值范围为[0, 255]的整数。 |

**示例**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
const brush = new drawing.Brush();
brush.setColor(color);
let currentColor = brush.getColor();
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
const pen = new drawing.Pen();
pen.setColor(color);
let colorGet = pen.getColor();
```

## getColor

```TypeScript
getColor(): common2D.Color | undefined
```

获取画刷的颜色。

**起始版本：** 23

<!--Device-Brush-getColor(): common2D.Color | undefined--><!--Device-Brush-getColor(): common2D.Color | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common2D.Color \| undefined | 返回画刷的颜色，为ARGB格式的颜色对象，包含alpha、red、green、blue四个通道值，每个通道取值范围为[0, 255]的整数。获取颜色失败时返回undefined。 |

**示例**

参见 [getColor](#getcolor)

## getColor4f

```TypeScript
getColor4f(): common2D.Color4f
```

获取画刷的颜色，与[getColor](#getcolor)的区别是返回值类型为浮点数，适用于需要浮点数类型的场景。

**起始版本：** 20

<!--Device-Brush-getColor4f(): common2D.Color4f--><!--Device-Brush-getColor4f(): common2D.Color4f-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common2D.Color4f | 返回画刷的颜色，为浮点数格式的ARGB颜色对象，每个通道值为[0.0, 1.0]之间的浮点数。 |

**示例**

```TypeScript
import { common2D, drawing, colorSpaceManager } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
let colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.BT2020_HLG);
let color4f: common2D.Color4f = { alpha: 1, red: 0.5, green: 0.4, blue: 0.7 };
brush.setColor4f(color4f, colorSpace);
let color = brush.getColor4f();
```

```TypeScript
import { common2D, drawing, colorSpaceManager } from "@kit.ArkGraphics2D";

const pen = new drawing.Pen();
let colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.BT2020_HLG);
let color4f: common2D.Color4f = {alpha: 1, red: 0.5, green: 0.4, blue: 0.7};
pen.setColor4f(color4f, colorSpace);
let color = pen.getColor4f();
```

## getColor4f

```TypeScript
getColor4f(): common2D.Color4f | undefined
```

获取画刷的颜色，与[getColor](#getcolor)的区别是返回值类型为浮点数，适用于需要浮点数类型的场景。

**起始版本：** 24

<!--Device-Brush-getColor4f(): common2D.Color4f | undefined--><!--Device-Brush-getColor4f(): common2D.Color4f | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common2D.Color4f \| undefined | 返回画刷的颜色，为浮点数格式的ARGB颜色对象，每个通道值为[0.0, 1.0]之间的浮点数。获取颜色失败时返回undefined。 |

**示例**

参见 [getColor4f](#getcolor4f)

## getColorFilter

```TypeScript
getColorFilter(): ColorFilter
```

获取画刷的颜色滤波器。

**起始版本：** 12

<!--Device-Brush-getColorFilter(): ColorFilter--><!--Device-Brush-getColorFilter(): ColorFilter-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ColorFilter | 返回画刷的颜色滤波器，用于对绘制内容进行颜色调整，如伽马校正、颜色矩阵变换等。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let brush = new drawing.Brush();
let colorFilter = drawing.ColorFilter.createSRGBGammaToLinear();
brush.setColorFilter(colorFilter);
let currentFilter = brush.getColorFilter();
```

ArkTS-Sta示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let brush = new drawing.Brush();
let setColorFilter = drawing.ColorFilter.createSRGBGammaToLinear();
if (setColorFilter != undefined) {
  brush.setColorFilter(setColorFilter!);
}
let filter = brush.getColorFilter();
```

ArkTS-Dyn示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let pen = new drawing.Pen();
let colorFilter = drawing.ColorFilter.createLumaColorFilter();
pen.setColorFilter(colorFilter);
let filter = pen.getColorFilter();
```

ArkTS-Sta示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let pen = new drawing.Pen();
let setColorFilter = drawing.ColorFilter.createSRGBGammaToLinear();
if (setColorFilter != undefined) {
  pen.setColorFilter(setColorFilter!);
}
let filter = pen.getColorFilter();
```

## getColorFilter

```TypeScript
getColorFilter(): ColorFilter | undefined
```

获取画刷的颜色滤波器。

**起始版本：** 23

<!--Device-Brush-getColorFilter(): ColorFilter | undefined--><!--Device-Brush-getColorFilter(): ColorFilter | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ColorFilter \| undefined | 返回颜色滤波器，用于对绘制内容进行颜色调整，如伽马校正、颜色矩阵变换等。获取颜色滤波器失败时返回undefined。 |

**示例**

参见 [getColorFilter](#getcolorfilter)

## getHexColor

```TypeScript
getHexColor(): int
```

获取画刷颜色的16进制ARGB格式值。与[getColor](#getcolor)的区别是返回值类型为16进制ARGB格式的32位无符号整数。

**起始版本：** 23

<!--Device-Brush-getHexColor(): int--><!--Device-Brush-getHexColor(): int-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 返回画刷的颜色，以16进制ARGB格式的32位无符号整数表示。 |

**示例**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
let brush = new drawing.Brush();
brush.setColor(color);
let hexColor = brush.getHexColor();
console.info('getHexColor: ', hexColor.toString(16));
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
let pen = new drawing.Pen();
pen.setColor(color);
let hexColor = pen.getHexColor();
console.info('getHexColor: ', hexColor.toString(16));
```

## isAntiAlias

```TypeScript
isAntiAlias(): boolean
```

获取画刷是否开启抗锯齿属性。

**起始版本：** 23

<!--Device-Brush-isAntiAlias(): boolean--><!--Device-Brush-isAntiAlias(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回画刷是否开启抗锯齿属性，true表示开启，false表示关闭。 |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
let isAntiAlias = brush.isAntiAlias();
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
let isAntiAlias = pen.isAntiAlias();
```

## reset

```TypeScript
reset(): void
```

重置当前画刷为初始状态，清除已设置的颜色、透明度、抗锯齿、颜色滤波器、蒙版滤波器、着色器效果、阴影层效果、混合模式和图像滤波器等属性。初始状态的具体取值：抗锯齿关闭、混合模式为SRC_OVER，且未设置颜色滤波器、蒙版滤波器、 着色器效果、阴影层效果和图像滤波器。如需使用上述属性，需要重新调用对应的set接口进行设置。

**起始版本：** 23

<!--Device-Brush-reset(): void--><!--Device-Brush-reset(): void-End-->

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

## setAlpha

```TypeScript
setAlpha(alpha: int): void
```

设置画刷的透明度。调用setAlpha后，渲染时以setAlpha设置的透明度为准，覆盖setColor中Color对象的alpha通道值。

**起始版本：** 23

<!--Device-Brush-setAlpha(alpha: int): void--><!--Device-Brush-setAlpha(alpha: int): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alpha | int | 是 | 用于表示透明度的取值范围为[0, 255]的整数，传入范围内的浮点数会向下取整。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
brush.setAlpha(128);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
pen.setAlpha(128);
```

## setAntiAlias

```TypeScript
setAntiAlias(aa: boolean): void
```

设置画刷是否开启抗锯齿。开启后，图形边缘显示更平滑。未调用此接口设置时，系统默认关闭抗锯齿。

**起始版本：** 23

<!--Device-Brush-setAntiAlias(aa: boolean): void--><!--Device-Brush-setAntiAlias(aa: boolean): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aa | boolean | 是 | 表示是否开启抗锯齿，true表示开启，false表示关闭。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
brush.setAntiAlias(true);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
pen.setAntiAlias(true);
```

## setBlendMode

```TypeScript
setBlendMode(mode: BlendMode): void
```

设置画刷的混合模式。未调用此接口设置时，系统默认的混合模式为SRC_OVER。

**起始版本：** 23

<!--Device-Brush-setBlendMode(mode: BlendMode): void--><!--Device-Brush-setBlendMode(mode: BlendMode): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | BlendMode | 是 | 颜色的混合模式，用于控制绘制时源颜色与已有目标颜色的混合方式。未调用此接口设置时，系统默认的混合模式为SRC_OVER。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
brush.setBlendMode(drawing.BlendMode.SRC);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
pen.setBlendMode(drawing.BlendMode.SRC);
```

## setColor

```TypeScript
setColor(color: common2D.Color): void
```

设置画刷的颜色。设置的颜色将作为图形填充的基础颜色，在未设置ShaderEffect时以该颜色进行渲染填充。

**起始版本：** 23

<!--Device-Brush-setColor(color: common2D.Color): void--><!--Device-Brush-setColor(color: common2D.Color): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | common2D.Color | 是 | ARGB格式的颜色，每个颜色通道的取值范围为[0, 255]的整数，传入范围内的浮点数会向下取整。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
const brush = new drawing.Brush();
brush.setColor(color);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
brush.setColor(255, 255, 0, 0);
```

ArkTS-Dyn示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
brush.setColor(0xffff0000);
```

ArkTS-Sta示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
brush.setColor((0xffff0000).toInt());
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const color : common2D.Color = { alpha: 255, red: 255, green: 0, blue: 0 };
const pen = new drawing.Pen();
pen.setColor(color);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
pen.setColor(255, 255, 0, 0);
```

ArkTS-Dyn示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
pen.setColor(0xffff0000);
```

ArkTS-Sta示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
pen.setColor((0xffff0000).toInt());
```

## setColor

```TypeScript
setColor(alpha: int, red: int, green: int, blue: int): void
```

设置画刷的颜色。性能优于[setColor](#setcolor)接口，推荐使用本接口。

**起始版本：** 23

<!--Device-Brush-setColor(alpha: int, red: int, green: int, blue: int): void--><!--Device-Brush-setColor(alpha: int, red: int, green: int, blue: int): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alpha | int | 是 | ARGB格式颜色的透明度通道值，取值范围为[0, 255]的整数，传入范围内的浮点数会向下取整。 |
| red | int | 是 | ARGB格式颜色的红色通道值，取值范围为[0, 255]的整数，传入范围内的浮点数会向下取整。 |
| green | int | 是 | ARGB格式颜色的绿色通道值，取值范围为[0, 255]的整数，传入范围内的浮点数会向下取整。 |
| blue | int | 是 | ARGB格式颜色的蓝色通道值，取值范围为[0, 255]的整数，传入范围内的浮点数会向下取整。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**

参见 [setColor](#setcolor)

## setColor

```TypeScript
setColor(color: int): void
```

设置画刷的颜色。与[setColor](#setcolor)的区别是支持通过16进制ARGB数值直接设置颜色。

**起始版本：** 23

<!--Device-Brush-setColor(color: int): void--><!--Device-Brush-setColor(color: int): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | int | 是 | 16进制ARGB格式的颜色，以32位无符号整数表示，格式为0xAARRGGBB，其中AA为透明度通道，RR为红色通道， GG为绿色通道，BB为蓝色通道，取值范围均为0x00到0xFF，整体取值范围为[0x00000000, 0xFFFFFFFF]。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**

参见 [setColor](#setcolor)

## setColor4f

```TypeScript
setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void
```

设置画刷的颜色以及标准色域。与[setColor](#setcolor)的区别是可以单独设置色域， 适用于需要单独设置色域的场景。

**起始版本：** 24

<!--Device-Brush-setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void--><!--Device-Brush-setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color4f | common2D.Color4f | 是 | ARGB格式的颜色，每个颜色通道的值是0.0-1.0之间的浮点数，大于1.0时，取1.0， 小于0.0时，取0.0。颜色值在colorSpace参数指定的色域下进行映射。 |
| colorSpace | colorSpaceManager.ColorSpaceManager \| null | 是 | 标准色域对象，需通过 [colorSpaceManager.create()](arkts-arkgraphics2d-colorspacemanager-create-f.md)方法创建，与color4f配合使 用，决定color4f颜色值的映射色域。null表示使用sRGB色域。 |

**示例**

```TypeScript
import { common2D, drawing, colorSpaceManager } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
let colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.BT2020_HLG);
let color4f: common2D.Color4f = { alpha: 1, red: 0.5, green: 0.4, blue: 0.7 };
brush.setColor4f(color4f, colorSpace);
```

```TypeScript
import { common2D, drawing, colorSpaceManager } from "@kit.ArkGraphics2D";

const pen = new drawing.Pen();
let colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.BT2020_HLG);
let color4f: common2D.Color4f = {alpha: 1, red: 0.5, green: 0.4, blue: 0.7};
pen.setColor4f(color4f, colorSpace);
```

## setColorFilter

```TypeScript
setColorFilter(filter: ColorFilter | null): void
```

设置画刷的颜色滤波器。

**起始版本：** 23

<!--Device-Brush-setColorFilter(filter: ColorFilter | null): void--><!--Device-Brush-setColorFilter(filter: ColorFilter | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | ColorFilter \| null | 是 | 颜色滤波器，用于对绘制内容进行颜色调整（如伽马校正、颜色矩阵变换等）。null表示清空颜色滤波器。<br>**起始版本：** 20 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
let colorFilter = drawing.ColorFilter.createLinearToSRGBGamma();
brush.setColorFilter(colorFilter);
```

ArkTS-Sta示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
let colorFilter = drawing.ColorFilter.createLinearToSRGBGamma();
if (colorFilter != undefined) {
  brush.setColorFilter(colorFilter!);
}
brush.setColorFilter(null);
```

ArkTS-Dyn示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
let colorFilter = drawing.ColorFilter.createLinearToSRGBGamma();
pen.setColorFilter(colorFilter);
```

ArkTS-Sta示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
let colorFilter = drawing.ColorFilter.createLinearToSRGBGamma();
if (colorFilter != undefined) {
  pen.setColorFilter(colorFilter!);
}
pen.setColorFilter(null);
```

## setImageFilter

```TypeScript
setImageFilter(filter: ImageFilter | null): void
```

设置画刷的图像滤波器。

**起始版本：** 23

<!--Device-Brush-setImageFilter(filter: ImageFilter | null): void--><!--Device-Brush-setImageFilter(filter: ImageFilter | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) \| null | 是 | 图像滤波器，用于对绘制内容进行模糊、锐化等图像处理。null表示清空图像滤波器。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let brush = new drawing.Brush();
let imageFilter = drawing.ImageFilter.createBlurImageFilter(5, 10, drawing.TileMode.DECAL);
brush.setImageFilter(imageFilter);
brush.setImageFilter(null);
```

ArkTS-Sta示例：

```TypeScript
import { drawing }  from '@kit.ArkGraphics2D';

let brush = new drawing.Brush();
let imgFilter = drawing.ImageFilter.createBlurImageFilter(5, 10, drawing.TileMode.DECAL);
if (imgFilter != undefined) {
  brush.setImageFilter(imgFilter!);
}
brush.setImageFilter(null);
```

ArkTS-Dyn示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let colorfilter = drawing.ColorFilter.createSRGBGammaToLinear();
let imgFilter = drawing.ImageFilter.createFromColorFilter(colorfilter);
let pen = new drawing.Pen();
pen.setImageFilter(imgFilter);
pen.setImageFilter(null);
```

ArkTS-Sta示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let colorfilter = drawing.ColorFilter.createSRGBGammaToLinear();
let imgFilter = colorfilter == undefined ? undefined : drawing.ImageFilter.createFromColorFilter(colorfilter!);
let pen = new drawing.Pen();
if (imgFilter != undefined) {
  pen.setImageFilter(imgFilter!);
}
pen.setImageFilter(null);
```

## setMaskFilter

```TypeScript
setMaskFilter(filter: MaskFilter | null): void
```

设置画刷的蒙版滤波器。

**起始版本：** 23

<!--Device-Brush-setMaskFilter(filter: MaskFilter | null): void--><!--Device-Brush-setMaskFilter(filter: MaskFilter | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [MaskFilter](arkts-arkgraphics2d-drawing-maskfilter-c.md) \| null | 是 | 蒙版滤波器，用于对绘制图形边缘进行模糊处理等场景。null表示清空蒙版滤波器。<br>**起始版本：** 20 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const brush = new drawing.Brush();
    let maskFilter = drawing.MaskFilter.createBlurMaskFilter(drawing.BlurType.OUTER, 10);
    brush.setMaskFilter(maskFilter);
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
    const brush = new drawing.Brush();
    let maskFilter = drawing.MaskFilter.createBlurMaskFilter(drawing.BlurType.OUTER, 10);
    if (maskFilter == undefined) {
      return;
    }
    brush.setMaskFilter(maskFilter);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const pen = new drawing.Pen();
    pen.setStrokeWidth(5);
    pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
    let maskFilter = drawing.MaskFilter.createBlurMaskFilter(drawing.BlurType.OUTER, 10);
    pen.setMaskFilter(maskFilter);
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
    pen.setStrokeWidth(5.0);
    pen.setColor({alpha: 255, red: 255, green: 0, blue: 0});
    let maskFilter = drawing.MaskFilter.createBlurMaskFilter(drawing.BlurType.OUTER, 10.0);
    if (maskFilter == undefined) {
      return;
    }
    pen.setMaskFilter(maskFilter);
    pen.setMaskFilter(null);
  }
}
```

## setShaderEffect

```TypeScript
setShaderEffect(shaderEffect: ShaderEffect | null): void
```

设置画刷的着色器效果。

**起始版本：** 23

<!--Device-Brush-setShaderEffect(shaderEffect: ShaderEffect | null): void--><!--Device-Brush-setShaderEffect(shaderEffect: ShaderEffect | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) \| null | 是 | 着色器效果对象，用于实现渐变填充、图案填充等复杂绘制效果。null表示清空着色器效果。<br>**起始版本：** 20 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
let shaderEffect = drawing.ShaderEffect.createLinearGradient({x: 100, y: 100}, {x: 300, y: 300}, [0xFF00FF00, 0xFFFF0000], drawing.TileMode.REPEAT);
brush.setShaderEffect(shaderEffect);
```

ArkTS-Sta示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
let shaderEffect = drawing.ShaderEffect.createLinearGradient({x: 100, y: 100}, {x: 300, y: 300}, [(0xFF00FF00).toInt(), (0xFFFF0000).toInt()], drawing.TileMode.REPEAT);
if (shaderEffect != undefined) {
  brush.setShaderEffect(shaderEffect!);
}
```

ArkTS-Dyn示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
let shaderEffect = drawing.ShaderEffect.createLinearGradient({x: 100, y: 100}, {x: 300, y: 300}, [0xFF00FF00, 0xFFFF0000], drawing.TileMode.REPEAT);
pen.setShaderEffect(shaderEffect);
```

ArkTS-Sta示例：

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
let shaderEffect = drawing.ShaderEffect.createLinearGradient({x: 100.0, y: 100.0}, {x: 300.0, y: 300.0}, [(0xFF00FF00).toInt(), (0xFFFF0000).toInt()], drawing.TileMode.REPEAT);
if (shaderEffect != undefined) {
  pen.setShaderEffect(shaderEffect!);
}
pen.setShaderEffect(null);
```

## setShadowLayer

```TypeScript
setShadowLayer(shadowLayer: ShadowLayer | null): void
```

设置画刷的阴影层效果。当前仅在通过Canvas的[drawTextBlob](arkts-arkgraphics2d-drawing-canvas-c.md#drawtextblob)等方法绘制文字时生效。

**起始版本：** 23

<!--Device-Brush-setShadowLayer(shadowLayer: ShadowLayer | null): void--><!--Device-Brush-setShadowLayer(shadowLayer: ShadowLayer | null): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shadowLayer | [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) \| null | 是 | 阴影层对象，用于给画刷添加阴影效果。null表示清空阴影层效果。该阴影层效果仅在绘制文字时生效。<br>**起始版本：** 20 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let font = new drawing.Font();
    font.setSize(60);

    let textBlob = drawing.TextBlob.makeFromString('hello', font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    let pen = new drawing.Pen();
    pen.setStrokeWidth(2.0);

    let penColor : common2D.Color = {alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00};
    pen.setColor(penColor);
    canvas.attachPen(pen);
    canvas.drawTextBlob(textBlob, 100, 100);
    canvas.detachPen();

    let color : common2D.Color = {alpha: 0xFF, red: 0x00, green: 0xFF, blue: 0x00};
    let shadowLayer = drawing.ShadowLayer.create(3, -3, 3, color);
    pen.setShadowLayer(shadowLayer);
    canvas.attachPen(pen);
    canvas.drawTextBlob(textBlob, 100, 200);
    canvas.detachPen();

    let brush = new drawing.Brush();
    let brushColor : common2D.Color = {alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00};
    brush.setColor(brushColor);
    canvas.attachBrush(brush);
    canvas.drawTextBlob(textBlob, 300, 100);
    canvas.detachBrush();

    brush.setShadowLayer(shadowLayer);
    canvas.attachBrush(brush);
    canvas.drawTextBlob(textBlob, 300, 200);
    canvas.detachBrush();
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context: DrawContext) {
    const canvas = context.canvas;
    let font = new drawing.Font();
    font.setSize(60);

    let textBlob = drawing.TextBlob.makeFromString("hello", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    if (textBlob == undefined) {
      return;
    }
    let pen = new drawing.Pen();
    pen.setStrokeWidth(2.0);

    let pen_color : common2D.Color = {alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00};
    pen.setColor(pen_color);
    canvas.attachPen(pen);
    canvas.drawTextBlob(textBlob, 100, 100);
    canvas.detachPen();

    let color : common2D.Color = {alpha: 0xFF, red: 0x00, green: 0xFF, blue: 0x00};
    let shadowLayer = drawing.ShadowLayer.create(3, -3, 3, color);
    if (shadowLayer == undefined) {
      return;
    }
    pen.setShadowLayer(shadowLayer);
    canvas.attachPen(pen);
    canvas.drawTextBlob(textBlob, 100, 200);
    canvas.detachPen();

    let brush = new drawing.Brush();
    let brush_color : common2D.Color = {alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00};
    brush.setColor(brush_color);
    canvas.attachBrush(brush);
    canvas.drawTextBlob(textBlob, 300, 100);
    canvas.detachBrush();

    brush.setShadowLayer(shadowLayer);
    canvas.attachBrush(brush);
    canvas.drawTextBlob(textBlob, 300, 200);
    canvas.detachBrush();
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let font = new drawing.Font();
    font.setSize(60);
    let textBlob = drawing.TextBlob.makeFromString("hello", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    let pen = new drawing.Pen();
    pen.setStrokeWidth(2.0);
    let pen_color : common2D.Color = {alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00};
    pen.setColor(pen_color);
    canvas.attachPen(pen);
    canvas.drawTextBlob(textBlob, 100, 100);
    canvas.detachPen();
    let color : common2D.Color = {alpha: 0xFF, red: 0x00, green: 0xFF, blue: 0x00};
    let shadowLayer = drawing.ShadowLayer.create(3, -3, 3, color);
    pen.setShadowLayer(shadowLayer);
    canvas.attachPen(pen);
    canvas.drawTextBlob(textBlob, 100, 200);
    canvas.detachPen();
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
    let font = new drawing.Font();
    font.setSize(60.0);
    let textBlob = drawing.TextBlob.makeFromString("hello", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    if (textBlob == undefined) {
      return;
    }
    let pen = new drawing.Pen();
    pen.setStrokeWidth(2.0);
    let pen_color : common2D.Color = {alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00};
    pen.setColor(pen_color);
    canvas.attachPen(pen);
    canvas.drawTextBlob(textBlob, 100.0, 100.0);
    canvas.detachPen();
    let color : common2D.Color = {alpha: 0xFF, red: 0x00, green: 0xFF, blue: 0x00};
    let shadowLayer = drawing.ShadowLayer.create(3.0, -3.0, 3.0, color);
    if (shadowLayer == undefined) {
      return;
    }
    pen.setShadowLayer(shadowLayer);
    canvas.attachPen(pen);
    canvas.drawTextBlob(textBlob, 100.0, 200.0);
    canvas.detachPen();
    pen.setShadowLayer(null);
    canvas.attachPen(pen);
    canvas.drawTextBlob(textBlob, 100, 200);
    canvas.detachPen();
  }
}
```

