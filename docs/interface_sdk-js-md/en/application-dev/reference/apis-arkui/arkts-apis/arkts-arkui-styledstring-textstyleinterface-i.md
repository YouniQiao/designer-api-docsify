# TextStyleInterface

TextStyleInterface

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TextStyleInterface--><!--Device-unnamed-export declare interface TextStyleInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: ResourceColor
```

字体颜色。

默认为主题色。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyleInterface-fontColor?: ResourceColor--><!--Device-TextStyleInterface-fontColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontConfigs

```TypeScript
fontConfigs?: FontConfigs
```

字体配置。默认值继承[FontConfigs](../../../reference/apis-arkui/arkui-ts/ts-text-common.md#fontconfigs24)。

**Type:** [FontConfigs](arkts-arkui-fontconfigs-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyleInterface-fontConfigs?: FontConfigs--><!--Device-TextStyleInterface-fontConfigs?: FontConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontFamily

```TypeScript
fontFamily?: ResourceStr
```

文本字体。

默认为主题字体。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyleInterface-fontFamily?: ResourceStr--><!--Device-TextStyleInterface-fontFamily?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize?: LengthMetrics
```

字体大小。

默认字体大小为16fp。

如果LengthMetrics的unit值是PERCENT，当前设置不生效，处理为16fp。

单位：[fp](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位)

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyleInterface-fontSize?: LengthMetrics--><!--Device-TextStyleInterface-fontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontStyle

```TypeScript
fontStyle?: FontStyle
```

字体样式。

默认值：FontStyle.Normal

**Type:** [FontStyle](arkts-arkui-fontstyle-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyleInterface-fontStyle?: FontStyle--><!--Device-TextStyleInterface-fontStyle?: FontStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontVariations

```TypeScript
fontVariations?: Array<FontVariation>
```

可变字体的属性。

默认值：undefined，表示未设置可变字体的属性。

fontVariations属性的优先级高于fontWeight。

**Type:** Array&lt;[FontVariation](arkts-arkui-fontvariation-t.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyleInterface-fontVariations?: Array<FontVariation>--><!--Device-TextStyleInterface-fontVariations?: Array<FontVariation>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
fontWeight?: int | FontWeight | string
```

字体粗细。

number类型取值[100, 900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。

**Type:** int \| FontWeight \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyleInterface-fontWeight?: int | FontWeight | string--><!--Device-TextStyleInterface-fontWeight?: int | FontWeight | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeColor

```TypeScript
strokeColor?: ResourceColor
```

文本描边颜色。

默认值为字体颜色，设置异常值时取字体颜色。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyleInterface-strokeColor?: ResourceColor--><!--Device-TextStyleInterface-strokeColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeJoinStyle

```TypeScript
strokeJoinStyle?: StrokeJoinStyle
```

文本描边拐角样式。

默认值：StrokeJoinStyle.MITER_JOIN。

**Type:** [StrokeJoinStyle](arkts-arkui-strokejoinstyle-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyleInterface-strokeJoinStyle?: StrokeJoinStyle--><!--Device-TextStyleInterface-strokeJoinStyle?: StrokeJoinStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth?: LengthMetrics
```

文本描边宽度。如果LengthMetrics的unit值是PERCENT，当前设置不生效，处理为0。

设置值小于0时为实心字，大于0时为空心字。

默认值为0。

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyleInterface-strokeWidth?: LengthMetrics--><!--Device-TextStyleInterface-strokeWidth?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## superscript

```TypeScript
superscript?: SuperscriptStyle
```

文本上下角标。

默认值：SuperscriptStyle.NORMAL

**Type:** [SuperscriptStyle](arkts-arkui-superscriptstyle-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyleInterface-superscript?: SuperscriptStyle--><!--Device-TextStyleInterface-superscript?: SuperscriptStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

