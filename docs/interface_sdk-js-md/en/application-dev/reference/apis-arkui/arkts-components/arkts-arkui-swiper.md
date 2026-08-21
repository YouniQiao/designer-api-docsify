# Swiper

The **Swiper** component is able to display child components in a carousel-like manner.

> **NOTE**

> - The **Swiper** component implements the scrolling carousel effect through the built-in > PanGesture gesture. When the [disableSwipe](arkts-arkui-swiper-attribute.md#disableswipe) attribute is set > to **true**, the gesture listening is disabled, thereby preventing the scrolling operation. > > - When NodeContainer is reused in the **Swiper** component, recursive updates of parent > component state variables by child nodes are prohibited.

## Child Components

Supported

> **NOTE：**
> 
> - Allowed child component types: built-in and custom components, including rendering control types (
> [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md),
> [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md),
> [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md), and
> [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md)). To maximize the benefits of lazy
> loading, avoid mixing lazy loading components (including **LazyForEach** and **Repeat**) and non-lazy loading
> components, and exercise caution when using multiple lazy loading components. Avoid modifying the data source while
> an animation is in progress, as doing so can lead to layout issues.
> 
> - If a child component has its
> [visibility](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-visibility.md#visibility) attribute
> set to **Visibility.None** and the **Swiper** component has its **displayCount** attribute set to **'auto'**, the
> child component does not take up space in the viewport, but does not affect the number of navigation points. If a
> child component has its **visibility** attribute set to **Visibility.None** or **Visibility.Hidden**, it takes up
> space in the viewport, but is not displayed.
> 
> - Child components of the **Swiper** component are drawn based on their level if they have the
> offset attribute set. A child component with a higher level overwrites one with a
> lower level. For example, if the **Swiper** contains three child components and **offset({ x: 100 })** is set for
> the third child component, the third child component overwrites the first child component during horizontal loop
> playback. To prevent the first child component from being overwritten, set its zIndex
> attribute to a value greater than that of the third child component.
> 
> - When focus is moved to a custom child node, navigation indicators and arrows may be obscured by
> [focus styles](../../../ui/arkts-common-events-focus-event.md#focus-style) modifications that change **zIndex**.
> 
> - For a **Swiper** component with many child components, you can optimize the performance and reduce memory
> consumption by using lazy loading, data caching, preloading, and component reuse techniques. For best practices,
> see
> [Optimizing Frame Loss During Swiper Component Loading](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-swiper_high_performance_development_guide). &gt;

## Swiper

```TypeScript
Swiper(controller?: SwiperController)
```

Creates a **Swiper** component.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-SwiperInterface-(controller?: SwiperController): SwiperAttribute--><!--Device-SwiperInterface-(controller?: SwiperController): SwiperAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [SwiperController](arkts-arkui-swipercontroller-c.md) | No | Controller to bind to the component to manage page switching and preload specific child components. |

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

