# CapsuleStyleOptions

Capsule style options. Inherits from [ScanEffectOptions](arkts-arkui-scaneffectoptions-i.md#ScanEffectOptions) and [CommonProgressStyleOptions](arkts-arkui-commonprogressstyleoptions-i.md#CommonProgressStyleOptions).

**Inheritance/Implementation:** CapsuleStyleOptions extends [ScanEffectOptions](arkts-arkui-scaneffectoptions-i.md#ScanEffectOptions), [CommonProgressStyleOptions](arkts-arkui-commonprogressstyleoptions-i.md#CommonProgressStyleOptions)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-unnamed-declare interface CapsuleStyleOptions--><!--Device-unnamed-declare interface CapsuleStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
borderColor?: ResourceColor
```

Border color. Default value: API version 10: **'#33006cde'** API version 11 or later: **'#33007dff'**

**Type:** ResourceColor

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CapsuleStyleOptions-borderColor?: ResourceColor--><!--Device-CapsuleStyleOptions-borderColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderRadius

```TypeScript
borderRadius?: LengthMetrics
```

Border radius. Percentage values are not supported. Value range: [0, min(width, height)/2] Default value: min(width, height)/2 If an invalid value is set, the default value is used.

**Type:** LengthMetrics

**Default:** min(width, height) / 2

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CapsuleStyleOptions-borderRadius?: LengthMetrics--><!--Device-CapsuleStyleOptions-borderRadius?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: Length
```

Border width. Percentage values are not supported. Default value: **1vp**

**Type:** Length

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CapsuleStyleOptions-borderWidth?: Length--><!--Device-CapsuleStyleOptions-borderWidth?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
content?: ResourceStr
```

Text content, which can be customized.

**Type:** ResourceStr

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CapsuleStyleOptions-content?: ResourceStr--><!--Device-CapsuleStyleOptions-content?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## font

```TypeScript
font?: Font
```

Text style. Default value: Font size (percentage values are not supported): **12fp** Other text parameters are subject to the theme values of the Text component.

**Type:** Font

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CapsuleStyleOptions-font?: Font--><!--Device-CapsuleStyleOptions-font?: Font-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: ResourceColor
```

Font color. Default value: **'#ff182431'**

**Type:** ResourceColor

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CapsuleStyleOptions-fontColor?: ResourceColor--><!--Device-CapsuleStyleOptions-fontColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showDefaultPercentage

```TypeScript
showDefaultPercentage?: boolean
```

Whether to display the percentage text. After this feature is enabled, the progress percentage is displayed on the progress indicator. This property does not take effect when **content** is set. **true**: The percentage text is displayed. **false**: The percentage text is not displayed. Default value: **false**

**Type:** boolean

**Default:** false

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CapsuleStyleOptions-showDefaultPercentage?: boolean--><!--Device-CapsuleStyleOptions-showDefaultPercentage?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

