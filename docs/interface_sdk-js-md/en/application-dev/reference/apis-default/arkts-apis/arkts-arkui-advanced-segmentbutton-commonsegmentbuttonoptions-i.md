# CommonSegmentButtonOptions

Defines SegmentButton common options.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-interface CommonSegmentButtonOptions--><!--Device-unnamed-interface CommonSegmentButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

The blurStyle of background.

**Type:** BlurStyle

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-backgroundBlurStyle?: BlurStyle--><!--Device-CommonSegmentButtonOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBorderRadius

```TypeScript
backgroundBorderRadius?: LengthMetrics
```

The background border radius of SegmentButton. Only takes effect when borderRadiusMode is set to BorderRadiusMode.Custom.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-backgroundBorderRadius?: LengthMetrics--><!--Device-CommonSegmentButtonOptions-backgroundBorderRadius?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

The background color of SegmentButton.

**Type:** ResourceColor

**Default:** $r('sys.color.ohos_id_color_button_normal')

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-backgroundColor?: ResourceColor--><!--Device-CommonSegmentButtonOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderRadiusMode

```TypeScript
borderRadiusMode?: BorderRadiusMode
```

The border radius mode of SegmentButton.

**Type:** [BorderRadiusMode](arkts-arkui-advanced-segmentbutton-borderradiusmode-e.md)

**Default:** BorderRadiusMode.Default

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-borderRadiusMode?: BorderRadiusMode--><!--Device-CommonSegmentButtonOptions-borderRadiusMode?: BorderRadiusMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonPadding

```TypeScript
buttonPadding?: Padding | Dimension
```

The padding of buttons.

**Type:** Padding \| Dimension

**Default:** For text only / icon only buttons Padding { top: 4, right: 8, bottom: 4, left: 8 }. For text & icon buttons Padding { top: 6, right: 8, bottom: 6, left: 8 }.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-buttonPadding?: Padding | Dimension--><!--Device-CommonSegmentButtonOptions-buttonPadding?: Padding | Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: Direction
```

Indicates the attribute of the current segment button direction.

**Type:** Direction

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-direction?: Direction--><!--Device-CommonSegmentButtonOptions-direction?: Direction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: ResourceColor
```

The font color of buttons.

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-fontColor?: ResourceColor--><!--Device-CommonSegmentButtonOptions-fontColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize?: DimensionNoPercentage
```

The font size of buttons.

**Type:** [DimensionNoPercentage](arkts-dimensionnopercentage-t.md)

**Default:** $r('sys.float.ohos_id_text_size_body2')

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-fontSize?: DimensionNoPercentage--><!--Device-CommonSegmentButtonOptions-fontSize?: DimensionNoPercentage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
fontWeight?: FontWeight
```

The font weight of buttons.

**Type:** FontWeight

**Default:** FontWeight.Regular

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-fontWeight?: FontWeight--><!--Device-CommonSegmentButtonOptions-fontWeight?: FontWeight-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageSize

```TypeScript
imageSize?: SizeOptions
```

The image size of buttons.

**Type:** SizeOptions

**Default:** SizeOptions { width: 24, height: 24 }

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-imageSize?: SizeOptions--><!--Device-CommonSegmentButtonOptions-imageSize?: SizeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemBorderRadius

```TypeScript
itemBorderRadius?: LengthMetrics
```

The border radius of selected item in SegmentButton. Only takes effect when borderRadiusMode is set to BorderRadiusMode.Custom.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-itemBorderRadius?: LengthMetrics--><!--Device-CommonSegmentButtonOptions-itemBorderRadius?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## localizedButtonPadding

```TypeScript
localizedButtonPadding?: LocalizedPadding
```

The localized padding of buttons.

**Type:** LocalizedPadding

**Default:** For text only / icon only buttons LocalizedPadding { top: LengthMetrics.vp(4), end: LengthMetrics.vp(8), bottom: LengthMetrics.vp(4), start: LengthMetrics.vp(8) }. For text & icon buttons LocalizedPadding { top: LengthMetrics.vp(6), end: LengthMetrics.vp(8), bottom: LengthMetrics.vp(6), start: LengthMetrics.vp(8) }.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-localizedButtonPadding?: LocalizedPadding--><!--Device-CommonSegmentButtonOptions-localizedButtonPadding?: LocalizedPadding-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## localizedTextPadding

```TypeScript
localizedTextPadding?: LocalizedPadding
```

The localized padding of text in button.

**Type:** LocalizedPadding

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-localizedTextPadding?: LocalizedPadding--><!--Device-CommonSegmentButtonOptions-localizedTextPadding?: LocalizedPadding-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedBackgroundColor

```TypeScript
selectedBackgroundColor?: ResourceColor
```

The background color of selected button.

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-selectedBackgroundColor?: ResourceColor--><!--Device-CommonSegmentButtonOptions-selectedBackgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedFontColor

```TypeScript
selectedFontColor?: ResourceColor
```

The font color of selected button.

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-selectedFontColor?: ResourceColor--><!--Device-CommonSegmentButtonOptions-selectedFontColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedFontSize

```TypeScript
selectedFontSize?: DimensionNoPercentage
```

The font size of selected button.

**Type:** [DimensionNoPercentage](arkts-dimensionnopercentage-t.md)

**Default:** $r('sys.float.ohos_id_text_size_body2')

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-selectedFontSize?: DimensionNoPercentage--><!--Device-CommonSegmentButtonOptions-selectedFontSize?: DimensionNoPercentage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedFontWeight

```TypeScript
selectedFontWeight?: FontWeight
```

The font weight of selected button.

**Type:** FontWeight

**Default:** FontWeight.Medium

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-selectedFontWeight?: FontWeight--><!--Device-CommonSegmentButtonOptions-selectedFontWeight?: FontWeight-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textPadding

```TypeScript
textPadding?: Padding | Dimension
```

The padding of text in button.

**Type:** Padding \| Dimension

**Default:** 0

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonSegmentButtonOptions-textPadding?: Padding | Dimension--><!--Device-CommonSegmentButtonOptions-textPadding?: Padding | Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

