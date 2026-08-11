# LayoutManager

布局管理器对象。

> **说明：**
> 
> 文本内容变更后，需等待布局完成才可获取到最新的布局信息。

## 导入对象

以Text组件为例，完整示例请参考Text组件的  
[示例10（获取文本信息）](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md#示例10获取文本信息)。

```ts controller: TextController = new TextController();let layoutManager: LayoutManager = this.controller.getLayoutManager();```

**起始版本：** 12

<!--Device-unnamed-declare interface LayoutManager--><!--Device-unnamed-declare interface LayoutManager-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## getCharacterPositionAtCoordinate

```TypeScript
getCharacterPositionAtCoordinate(x: number, y: number): PositionWithAffinity | undefined
```

获取距离指定坐标最近的字符的位置信息。

> **说明：**
> 
> - 字形（Glyph）是文本渲染的基本单元，与字符（Character）可能存在一对多关系。如需获取字形级别的位置信息，可使用
> [getGlyphPositionAtCoordinate](arkts-arkui-layoutmanager-i.md#getglyphpositionatcoordinate)方法。
> 
> - 文本内容变更后，需等待布局完成才可获取到最新的位置信息。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-LayoutManager-getCharacterPositionAtCoordinate(x: number, y: number): PositionWithAffinity | undefined--><!--Device-LayoutManager-getCharacterPositionAtCoordinate(x: number, y: number): PositionWithAffinity | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| [PositionWithAffinity](arkts-arkui-positionwithaffinity-i.md) |

## getCharacterPositionAtCoordinate

```TypeScript
getCharacterPositionAtCoordinate(
    x: number, y: number, encoding?: TextEncoding): PositionWithAffinity | undefined
```

根据指定编码类型，获取距离指定坐标最近的字符位置信息。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-LayoutManager-getCharacterPositionAtCoordinate(    x: number, y: number, encoding?: TextEncoding): PositionWithAffinity | undefined--><!--Device-LayoutManager-getCharacterPositionAtCoordinate(    x: number, y: number, encoding?: TextEncoding): PositionWithAffinity | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| encoding | [TextEncoding](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-drawing-textencoding-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PositionWithAffinity](arkts-arkui-positionwithaffinity-i.md) |

## getCharacterRangeForGlyphRange

```TypeScript
getCharacterRangeForGlyphRange(glyphRange: TextRange): Array<TextRange> | undefined
```

根据给定的文本字形范围来获取范围内的字符范围，以及实际的字形范围。

> **说明：**
> 
> 文本内容变更后，需等待布局完成才可获取到最新的字符范围信息。
> 以文本“世界Hello”为例，其字形索引与字符索引的对应关系如下：

| 文本 | 世 | 界 | H | e | l | l | o |
|---|---|---|---|---|---|---|---|
| 字形索引范围 | [0, 1] | [1, 2] | [2, 3] | [3, 4] | [4, 5] | [5, 6] | [6, 7] |
| 字符索引范围 | [0, 3] | [3, 6] | [6, 7] | [7, 8] | [8, 9] | [9, 10] |

其字形索引范围为[0, 7]，一个汉字占三个字符，所以其对应的字符索引范围为[0, 11]。如果指定的字形索引范围是[0, 11]，但字形一共只有7个，所以实际的字形索引范围是[0, 7]。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-LayoutManager-getCharacterRangeForGlyphRange(glyphRange: TextRange): Array<TextRange> | undefined--><!--Device-LayoutManager-getCharacterRangeForGlyphRange(glyphRange: TextRange): Array<TextRange> | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| glyphRange | [TextRange](arkts-arkui-textrange-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;TextRange&gt; |

## getCharacterRangeForGlyphRange

```TypeScript
getCharacterRangeForGlyphRange(glyphRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined
```

根据指定编码类型和文本字形范围，获取字符范围以及实际的字形范围。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-LayoutManager-getCharacterRangeForGlyphRange(glyphRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined--><!--Device-LayoutManager-getCharacterRangeForGlyphRange(glyphRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| glyphRange | [TextRange](arkts-arkui-textrange-i.md) | 是 |
| encoding | [TextEncoding](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-drawing-textencoding-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;TextRange&gt; |

## getGlyphPositionAtCoordinate

```TypeScript
getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity
```

获取较为接近给定坐标的字形的位置信息。

> **说明：**
> 
> - 字形（Glyph）是文本渲染的基本单元，与字符（Character）可能存在一对多关系。如需获取字符级别的位置信息，可使用
> [getCharacterPositionAtCoordinate](arkts-arkui-layoutmanager-i.md#getcharacterpositionatcoordinate)方法。
> 
> - 文本内容变更后，需等待布局完成才可获取到最新的位置信息。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LayoutManager-getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity--><!--Device-LayoutManager-getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| [PositionWithAffinity](arkts-arkui-positionwithaffinity-i.md) |

## getGlyphRangeForCharacterRange

```TypeScript
getGlyphRangeForCharacterRange(charRange: TextRange): Array<TextRange> | undefined
```

根据给定的文本字符范围来获取范围内的字形范围，以及实际的字符范围。

> **说明：**
> 
> 文本内容变更后，需等待布局完成才可获取到最新的字形范围信息。
> 以文本“世界Hello”为例，其字形索引与字符索引的对应关系如下：

| 文本 | 世 | 界 | H | e | l | l | o |
|---|---|---|---|---|---|---|---|
| 字形索引范围 | [0, 1] | [1, 2] | [2, 3] | [3, 4] | [4, 5] | [5, 6] | [6, 7] |
| 字符索引范围 | [0, 3] | [3, 6] | [6, 7] | [7, 8] | [8, 9] | [9, 10] |

其中文本“世”的字形索引范围为[0, 1]，一个汉字占三个字符，所以其对应的字符索引范围为[0, 3]。如果指定的字符索引范围是[0, 1]，但无法解析出三分之一个汉字，所以实际的字符索引范围是[0, 3]。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-LayoutManager-getGlyphRangeForCharacterRange(charRange: TextRange): Array<TextRange> | undefined--><!--Device-LayoutManager-getGlyphRangeForCharacterRange(charRange: TextRange): Array<TextRange> | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| charRange | [TextRange](arkts-arkui-textrange-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;TextRange&gt; |

## getGlyphRangeForCharacterRange

```TypeScript
getGlyphRangeForCharacterRange(charRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined
```

根据指定编码类型和文本字符范围，获取字形范围以及实际的字符范围。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-LayoutManager-getGlyphRangeForCharacterRange(charRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined--><!--Device-LayoutManager-getGlyphRangeForCharacterRange(charRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| charRange | [TextRange](arkts-arkui-textrange-i.md) | 是 |
| encoding | [TextEncoding](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-drawing-textencoding-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;TextRange&gt; |

## getLineCount

```TypeScript
getLineCount(): number
```

获取组件内容的总行数。

> **说明：**
> 
> 文本内容变更后，需等待布局完成才可获取到最新的总行数。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LayoutManager-getLineCount(): number--><!--Device-LayoutManager-getLineCount(): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getLineMetrics

```TypeScript
getLineMetrics(lineNumber: number): LineMetrics
```

获取指定行的行信息、文本样式信息、以及字体属性信息。

> **说明：**
> 
> 文本内容变更后，需等待布局完成才可获取到最新的行信息。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-LayoutManager-getLineMetrics(lineNumber: number): LineMetrics--><!--Device-LayoutManager-getLineMetrics(lineNumber: number): LineMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| lineNumber | number | 是 |

**返回值：**

| 类型 |
| --- |
| [LineMetrics](arkts-arkui-linemetrics-t.md) |

## getRectsForRange

```TypeScript
getRectsForRange(range: TextRange, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>
```

根据给定的矩形区域宽度样式和高度样式，获取文本中任意区间范围内的字符或占位符所占的绘制区域信息。

> **说明：**
> 
> 文本内容变更后，需等待布局完成才可获取到最新的绘制区域信息。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-LayoutManager-getRectsForRange(range: TextRange, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>--><!--Device-LayoutManager-getRectsForRange(range: TextRange, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [TextRange](arkts-arkui-textrange-i.md) | 是 |
| widthStyle | [RectWidthStyle](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-rectwidthstyle-e.md) | 是 |
| heightStyle | [RectHeightStyle](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-rectheightstyle-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;TextBox&gt; |
