# Run

文本排版单元，表示一段具有相同样式属性的连续文本片段。Run由[TextLine](arkts-arkgraphics2d-text-textline-c.md)类的[getGlyphRuns()](arkts-arkgraphics2d-text-textline-c.md#getglyphruns)接 口获取。下列API示例中都需先使用[TextLine](arkts-arkgraphics2d-text-textline-c.md)类的[getGlyphRuns()](arkts-arkgraphics2d-text-textline-c.md#getglyphruns)接口获取Run对象实例，再通过此实例调 用对应方法。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## getAdvances

```TypeScript
getAdvances(range: Range): Array<common2D.Point>
```

获取该排版单元指定范围内每个字形的字形宽度数组。

**起始版本：** 20

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;common2D.Point & gt; |

## getFont

```TypeScript
getFont(): drawing.Font
```

获取排版单元的字体属性对象。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| drawing.Font |

## getGlyphCount

```TypeScript
getGlyphCount(): number
```

获取该排版单元中字形的数量。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getGlyphs

```TypeScript
getGlyphs(): Array<number>
```

获取该排版单元中每个字符的字形序号。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array & lt;number & gt; |

## getGlyphs

```TypeScript
getGlyphs(range: Range): Array<number>
```

获取该排版单元指定范围内每个字符的字形序号。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;number & gt; |

## getImageBounds

```TypeScript
getImageBounds(): common2D.Rect
```

获取该排版单元的图像边界，图像边界与排版字体、排版字号、字符本身都有关，相当于视觉边界，例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格，用户在界面上只能看到"a b"，图像边界即为不包括带行首和 末尾空格的边界。

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

## getOffsets

```TypeScript
getOffsets(): Array<common2D.Point>
```

获取该排版单元中每个字形的索引偏移量。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array & lt;common2D.Point & gt; |

## getPositions

```TypeScript
getPositions(): Array<common2D.Point>
```

获取该排版单元中每个字形相对于每行的字形位置。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array & lt;common2D.Point & gt; |

## getPositions

```TypeScript
getPositions(range: Range): Array<common2D.Point>
```

获取该排版单元指定范围内每个字形相对于每行的字形位置数组。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;common2D.Point & gt; |

## getStringIndices

```TypeScript
getStringIndices(range?: Range): Array<number>
```

获取排版单元指定范围内字形的字符索引，该索引是相对于整个段落的偏移。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;number & gt; |

## getStringRange

```TypeScript
getStringRange(): Range
```

获取排版单元生成字形的字符范围。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) |

## getTextDirection

```TypeScript
getTextDirection(): TextDirection
```

获取该排版单元的文本方向。

**起始版本：** 20

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [TextDirection](arkts-arkgraphics2d-text-textdirection-e.md) |

## getTextStyle

```TypeScript
getTextStyle(): TextStyle
```

获取该排版单元的文本样式。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [TextStyle](arkts-arkgraphics2d-text-textstyle-i.md) |

## getTypographicBounds

```TypeScript
getTypographicBounds(): TypographicBounds
```

获取该排版单元的排版边界，排版边界与排版字体、排版字号有关，与字符本身无关，例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格，排版边界就包括行首和末尾空格的边界。

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

在画布上以(x, y)为左上角位置绘制排版单元。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| canvas | drawing.Canvas | 是 |
| x | number | 是 |
| y | number | 是 |
