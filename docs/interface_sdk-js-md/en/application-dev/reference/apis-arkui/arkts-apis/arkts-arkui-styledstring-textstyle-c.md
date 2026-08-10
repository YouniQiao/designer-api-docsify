# TextStyle

文本字体样式对象说明。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class TextStyle--><!--Device-unnamed-export declare class TextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value?: TextStyleInterface)
```

文本字体样式的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyle-constructor(value?: TextStyleInterface)--><!--Device-TextStyle-constructor(value?: TextStyleInterface)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [TextStyleInterface](arkts-arkui-styledstring-textstyleinterface-i.md) | No | 字体样式设置项。 |

## fontColor

```TypeScript
readonly fontColor?: ResourceColor
```

获取属性字符串的文本颜色。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyle-readonly fontColor?: ResourceColor--><!--Device-TextStyle-readonly fontColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontConfigs

```TypeScript
readonly fontConfigs?: FontConfigs
```

获取属性字符串的字体配置。

默认返回undefined，表示未设置fontConfigs。

**Type:** [FontConfigs](arkts-arkui-fontconfigs-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyle-readonly fontConfigs?: FontConfigs--><!--Device-TextStyle-readonly fontConfigs?: FontConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontFamily

```TypeScript
readonly fontFamily?: string
```

获取属性字符串的文本字体。

默认返回undefined。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyle-readonly fontFamily?: string--><!--Device-TextStyle-readonly fontFamily?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
readonly fontSize?: double
```

获取属性字符串的文本字体大小。

单位：[vp](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位)

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyle-readonly fontSize?: double--><!--Device-TextStyle-readonly fontSize?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontStyle

```TypeScript
readonly fontStyle?: FontStyle
```

获取属性字符串的文本字体样式。

**Type:** [FontStyle](arkts-arkui-fontstyle-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyle-readonly fontStyle?: FontStyle--><!--Device-TextStyle-readonly fontStyle?: FontStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontVariations

```TypeScript
readonly fontVariations?: Array<FontVariation>
```

获取可变字体的属性数组。

默认值：undefined，表示未设置可变字体的属性。

**Type:** Array&lt;[FontVariation](arkts-arkui-fontvariation-t.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyle-readonly fontVariations?: Array<FontVariation>--><!--Device-TextStyle-readonly fontVariations?: Array<FontVariation>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
readonly fontWeight?: int
```

获取属性字符串的文本字体粗细。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyle-readonly fontWeight?: int--><!--Device-TextStyle-readonly fontWeight?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeColor

```TypeScript
readonly strokeColor?: ResourceColor
```

获取属性字符串的文本描边颜色。

默认返回字体颜色。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyle-readonly strokeColor?: ResourceColor--><!--Device-TextStyle-readonly strokeColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeJoinStyle

```TypeScript
readonly strokeJoinStyle?: StrokeJoinStyle
```

获取属性字符串的文本描边拐角样式。

默认值：StrokeJoinStyle.MITER_JOIN。

**Type:** [StrokeJoinStyle](arkts-arkui-strokejoinstyle-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyle-readonly strokeJoinStyle?: StrokeJoinStyle--><!--Device-TextStyle-readonly strokeJoinStyle?: StrokeJoinStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
readonly strokeWidth?: double
```

获取属性字符串的文本描边宽度。

默认返回0，单位为[vp](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位)。

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyle-readonly strokeWidth?: double--><!--Device-TextStyle-readonly strokeWidth?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## superscript

```TypeScript
readonly superscript?: SuperscriptStyle
```

获取属性字符串的文本上下角标。

默认值：SuperscriptStyle.NORMAL。

**Type:** [SuperscriptStyle](arkts-arkui-superscriptstyle-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextStyle-readonly superscript?: SuperscriptStyle--><!--Device-TextStyle-readonly superscript?: SuperscriptStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

