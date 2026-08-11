# OnTabsContentDidScrollCallback

```TypeScript
declare type OnTabsContentDidScrollCallback = (selectedIndex: number, index: number, position: number, mainAxisLength: number) => void
```

Defines the callback triggered when content in the **Tabs** component scrolls.  
> **NOTE：**
> 
> - For example, when the index of the currently selected tab page is **0**, during a transition animation from page
> 0 to page 1, the callback is triggered for all pages within the viewport on every frame. When pages 0 and 1 are
> both in the viewport, the callback is triggered twice per frame. The first callback has **selectedIndex** as **0**,
> **index** as **0**, **position** as the ratio of how much page 0 has moved relative to its position before the
> animation started on the current frame, and **mainAxisLength** as the length of page 0 on the main axis. The second
> callback has **selectedIndex** as **0**, **index** as **1**, **position** as the ratio of how much page 1 has moved
> relative to page 0 before the animation started on the current frame, and **mainAxisLength** as the length of page
> 1 on the main axis.
> 
> - If the animation curve is a spring interpolation curve, during the transition animation from page 0 to page 1,
> due to the position and velocity when the user lifts their finger off the screen, animation may overshoot and slide
> past to page 2, then bounce back to page 1. Throughout this process, a callback is triggered for pages 1 and 2
> within the viewport on every frame.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-declare type OnTabsContentDidScrollCallback = (selectedIndex: number, index: number, position: number, mainAxisLength: number) => void--><!--Device-unnamed-declare type OnTabsContentDidScrollCallback = (selectedIndex: number, index: number, position: number, mainAxisLength: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| selectedIndex | number | Yes |
| index | number | Yes |
| position | number | Yes |
| mainAxisLength | number | Yes |
