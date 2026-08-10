# LayoutManager

布局管理器对象。

> **说明：**
> 
> 文本内容变更后，需等待布局完成才可获取到最新的布局信息。

## 导入对象

以Text组件为例，完整示例请参考Text组件的  
[示例10（获取文本信息）](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md#示例10获取文本信息)。

```ts controller: TextController = new TextController();let layoutManager: LayoutManager = this.controller.getLayoutManager();```

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface LayoutManager--><!--Device-unnamed-declare interface LayoutManager-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

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

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-LayoutManager-getCharacterPositionAtCoordinate(x: number, y: number): PositionWithAffinity | undefined--><!--Device-LayoutManager-getCharacterPositionAtCoordinate(x: number, y: number): PositionWithAffinity | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | Yes | 相对于组件的横坐标。 &lt;br&gt;单位：[px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位) |
| y | number | Yes | 相对于组件的纵坐标。 &lt;br&gt;单位：[px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位) |

**Return value:**

| Type | Description |
| --- | --- |
| [PositionWithAffinity](arkts-arkui-positionwithaffinity-i.md) | 字符的位置信息。当[LayoutManager]{ |

## getCharacterPositionAtCoordinate

```TypeScript
getCharacterPositionAtCoordinate(
    x: number, y: number, encoding?: TextEncoding): PositionWithAffinity | undefined
```

根据指定编码类型，获取距离指定坐标最近的字符位置信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LayoutManager-getCharacterPositionAtCoordinate(    x: number, y: number, encoding?: TextEncoding): PositionWithAffinity | undefined--><!--Device-LayoutManager-getCharacterPositionAtCoordinate(    x: number, y: number, encoding?: TextEncoding): PositionWithAffinity | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | Yes | 相对于组件的横坐标。&lt;br&gt;单位：[px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位) |
| y | number | Yes | 相对于组件的纵坐标。&lt;br&gt;单位：[px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位) |
| encoding | [TextEncoding](arkts-arkui-textcommon-textencoding-e.md) | No | 字符位置使用的编码类型，默认值为**TextEncoding.TEXT_ENCODING_UTF8**。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PositionWithAffinity](arkts-arkui-positionwithaffinity-i.md) | 字符的位置信息。当[LayoutManager]{ |

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
| 字符索引范围 | [0, 3] | [3, 6] | [6, 7] | [7, 8] | [8, 9] | [9, 10] | [10, 11] |

其字形索引范围为[0, 7]，一个汉字占三个字符，所以其对应的字符索引范围为[0, 11]。如果指定的字形索引范围是[0, 11]，但字形一共只有7个，所以实际的字形索引范围是[0, 7]。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-LayoutManager-getCharacterRangeForGlyphRange(glyphRange: TextRange): Array<TextRange> | undefined--><!--Device-LayoutManager-getCharacterRangeForGlyphRange(glyphRange: TextRange): Array<TextRange> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| glyphRange | [TextRange](arkts-arkui-textrange-i.md) | Yes | 文本的字形范围。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;TextRange&gt; | 数组中含有两个元素，第一个元素是字符范围，第二个元素是实际的字形范围。 &lt;br&gt;当返回的范围是异常值时，范围内元素为-1。 &lt;br&gt;当[LayoutManager]{ |

## getCharacterRangeForGlyphRange

```TypeScript
getCharacterRangeForGlyphRange(glyphRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined
```

根据指定编码类型和文本字形范围，获取字符范围以及实际的字形范围。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LayoutManager-getCharacterRangeForGlyphRange(glyphRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined--><!--Device-LayoutManager-getCharacterRangeForGlyphRange(glyphRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| glyphRange | [TextRange](arkts-arkui-textrange-i.md) | Yes | 文本的字形范围。 |
| encoding | [TextEncoding](arkts-arkui-textcommon-textencoding-e.md) | No | 字符范围使用的编码类型，默认值为**TextEncoding.TEXT_ENCODING_UTF8**。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;TextRange&gt; | 数组中含有两个元素，第一个元素是字符范围，第二个元素是实际的字形范围。 &lt;br&gt;当返回的范围是异常值时，范围内元素为-1。 &lt;br&gt;当[LayoutManager]{ |

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

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LayoutManager-getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity--><!--Device-LayoutManager-getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | Yes | 相对于组件的横坐标。 &lt;br&gt;单位：[px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位) |
| y | number | Yes | 相对于组件的纵坐标。 &lt;br&gt;单位：[px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位) |

**Return value:**

| Type | Description |
| --- | --- |
| [PositionWithAffinity](arkts-arkui-positionwithaffinity-i.md) | 字形位置信息。当[LayoutManager]{ |

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
| 字符索引范围 | [0, 3] | [3, 6] | [6, 7] | [7, 8] | [8, 9] | [9, 10] | [10, 11] |

其中文本“世”的字形索引范围为[0, 1]，一个汉字占三个字符，所以其对应的字符索引范围为[0, 3]。如果指定的字符索引范围是[0, 1]，但无法解析出三分之一个汉字，所以实际的字符索引范围是[0, 3]。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-LayoutManager-getGlyphRangeForCharacterRange(charRange: TextRange): Array<TextRange> | undefined--><!--Device-LayoutManager-getGlyphRangeForCharacterRange(charRange: TextRange): Array<TextRange> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| charRange | [TextRange](arkts-arkui-textrange-i.md) | Yes | 文本的字符范围。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;TextRange&gt; | 数组中含有两个元素，第一个元素是字形范围，第二个元素是实际的字符范围。 &lt;br&gt;当返回的范围是异常值时，范围内元素为-1。 &lt;br&gt;当[LayoutManager]{ |

## getGlyphRangeForCharacterRange

```TypeScript
getGlyphRangeForCharacterRange(charRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined
```

根据指定编码类型和文本字符范围，获取字形范围以及实际的字符范围。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LayoutManager-getGlyphRangeForCharacterRange(charRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined--><!--Device-LayoutManager-getGlyphRangeForCharacterRange(charRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| charRange | [TextRange](arkts-arkui-textrange-i.md) | Yes | 文本的字符范围。 |
| encoding | [TextEncoding](arkts-arkui-textcommon-textencoding-e.md) | No | 字符范围使用的编码类型，默认值为**TextEncoding.TEXT_ENCODING_UTF8**。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;TextRange&gt; | 数组中含有两个元素，第一个元素是字形范围，第二个元素是实际的字符范围。 &lt;br&gt;当返回的范围是异常值时，范围内元素为-1。 &lt;br&gt;当[LayoutManager]{ |

## getLineCount

```TypeScript
getLineCount(): number
```

获取组件内容的总行数。

> **说明：**
> 
> 文本内容变更后，需等待布局完成才可获取到最新的总行数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LayoutManager-getLineCount(): number--><!--Device-LayoutManager-getLineCount(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | 组件内容的总行数。当[LayoutManager]{ |

## getLineMetrics

```TypeScript
getLineMetrics(lineNumber: number): LineMetrics
```

获取指定行的行信息、文本样式信息、以及字体属性信息。

> **说明：**
> 
> 文本内容变更后，需等待布局完成才可获取到最新的行信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LayoutManager-getLineMetrics(lineNumber: number): LineMetrics--><!--Device-LayoutManager-getLineMetrics(lineNumber: number): LineMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lineNumber | number | Yes | 行号，取值范围[0, 实际行数-1]，从0开始。当行号小于0或超出实际行数时，返回无效值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LineMetrics](arkts-arkui-linemetrics-t.md) | 行信息、文本样式信息、以及字体属性信息。 &lt;br&gt;当行号小于0或超出实际行，返回无效值。当[LayoutManager]{ |

## getRectsForRange

```TypeScript
getRectsForRange(range: TextRange, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>
```

根据给定的矩形区域宽度样式和高度样式，获取文本中任意区间范围内的字符或占位符所占的绘制区域信息。

> **说明：**
> 
> 文本内容变更后，需等待布局完成才可获取到最新的绘制区域信息。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-LayoutManager-getRectsForRange(range: TextRange, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>--><!--Device-LayoutManager-getRectsForRange(range: TextRange, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [TextRange](arkts-arkui-textrange-i.md) | Yes | 需要获取的区域的文本区间。 |
| widthStyle | [RectWidthStyle](arkts-arkui-rectwidthstyle-t.md) | Yes | 返回的矩形区域的宽度规格，用于控制返回矩形的宽度计算方式，不同规格值会影响矩形的宽度边界。 |
| heightStyle | [RectHeightStyle](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-rectheightstyle-e.md) | Yes | 返回的矩形区域的高度规格，用于控制返回矩形的高度计算方式，不同规格值会影响矩形的高度边界。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;TextBox&gt; | 矩形区域数组。当[LayoutManager]{ |

