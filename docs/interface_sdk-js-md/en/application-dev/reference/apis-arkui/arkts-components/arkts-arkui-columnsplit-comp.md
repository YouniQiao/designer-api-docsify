# ColumnSplit

The **ColumnSplit** component lays out child components vertically and inserts a horizontal divider between every two child components. It is suitable for scenarios that require a vertical multi-area layout with dynamic area resizing, such as dashboard UIs and adjustable top-bottom split layouts. Through draggable dividers, users can flexibly adjust the height of each area, enhancing UI interactivity and user experience.

## Child Components

Supported

**ColumnSplit** limits the height of child components through dividers. During initialization, the divider positions are calculated based on the heights of the child components. After initialization, dynamically modifying the height of child components does not take effect, and the divider positions remain unchanged. After **resizeable** is set to **true**, the height of child components can be changed by dragging adjacent dividers.

After initialization, when dynamic modification of the margin, [border](arkts-arkui-common-comp-commonmethod-c.md#border), or padding universal attributes causes a child component size to exceed the spacing between adjacent dividers, dragging the divider to change the child component height is not supported.

## ColumnSplit

```TypeScript
ColumnSplit()
```

Creates a vertical split layout container with dividers between child components.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [ColumnSplitDividerStyle](arkts-arkui-columnsplit-comp-columnsplitdividerstyle-i.md) | Sets the distance between the child component and the upper and lower dividers. |

## Examples

```TypeScript
### Example 1: Setting the Resizable ColumnSplit Component

This example shows how to set the resizable ColumnSplit component and its effect.


```

```TypeScript
### Example 2: Setting the ColumnSplit Component with Spacing

This example shows how to set the ColumnSplit component with spacing and its effect.
```
