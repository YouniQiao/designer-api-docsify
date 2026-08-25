# TextLine

描述段落基础文本行结构的载体。下列API示例中都需先使用[Paragraph](arkts-arkgraphics2d-text-paragraph-c.md)类的[getTextLines()](arkts-arkgraphics2d-text-paragraph-c.md#gettextlines)接口或者 [LineTypeset](arkts-arkgraphics2d-text-linetypeset-c.md)类的[createLine()](arkts-arkgraphics2d-text-linetypeset-c.md#createline)接口获取到TextLine对象实例，再通过此实例调用对 应方法。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## createTruncatedLine

```TypeScript
createTruncatedLine(width: number, ellipsisMode: EllipsisMode, ellipsis: string): TextLine
```

创建一个截断的文本行对象。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |
| ellipsisMode | [EllipsisMode](arkts-arkgraphics2d-text-ellipsismode-e.md) | 是 |
| [ellipsis](arkts-arkgraphics2d-text-textstyle-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| [TextLine](arkts-arkgraphics2d-text-textline-c.md) |

## enumerateCaretOffsets

```TypeScript
enumerateCaretOffsets(callback: CaretOffsetsCallback): void
```

枚举文本行中每个字符的偏移量和索引值。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [CaretOffsetsCallback](arkts-arkgraphics2d-text-caretoffsetscallback-t.md) | 是 |

## getAlignmentOffset

```TypeScript
getAlignmentOffset(alignmentFactor: number, alignmentWidth: number): number
```

获取文本行根据对齐因子和对齐宽度计算的对齐所需偏移量。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alignmentFactor | number | 是 |
| alignmentWidth | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getGlyphCount

```TypeScript
getGlyphCount(): number
```

获取文本行中字形的数量。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getGlyphRuns

```TypeScript
getGlyphRuns(): Array<Run>
```

获取文本行的排版单元数组。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array&lt;[Run](arkts-arkgraphics2d-text-run-c.md)&gt; |

## getImageBounds

```TypeScript
getImageBounds(): common2D.Rect
```

获取文本行的图像边界。文本行图像边界与排版字体、排版字号、字符本身都有关，相当于视觉边界。例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格，用户在界面上只能看到"a b"，图像边界即为不包括带行首 和末尾空格的边界。例如字符串为"j"或"E"，视觉边界不同，即与字符本身有关，"j"字符串的视觉边界宽度小于"E"字符串的视觉边界宽度，"j"字符串的视觉边界高度大于"E"字符串的视觉边界高度。

> **说明：**&gt;
> 示意图展示了字符串为" a b "的图像边界。&gt;
> &gt;
> 示意图展示了字符串为"j"或"E"的图像边界。&gt;
> 

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Rect |

## getOffsetForStringIndex

```TypeScript
getOffsetForStringIndex(index: number): number
```

获取文本行中给定字符串索引处的偏移量。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getStringIndexForPosition

```TypeScript
getStringIndexForPosition(point: common2D.Point): number
```

获取给定位置在原始字符串中的字符索引。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | common2D.Point | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getTextRange

```TypeScript
getTextRange(): Range
```

获取该行文本在整个段落文本中的索引区间。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) |

## getTrailingSpaceWidth

```TypeScript
getTrailingSpaceWidth(): number
```

获取文本行尾部空白字符的宽度。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getTypographicBounds

```TypeScript
getTypographicBounds(): TypographicBounds
```

获取文本行的排版边界。文本行排版边界与排版字体、排版字号有关，与字符本身无关。例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格，排版边界就包括行首和末尾空格的边界。例如字符串为"j"或"E"，排版 边界相同，即与字符本身无关。

> **说明：**&gt;
> 示意图展示了字符串为" a b "的排版边界。&gt;
> &gt;
> 示意图展示了字符串为"j"或"E"的排版边界。&gt;
> !
> [TypographicBounds-Character.png](../../../reference/apis-arkgraphics2d/figures/TypographicBounds-Character.png)

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [TypographicBounds](arkts-arkgraphics2d-text-typographicbounds-i.md) |

## paint

```TypeScript
paint(canvas: drawing.Canvas, x: number, y: number): void
```

在画布上以坐标点(x, y)为左上角位置绘制该文本行。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| canvas | drawing.Canvas | 是 |
| x | number | 是 |
| y | number | 是 |
