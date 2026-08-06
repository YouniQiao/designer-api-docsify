# ScrollBar

The **ScrollBar** component is designed to be used together with scrollable components such as
[ArcList]{@link @ohos.arkui.ArcList}, [List]{@link list}, [Grid]{@link grid}, [Scroll]{@link scroll}, and
[WaterFlow]{@link water_flow}.

> **NOTE**
>
> - This component is supported since API version 8. Updates will be marked with a superscript to indicate their
> earliest API version.
>
> - If the size of the main axis direction is not set for **ScrollBar**, the **maxSize** value in the
> [layout constraints]{@link FrameNode:LayoutConstraint} of the parent component is used. If the parent component of
> the **ScrollBar** component contains a scrollable component, such as [ArcList]{@link @ohos.arkui.ArcList},
> [List]{@link list}, [Grid]{@link grid}, [Scroll]{@link scroll}, or [WaterFlow]{@link water_flow}, you are advised
> to set the size in the main axis direction of the **ScrollBar**; otherwise, the size in the main axis direction of
> **ScrollBar** may become infinite.

## Child Components

This component can contain a single child component.

## Example 1: Implementing a ScrollBar Component with Child Components

This example illustrates the style of a **ScrollBar** component with child components.

\_\_\_CODE\_BLOCK\_DESC\_USD\_0\_\_\_

!\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_

## Example 2: Implementing a ScrollBar Component Without Child Components

This example illustrates the style of a **ScrollBar** component without child components. The  
[scrollBarColor]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ attribute is added since API version 20.

\_\_\_CODE\_BLOCK\_DESC\_USD\_0\_\_\_

!\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_

## Example 3: Enabling Nested Scrolling

This example demonstrates how to enable nested scrolling for a **ScrollBar** component using the  
[enableNestedScroll]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ attribute. This feature is available from API version 20.

\_\_\_CODE\_BLOCK\_DESC\_USD\_0\_\_\_

!\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_

## ScrollBar

```TypeScript
ScrollBar(value: ScrollBarOptions)
```

Creates a scroll bar.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollBarInterface-(value: ScrollBarOptions): ScrollBarAttribute--><!--Device-ScrollBarInterface-(value: ScrollBarOptions): ScrollBarAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Parameters of the **ScrollBar** component.  |

## Summary

