# DynamicLayoutInterface

```TypeScript
export interface DynamicLayoutInterface
```

A dynamic layout container component that supports dynamically switching between different layout algorithms at runtime without altering the state of child components. Using **DynamicLayout** improves layout flexibility and simplifies the development process for UI adaptation and multi-view switching. It is suitable for scenarios such as responsive layouts (adapting to different screen sizes), multi-view mode switching (e.g., switching between list, grid, and waterfall layouts), and user-defined layouts.

**Since:** 24

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DynamicLayout, DynamicLayoutAttribute } from '@kit.ArkUI';
```

## [[Call]]

```TypeScript
(algorithm: LayoutAlgorithm): DynamicLayoutAttribute
```

Defines the dynamic layout container.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algorithm | [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md) | Yes | Layout algorithm for the dynamic layout container. Supported layout algorithm instances include [RowLayoutAlgorithm](arkts-arkui-layoutalgorithm-rowlayoutalgorithm-c.md) (horizontal linear layout, suitable for horizontal arrangement scenarios), [ColumnLayoutAlgorithm](arkts-arkui-layoutalgorithm-columnlayoutalgorithm-c.md) (vertical linear layout, suitable for vertical arrangement scenarios), [StackLayoutAlgorithm](arkts-arkui-layoutalgorithm-stacklayoutalgorithm-c.md) (stack layout, suitable for overlapping scenarios), [GridLayoutAlgorithm](arkts-arkui-layoutalgorithm-gridlayoutalgorithm-c.md) (grid layout, suitable for regular grid scenarios), and [CustomLayoutAlgorithm](arkts-arkui-layoutalgorithm-customlayoutalgorithm-c.md) (custom layout, suitable for complex and special layout scenarios). For details, see [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md). If an invalid value (such as **null**, **undefined**, or an invalid layout algorithm object) is passed, child components are laid out according to [StackLayoutAlgorithm](arkts-arkui-layoutalgorithm-stacklayoutalgorithm-c.md), with child components stacked on top of each other. |

**Return value:**

| Type | Description |
| --- | --- |
| [DynamicLayoutAttribute](arkts-arkui-arkui-components-arkdynamiclayout-dynamiclayoutattribute-c.md) |  |
