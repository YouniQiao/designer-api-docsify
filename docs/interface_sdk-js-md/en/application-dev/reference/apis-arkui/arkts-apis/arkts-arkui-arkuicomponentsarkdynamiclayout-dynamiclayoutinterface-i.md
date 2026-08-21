# DynamicLayoutInterface

Defines the dynamic layout container.

**Since:** 24

<!--Device-unnamed-export interface DynamicLayoutInterface--><!--Device-unnamed-export interface DynamicLayoutInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DynamicLayout, DynamicLayoutAttribute } from '@kit.ArkUI';
```

## constructor

```TypeScript
(algorithm: LayoutAlgorithm): DynamicLayoutAttribute
```

Defines the dynamic layout container.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-DynamicLayoutInterface-(algorithm: LayoutAlgorithm): DynamicLayoutAttribute--><!--Device-DynamicLayoutInterface-(algorithm: LayoutAlgorithm): DynamicLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algorithm | [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md) | Yes | Layout algorithm of the dynamic layout component. If an invalid value is used, the child components are stacked and arranged according to StackLayoutAlgorithm. |

**Return value:**

| Type | Description |
| --- | --- |
| [DynamicLayoutAttribute](../../apis-default/arkts-apis/arkts-arkuicomponentsarkdynamiclayout-dynamiclayoutattribute-i.md) |  |

