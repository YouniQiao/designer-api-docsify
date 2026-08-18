# Swiper

The **Swiper** component is able to display child components in a carousel-like manner. > **NOTE** > - The **Swiper** component implements the scrolling carousel effect through the built-in > PanGesture gesture. When the disableSwipe attribute is set > to **true**, the gesture listening is disabled, thereby preventing the scrolling operation. > > - When NodeContainer is reused in the **Swiper** component, recursive updates of parent > component state variables by child nodes are prohibited.

## Child Components Supported > **NOTE** > > - Allowed child component types: built-in and custom components, including rendering control types ( > [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md), > [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md), > [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md), and > [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md)). To maximize the benefits of lazy > loading, avoid mixing lazy loading components (including **LazyForEach** and **Repeat**) and non-lazy loading > components, and exercise caution when using multiple lazy loading components. Avoid modifying the data source while > an animation is in progress, as doing so can lead to layout issues. > > - If a child component has its > [visibility](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-visibility.md#visibility) attribute > set to **Visibility.None** and the **Swiper** component has its **displayCount** attribute set to **'auto'**, the > child component does not take up space in the viewport, but does not affect the number of navigation points. If a > child component has its **visibility** attribute set to **Visibility.None** or **Visibility.Hidden**, it takes up > space in the viewport, but is not displayed. > > - Child components of the **Swiper** component are drawn based on their level if they have the > offset attribute set. A child component with a higher level overwrites one with a > lower level. For example, if the **Swiper** contains three child components and **offset({ x: 100 })** is set for > the third child component, the third child component overwrites the first child component during horizontal loop > playback. To prevent the first child component from being overwritten, set its zIndex > attribute to a value greater than that of the third child component. > > - When focus is moved to a custom child node, navigation indicators and arrows may be obscured by > [focus styles](../../../ui/arkts-common-events-focus-event.md#focus-style) modifications that change **zIndex**. > > - For a **Swiper** component with many child components, you can optimize the performance and reduce memory > consumption by using lazy loading, data caching, preloading, and component reuse techniques. For best practices, > see > [Optimizing Frame Loss During Swiper Component Loading](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-swiper_high_performance_development_guide). >

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
| [ArrowStyle](arkts-arkui-arrowstyle-i.md) | Describes the left and right arrow attributes. |
| [AutoPlayOptions](arkts-arkui-autoplayoptions-i.md) | Defines the properties for controlling the automatic playback behavior. |
| [CachedCountOptions](arkts-arkui-cachedcountoptions-i.md) | Describes the configuration options for child components to be preloaded. |
| [IndicatorIconInfo](arkts-arkui-indicatoriconinfo-i.md) | Set the indicator item's icon for a specified index. |
| [IndicatorStyle](arkts-arkui-indicatorstyle-i.md) | Defines the style of the navigation indicator. |
| [SwiperAnimationEvent](arkts-arkui-swiperanimationevent-i.md) | Describes the animation information of the **Swiper** component. |
| [SwiperAutoFill](arkts-arkui-swiperautofill-i.md) | Describes the auto-fill attribute. |
| [SwiperContentAnimatedTransition](arkts-arkui-swipercontentanimatedtransition-i.md) | Provides the information about the custom page transition animation. |
| [SwiperContentTransitionProxy](arkts-arkui-swipercontenttransitionproxy-i.md) | Implements the proxy object returned during the execution of the custom page transition animation of the **Swiper** component. You can use this object to obtain the page information in the custom animation viewport. You can also call the **finishTransition** API of this object to notify the **Swiper** component that the custom animation has finished playing. |
| [SwiperContentWillScrollResult](arkts-arkui-swipercontentwillscrollresult-i.md) | Provides information related to the upcoming scroll action, including the index of the current page, the index of the page that will be displayed in the scroll direction, and the displacement of the scroll action. |

### Types

| Name | Description |
| --- | --- |
| [ContentDidScrollCallback](arkts-arkui-contentdidscrollcallback-t.md) | Triggered during the swipe action of the **Swiper** component. For details about the parameters, see [SwiperContentTransitionProxy](arkts-arkui-swipercontenttransitionproxy-i.md). |
| [ContentWillScrollCallback](arkts-arkui-contentwillscrollcallback-t.md) | Defines the callback triggered when the **Swiper** component is about to scroll. The return value indicates whether the scroll action is allowed. |
| [OnSwiperAnimationEndCallback](arkts-arkui-onswiperanimationendcallback-t.md) | Defines the callback triggered when the page transition animation ends. |
| [OnSwiperAnimationStartCallback](arkts-arkui-onswiperanimationstartcallback-t.md) | Defines the callback triggered when the page transition animation starts. |
| [OnSwiperGestureSwipeCallback](arkts-arkui-onswipergestureswipecallback-t.md) | Defines the callback triggered on a frame-by-frame basis when the page is turned by a swipe. |

### Enums

| Name | Description |
| --- | --- |
| [SwiperAnimationMode](arkts-arkui-swiperanimationmode-e.md) | Enumerates the animation mode for moving to a specific page in the **Swiper** component. |
| [SwiperDisplayMode](arkts-arkui-swiperdisplaymode-e.md) | Enumerates the modes in which elements are displayed along the main axis. |
| [SwiperNestedScrollMode](arkts-arkui-swipernestedscrollmode-e.md) | Enumerates the nested scrolling modes of the **Swiper** component and its parent container. |

