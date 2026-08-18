# List

The **List** component provides a list container that presents a series of list items arranged in a column with the same width. It supports presentations of the same type of data in a multiple and coherent row style, for example, images or text. Lazy loading of **List** loads the child components in the visible area as required. Compared with full loading, lazy loading can improve the app startup speed and reduce the memory usage. The lazy loading capabilities vary when the **List** component is used together with [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md), [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md), or [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md). - When **List** is used together with **ForEach**, all child nodes are created at a time. The nodes within the screen range are laid out and rendered when needed. When a user swipes, the nodes that are out of the screen range are not removed from the tree, and the nodes that are within the screen range are laid out and rendered. - When **List** is used together with **LazyForEach**, all nodes within the screen range are created, laid out, and rendered at a time. When a user swipes, the nodes that are out of the screen range are removed from the tree, and the nodes that are within the screen range are created, laid out, and rendered. - When the **List** component is used together with **Repeat** with virtualScroll, the lazy loading behavior is the same as that of **LazyForEach**. When the **List** component is used together with **Repeat** without **virtualScroll**, the lazy loading behavior is the same as that of **ForEach**. If a scrollable component is nested in a **List** component, their scrolling directions are the same, and the main axis size is not set for the **List** component, the **List** component loads all child components. As a result, lazy loading does not take effect. In this scenario, you are advised to use the ListItemGroup component to optimize the performance. Preloading in **List** refers to loading not only the visible child components within the display area but also some invisible child components outside the display area during idle time. Preloading can reduce frame loss during scrolling and improve smoothness. Preloading takes effect only when lazy loading is used. You can set the number of components to be preloaded for the **List** component using cachedCount. By default, child components equivalent to one screen above and below the visible area are preloaded (up to a maximum of 16 rows). The preloading capabilities vary when the **List** component is used together with [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md), [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md), or [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md). - When the **List** component is used together with **ForEach** and **cachedCount** is set, in addition to laying out child components within the visible area, child components within the range of **cachedCount** outside the visible area are pre-laid out during idle time. - When the **List** component is used together with **LazyForEach** and **cachedCount** is set, in addition to creating and laying out child components within the display area, child components within the range of **cachedCount** outside the display area are pre-created and pre-laid out during idle time. - When the **List** component is used together with **Repeat** with virtualScroll, the preloading behavior is the same as that of **LazyForEach**. When the **List** component is used together with **Repeat** without **virtualScroll**, the preloading behavior is the same as that of **ForEach**. > **NOTE** > The component has been bound with gestures to implement functions such as follow-up scrolling. If you need to add > custom gestures, refer to Gesture Blocking Enhancement.

## Child Components Only the ListItem and ListItemGroup child components and custom components are supported. When using custom components inside **List**, you are advised to wrap the custom component with a **ListItem** or **ListItemGroup** as the top-level container. Setting attributes or event methods directly on custom components is not recommended. Child components can be dynamically generated using rendering control types [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md), [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md), [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md), and [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md). **LazyForEach** or **Repeat** is recommended to optimize performance. > **NOTE** > > If performance lag occurs when you process a large number of child components, consider using lazy loading, list > item caching, dynamic preloading, component reuse, and layout optimization. For best practices, see > [Optimizing Frame Loss for Long List Loading](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-best-practices-long-list). > > Starting from API version 21, the maximum width or height for a single child component inside a **List** container > is 16,777,216 px. In API version 20 and earlier versions, the limit was 1,000,000 px. If a child component exceeds > the applicable size limit, scrolling or display behavior may become abnormal. > > Below are the rules for calculating the indexes of the child components of **List**: > > - The index increases in ascending order of child components. > > - In the **if/else** statement, only the child components for which the condition evaluates to true participate in > the index calculation. > > - In the **ForEach**, **LazyForEach**, or **Repeat** statement, the indexes of all expanded subnodes are > calculated. > > - After changes occur in [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md), > [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md), > [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md), and > [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md), index values are updated > accordingly for child components. > > - Each **ListItemGroup** component is taken as a whole and assigned an index, and the indexes of the list items > within are not included in the index calculation. > > - Child components of **List** whose **visibility** attribute is set to **Hidden** or **None** are included in the > index calculation.

## List

```TypeScript
List(options?: ListOptions)
```

Creates a list container.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListInterface-(options?: ListOptions): ListAttribute--><!--Device-ListInterface-(options?: ListOptions): ListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ListOptions](arkts-arkui-listoptions-i.md) | No | Options of the **List** component. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [ChainAnimationOptions](arkts-arkui-chainanimationoptions-i-sys.md) | Defines the chain animation options. |
| [CloseSwipeActionOptions](arkts-arkui-closeswipeactionoptions-i.md) | Implements the callbacks and events for the ListItem in the expanded state. |
| [ListBackPressBehavior](arkts-arkui-listbackpressbehavior-i.md) | Defines the system back button behavior of the **List** component. |
| [ListDividerOptions](arkts-arkui-listdivideroptions-i.md) | Defines the divider style of the list or list item group. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. |
| [ListOptions](arkts-arkui-listoptions-i.md) | Defines the options of the **List** component. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. |
| [UIListEvent](arkts-arkui-uilistevent-i.md) | Represents the return value of the [getEvent('List')](../arkts-apis/arkts-arkui-typenode-getevent-f.md) method in **frameNode**, which can be used to set scroll events for a **List** node. |
| [VisibleListContentInfo](arkts-arkui-visiblelistcontentinfo-i.md) | Describes the details of the child components in the visible area of a list. |

### Types

| Name | Description |
| --- | --- |
| [OnListScrollIndexCallback](arkts-arkui-onlistscrollindexcallback-t.md) | Represents a callback for item changes in the visible area of the **List** component. |
| [OnScrollVisibleContentChangeCallback](arkts-arkui-onscrollvisiblecontentchangecallback-t.md) | Triggered when a child component enters or leaves the list display area. When the **List** component changes from having child components to being empty, the values of the reported **start** and **end** parameters remain the same as those when the component had child components last time. If the values of **start** and **end** are both **0**, the **List** component contains only one child component. > **NOTE：**> > This API can be called within attributeModifier since API version 14. |

### Enums

| Name | Description |
| --- | --- |
| [ChainEdgeEffect](arkts-arkui-chainedgeeffect-e-sys.md) | Declare edge effect of chain animation. |
| [ListItemAlign](arkts-arkui-listitemalign-e.md) | Sets the alignment mode of child components in the cross-axis direction of the list. |
| [ListItemGroupArea](arkts-arkui-listitemgrouparea-e.md) | Enumerates the areas of **ListItemGroup**. |
| [ScrollSnapAlign](arkts-arkui-scrollsnapalign-e.md) | Enumerates the alignment modes of list items when scrolling ends. |
| [ScrollSnapAnimationSpeed](arkts-arkui-scrollsnapanimationspeed-e.md) | Enumerates the speeds of the snap animation for list scrolling. |
| [ScrollState](arkts-arkui-scrollstate-e.md) | Enumerates the scrolling states. |
| [StickyStyle](arkts-arkui-stickystyle-e.md) | Enumerates the sticky styles. |

