# Tabs

The **Tabs** component is a container component that allows users to switch between content views through tabs. Each tab page corresponds to a content view.
> **NOTE**>> ->> - Since API version 11, this component supports the safe area avoidance feature. The default value of the> [expandSafeArea]{}> **expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])**. You can override the default behavior by> rewriting this attribute. For versions earlier than API version 11, you need to manually implement safe area> avoidance together with the **expandSafeArea** attribute.

## Child Components

Only the child component TabContent and rendering control types [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md) and [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md) are supported. You are advised not to use custom components as child components. If **if/else** or **ForEach** is used, only **TabContent** can be used as the child component. You are advised not to use custom components as child components.

> **NOTE：**&gt;
> If the child component has the **visibility** attribute set to **None** or **Hidden**, it is hidden but still takes
> up space in the layout.&gt;
> When a displayed **Tabs** child component **TabContent** is hidden, it is not destroyed. For details about how to
> implement lazy loading and release on the page, see
> [Example 13](../../../reference/apis-arkui/arkui-ts/ts-container-tabs.md#example-13-implementing-lazy-loading-and-resource-release-of-pages).&gt;>
> If height is set to **auto** for **Tabs**, the tab height can be
> automatically adjusted based on that of the child component. When width
> is set to **auto**, the tab width can be automatically adjusted based on that of the child component.

## Tabs

```TypeScript
Tabs(options?: TabsOptions)
```

Create a **Tabs** container.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TabsOptions](arkts-arkui-tabsoptions-i.md) | No |

## Summary

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DividerStyle](arkts-arkui-dividerstyle-i.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [OnTabsAnimationEndCallback](arkts-arkui-ontabsanimationendcallback-t.md) |
| [OnTabsAnimationStartCallback](arkts-arkui-ontabsanimationstartcallback-t.md) |
| [OnTabsContentDidScrollCallback](arkts-arkui-ontabscontentdidscrollcallback-t.md) | Defines the callback triggered when content in the **Tabs** component scrolls. 
> **NOTE：**&gt;
> - For example, when the index of the currently selected tab page is **0**, during a transition animation from page
> 0 to page 1, the callback is triggered for all pages within the viewport on every frame. When pages 0 and 1 are
> both in the viewport, the callback is triggered twice per frame. The first callback has **selectedIndex** as **0**,
> **index** as **0**, **position** as the ratio of how much page 0 has moved relative to its position before the
> animation started on the current frame, and **mainAxisLength** as the length of page 0 on the main axis. The second
> callback has **selectedIndex** as **0**, **index** as **1**, **position** as the ratio of how much page 1 has moved
> relative to page 0 before the animation started on the current frame, and **mainAxisLength** as the length of page
> 1 on the main axis.&gt;
> - If the animation curve is a spring interpolation curve, during the transition animation from page 0 to page 1,
> due to the position and velocity when the user lifts their finger off the screen, animation may overshoot and slide
> past to page 2, then bounce back to page 1. Throughout this process, a callback is triggered for pages 1 and 2
> within the viewport on every frame. |
| [OnTabsContentWillChangeCallback](arkts-arkui-ontabscontentwillchangecallback-t.md) |
| [OnTabsGestureSwipeCallback](arkts-arkui-ontabsgestureswipecallback-t.md) |
| [TabsCustomContentTransitionCallback](arkts-arkui-tabscustomcontenttransitioncallback-t.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
