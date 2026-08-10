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

Swiper自定义切换动画超时时间。从页面执行默认动画（页面滑动）至移出视窗外的第一帧开始计时，如果到达该时间后，开发者仍未调用  
[SwiperContentTransitionProxy](../arkts-components/arkts-arkui-swipercontenttransitionproxy-i.md/arkts-arkui-swipercontenttransitionproxy-i.md)的finishTransition接口通知Swiper组件此页面的自定义动画已结束，那么组件就会认为此页面的自定义动画已结束，立即将该页面节点下渲染树。单位：ms单位为： ms，取值范围为全体整数，取值为undefined时，按默认值处理。 默认值： 0。

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

自定义切换动画具体内容。

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;SwiperContentTransitionProxy&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperContentAnimatedTransition-transition: Callback<SwiperContentTransitionProxy>--><!--Device-SwiperContentAnimatedTransition-transition: Callback<SwiperContentTransitionProxy>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

