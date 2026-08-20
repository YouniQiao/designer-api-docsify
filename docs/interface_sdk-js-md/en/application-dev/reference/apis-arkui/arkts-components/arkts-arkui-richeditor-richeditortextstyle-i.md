# RichEditorTextStyle

Defines the span text style.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface RichEditorTextStyle--><!--Device-unnamed-export declare interface RichEditorTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## decoration

```TypeScript
decoration?: DecorationStyleInterface
```

Font decoration.

**Type:** [DecorationStyleInterface](../arkts-apis/arkts-arkui-styledstring-decorationstyleinterface-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-decoration?: DecorationStyleInterface--><!--Device-RichEditorTextStyle-decoration?: DecorationStyleInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: ResourceColor
```

font color.

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-fontColor?: ResourceColor--><!--Device-RichEditorTextStyle-fontColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontFamily

```TypeScript
fontFamily?: ResourceStr
```

font family.

**Type:** [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-fontFamily?: ResourceStr--><!--Device-RichEditorTextStyle-fontFamily?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontFeature

```TypeScript
fontFeature?: string
```

Set font feature, advanced text styles and effects as designed by the font author. The format is the like the CSS font-feature-settings attribute.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-fontFeature?: string--><!--Device-RichEditorTextStyle-fontFeature?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize?: Length | double
```

font size.

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md) \| double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-fontSize?: Length | double--><!--Device-RichEditorTextStyle-fontSize?: Length | double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontStyle

```TypeScript
fontStyle?: FontStyle
```

font style.

**Type:** [FontStyle](../arkts-apis/arkts-arkui-fontstyle-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-fontStyle?: FontStyle--><!--Device-RichEditorTextStyle-fontStyle?: FontStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
fontWeight?: int | FontWeight | string
```

font weight.

**Type:** int \| [FontWeight](../arkts-apis/arkts-arkui-fontweight-e.md) \| string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-fontWeight?: int | FontWeight | string--><!--Device-RichEditorTextStyle-fontWeight?: int | FontWeight | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## halfLeading

```TypeScript
halfLeading?: boolean
```

Set the text with half leading.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-halfLeading?: boolean--><!--Device-RichEditorTextStyle-halfLeading?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## letterSpacing

```TypeScript
letterSpacing?: double | string
```

letter spacing.

**Type:** double \| string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-letterSpacing?: double | string--><!--Device-RichEditorTextStyle-letterSpacing?: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineHeight

```TypeScript
lineHeight?: double | string | Resource
```

line height.

**Type:** double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-lineHeight?: double | string | Resource--><!--Device-RichEditorTextStyle-lineHeight?: double | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeColor

```TypeScript
strokeColor?: ResourceColor
```

The stroke color of the text.

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-strokeColor?: ResourceColor--><!--Device-RichEditorTextStyle-strokeColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeJoinStyle

```TypeScript
strokeJoinStyle?: StrokeJoinStyle
```

The stroke join style of the text.

**Type:** [StrokeJoinStyle](../arkts-apis/arkts-arkui-textcommon-strokejoinstyle-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-strokeJoinStyle?: StrokeJoinStyle--><!--Device-RichEditorTextStyle-strokeJoinStyle?: StrokeJoinStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth?: LengthMetrics | double
```

The stroke width of the text.

**Type:** [LengthMetrics](../../apis-default/arkts-apis/arkts-graphics-lengthmetrics-c.md) \| double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-strokeWidth?: LengthMetrics | double--><!--Device-RichEditorTextStyle-strokeWidth?: LengthMetrics | double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textBackgroundStyle

```TypeScript
textBackgroundStyle?: TextBackgroundStyle
```

Text background style.

**Type:** [TextBackgroundStyle](arkts-arkui-textbackgroundstyle-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-textBackgroundStyle?: TextBackgroundStyle--><!--Device-RichEditorTextStyle-textBackgroundStyle?: TextBackgroundStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textShadow

```TypeScript
textShadow?: ShadowOptions | Array<ShadowOptions>
```

Text shadow

**Type:** [ShadowOptions](arkts-arkui-shadowoptions-i.md) \| Array&lt;[ShadowOptions](arkts-arkui-shadowoptions-i.md)&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextStyle-textShadow?: ShadowOptions | Array<ShadowOptions>--><!--Device-RichEditorTextStyle-textShadow?: ShadowOptions | Array<ShadowOptions>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

