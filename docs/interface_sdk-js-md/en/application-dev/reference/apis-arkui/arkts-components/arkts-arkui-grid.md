# Grid

The **Grid** component consists of cells formed by rows and columns. You can specify the cells where items are located to form various layouts.
> **NOTE**>> The component has been bound with gestures to implement functions such as follow-up scrolling. If you need to add> custom gestures, refer to Gesture Blocking Enhancement.

## Child Components

Child components are limited to GridItem and custom components. When using custom components inside **Grid**, it is recommended to wrap the custom component with a **GridItem** as the top-level container. Setting attributes or event methods directly on custom components is not recommended.Child components can be dynamically generated using rendering control types [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md), [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md), [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md), and [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md). **LazyForEach** or **Repeat** is recommended to optimize performance.

> **NOTE：**&gt;
> Below are the rules for calculating the indexes of the child components of **Grid**:&gt;
> The index increases in ascending order of child components.&gt;
> In the **if/else** statement, only the child components in the branch where the condition is met participate in the
> index calculation.&gt;
> In the ForEach/LazyForEach and Repeat statements, index values are calculated for all expanded child components.&gt;
> After changes occur in [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md),
> [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md),
> [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md), and
> [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md), index values are updated
> accordingly for child components.&gt;
> The child component that has the **visibility** attribute set to **Hidden** or **None** is included in the index
> calculation.&gt;
> The child component that has the **visibility** attribute set to **None** is not displayed, but still takes up the
> corresponding cell.&gt;
> The child component that has the **position** attribute set is displayed in the corresponding cell, offset by the
> distance specified by **position** relative to the upper left corner of the grid. This child component does not
> scroll with the corresponding cell and is not displayed after the corresponding cell extends beyond the display
> range of the grid.&gt;
> When there is a gap between child components, it is filled as much as possible based on the current display area.
> Therefore, the relative position of grid items may change as the grid scrolls.&gt;
> Since API version 21, the maximum width and height of a single **Grid** child component are 16777216 px. In API
> version 20 and earlier versions, the maximum width and height of a single **Grid** child component are 1000000 px.
> Exceeding these limits may result in scrolling or display abnormalities.

## Grid

```TypeScript
Grid(scroller?: Scroller, layoutOptions?: GridLayoutOptions)
```

Creates a **Grid** component.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GridInterface-(scroller?: Scroller, layoutOptions?: GridLayoutOptions): GridAttribute--><!--Device-GridInterface-(scroller?: Scroller, layoutOptions?: GridLayoutOptions): GridAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scroller | Scroller | No | Controller, which can be bound to scrollable components.<br>**NOTE**<br>It cannot be bound to the same scrolling control object as other scrollable components, such as ArcList, List, Grid, Scroll, and WaterFlow. |
| layoutOptions | [GridLayoutOptions](arkts-arkui-gridlayoutoptions-i.md) | No | Grid layout options. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |

### Types

| Name | Description |
| --- | --- |

### Enums

| Name | Description |
| --- | --- |

