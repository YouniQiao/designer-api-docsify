# ChipV2Label

Defines chip label class.

**Since:** 26.0.0

<!--Device-unnamed-export declare class ChipV2Label--><!--Device-unnamed-export declare class ChipV2Label-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ChipV2Size, ChipV2AccessibilitySelectedType, ChipV2ImageIconConfig, ChipV2ImageIcon, ChipV2SuffixImageIconConfig, ChipV2SuffixImageIcon, ChipV2Icon, ChipV2PrefixImageIconConfig, ChipV2PrefixImageIcon, ChipV2AccessibilityConfig, ChipV2Accessibility, ChipV2CloseConfig, ChipV2CloseIcon, ChipV2SymbolIconConfig, ChipV2SymbolIcon, ChipV2PrefixSymbolIconConfig, ChipV2PrefixSymbolIcon, ChipV2SuffixSymbolIconConfig, ChipV2SuffixSymbolIcon, ChipV2LabelMarginConfig, ChipV2LocalizedLabelMarginConfig, ChipV2LabelConfig, ChipV2Label, IChipV2OptionsConfig, ChipV2Options, ChipV2 } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(config: ChipV2LabelConfig)
```

The constructor of ChipLabel

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Label-constructor(config: ChipV2LabelConfig)--><!--Device-ChipV2Label-constructor(config: ChipV2LabelConfig)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [ChipV2LabelConfig](arkts-arkui-arkuiadvancedchipv2-chipv2labelconfig-i.md) | Yes | config of the chip label |

## activatedFontColor

```TypeScript
@Trace
  public activatedFontColor?: ColorMetrics
```

Text font color when chip is activated.

**Type:** ColorMetrics

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Label-@Trace  public activatedFontColor?: ColorMetrics--><!--Device-ChipV2Label-@Trace  public activatedFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
@Trace
  public fontColor?: ColorMetrics
```

Text font color.

**Type:** ColorMetrics

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Label-@Trace  public fontColor?: ColorMetrics--><!--Device-ChipV2Label-@Trace  public fontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontFamily

```TypeScript
@Trace
  public fontFamily?: string
```

Text font family.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Label-@Trace  public fontFamily?: string--><!--Device-ChipV2Label-@Trace  public fontFamily?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
@Trace
  public fontSize?: LengthMetrics
```

Text font size.

**Type:** LengthMetrics

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Label-@Trace  public fontSize?: LengthMetrics--><!--Device-ChipV2Label-@Trace  public fontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## labelMargin

```TypeScript
@Trace
  public labelMargin?: ChipV2LabelMarginConfig
```

Label margin.

**Type:** [ChipV2LabelMarginConfig](arkts-arkui-arkuiadvancedchipv2-chipv2labelmarginconfig-i.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Label-@Trace  public labelMargin?: ChipV2LabelMarginConfig--><!--Device-ChipV2Label-@Trace  public labelMargin?: ChipV2LabelMarginConfig-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## localizedLabelMargin

```TypeScript
@Trace
  public localizedLabelMargin?: ChipV2LocalizedLabelMarginConfig
```

Localized label margin.

**Type:** [ChipV2LocalizedLabelMarginConfig](arkts-arkui-arkuiadvancedchipv2-chipv2localizedlabelmarginconfig-i.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Label-@Trace  public localizedLabelMargin?: ChipV2LocalizedLabelMarginConfig--><!--Device-ChipV2Label-@Trace  public localizedLabelMargin?: ChipV2LocalizedLabelMarginConfig-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## modifier

```TypeScript
@Trace
  public modifier?: TextModifier
```

Modifier for the label text.

**Type:** [TextModifier](arkts-arkui-textmodifier-c.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Label-@Trace  public modifier?: TextModifier--><!--Device-ChipV2Label-@Trace  public modifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
@Trace
  public text: string
```

Text content.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Label-@Trace  public text: string--><!--Device-ChipV2Label-@Trace  public text: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

