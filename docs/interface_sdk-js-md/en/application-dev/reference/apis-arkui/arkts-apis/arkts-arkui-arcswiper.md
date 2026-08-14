# @ohos.arkui.ArcSwiper

## Modules to Import

```TypeScript
import { ArcSwiper } from 'ArcSwiper';
import { ArcSwiperAttribute } from 'ArcSwiperAttribute';
import { ArcDotIndicator } from 'ArcDotIndicator';
import { ArcDirection } from 'ArcDirection';
import { ArcSwiperController } from 'ArcSwiperController';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ArcSwiperController](arkts-arkui-arkui-arcswiper-arcswipercontroller-c.md) | Implements the controller of the **ArcSwiper** component. You can bind this object to the **ArcSwiper** component and use it to control page switching. |

### Interfaces

| Name | Description |
| --- | --- |
| [SwiperContentAnimatedTransition](arkts-arkui-arkui-arcswiper-swipercontentanimatedtransition-i.md) | Provides the information about the custom page transition animation. |
| [SwiperContentTransitionProxy](arkts-arkui-arkui-arcswiper-swipercontenttransitionproxy-i.md) | Implements the proxy object returned during the execution of the custom page transition animation of the **ArcSwiper** component. You can use this object to obtain the page information in the custom animation viewport. You can also call the **finishTransition** API of this object to notify the **ArcSwiper** component that the custom animation has finished playing. > **NOTE：**> - For example, when the index of the currently selected child component is 0, during a transition animation from > page 0 to page 1, the callback is triggered for all pages within the viewport on every frame. When pages 0 and 1 > are both in the viewport, the callback is triggered twice per frame. The first callback has **selectedIndex** as > **0**, **index** as **0**, **position** as the ratio of how much page 0 has moved relative to its position before > the animation started on the current frame, and **mainAxisLength** as the length of page 0 on the main axis. The > second callback has **selectedIndex** as **0**, **index** as **1**, **position** as the ratio of how much page 1 > has moved relative to page 0 before the animation started on the current frame, and **mainAxisLength** as the > length of page 1 on the main axis. > > - If the animation curve is a spring interpolation curve, during the transition animation from page 0 to page 1, > due to the position and velocity when the user lifts their finger off the screen, animation may overshoot and slide > past to page 2, then bounce back to page 1. Throughout this process, a callback is triggered for pages 1 and 2 > within the viewport on every frame. |

### Enums

| Name | Description |
| --- | --- |
| [ArcDirection](arkts-arkui-arkui-arcswiper-arcdirection-e.md) | Declare the direction of arc indicator. |

### Types

| Name | Description |
| --- | --- |
| [AnimationEndHandler](arkts-arkui-animationendhandler-t.md) | Defines the callback triggered when the page transition animation ends. |
| [AnimationStartHandler](arkts-arkui-animationstarthandler-t.md) | Defines the callback triggered when the page transition animation starts. |
| [FinishAnimationHandler](arkts-arkui-finishanimationhandler-t.md) | Defines the callback to notify the application when the animation stops playing. |
| [GestureSwipeHandler](arkts-arkui-gestureswipehandler-t.md) | Defines the callback triggered on a frame-by-frame basis during a swipe-based page turn. |
| [IndexChangedHandler](arkts-arkui-indexchangedhandler-t.md) | Defines the callback to notify the application when the index of the currently displayed element changes. |

