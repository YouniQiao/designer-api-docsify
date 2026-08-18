# TextBlob

TextBlob是由一个或多个具有相同字型的字符组成的字块。支持通过文本、字符串、RunBuffer等多种方式创建字形集合，适用于需要批量渲染文本或获取文字边界框的场景。 > **说明：** > > - 本模块使用屏幕物理像素单位px。 > > - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 23

<!--Device-drawing-class TextBlob--><!--Device-drawing-class TextBlob-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
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

| 类型 |
| --- |
| common2D.Rect |

## bounds

```TypeScript
bounds(): common2D.Rect | undefined
```

获取文字边界框的矩形区域。

**起始版本：** 23

<!--Device-TextBlob-bounds(): common2D.Rect | undefined--><!--Device-TextBlob-bounds(): common2D.Rect | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Rect |

## makeFromPosText

```TypeScript
static makeFromPosText(text: string, len: number, points: common2D.Point[], font: Font): TextBlob
```

使用文本创建TextBlob对象，其中每个字形的坐标由points中对应的坐标信息决定。

**起始版本：** 12

<!--Device-TextBlob-static makeFromPosText(text: string, len: number, points: common2D.Point[], font: Font): TextBlob--><!--Device-TextBlob-static makeFromPosText(text: string, len: number, points: common2D.Point[], font: Font): TextBlob-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| len | number | 是 |
| points | common2D.Point[] | 是 |
| font | [Font](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-font-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## makeFromPosText

```TypeScript
static makeFromPosText(text: string, len: number, points: common2D.Point[], font: Font): TextBlob | undefined
```

使用文本创建TextBlob对象，其中每个字形的坐标由points中对应的坐标信息决定。

**起始版本：** 23

<!--Device-TextBlob-static makeFromPosText(text: string, len: int, points: common2D.Point[], font: Font): TextBlob | undefined--><!--Device-TextBlob-static makeFromPosText(text: string, len: int, points: common2D.Point[], font: Font): TextBlob | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| len | number | 是 |
| points | common2D.Point[] | 是 |
| font | [Font](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-font-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## makeFromRunBuffer

```TypeScript
static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob
```

基于RunBuffer信息创建TextBlob对象。

**起始版本：** 11

<!--Device-TextBlob-static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob--><!--Device-TextBlob-static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pos | Array&lt;[TextBlobRunBuffer](arkts-arkgraphics2d-drawing-textblobrunbuffer-i.md)&gt; | 是 |
| font | [Font](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-font-c.md) | 是 |
| [bounds](arkts-arkgraphics2d-drawing-textblob-c.md) | common2D.Rect | 否 |

**返回值：**

| 类型 |
| --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## makeFromRunBuffer

```TypeScript
static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob | undefined
```

基于RunBuffer信息创建TextBlob对象。

**起始版本：** 23

<!--Device-TextBlob-static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob | undefined--><!--Device-TextBlob-static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pos | Array&lt;[TextBlobRunBuffer](arkts-arkgraphics2d-drawing-textblobrunbuffer-i.md)&gt; | 是 |
| font | [Font](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-font-c.md) | 是 |
| [bounds](arkts-arkgraphics2d-drawing-textblob-c.md) | common2D.Rect | 否 |

**返回值：**

| 类型 |
| --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## makeFromString

```TypeScript
static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob
```

根据指定的编码类型和字型，使用string类型的值创建TextBlob对象。

**起始版本：** 11

<!--Device-TextBlob-static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob--><!--Device-TextBlob-static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| font | [Font](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-font-c.md) | 是 |
| encoding | [TextEncoding](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-textencoding-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## makeFromString

```TypeScript
static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob | undefined
```

根据指定的编码类型和字型，使用string类型的值创建TextBlob对象

**起始版本：** 23

<!--Device-TextBlob-static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob | undefined--><!--Device-TextBlob-static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| font | [Font](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-font-c.md) | 是 |
| encoding | [TextEncoding](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-textencoding-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## uniqueID

```TypeScript
uniqueID(): number
```

获取该TextBlob对象的唯一非零标识符。

**起始版本：** 23

<!--Device-TextBlob-uniqueID(): long--><!--Device-TextBlob-uniqueID(): long-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |
