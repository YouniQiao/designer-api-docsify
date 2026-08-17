# ChipV2CloseIcon

Defines default close icon.

**Inheritance/Implementation:** ChipV2CloseIcon extends [ChipV2Accessibility](arkts-arkui-arkui-advanced-chipv2-chipv2accessibility-c.md#chipv2accessibility)

**Since:** 26.0.0

<!--Device-unnamed-export declare class ChipV2CloseIcon--><!--Device-unnamed-export declare class ChipV2CloseIcon-End-->

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
constructor(config: ChipV2CloseConfig)
```

The constructor of ChipV2CloseIcon

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2CloseIcon-constructor(config: ChipV2CloseConfig)--><!--Device-ChipV2CloseIcon-constructor(config: ChipV2CloseConfig)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [ChipV2CloseConfig](arkts-arkui-arkui-advanced-chipv2-chipv2closeconfig-i.md) | Yes | config of close icon |

## fontSize

```TypeScript
@Trace
  public fontSize?: LengthMetrics
```

Set font size for the close icon.

**Type:** LengthMetrics

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2CloseIcon-@Trace  public fontSize?: LengthMetrics--><!--Device-ChipV2CloseIcon-@Trace  public fontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

