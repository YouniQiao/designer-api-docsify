# Paragraph

保存文本内容及样式的载体，支持排版与绘制操作。下列API示例中都需先使用[ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md)类的[build()](arkts-arkgraphics2d-text-paragraphbuilder-c.md#build)接口获取到 Paragraph对象实例，再通过此实例调用对应方法。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## didExceedMaxLines

```TypeScript
didExceedMaxLines(): boolean
```

返回段落是否超过最大行数。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## forceReuseRasterResult

```TypeScript
forceReuseRasterResult(isForce: boolean): void
```

设置是否强制复用光栅化结果。不调用此接口时，系统默认允许更新光栅化结果。适用于文本内容未发生变化但需要多次调用[paint](#paint)绘制的场景，通过复用光栅化结果可避免重复光栅化计算以提升绘制性能。设置后，在下次调用 [paint](#paint)绘制时生效。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isForce | boolean | 是 |

## getActualTextRange

```TypeScript
getActualTextRange(lineNumber: number, includeSpaces: boolean): Range
```

获取指定行的实际可见文本范围，不包括溢出的省略号。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [lineNumber](arkts-arkgraphics2d-text-linemetrics-i.md) | number | 是 |
| includeSpaces | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) |

## getAlphabeticBaseline

```TypeScript
getAlphabeticBaseline(): number
```

获取拉丁字母基线位置。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getCharacterPositionAtCoordinate

```TypeScript
getCharacterPositionAtCoordinate(x: number, y: number, encoding: drawing.TextEncoding): PositionWithAffinity
```

获取与给定坐标最接近的字符位置信息。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| encoding | drawing.TextEncoding | 是 |

**返回值：**

| 类型 |
| --- |
| [PositionWithAffinity](../../apis-arkui/arkts-apis/arkts-arkui-positionwithaffinity-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |

## getCharacterRangeForGlyphRange

```TypeScript
getCharacterRangeForGlyphRange(glyphRange: Range, encoding: drawing.TextEncoding): Array<Range>
```

获取指定字形范围对应的字符范围。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| glyphRange | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | 是 |
| encoding | drawing.TextEncoding | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;Range & gt; |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |

## getGlyphPositionAtCoordinate

```TypeScript
getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity
```

获取与给定坐标最接近的字形位置信息。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| [PositionWithAffinity](../../apis-arkui/arkts-apis/arkts-arkui-positionwithaffinity-i.md) |

## getGlyphRangeForCharacterRange

```TypeScript
getGlyphRangeForCharacterRange(characterRange: Range, encoding: drawing.TextEncoding): Array<Range>
```

获取指定字符范围对应的字形范围。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| characterRange | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | 是 |
| encoding | drawing.TextEncoding | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;Range & gt; |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |

## getHeight

```TypeScript
getHeight(): number
```

获取文本总高度。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getIdeographicBaseline

```TypeScript
getIdeographicBaseline(): number
```

获取表意字（如CJK（中文，日文，韩文））下的基线位置。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getLineCount

```TypeScript
getLineCount(): number
```

返回文本行数。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getLineHeight

```TypeScript
getLineHeight(line: number): number
```

返回指定行的行高。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| line | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getLineMetrics

```TypeScript
getLineMetrics(): Array<LineMetrics>
```

获取文本行的行度量数组。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array & lt;LineMetrics & gt; |

## getLineMetrics

```TypeScript
getLineMetrics(lineNumber: number): LineMetrics | undefined
```

获取特定行号的行度量信息。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [lineNumber](arkts-arkgraphics2d-text-linemetrics-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| LineMetrics \| undefined |

## getLineWidth

```TypeScript
getLineWidth(line: number): number
```

返回指定行的行宽。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| line | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getLongestLine

```TypeScript
getLongestLine(): number
```

获取文本最长行宽。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getLongestLineWithIndent

```TypeScript
getLongestLineWithIndent(): number
```

获取文本最长一行的宽度（包含缩进），建议向上取整。文本内容为空时返回0。

**起始版本：** 13

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getMaxIntrinsicWidth

```TypeScript
getMaxIntrinsicWidth(): number
```

获取段落最大固有宽度。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getMaxWidth

```TypeScript
getMaxWidth(): number
```

获取文本最大行宽。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getMinIntrinsicWidth

```TypeScript
getMinIntrinsicWidth(): number
```

获取段落最小固有宽度。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getParagraphStyle

```TypeScript
getParagraphStyle(): ParagraphStyle
```

获取段落的样式配置。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md) |

## getProcessState

```TypeScript
getProcessState(): TextProcessState
```

获取段落的文本处理状态。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [TextProcessState](arkts-arkgraphics2d-text-textprocessstate-e.md) |

## getRectsForPlaceholders

```TypeScript
getRectsForPlaceholders(): Array<TextBox>
```

获取文本中所有占位符所占的矩形区域。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array & lt;TextBox & gt; |

## getRectsForRange

```TypeScript
getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>
```

获取给定的矩形区域宽度以及矩形区域高度的规格下，文本中该区间范围内的字符所占的矩形区域。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | 是 |
| widthStyle | [RectWidthStyle](arkts-arkgraphics2d-text-rectwidthstyle-e.md) | 是 |
| heightStyle | [RectHeightStyle](arkts-arkgraphics2d-text-rectheightstyle-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;TextBox & gt; |

## getTextDisplayState

```TypeScript
getTextDisplayState(): TextDisplayState
```

获取段落的文本显示状态。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [TextDisplayState](arkts-arkgraphics2d-text-textdisplaystate-e.md) |

## getTextLines

```TypeScript
getTextLines(): Array<TextLine>
```

返回所有的文本行。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array&lt;[TextLine](arkts-arkgraphics2d-text-textline-c.md)&gt; |

## getVisibleTextRanges

```TypeScript
getVisibleTextRanges(): Array<Range>
```

获取段落中在屏幕上可见的文本范围。不包含因最大行数（[ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md)的maxLines属性）截断或省略号模式（ [EllipsisMode](arkts-arkgraphics2d-text-ellipsismode-e.md)）替换而未显示的文本。  
**说明：**返回的范围取决于段落的具体截断情况（如是否设置最大行数或省略号等）： | 场景 | 说明 | |---|---| | 文本未被截断 | 范围包含全部已排版文本 | | 仅设置maxLines截断（未设置省略号） | 范围为实际显示的文本，即第一行至第maxLines行末尾的文本。 | | 尾部省略（EllipsisMode.END） | 范围为省略号之前的文本。 | | 头部省略（EllipsisMode.START） | 范围为省略号之后的文本。 | | 中部省略（EllipsisMode.MIDDLE） | 第一个范围为省略号之前的文本，第二个范围为省略号之后的文本。 | | 多行头部省略（EllipsisMode.MULTILINE_START） | 同中部省略，返回省略号前后的文本范围。 | | 多行中部省略（EllipsisMode.MULTILINE_MIDDLE） | 同中部省略，返回省略号前后的文本范围。 |

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array & lt;Range & gt; |

## getWordBoundary

```TypeScript
getWordBoundary(offset: number): Range
```

返回给定offset的字形所在单词的索引区间。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) |

## layout

```TypeScript
layout(width: number): Promise<void>
```

进行排版并计算所有字形位置，使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## layoutSync

```TypeScript
layoutSync(width: number): void
```

进行排版并计算所有字形位置。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |

## layoutWithConstraints

```TypeScript
layoutWithConstraints(size: TextRectSize): TextLayoutResult
```

使用给定的高度和宽度进行排版并计算所有字形的位置。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | [TextRectSize](arkts-arkgraphics2d-text-textrectsize-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TextLayoutResult](arkts-arkgraphics2d-text-textlayoutresult-i.md) |

## paint

```TypeScript
paint(canvas: drawing.Canvas, x: number, y: number): void
```

在画布上以 (x, y) 为左上角绘制文本。调用前必须先调用[layout()](#layout)接口进行排版，否则无法正确显示文本内容。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| canvas | drawing.Canvas | 是 |
| x | number | 是 |
| y | number | 是 |

## paintOnPath

```TypeScript
paintOnPath(canvas: drawing.Canvas, path: drawing.Path, hOffset: number, vOffset: number): void
```

在画布上沿路径绘制文本。调用前必须先调用[layout()](#layout)接口进行排版，否则无法正确显示文本内容。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| canvas | drawing.Canvas | 是 |
| path | drawing.Path | 是 |
| hOffset | number | 是 |
| vOffset | number | 是 |

## updateColor

```TypeScript
updateColor(color: common2D.Color): void
```

更新整个文本段落的颜色。如果当前装饰线未设置颜色，使用该接口也会同时更新装饰线的颜色。

**起始版本：** 20

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | common2D.Color | 是 |

## updateDecoration

```TypeScript
updateDecoration(decoration: Decoration): void
```

更新整个文本段落的装饰线。

**起始版本：** 20

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| decoration | [Decoration](arkts-arkgraphics2d-text-decoration-i.md) | 是 |
