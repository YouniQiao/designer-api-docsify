# Grid

The **Grid** component consists of cells formed by rows and columns. You can specify the cells where items are located to form various layouts. > **NOTE** > > The component has been bound with gestures to implement functions such as follow-up scrolling. If you need to add > custom gestures, refer to Gesture Blocking Enhancement.

## Child Components Child components are limited to GridItem and custom components. When using custom components inside **Grid**, it is recommended to wrap the custom component with a **GridItem** as the top-level container. Setting attributes or event methods directly on custom components is not recommended. Child components can be dynamically generated using rendering control types [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md), [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md), [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md), and [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md). **LazyForEach** or **Repeat** is recommended to optimize performance. > **NOTE** > > Below are the rules for calculating the indexes of the child components of **Grid**: > > The index increases in ascending order of child components. > > In the **if/else** statement, only the child components in the branch where the condition is met participate in the > index calculation. > > In the ForEach/LazyForEach and Repeat statements, index values are calculated for all expanded child components. > > After changes occur in [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md), > [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md), > [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md), and > [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md), index values are updated > accordingly for child components. > > The child component that has the **visibility** attribute set to **Hidden** or **None** is included in the index > calculation. > > The child component that has the **visibility** attribute set to **None** is not displayed, but still takes up the > corresponding cell. > > The child component that has the **position** attribute set is displayed in the corresponding cell, offset by the > distance specified by **position** relative to the upper left corner of the grid. This child component does not > scroll with the corresponding cell and is not displayed after the corresponding cell extends beyond the display > range of the grid. > > When there is a gap between child components, it is filled as much as possible based on the current display area. > Therefore, the relative position of grid items may change as the grid scrolls. > > Since API version 21, the maximum width and height of a single **Grid** child component are 16777216 px. In API > version 20 and earlier versions, the maximum width and height of a single **Grid** child component are 1000000 px. > Exceeding these limits may result in scrolling or display abnormalities.

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
| [ComputedBarAttribute](arkts-arkui-computedbarattribute-i.md) | Provides information about the position and length of the scrollbar. |
| [GridLayoutOptions](arkts-arkui-gridlayoutoptions-i.md) | Defines the grid layout options. In this API, **irregularIndexes** and **onGetIrregularSizeByIndex** can be used for grids where either **rowsTemplate** or **columnsTemplate** is set. These properties allow you to specify an index array and set the number of rows and columns to be occupied by a grid item at the specified index. For details about the usage, see [Example 3](../../../reference/apis-arkui/arkui-ts/ts-container-grid.md#example-3-implementing-a-scrollable-grid-with-grid-items-spanning-rows-and-columns). On the other hand, **onGetRectByIndex** can be used for grids where both **rowsTemplate** and **columnsTemplate** are set. It allows you to specify the position and size for the grid item at the specified index. For details about the usage, see [Example 1](../../../reference/apis-arkui/arkui-ts/ts-container-grid.md#example-1-creating-a-fixed-row-and-column-grid-layout). To improve the performance of **Grid** in scenarios such as jumps and column quantity changes, you are advised to use **GridLayoutOptions** whenever possible. Even if there are no special cross-row or cross-column nodes in **Grid**, performance during jumps can still be enhanced by using 'Grid(this.scroller, {regularSize: [1, 1]})'. |
| [StartLineInfo](arkts-arkui-startlineinfo-i-sys.md) | Define start line info used in GridLayoutOptions. |
| [UIGridEvent](arkts-arkui-uigridevent-i.md) | Represents the return value of the [getEvent('Grid')](../arkts-apis/arkts-arkui-typenode-getevent-f.md) method in **frameNode**, which can be used to set scroll events for a **Grid** node. |

### Types

| Name | Description |
| --- | --- |
| [OnGetStartIndexByIndexCallback](arkts-arkui-ongetstartindexbyindexcallback-t-sys.md) | Defines the callback type used in onGetStartIndexByIndex of GridLayoutOptions. |
| [OnGetStartIndexByOffsetCallback](arkts-arkui-ongetstartindexbyoffsetcallback-t-sys.md) | Defines the callback type used in onGetStartIndexByOffset of GridLayoutOptions. |
| [OnGridScrollIndexCallback](arkts-arkui-ongridscrollindexcallback-t.md) | Represents a callback for item changes in the visible area of the **Grid** component. |

### Enums

| Name | Description |
| --- | --- |
| [GridDirection](arkts-arkui-griddirection-e.md) | Enumerates the main axis layout directions. |
| [GridItemAlignment](arkts-arkui-griditemalignment-e.md) | Enumerates the alignment modes of grid items. > **NOTE：**> > 1. The **STRETCH** option only takes effect in scrollable grids.<br> > 2. The **STRETCH** option takes effect only if each grid item in a row is of a regular size (occupying only one > row and one column). It is not effective in scenarios where there are grid items spanning across rows or columns.<br> > 3. When **STRETCH** is used, only grid items without a set height will adopt the height of the tallest grid item > in the current row; the height of grid items with a set height will remain unchanged.<br> > 4. When **STRETCH** is used, the grid undergoes an additional layout process, which may incur additional > performance overhead. |

