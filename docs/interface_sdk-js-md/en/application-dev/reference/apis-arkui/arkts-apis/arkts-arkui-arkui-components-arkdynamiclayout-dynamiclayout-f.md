# DynamicLayout

## Modules to Import

```TypeScript
import { DynamicLayoutAttribute, DynamicLayout } from 'kits/@kit.ArkUI';
```

## DynamicLayout

```TypeScript
export declare function DynamicLayout (
    algorithm: LayoutAlgorithm,
    content_: CustomBuilder,
): DynamicLayoutAttribute
```

动态布局容器。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function DynamicLayout (    algorithm: LayoutAlgorithm,    content_: CustomBuilder,): DynamicLayoutAttribute--><!--Device-unnamed-export declare function DynamicLayout (    algorithm: LayoutAlgorithm,    content_: CustomBuilder,): DynamicLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algorithm | [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md) | Yes | 指定动态布局组件的布局算法。 取非法值时，按照堆叠布局算法[StackLayoutAlgorithm](../../../reference/apis-arkui/js-apis-arkui-layoutAlgorithm.md#stacklayoutalgorithm)布局子组件，子组件堆叠排列。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [DynamicLayoutAttribute](arkts-arkui-arkui-components-arkdynamiclayout-dynamiclayoutattribute-c.md) |  |

