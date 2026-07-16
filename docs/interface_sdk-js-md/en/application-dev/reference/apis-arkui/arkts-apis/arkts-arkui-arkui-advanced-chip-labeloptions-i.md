# LabelOptions

Defines text configuration options.

**Since:** 11

<!--Device-unnamed-export interface LabelOptions--><!--Device-unnamed-export interface LabelOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SuffixIconOptions, CloseOptions, ChipSymbolGlyphOptions, Chip, AccessibilitySelectedType, LabelMarginOptions, LabelOptions, PrefixIconOptions, IconCommonOptions, ChipOptions, ChipSuffixSymbolGlyphOptions, ChipSize, AccessibilityOptions } from '@kit.ArkUI';
```

## activatedFontColor

```TypeScript
activatedFontColor?: ResourceColor
```

Font color when the chip is activated.

Default value: **$r('sys.color.ohos_id_color_text_primary_contrary')**

If the value is **undefined**, the default value is used.

**Type:** ResourceColor

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LabelOptions-activatedFontColor?: ResourceColor--><!--Device-LabelOptions-activatedFontColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: ResourceColor
```

Font color.

Default value: **$r('sys.color.ohos_id_color_text_primary')**

If the value is **undefined**, the default value is used.

**Type:** ResourceColor

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LabelOptions-fontColor?: ResourceColor--><!--Device-LabelOptions-fontColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontFamily

```TypeScript
fontFamily?: string
```

Font family.

Default value: **"HarmonyOS Sans"**

If the value is **undefined**, the default value is used.

**Type:** string

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LabelOptions-fontFamily?: string--><!--Device-LabelOptions-fontFamily?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize?: Dimension
```

Font size. This parameter cannot be set in percentage.

Default value: **$r('sys.float.ohos_id_text_size_button2')**

If the value is **undefined**, the default value is used.

**Type:** Dimension

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LabelOptions-fontSize?: Dimension--><!--Device-LabelOptions-fontSize?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## labelMargin

```TypeScript
labelMargin?: LabelMarginOptions
```

Spacing between the text and the left and right icons.

Default value:

When **size** is **ChipSize.SMALL**: **{ left: 4, right: 4 }**.

When **size** is **ChipSize.NORMAL**: **{ left: 6, right: 6 }**.

Unit: vp.

If the value is **undefined**, the default value is used.

**Type:** LabelMarginOptions

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LabelOptions-labelMargin?: LabelMarginOptions--><!--Device-LabelOptions-labelMargin?: LabelMarginOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## localizedLabelMargin

```TypeScript
localizedLabelMargin?: LocalizedLabelMarginOptions
```

Spacing between the localized text and the left and right icons.

Default value:

When **size** is set to **ChipSize.SMALL**, the default value is as follows:

`{ start: LengthMetrics.resource($r('sys.float.chip_small_text_margin')),end: LengthMetrics.resource($r('sys.float.chip_small_text_margin')) }`

When **size** is set to **ChipSize.NORMAL**, the default value is as follows:

`{ start: LengthMetrics.resource($r('sys.float.chip_normal_text_margin')),end: LengthMetrics.resource($r('sys.float.chip_normal_text_margin')) }`

If the value is **undefined**, the default value is used.

**Type:** LocalizedLabelMarginOptions

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LabelOptions-localizedLabelMargin?: LocalizedLabelMarginOptions--><!--Device-LabelOptions-localizedLabelMargin?: LocalizedLabelMarginOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text: string
```

Text content.

**Type:** string

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LabelOptions-text: string--><!--Device-LabelOptions-text: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

