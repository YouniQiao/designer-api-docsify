# DynamicLayout

A dynamic layout container component that supports dynamically switching between different layout algorithms at runtime without altering the state of child components. Using **DynamicLayout** improves layout flexibility and simplifies the development process for UI adaptation and multi-view switching. It is suitable for scenarios such as responsive layouts (adapting to different screen sizes), multi-view mode switching (e.g., switching between list, grid, and waterfall layouts), and user-defined layouts.

## Child Components

Child components are supported.

## DynamicLayout

```TypeScript
DynamicLayout(algorithm: LayoutAlgorithm)
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
| algorithm | [LayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-i.md) | Yes | Layout algorithm for the dynamic layout container. Supported layout algorithm instances include [RowLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-rowlayoutalgorithm-c.md) (horizontal linear layout, suitable for horizontal arrangement scenarios), [ColumnLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-columnlayoutalgorithm-c.md) (vertical linear layout, suitable for vertical arrangement scenarios), [StackLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-stacklayoutalgorithm-c.md) (stack layout, suitable for overlapping scenarios), [GridLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-gridlayoutalgorithm-c.md) (grid layout, suitable for regular grid scenarios), and [CustomLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-customlayoutalgorithm-c.md) (custom layout, suitable for complex and special layout scenarios). For details, see [LayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-i.md). If an invalid value (such as **null**, **undefined**, or an invalid layout algorithm object) is passed, child components are laid out according to [StackLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-stacklayoutalgorithm-c.md), with child components stacked on top of each other. |

## Summary

## Examples

```TypeScript
### Example 1: Implementing Waterfall Layout Using a Custom Layout Algorithm

This example shows how to override the onMeasure and onLayout functions to implement a waterfall layout for displaying a product list. In the waterfall layout, the heights of child components are calculated and the cumulative height of each column is recorded during the measurement phase, and child components are assigned to the column with the smallest current height during the layout phase, achieving an automatic fill effect.

Since API version 24, onMeasure and onLayout are added.


```

```TypeScript
### Example 2: Switching the Layout Algorithm

This example shows how to dynamically switch the layout algorithm of the DynamicLayout component by changing the [LayoutAlgorithm](../arkts-apis/arkts-arkui-arkui-layoutalgorithm.md) variable decorated with [@Local](../../../ui/state-management/arkts-new-local.md). The example demonstrates how to switch the layout algorithm to [RowLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-rowlayoutalgorithm-c.md) (horizontal linear layout), [ColumnLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-columnlayoutalgorithm-c.md) (vertical linear layout), [StackLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-stacklayoutalgorithm-c.md) (stack layout), and [GridLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-gridlayoutalgorithm-c.md) (grid layout).

> NOTE
> 
> In this example, the preset layoutGravity attribute takes effect only under the Stack layout algorithm and does not take effect under the Row or Column layout algorithm.

Since API version 24, RowLayoutAlgorithm, ColumnLayoutAlgorithm, StackLayoutAlgorithm, and GridLayoutAlgorithm have been added.


```

```TypeScript
### Example 3: Modifying the Layout Algorithm Attributes

This example shows how to modify the space and justifyContent attributes of [RowLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-rowlayoutalgorithm-c.md) to update the layout effect of the DynamicLayout component.

Since API version 24, the space and justifyContent attributes are added.
```
