# SegmentButtonOptions

The class for SegmentButton options.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-declare class SegmentButtonOptions--><!--Device-unnamed-declare class SegmentButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## capsule

```TypeScript
static capsule(options: CapsuleSegmentButtonConstructionOptions): SegmentButtonOptions
```

The function used to create a SegmentButtonOptions of capsule type.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-static capsule(options: CapsuleSegmentButtonConstructionOptions): SegmentButtonOptions--><!--Device-SegmentButtonOptions-static capsule(options: CapsuleSegmentButtonConstructionOptions): SegmentButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CapsuleSegmentButtonConstructionOptions](arkts-arkui-advanced-segmentbutton-capsulesegmentbuttonconstructionoptions-i.md) | Yes | The options of SegmentButton. |

**Return value:**

| Type | Description |
| --- | --- |
| [SegmentButtonOptions](arkts-arkui-advanced-segmentbutton-segmentbuttonoptions-c.md) | Returns the a new SegmentButtonOptions object of capsule type. |

## constructor

```TypeScript
constructor(options: TabSegmentButtonOptions | CapsuleSegmentButtonOptions)
```

The constructor used to create a SegmentButtonOptions object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-constructor(options: TabSegmentButtonOptions | CapsuleSegmentButtonOptions)--><!--Device-SegmentButtonOptions-constructor(options: TabSegmentButtonOptions | CapsuleSegmentButtonOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TabSegmentButtonOptions](arkts-arkui-advanced-segmentbutton-tabsegmentbuttonoptions-i.md) \| [CapsuleSegmentButtonOptions](arkts-arkui-advanced-segmentbutton-capsulesegmentbuttonoptions-i.md) | Yes | The options of SegmentButton. |

## tab

```TypeScript
static tab(options: TabSegmentButtonConstructionOptions): SegmentButtonOptions
```

The function used to create a SegmentButtonOptions of tab type.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-static tab(options: TabSegmentButtonConstructionOptions): SegmentButtonOptions--><!--Device-SegmentButtonOptions-static tab(options: TabSegmentButtonConstructionOptions): SegmentButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TabSegmentButtonConstructionOptions](arkts-arkui-advanced-segmentbutton-tabsegmentbuttonconstructionoptions-i.md) | Yes | The options of SegmentButton. |

**Return value:**

| Type | Description |
| --- | --- |
| [SegmentButtonOptions](arkts-arkui-advanced-segmentbutton-segmentbuttonoptions-c.md) | Returns the a new SegmentButtonOptions object of tab type. |

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle: BlurStyle
```

The blurStyle of background.

**Type:** BlurStyle

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-backgroundBlurStyle: BlurStyle--><!--Device-SegmentButtonOptions-backgroundBlurStyle: BlurStyle-End-->

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

<!--Device-SegmentButtonOptions-backgroundBorderRadius?: LengthMetrics--><!--Device-SegmentButtonOptions-backgroundBorderRadius?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor: ResourceColor
```

The background color of SegmentButton.

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-backgroundColor: ResourceColor--><!--Device-SegmentButtonOptions-backgroundColor: ResourceColor-End-->

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

<!--Device-SegmentButtonOptions-borderRadiusMode?: BorderRadiusMode--><!--Device-SegmentButtonOptions-borderRadiusMode?: BorderRadiusMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonPadding

```TypeScript
buttonPadding: Padding | Dimension
```

The padding of buttons.

**Type:** Padding \| Dimension

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-buttonPadding: Padding | Dimension--><!--Device-SegmentButtonOptions-buttonPadding: Padding | Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttons

```TypeScript
buttons: SegmentButtonItemOptionsArray
```

The buttons information of SegmentButton.

**Type:** [SegmentButtonItemOptionsArray](arkts-arkui-advanced-segmentbutton-segmentbuttonitemoptionsarray-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-buttons: SegmentButtonItemOptionsArray--><!--Device-SegmentButtonOptions-buttons: SegmentButtonItemOptionsArray-End-->

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

<!--Device-SegmentButtonOptions-direction?: Direction--><!--Device-SegmentButtonOptions-direction?: Direction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor: ResourceColor
```

The font color of buttons.

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-fontColor: ResourceColor--><!--Device-SegmentButtonOptions-fontColor: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize: DimensionNoPercentage
```

The font size of buttons.

**Type:** [DimensionNoPercentage](arkts-dimensionnopercentage-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-fontSize: DimensionNoPercentage--><!--Device-SegmentButtonOptions-fontSize: DimensionNoPercentage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
fontWeight: FontWeight
```

The font weight of buttons.

**Type:** FontWeight

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-fontWeight: FontWeight--><!--Device-SegmentButtonOptions-fontWeight: FontWeight-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageSize

```TypeScript
imageSize: SizeOptions
```

The image size of buttons.

**Type:** SizeOptions

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-imageSize: SizeOptions--><!--Device-SegmentButtonOptions-imageSize: SizeOptions-End-->

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

<!--Device-SegmentButtonOptions-itemBorderRadius?: LengthMetrics--><!--Device-SegmentButtonOptions-itemBorderRadius?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## localizedButtonPadding

```TypeScript
localizedButtonPadding?: LocalizedPadding
```

The localized padding of buttons.

**Type:** LocalizedPadding

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-localizedButtonPadding?: LocalizedPadding--><!--Device-SegmentButtonOptions-localizedButtonPadding?: LocalizedPadding-End-->

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

<!--Device-SegmentButtonOptions-localizedTextPadding?: LocalizedPadding--><!--Device-SegmentButtonOptions-localizedTextPadding?: LocalizedPadding-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## multiply

```TypeScript
multiply: boolean
```

The support multiple selections flag of SegmentButton.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-multiply: boolean--><!--Device-SegmentButtonOptions-multiply: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedBackgroundColor

```TypeScript
selectedBackgroundColor: ResourceColor
```

The background color of selected button.

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-selectedBackgroundColor: ResourceColor--><!--Device-SegmentButtonOptions-selectedBackgroundColor: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedFontColor

```TypeScript
selectedFontColor: ResourceColor
```

The font color of selected button.

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-selectedFontColor: ResourceColor--><!--Device-SegmentButtonOptions-selectedFontColor: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedFontSize

```TypeScript
selectedFontSize: DimensionNoPercentage
```

The font size of selected button.

**Type:** [DimensionNoPercentage](arkts-dimensionnopercentage-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-selectedFontSize: DimensionNoPercentage--><!--Device-SegmentButtonOptions-selectedFontSize: DimensionNoPercentage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedFontWeight

```TypeScript
selectedFontWeight: FontWeight
```

The font weight of selected button.

**Type:** FontWeight

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-selectedFontWeight: FontWeight--><!--Device-SegmentButtonOptions-selectedFontWeight: FontWeight-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textPadding

```TypeScript
textPadding: Padding | Dimension
```

The padding of text in button.

**Type:** Padding \| Dimension

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-textPadding: Padding | Dimension--><!--Device-SegmentButtonOptions-textPadding: Padding | Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: "tab" | "capsule"
```

The type of SegmentButton.

**Type:** "tab" \| "capsule"

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButtonOptions-type: "tab" | "capsule"--><!--Device-SegmentButtonOptions-type: "tab" | "capsule"-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

