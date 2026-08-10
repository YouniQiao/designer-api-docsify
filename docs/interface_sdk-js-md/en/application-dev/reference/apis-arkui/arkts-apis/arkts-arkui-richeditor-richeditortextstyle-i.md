# RichEditorTextStyle

文本样式信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RichEditorTextStyle--><!--Device-unnamed-export declare interface RichEditorTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## decoration

```TypeScript
decoration?: DecorationStyleInterface
```

文本装饰线样式信息。

**Type:** [DecorationStyleInterface](arkts-arkui-decorationstyleinterface-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-decoration?: DecorationStyleInterface--><!--Device-RichEditorTextStyle-decoration?: DecorationStyleInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: ResourceColor
```

文本颜色。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-fontColor?: ResourceColor--><!--Device-RichEditorTextStyle-fontColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontFamily

```TypeScript
fontFamily?: ResourceStr
```

字体列表。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-fontFamily?: ResourceStr--><!--Device-RichEditorTextStyle-fontFamily?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontFeature

```TypeScript
fontFeature?: string
```

文字特性效果。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-fontFeature?: string--><!--Device-RichEditorTextStyle-fontFeature?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize?: Length | double
```

字体大小，默认单位为fp。

**Type:** [Length](arkts-arkui-length-t.md) \| double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-fontSize?: Length | double--><!--Device-RichEditorTextStyle-fontSize?: Length | double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontStyle

```TypeScript
fontStyle?: FontStyle
```

字体样式。

**Type:** [FontStyle](arkts-arkui-fontstyle-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-fontStyle?: FontStyle--><!--Device-RichEditorTextStyle-fontStyle?: FontStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
fontWeight?: int | FontWeight | string
```

字体粗细。

**Type:** int \| FontWeight \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-fontWeight?: int | FontWeight | string--><!--Device-RichEditorTextStyle-fontWeight?: int | FontWeight | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## halfLeading

```TypeScript
halfLeading?: boolean
```

文本是否将行间距平分至行的顶部与底部。

true表示将行间距平分至行的顶部与底部，false则不平分。

默认值：false。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-halfLeading?: boolean--><!--Device-RichEditorTextStyle-halfLeading?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## letterSpacing

```TypeScript
letterSpacing?: double | string
```

文本字符间距，默认单位为fp。

**Type:** double \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-letterSpacing?: double | string--><!--Device-RichEditorTextStyle-letterSpacing?: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineHeight

```TypeScript
lineHeight?: double | string | Resource
```

文本行高，默认单位为fp。

**Type:** double \| string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-lineHeight?: double | string | Resource--><!--Device-RichEditorTextStyle-lineHeight?: double | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeColor

```TypeScript
strokeColor?: ResourceColor
```

文本描边颜色。

默认值：跟随字体颜色。

设置异常值时跟随字体颜色。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-strokeColor?: ResourceColor--><!--Device-RichEditorTextStyle-strokeColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeJoinStyle

```TypeScript
strokeJoinStyle?: StrokeJoinStyle
```

文本描边拐角样式。

默认值：StrokeJoinStyle.MITER_JOIN。

**模型约束：** 此接口仅可在Stage模型下使用。

**Type:** [StrokeJoinStyle](arkts-arkui-strokejoinstyle-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-strokeJoinStyle?: StrokeJoinStyle--><!--Device-RichEditorTextStyle-strokeJoinStyle?: StrokeJoinStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth?: LengthMetrics | double
```

文本描边宽度。如果LengthMetrics的unit值是[PERCENT](arkts-arkui-graphics-lengthunit-e.md)，当前设置不生效，作为0处理。

值小于0时为实体字，大于0时为轮廓字，等于0时无描边效果。

默认值：0vp。

单位：LengthMetrics类型时跟随LengthMetrics，number或double类型时是vp。

取值范围：(-∞, +∞)

**模型约束：** 此接口仅可在Stage模型下使用。

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) \| double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-strokeWidth?: LengthMetrics | double--><!--Device-RichEditorTextStyle-strokeWidth?: LengthMetrics | double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textBackgroundStyle

```TypeScript
textBackgroundStyle?: TextBackgroundStyle
```

文本背景样式。

**Type:** [TextBackgroundStyle](../arkts-components/arkts-arkui-textbackgroundstyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-textBackgroundStyle?: TextBackgroundStyle--><!--Device-RichEditorTextStyle-textBackgroundStyle?: TextBackgroundStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textShadow

```TypeScript
textShadow?: ShadowOptions | Array<ShadowOptions>
```

文字阴影效果。

**说明：**

仅支持查询阴影模糊半径、颜色和偏移量。

**Type:** [ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md) \| Array&lt;[ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-textShadow?: ShadowOptions | Array<ShadowOptions>--><!--Device-RichEditorTextStyle-textShadow?: ShadowOptions | Array<ShadowOptions>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

