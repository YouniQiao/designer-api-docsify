# LayoutManager

布局管理器对象。

> **说明：**&gt;
> 文本内容变更后，需等待布局完成才可获取到最新的布局信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## getCharacterPositionAtCoordinate

```TypeScript
getCharacterPositionAtCoordinate(x: double, y: double): PositionWithAffinity | undefined
```

获取距离指定坐标最近的字符的位置信息。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | double | 是 |
| y | double | 是 |

**返回值：**

| 类型 |
| --- |
| [PositionWithAffinity](arkts-arkui-textcommon-positionwithaffinity-i.md) \| undefined |

## getCharacterPositionAtCoordinate

```TypeScript
getCharacterPositionAtCoordinate(x: double, y: double, encoding?: TextEncoding): PositionWithAffinity | undefined
```

根据指定编码类型，获取距离指定坐标最近的字符位置信息。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | double | 是 |
| y | double | 是 |
| encoding | [TextEncoding](arkts-arkui-textcommon-textencoding-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PositionWithAffinity](arkts-arkui-textcommon-positionwithaffinity-i.md) \| undefined |

## getCharacterRangeForGlyphRange

```TypeScript
getCharacterRangeForGlyphRange(glyphRange: TextRange): Array<TextRange> | undefined
```

根据给定的文本字形范围来获取范围内的字符范围，以及实际的字形范围。例如文本为"世界Hello"，其字形索引范围为[0, 7]，一个汉字占三个字符，所以其对应的字符索引范围为[0, 11]。如果指定的索引范围是[0, 11]，但 字形一共只有7个，所以实际的字形索引范围是[0, 7]。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| glyphRange | [TextRange](arkts-arkui-textcommon-textrange-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[TextRange](arkts-arkui-textcommon-textrange-i.md)&gt; \| undefined |

## getCharacterRangeForGlyphRange

```TypeScript
getCharacterRangeForGlyphRange(glyphRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined
```

根据指定编码类型和文本字形范围，获取字符范围以及实际的字形范围。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| glyphRange | [TextRange](arkts-arkui-textcommon-textrange-i.md) | 是 |
| encoding | [TextEncoding](arkts-arkui-textcommon-textencoding-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[TextRange](arkts-arkui-textcommon-textrange-i.md)&gt; \| undefined |

## getGlyphPositionAtCoordinate

```TypeScript
getGlyphPositionAtCoordinate(x: double, y: double): PositionWithAffinity | undefined
```

获取较为接近给定坐标的字形的位置信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | double | 是 |
| y | double | 是 |

**返回值：**

| 类型 |
| --- |
| [PositionWithAffinity](arkts-arkui-textcommon-positionwithaffinity-i.md) \| undefined |

## getGlyphRangeForCharacterRange

```TypeScript
getGlyphRangeForCharacterRange(charRange: TextRange): Array<TextRange> | undefined
```

根据给定的文本字符范围来获取范围内的字形范围，以及实际的字符范围。例如文本为"世界Hello"，其中文本"世"的字形索引范围为[0, 1]，一个汉字占三个字符，所以其对应的字符索引范围为[0, 3]。如果指定的字符索引范围是 [0, 1]，但无法解析出三分之一个汉字，所以实际的字符索引范围是[0, 3]。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| charRange | [TextRange](arkts-arkui-textcommon-textrange-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[TextRange](arkts-arkui-textcommon-textrange-i.md)&gt; \| undefined |

## getGlyphRangeForCharacterRange

```TypeScript
getGlyphRangeForCharacterRange(charRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined
```

根据指定编码类型和文本字符范围，获取字形范围以及实际的字符范围。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| charRange | [TextRange](arkts-arkui-textcommon-textrange-i.md) | 是 |
| encoding | [TextEncoding](arkts-arkui-textcommon-textencoding-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[TextRange](arkts-arkui-textcommon-textrange-i.md)&gt; \| undefined |

## getLineCount

```TypeScript
getLineCount(): int | undefined
```

获取组件内容的总行数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| int \| undefined |

## getLineMetrics

```TypeScript
getLineMetrics(lineNumber: int): LineMetrics | undefined
```

ArkTS-Sta: getLineMetrics(lineNumber: int): LineMetrics | undefined获取指定行的行信息、文本样式信息、以及字体属性信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [lineNumber](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-linemetrics-i.md) | int | 是 |

**返回值：**

| 类型 |
| --- |
| [LineMetrics](arkts-arkui-linemetrics-t.md) \| undefined |

## getRectsForRange

```TypeScript
getRectsForRange(range: TextRange, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox> | undefined
```

获取给定的矩形区域宽度以及矩形区域高度的规格下，文本中任意区间范围内的字符或占位符所占的绘制区域信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [TextRange](arkts-arkui-textcommon-textrange-i.md) | 是 |
| widthStyle | [RectWidthStyle](arkts-arkui-rectwidthstyle-t.md) | 是 |
| heightStyle | [RectHeightStyle](arkts-arkui-rectheightstyle-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[TextBox](arkts-arkui-textbox-t.md)&gt; \| undefined |
