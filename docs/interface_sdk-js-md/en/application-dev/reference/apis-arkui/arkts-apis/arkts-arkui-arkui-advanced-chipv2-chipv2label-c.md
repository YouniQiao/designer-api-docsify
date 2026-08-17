# ChipV2Label

Defines chip label class.

**Since:** 26.0.0

<!--Device-unnamed-export declare class ChipV2Label--><!--Device-unnamed-export declare class ChipV2Label-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ChipV2Size } from 'ChipV2Size';
import { ChipV2AccessibilitySelectedType } from 'ChipV2AccessibilitySelectedType';
import { ChipV2ImageIconConfig } from 'ChipV2ImageIconConfig';
import { ChipV2ImageIcon } from 'ChipV2ImageIcon';
import { ChipV2SuffixImageIconConfig } from 'ChipV2SuffixImageIconConfig';
import { ChipV2SuffixImageIcon } from 'ChipV2SuffixImageIcon';
import { ChipV2Icon } from 'ChipV2Icon';
import { ChipV2PrefixImageIconConfig } from 'ChipV2PrefixImageIconConfig';
import { ChipV2PrefixImageIcon } from 'ChipV2PrefixImageIcon';
import { ChipV2AccessibilityConfig } from 'ChipV2AccessibilityConfig';
import { ChipV2Accessibility } from 'ChipV2Accessibility';
import { ChipV2CloseConfig } from 'ChipV2CloseConfig';
import { ChipV2CloseIcon } from 'ChipV2CloseIcon';
import { ChipV2SymbolIconConfig } from 'ChipV2SymbolIconConfig';
import { ChipV2SymbolIcon } from 'ChipV2SymbolIcon';
import { ChipV2PrefixSymbolIconConfig } from 'ChipV2PrefixSymbolIconConfig';
import { ChipV2PrefixSymbolIcon } from 'ChipV2PrefixSymbolIcon';
import { ChipV2SuffixSymbolIconConfig } from 'ChipV2SuffixSymbolIconConfig';
import { ChipV2SuffixSymbolIcon } from 'ChipV2SuffixSymbolIcon';
import { ChipV2LabelMarginConfig } from 'ChipV2LabelMarginConfig';
import { ChipV2LocalizedLabelMarginConfig } from 'ChipV2LocalizedLabelMarginConfig';
import { ChipV2LabelConfig } from 'ChipV2LabelConfig';
import { ChipV2Label } from 'ChipV2Label';
import { IChipV2OptionsConfig } from 'IChipV2OptionsConfig';
import { ChipV2Options } from 'ChipV2Options';
import { ChipV2 } from 'ChipV2';
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
| config | [ChipV2LabelConfig](arkts-arkui-arkui-advanced-chipv2-chipv2labelconfig-i.md) | Yes | config of the chip label |

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

**Type:** [ChipV2LabelMarginConfig](arkts-arkui-arkui-advanced-chipv2-chipv2labelmarginconfig-i.md)

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

**Type:** [ChipV2LocalizedLabelMarginConfig](arkts-arkui-arkui-advanced-chipv2-chipv2localizedlabelmarginconfig-i.md)

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

**Type:** TextModifier

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

