# ChipV2Accessibility

Defines accessibility.

**Since:** 26.0.0

<!--Device-unnamed-export declare class ChipV2Accessibility--><!--Device-unnamed-export declare class ChipV2Accessibility-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ChipV2Size, ChipV2AccessibilitySelectedType, ChipV2ImageIconConfig, ChipV2ImageIcon, ChipV2SuffixImageIconConfig, ChipV2SuffixImageIcon, ChipV2Icon, ChipV2PrefixImageIconConfig, ChipV2PrefixImageIcon, ChipV2AccessibilityConfig, ChipV2Accessibility, ChipV2CloseConfig, ChipV2CloseIcon, ChipV2SymbolIconConfig, ChipV2SymbolIcon, ChipV2PrefixSymbolIconConfig, ChipV2PrefixSymbolIcon, ChipV2SuffixSymbolIconConfig, ChipV2SuffixSymbolIcon, ChipV2LabelMarginConfig, ChipV2LocalizedLabelMarginConfig, ChipV2LabelConfig, ChipV2Label, IChipV2OptionsConfig, ChipV2Options, ChipV2 } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(config: ChipV2AccessibilityConfig)
```

The constructor of ChipV2Accessibility

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Accessibility-constructor(config: ChipV2AccessibilityConfig)--><!--Device-ChipV2Accessibility-constructor(config: ChipV2AccessibilityConfig)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [ChipV2AccessibilityConfig](arkts-arkui-arkuiadvancedchipv2-chipv2accessibilityconfig-i.md) | Yes | config of accessibility. config is mandatory. |

## accessibilityDescription

```TypeScript
@Trace
  public accessibilityDescription?: ResourceStr
```

Set accessibility description.

**Type:** ResourceStr

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Accessibility-@Trace  public accessibilityDescription?: ResourceStr--><!--Device-ChipV2Accessibility-@Trace  public accessibilityDescription?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
@Trace
  public accessibilityLevel?: string
```

Set accessibility level.

**Type:** string

**Default:** auto

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Accessibility-@Trace  public accessibilityLevel?: string--><!--Device-ChipV2Accessibility-@Trace  public accessibilityLevel?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
@Trace
  public accessibilityText?: ResourceStr
```

Set accessibility text.

**Type:** ResourceStr

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Accessibility-@Trace  public accessibilityText?: ResourceStr--><!--Device-ChipV2Accessibility-@Trace  public accessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

