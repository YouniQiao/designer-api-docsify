# Tabs

The **Tabs** component is a container component that allows users to switch between content views through tabs. Each tab page corresponds to a content view. > **NOTE** > > - > > - Since API version 11, this component supports the safe area avoidance feature. The default value of the > [expandSafeArea]{} > **expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])**. You can override the default behavior by > rewriting this attribute. For versions earlier than API version 11, you need to manually implement safe area > avoidance together with the **expandSafeArea** attribute.

## Child Components Only the child component TabContent and rendering control types [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md) and [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md) are supported. You are advised not to use custom components as child components. If **if/else** or **ForEach** is used, only **TabContent** can be used as the child component. You are advised not to use custom components as child components. > **NOTE** > > If the child component has the **visibility** attribute set to **None** or **Hidden**, it is hidden but still takes > up space in the layout. > > When a displayed **Tabs** child component **TabContent** is hidden, it is not destroyed. For details about how to > implement lazy loading and release on the page, see > [Example 13](../../../reference/apis-arkui/arkui-ts/ts-container-tabs.md#example-13-implementing-lazy-loading-and-resource-release-of-pages). > > > If height is set to **auto** for **Tabs**, the tab height can be > automatically adjusted based on that of the child component. When width > is set to **auto**, the tab width can be automatically adjusted based on that of the child component.

## Tabs

```TypeScript
Tabs(options?: TabsOptions)
```

Create a **Tabs** container.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TabsInterface-(options?: TabsOptions): TabsAttribute--><!--Device-TabsInterface-(options?: TabsOptions): TabsAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | TabsOptions | No | Options of the **Tabs** component. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [BarGridColumnOptions](arkts-arkui-bargridcolumnoptions-i.md) | Implements a **BarGridColumnOptions** object for setting the visible area of the tab bar in grid mode, including the column margin and gutter, as well as the number of columns occupied by tabs under small, medium, and large screen sizes. |
| [FloatingTabBarStyle](arkts-arkui-floatingtabbarstyle-i.md) | Provides an interface for the options for the floating bar mode. |
| [FloatingTabBarWidth](arkts-arkui-floatingtabbarwidth-i.md) | Provides an interface for the options for the floating bar width of the tab width at different breakpoints. |
| [ScrollableBarModeOptions](arkts-arkui-scrollablebarmodeoptions-i.md) | Implements a **ScrollableBarModeOptions** object. |
| [TabContentAnimatedTransition](arkts-arkui-tabcontentanimatedtransition-i.md) | Provides the information about the custom tab switching animation. |
| [TabContentTransitionProxy](arkts-arkui-tabcontenttransitionproxy-i.md) | Implements the proxy object returned during the execution of the custom switching animation of the **Tabs** component. You can use this object to obtain the start and target pages for the custom tab switching animation. In addition, you can call the **finishTransition** API of this object to notify the **Tabs** component of the ending of the custom animation. |
| [TabsAnimationEvent](arkts-arkui-tabsanimationevent-i.md) | Describes the animation information of the **Tabs** component. |

### Types

| Name | Description |
| --- | --- |
| [OnTabsAnimationEndCallback](arkts-arkui-ontabsanimationendcallback-t.md) | Defines the callback triggered when the tab switching animation ends. |
| [OnTabsAnimationStartCallback](arkts-arkui-ontabsanimationstartcallback-t.md) | Defines the callback triggered when the tab switching animation starts. |
| [OnTabsContentDidScrollCallback](arkts-arkui-ontabscontentdidscrollcallback-t.md) | Defines the callback triggered when content in the **Tabs** component scrolls. > **NOTE：**> > - For example, when the index of the currently selected tab page is **0**, during a transition animation from page > 0 to page 1, the callback is triggered for all pages within the viewport on every frame. When pages 0 and 1 are > both in the viewport, the callback is triggered twice per frame. The first callback has **selectedIndex** as **0**, > **index** as **0**, **position** as the ratio of how much page 0 has moved relative to its position before the > animation started on the current frame, and **mainAxisLength** as the length of page 0 on the main axis. The second > callback has **selectedIndex** as **0**, **index** as **1**, **position** as the ratio of how much page 1 has moved > relative to page 0 before the animation started on the current frame, and **mainAxisLength** as the length of page > 1 on the main axis. > > - If the animation curve is a spring interpolation curve, during the transition animation from page 0 to page 1, > due to the position and velocity when the user lifts their finger off the screen, animation may overshoot and slide > past to page 2, then bounce back to page 1. Throughout this process, a callback is triggered for pages 1 and 2 > within the viewport on every frame. |
| [OnTabsContentWillChangeCallback](arkts-arkui-ontabscontentwillchangecallback-t.md) | Defines the callback invoked when a new page is about to be displayed. |
| [OnTabsGestureSwipeCallback](arkts-arkui-ontabsgestureswipecallback-t.md) | Defines the callback triggered on a frame-by-frame basis during a swipe-based page turn. |
| [TabsCustomContentTransitionCallback](arkts-arkui-tabscustomcontenttransitioncallback-t.md) | Defines the callback invoked when the custom tab transition animation starts. |
| [UIMaterial](arkts-arkui-uimaterial-t.md) | UIMaterial |

### Enums

| Name | Description |
| --- | --- |
| [AnimationMode](arkts-arkui-animationmode-e.md) | Enumerates the animation modes for switching between tabs. |
| [BarMode](arkts-arkui-barmode-e.md) | Enumerates layout modes of the tab bar. |
| [BarPosition](arkts-arkui-barposition-e.md) | Enumerates the positions of the **Tabs** component. |
| [LayoutStyle](arkts-arkui-layoutstyle-e.md) | Enumerates the tab layout styles of the tab bar when not scrolling in scrollable mode. |
| [TabsCacheMode](arkts-arkui-tabscachemode-e.md) | Enumerates the caching modes for child components. |
| [TabsNestedScrollMode](arkts-arkui-tabsnestedscrollmode-e.md) | Enumerates the nested scrolling modes of the **Tabs** component and its parent container. |

