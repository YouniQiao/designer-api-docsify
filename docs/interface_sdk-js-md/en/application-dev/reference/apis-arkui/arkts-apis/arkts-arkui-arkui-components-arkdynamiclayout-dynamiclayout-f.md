# DynamicLayout

## Modules to Import

```TypeScript
import { DynamicLayoutAttribute, DynamicLayout } from '@kit.ArkUI';
```

## DynamicLayout

```TypeScript
export declare function DynamicLayout (
    algorithm: LayoutAlgorithm, 
    content_: CustomBuilder,
): DynamicLayoutAttribute
```

Defines DynamicLayout Component.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function DynamicLayout (    algorithm: LayoutAlgorithm,     content_: CustomBuilder,): DynamicLayoutAttribute--><!--Device-unnamed-export declare function DynamicLayout (    algorithm: LayoutAlgorithm,     content_: CustomBuilder,): DynamicLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algorithm | [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md) | Yes |  |
| content_ | CustomBuilder | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [DynamicLayoutAttribute](arkts-arkui-arkui-components-arkdynamiclayout-dynamiclayoutattribute-i.md) |  |

