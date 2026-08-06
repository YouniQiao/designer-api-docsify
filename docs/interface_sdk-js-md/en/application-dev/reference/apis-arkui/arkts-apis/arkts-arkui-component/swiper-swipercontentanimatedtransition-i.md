# SwiperContentAnimatedTransition

Defines the swiper content animated transition options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SwiperContentAnimatedTransition--><!--Device-unnamed-export declare interface SwiperContentAnimatedTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timeout

```TypeScript
timeout?: int
```

Defines the timeout of custom content transition animation after the page is moved out of the swiper. The unit is ms.If SwiperContentTransitionProxy.finishTransition() is not invoked, use the timeout as animation end time.Unit: ms, The value range is all integers. Default value: 0.

**Type:** int

**Default:** 0 ms

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperContentAnimatedTransition-timeout?: int--><!--Device-SwiperContentAnimatedTransition-timeout?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transition

```TypeScript
transition: Callback<SwiperContentTransitionProxy>
```

Called when custom content transition animation start.

**Type:** Callback&lt;SwiperContentTransitionProxy&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperContentAnimatedTransition-transition: Callback<SwiperContentTransitionProxy>--><!--Device-SwiperContentAnimatedTransition-transition: Callback<SwiperContentTransitionProxy>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

