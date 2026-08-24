# TextBlob

TextBlob是由一个或多个具有相同字型的字符组成的字块。支持通过文本、字符串、RunBuffer等多种方式创建字形集合，适用于需要批量渲染文本或获取文字边界框的场景。

> **说明：**&gt;
> - 本模块使用屏幕物理像素单位px。&gt;
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 23

<!--Device-drawing-class TextBlob--><!--Device-drawing-class TextBlob-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## bounds

```TypeScript
bounds(): common2D.Rect
```

获取文字边界框的矩形区域。

**起始版本：** 11

<!--Device-TextBlob-bounds(): common2D.Rect--><!--Device-TextBlob-bounds(): common2D.Rect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common2D.Rect | 文字边界框的矩形区域。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const font = new drawing.Font();
font.setSize(20);
const textBlob = drawing.TextBlob.makeFromString("drawing", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
let bounds = textBlob.bounds();
```

ArkTS-Sta示例：

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const font = new drawing.Font();
font.setSize(20.0);
const textBlob = drawing.TextBlob.makeFromString("drawing", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
if (textBlob != undefined) {
  let bounds = textBlob!.bounds();
}
```

## bounds

```TypeScript
bounds(): common2D.Rect | undefined
```

获取文字边界框的矩形区域。

**起始版本：** 23

<!--Device-TextBlob-bounds(): common2D.Rect | undefined--><!--Device-TextBlob-bounds(): common2D.Rect | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common2D.Rect \| undefined | 文字边界框的矩形区域。创建失败时返回undefined。 |

**示例**

参见 [bounds](#bounds)

## makeFromPosText

```TypeScript
static makeFromPosText(text: string, len: number, points: common2D.Point[], font: Font): TextBlob
```

使用文本创建TextBlob对象，其中每个字形的坐标由points中对应的坐标信息决定。

**起始版本：** 12

<!--Device-TextBlob-static makeFromPosText(text: string, len: number, points: common2D.Point[], font: Font): TextBlob--><!--Device-TextBlob-static makeFromPosText(text: string, len: number, points: common2D.Point[], font: Font): TextBlob-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 绘制字形的文本内容。 |
| len | number | 是 | 字形个数，由[countText](arkts-arkgraphics2d-drawing-font-c.md#counttext)获取，该参数为整数。 |
| points | common2D.Point[] | 是 | 点数组，用于指定每个字形的坐标，长度必须为len。 |
| font | Font | 是 | 字型对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) | 由文本和坐标信息创建的TextBlob对象，用于后续绘制字形。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { drawing, common2D } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let text : string = 'makeFromPosText';
    let font : drawing.Font = new drawing.Font();
    font.setSize(100);
    let length = font.countText(text);
    let points : common2D.Point[] = [];
    for (let i = 0; i !== length; ++i) {
      points.push({ x: i * 35, y: i * 35 });
    }
    let textblob : drawing.TextBlob = drawing.TextBlob.makeFromPosText(text, points.length, points, font);
    canvas.drawTextBlob(textblob, 100, 100);
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { drawing, common2D } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context: DrawContext) {
    const canvas = context.canvas;
    let text: string = 'makeFromPosText';
    let font: drawing.Font = new drawing.Font();
    font.setSize(100);
    let length = font.countText(text);
    let points: common2D.Point[] = [];
    for (let i = 0; i !== length; ++i) {
      points.push({ x: i * 35.0, y: i * 35.0 });
    }
    let textblob = drawing.TextBlob.makeFromPosText(text, points.length, points, font);
    if (textblob == undefined) {
      return;
    }
    canvas.drawTextBlob(textblob, 100.0, 100.0);
  }
}
```

## makeFromPosText

```TypeScript
static makeFromPosText(text: string, len: int, points: common2D.Point[], font: Font): TextBlob | undefined
```

使用文本创建TextBlob对象，其中每个字形的坐标由points中对应的坐标信息决定。

**起始版本：** 23

<!--Device-TextBlob-static makeFromPosText(text: string, len: int, points: common2D.Point[], font: Font): TextBlob | undefined--><!--Device-TextBlob-static makeFromPosText(text: string, len: int, points: common2D.Point[], font: Font): TextBlob | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 绘制字形的文本内容。 |
| len | int | 是 | 字形个数，由[countText](arkts-arkgraphics2d-drawing-font-c.md#counttext)获取，该参数为整数。 |
| points | common2D.Point[] | 是 | 点数组，用于指定每个字形的坐标，长度必须为len。 |
| font | Font | 是 | 字型对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) \| undefined | 由文本和坐标信息创建的TextBlob对象，用于后续绘制字形。创建失败时返回undefined。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**示例**

参见 [makeFromPosText](#makefrompostext)

## makeFromRunBuffer

```TypeScript
static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob
```

基于RunBuffer信息创建TextBlob对象。

**起始版本：** 11

<!--Device-TextBlob-static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob--><!--Device-TextBlob-static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pos | Array&lt;[TextBlobRunBuffer](arkts-arkgraphics2d-drawing-textblobrunbuffer-i.md)&gt; | 是 | TextBlobRunBuffer数组，每个元素包含字形ID及位置坐标信息。 |
| font | Font | 是 | 字型对象。 |
| bounds | common2D.Rect | 否 | 文字边界框的矩形区域；如果不设置，则不预设边界框。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) | 基于RunBuffer创建的TextBlob对象，用于后续绘制字形。 |

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
    const font = new drawing.Font();
    font.setSize(20);
    let runBuffer : Array<drawing.TextBlobRunBuffer> = [
      { glyph: 65, positionX: 0, positionY: 0 },
      { glyph: 227, positionX: 14.9, positionY: 0 },
      { glyph: 283, positionX: 25.84, positionY: 0 },
      { glyph: 283, positionX: 30.62, positionY: 0 },
      { glyph: 299, positionX: 35.4, positionY: 0 }
    ];
    const textBlob = drawing.TextBlob.makeFromRunBuffer(runBuffer, font, null);
    const brush = new drawing.Brush();
    brush.setColor({alpha: 255, red: 255, green: 0, blue: 0});
    canvas.attachBrush(brush);
    canvas.drawTextBlob(textBlob, 20, 20);
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
    const font = new drawing.Font();
    font.setSize(20);
    let runBuffer: Array<drawing.TextBlobRunBuffer> = [
      { glyph: 65, positionX: 0.0, positionY: 0.0 },
      { glyph: 227, positionX: 14.9, positionY: 0.0 },
      { glyph: 283, positionX: 25.84, positionY: 0.0 },
      { glyph: 283, positionX: 30.62, positionY: 0.0 },
      { glyph: 299, positionX: 35.4, positionY: 0.0 }
    ];
    const textBlob = drawing.TextBlob.makeFromRunBuffer(runBuffer, font);
    if (textBlob == undefined) {
      return;
    }
    const brush = new drawing.Brush();
    brush.setColor({
      alpha: 255,
      red: 255,
      green: 0,
      blue: 0
    });
    canvas.attachBrush(brush);
    canvas.drawTextBlob(textBlob, 20.0, 20.0);
    canvas.detachBrush();
  }
}
```

## makeFromRunBuffer

```TypeScript
static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob | undefined
```

基于RunBuffer信息创建TextBlob对象。

**起始版本：** 23

<!--Device-TextBlob-static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob | undefined--><!--Device-TextBlob-static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pos | Array&lt;[TextBlobRunBuffer](arkts-arkgraphics2d-drawing-textblobrunbuffer-i.md)&gt; | 是 | TTextBlobRunBuffer数组，每个元素包含字形ID及位置坐标信息。 |
| font | Font | 是 | 字型对象。 |
| bounds | common2D.Rect | 否 | 文字边界框的矩形区域；如果不设置，则不预设边界框。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) \| undefined | 基于RunBuffer创建的TextBlob对象，用于后续绘制字形。创建失败时返回undefined。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**示例**

参见 [makeFromRunBuffer](#makefromrunbuffer)

## makeFromString

```TypeScript
static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob
```

根据指定的编码类型和字型，使用string类型的值创建TextBlob对象。

**起始版本：** 11

<!--Device-TextBlob-static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob--><!--Device-TextBlob-static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 绘制字形的文本内容。 |
| font | Font | 是 | 字型对象。 |
| encoding | TextEncoding | 否 | 编码类型，默认值为TEXT_ENCODING_UTF8。当前只有TEXT_ENCODING_UTF8生效，其余编码类型也会被视为 TEXT_ENCODING_UTF8。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) | TextBlob对象，用于后续绘制字形。 |

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
    const canvas = context.canvas;
    const brush = new drawing.Brush();
    brush.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    const font = new drawing.Font();
    font.setSize(20);
    const textBlob = drawing.TextBlob.makeFromString("drawing", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    canvas.attachBrush(brush);
    canvas.drawTextBlob(textBlob, 20, 20);
    canvas.detachBrush();
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
    const brush = new drawing.Brush();
    brush.setColor({alpha: 255, red: 255, green: 0, blue: 0});
    const font = new drawing.Font();
    font.setSize(20.0);
    const textBlob = drawing.TextBlob.makeFromString("drawing", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    if (textBlob == undefined) {
      return;
    }
    canvas.attachBrush(brush);
    canvas.drawTextBlob(textBlob, 20.0, 20.0);
    canvas.detachBrush();
  }
}
```

## makeFromString

```TypeScript
static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob | undefined
```

根据指定的编码类型和字型，使用string类型的值创建TextBlob对象

**起始版本：** 23

<!--Device-TextBlob-static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob | undefined--><!--Device-TextBlob-static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 绘制字形的文本内容。 |
| font | Font | 是 | 字型对象。 |
| encoding | TextEncoding | 否 | 编码类型，默认值为TEXT_ENCODING_UTF8。当前只有TEXT_ENCODING_UTF8生效，其余编码类型也会被视为 TEXT_ENCODING_UTF8。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) \| undefined | TextBlob对象，用于后续绘制字形。创建失败时返回undefined。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

**示例**

参见 [makeFromString](#makefromstring)

## uniqueID

```TypeScript
uniqueID(): long
```

获取该TextBlob对象的唯一非零标识符。

**起始版本：** 23

<!--Device-TextBlob-uniqueID(): long--><!--Device-TextBlob-uniqueID(): long-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 返回TextBlob对象的唯一的非零标识符。 |

**示例**

ArkTS-Dyn:

```TypeScript
import { drawing } from "@kit.ArkGraphics2D";

let text : string = 'TextBlobUniqueId';
let font : drawing.Font = new drawing.Font();
font.setSize(100);
let textBlob = drawing.TextBlob.makeFromString(text, font, 0);
let id = textBlob.uniqueID();
console.info('uniqueID---------------' + id);
```

ArkTS-Sta示例：

```TypeScript
import { drawing } from "@kit.ArkGraphics2D";

let text: string = 'TextBlobUniqueId';
let font: drawing.Font = new drawing.Font();
font.setSize(100);
let textBlob = drawing.TextBlob.makeFromString(text, font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
if (textBlob != undefined) {
  let id = textBlob!.uniqueID();
  console.info("uniqueID---------------" + id);
}
```

