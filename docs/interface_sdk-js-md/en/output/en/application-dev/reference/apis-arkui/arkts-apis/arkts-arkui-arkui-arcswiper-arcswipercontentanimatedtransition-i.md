# ArcSwiperContentAnimatedTransition

Defines the swiper content animated transition options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface ArcSwiperContentAnimatedTransition--><!--Device-unnamed-export declare interface ArcSwiperContentAnimatedTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## timeout

```TypeScript
timeout?: int
```

Defines the timeout of custom content transition animation after the page is moved out of the swiper. The unit is ms. If ArcSwiperContentTransitionProxy.finishTransition() is not invoked, use the timeout as animation end time.

**Type:** int

**Default:** 0ms

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperContentAnimatedTransition-timeout?: int--><!--Device-ArcSwiperContentAnimatedTransition-timeout?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## transition

```TypeScript
transition: Callback<ArcSwiperContentTransitionProxy>
```

Called when custom content transition animation start.

**Type:** Callback&lt;ArcSwiperContentTransitionProxy&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperContentAnimatedTransition-transition: Callback<ArcSwiperContentTransitionProxy>--><!--Device-ArcSwiperContentAnimatedTransition-transition: Callback<ArcSwiperContentTransitionProxy>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

