# ChipV2Options

Defines chip options class.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class ChipV2Options--><!--Device-unnamed-export class ChipV2Options-End-->

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
constructor(config: IChipV2OptionsConfig)
```

The constructor of ChipV2Options

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-constructor(config: IChipV2OptionsConfig)--><!--Device-ChipV2Options-constructor(config: IChipV2OptionsConfig)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [IChipV2OptionsConfig](../../apis-na/arkts-apis/arkts-na-arkui-advanced-chipv2-ichipv2optionsconfig-i.md) | Yes | config of the ChipV2Options |

## accessibilityDescription

```TypeScript
@Trace
  public accessibilityDescription?: ResourceStr
```

Set accessibility description for Chip.

**Type:** ResourceStr

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public accessibilityDescription?: ResourceStr--><!--Device-ChipV2Options-@Trace  public accessibilityDescription?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
@Trace
  public accessibilityLevel?: string
```

Set accessibility level for Chip.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public accessibilityLevel?: string--><!--Device-ChipV2Options-@Trace  public accessibilityLevel?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilitySelectedType

```TypeScript
@Trace
  public accessibilitySelectedType?: ChipV2AccessibilitySelectedType
```

Sets the accessibility selection type for the chip.

**Type:** [ChipV2AccessibilitySelectedType](arkts-arkui-arkui-advanced-chipv2-chipv2accessibilityselectedtype-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public accessibilitySelectedType?: ChipV2AccessibilitySelectedType--><!--Device-ChipV2Options-@Trace  public accessibilitySelectedType?: ChipV2AccessibilitySelectedType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## activated

```TypeScript
@Trace
  public activated?: boolean
```

Set whether chip is active or not.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public activated?: boolean--><!--Device-ChipV2Options-@Trace  public activated?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## activatedBackgroundColor

```TypeScript
@Trace
  public activatedBackgroundColor?: ColorMetrics
```

Chip background color when chip is activated.

**Type:** ColorMetrics

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public activatedBackgroundColor?: ColorMetrics--><!--Device-ChipV2Options-@Trace  public activatedBackgroundColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## activatedBackgroundSystemMaterial

```TypeScript
@Trace
  public activatedBackgroundSystemMaterial?: uiMaterial.Material
```

Set system-styled materials for the component which is activated. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of the component.

**Type:** uiMaterial.Material

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public activatedBackgroundSystemMaterial?: uiMaterial.Material--><!--Device-ChipV2Options-@Trace  public activatedBackgroundSystemMaterial?: uiMaterial.Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## allowClose

```TypeScript
@Trace
  public allowClose?: boolean
```

Show close icon.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public allowClose?: boolean--><!--Device-ChipV2Options-@Trace  public allowClose?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
@Trace
  public backgroundColor?: ColorMetrics
```

Chip background color.

**Type:** ColorMetrics

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public backgroundColor?: ColorMetrics--><!--Device-ChipV2Options-@Trace  public backgroundColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundSystemMaterial

```TypeScript
@Trace
  public backgroundSystemMaterial?: uiMaterial.Material
```

Set system-styled materials for the component. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of the component.

**Type:** uiMaterial.Material

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public backgroundSystemMaterial?: uiMaterial.Material--><!--Device-ChipV2Options-@Trace  public backgroundSystemMaterial?: uiMaterial.Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderRadius

```TypeScript
@Trace
  public borderRadius?: LengthMetrics
```

Chip radius.

**Type:** LengthMetrics

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public borderRadius?: LengthMetrics--><!--Device-ChipV2Options-@Trace  public borderRadius?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## closeIcon

```TypeScript
@Trace
  public closeIcon?: ChipV2CloseIcon
```

Set config for default close icon when 'allowClose' is true.

**Type:** [ChipV2CloseIcon](arkts-arkui-arkui-advanced-chipv2-chipv2closeicon-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public closeIcon?: ChipV2CloseIcon--><!--Device-ChipV2Options-@Trace  public closeIcon?: ChipV2CloseIcon-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
@Trace
  public direction?: Direction
```

Indicates the attribute of the current chip direction.

**Type:** Direction

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public direction?: Direction--><!--Device-ChipV2Options-@Trace  public direction?: Direction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enabled

```TypeScript
@Trace
  public enabled?: boolean
```

Enable chip.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public enabled?: boolean--><!--Device-ChipV2Options-@Trace  public enabled?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
@Trace
  public fontSize?: LengthMetrics
```

Set font size for the label text and the close icon.

**Type:** LengthMetrics

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public fontSize?: LengthMetrics--><!--Device-ChipV2Options-@Trace  public fontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## label

```TypeScript
@Trace
  public label: ChipV2Label
```

Chip prefix icon.

**Type:** [ChipV2Label](arkts-arkui-arkui-advanced-chipv2-chipv2label-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public label: ChipV2Label--><!--Device-ChipV2Options-@Trace  public label: ChipV2Label-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxFontScale

```TypeScript
@Trace
  public maxFontScale?: number | Resource
```

Maximum font scale for Chip.

**Type:** number \| Resource

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public maxFontScale?: number | Resource--><!--Device-ChipV2Options-@Trace  public maxFontScale?: number | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## minFontScale

```TypeScript
@Trace
  public minFontScale?: number | Resource
```

Minimum font scale for Chip.

**Type:** number \| Resource

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public minFontScale?: number | Resource--><!--Device-ChipV2Options-@Trace  public minFontScale?: number | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onClicked

```TypeScript
public onClicked?: Callback<void>
```

On clicked action.

**Type:** Callback&lt;void&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-public onClicked?: Callback<void>--><!--Device-ChipV2Options-public onClicked?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onClose

```TypeScript
public onClose?: VoidCallback
```

On close action.

**Type:** VoidCallback

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-public onClose?: VoidCallback--><!--Device-ChipV2Options-public onClose?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## padding

```TypeScript
@Trace
  public padding?: LocalizedPadding
```

Chip padding.

**Type:** LocalizedPadding

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public padding?: LocalizedPadding--><!--Device-ChipV2Options-@Trace  public padding?: LocalizedPadding-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## prefixIcon

```TypeScript
@Trace
  public prefixIcon?: ChipV2Icon
```

Chip prefix icon.

**Type:** [ChipV2Icon](arkts-arkui-arkui-advanced-chipv2-chipv2icon-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public prefixIcon?: ChipV2Icon--><!--Device-ChipV2Options-@Trace  public prefixIcon?: ChipV2Icon-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
@Trace
  public size?: ChipV2Size | SizeT<LengthMetrics>
```

Chip size.

**Type:** [ChipV2Size](arkts-arkui-arkui-advanced-chipv2-chipv2size-e.md) \| SizeT&lt;LengthMetrics&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public size?: ChipV2Size | SizeT<LengthMetrics>--><!--Device-ChipV2Options-@Trace  public size?: ChipV2Size | SizeT<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## suffixIcon

```TypeScript
@Trace
  public suffixIcon?: ChipV2Icon
```

Chip suffix icon.

**Type:** [ChipV2Icon](arkts-arkui-arkui-advanced-chipv2-chipv2icon-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipV2Options-@Trace  public suffixIcon?: ChipV2Icon--><!--Device-ChipV2Options-@Trace  public suffixIcon?: ChipV2Icon-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

