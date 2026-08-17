# ChipGroupV2Item

Defines chip group item.

**Since:** 26.0.0

<!--Device-unnamed-export declare class ChipGroupV2Item--><!--Device-unnamed-export declare class ChipGroupV2Item-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ChipGroupV2ItemConfig } from 'ChipGroupV2ItemConfig';
import { ChipGroupV2Item } from 'ChipGroupV2Item';
import { ChipGroupV2Items } from 'ChipGroupV2Items';
import { ChipGroupV2ItemStyleConfig } from 'ChipGroupV2ItemStyleConfig';
import { ChipGroupV2ItemStyle } from 'ChipGroupV2ItemStyle';
import { ChipGroupV2SpaceConfig } from 'ChipGroupV2SpaceConfig';
import { ChipGroupV2Space } from 'ChipGroupV2Space';
import { ChipGroupV2IconItemConfig } from 'ChipGroupV2IconItemConfig';
import { ChipGroupV2SymbolItemConfig } from 'ChipGroupV2SymbolItemConfig';
import { ChipGroupV2PaddingConfig } from 'ChipGroupV2PaddingConfig';
import { ChipGroupV2Padding } from 'ChipGroupV2Padding';
import { ChipGroupV2IconGroupSuffix } from 'ChipGroupV2IconGroupSuffix';
import { ChipGroupV2 } from 'ChipGroupV2';
```

## constructor

```TypeScript
constructor(config: ChipGroupV2ItemConfig)
```

The constructor of ChipGroupV2Item

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2Item-constructor(config: ChipGroupV2ItemConfig)--><!--Device-ChipGroupV2Item-constructor(config: ChipGroupV2ItemConfig)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [ChipGroupV2ItemConfig](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2itemconfig-i.md) | Yes | config of the chip group item |

## accessibilityDescription

```TypeScript
@Trace
    public accessibilityDescription?: ResourceStr
```

Set accessibility description for ChipGroupV2 item.

**Type:** ResourceStr

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2Item-@Trace    public accessibilityDescription?: ResourceStr--><!--Device-ChipGroupV2Item-@Trace    public accessibilityDescription?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
@Trace
    public accessibilityLevel?: string
```

Set accessibility level for ChipGroupV2 item.

**Type:** string

**Default:** auto

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2Item-@Trace    public accessibilityLevel?: string--><!--Device-ChipGroupV2Item-@Trace    public accessibilityLevel?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## allowClose

```TypeScript
@Trace
    public allowClose?: boolean
```

Allow close.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2Item-@Trace    public allowClose?: boolean--><!--Device-ChipGroupV2Item-@Trace    public allowClose?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## closeIcon

```TypeScript
@Trace
    public closeIcon?: ChipV2CloseConfig
```

Set config for default close icon when 'allowClose' is true.

**Type:** [ChipV2CloseConfig](arkts-arkui-arkui-advanced-chipv2-chipv2closeconfig-i.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2Item-@Trace    public closeIcon?: ChipV2CloseConfig--><!--Device-ChipGroupV2Item-@Trace    public closeIcon?: ChipV2CloseConfig-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## label

```TypeScript
@Trace
    public label: ChipV2Label
```

Chip label.

**Type:** [ChipV2Label](arkts-arkui-arkui-advanced-chipv2-chipv2label-c.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2Item-@Trace    public label: ChipV2Label--><!--Device-ChipGroupV2Item-@Trace    public label: ChipV2Label-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## prefixIcon

```TypeScript
@Trace
    public prefixIcon?: ChipV2PrefixImageIcon
```

Prefix icon.

**Type:** [ChipV2PrefixImageIcon](arkts-arkui-arkui-advanced-chipv2-chipv2prefiximageicon-c.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2Item-@Trace    public prefixIcon?: ChipV2PrefixImageIcon--><!--Device-ChipGroupV2Item-@Trace    public prefixIcon?: ChipV2PrefixImageIcon-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## prefixSymbolIcon

```TypeScript
@Trace
    public prefixSymbolIcon?: ChipV2PrefixSymbolIcon
```

Prefix symbol icon.

**Type:** [ChipV2PrefixSymbolIcon](arkts-arkui-arkui-advanced-chipv2-chipv2prefixsymbolicon-c.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2Item-@Trace    public prefixSymbolIcon?: ChipV2PrefixSymbolIcon--><!--Device-ChipGroupV2Item-@Trace    public prefixSymbolIcon?: ChipV2PrefixSymbolIcon-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## suffixIcon

```TypeScript
@Trace
    public suffixIcon?: ChipV2SuffixImageIcon
```

Suffix icon.

**Type:** [ChipV2SuffixImageIcon](arkts-arkui-arkui-advanced-chipv2-chipv2suffiximageicon-c.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2Item-@Trace    public suffixIcon?: ChipV2SuffixImageIcon--><!--Device-ChipGroupV2Item-@Trace    public suffixIcon?: ChipV2SuffixImageIcon-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## suffixSymbolIcon

```TypeScript
@Trace
    public suffixSymbolIcon?: ChipV2SuffixSymbolIcon
```

Suffix symbol icon.

**Type:** [ChipV2SuffixSymbolIcon](arkts-arkui-arkui-advanced-chipv2-chipv2suffixsymbolicon-c.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2Item-@Trace    public suffixSymbolIcon?: ChipV2SuffixSymbolIcon--><!--Device-ChipGroupV2Item-@Trace    public suffixSymbolIcon?: ChipV2SuffixSymbolIcon-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

