# ArcSwiperContentAnimatedTransition

ArcSwiper自定义切换动画相关信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface ArcSwiperContentAnimatedTransition--><!--Device-unnamed-export declare interface ArcSwiperContentAnimatedTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcSwiperAttribute, ArcSwiper, ArcDirection, ArcSwiperController, ArcDotIndicator } from 'kits/@kit.ArkUI';
```

## timeout

```TypeScript
timeout?: int
```

ArcSwiper自定义切换动画超时时间。从页面执行默认动画（页面滑动）至移出视窗外的第一帧开始计时，如果到达该时间后，开发者仍未调用  
[SwiperContentTransitionProxy](../../../reference/apis-arkui/arkui-ts/ts-container-arcswiper copy.md#swipercontenttransitionproxy)的[finishTransition](arkts-arkui-arkui-arcswiper-arcswipercontenttransitionproxy-i.md#finishtransition)接口通知ArcSwiper组件此页面的自定义动画已结束，那么组件就会认为此页面的自定义动画已结束，立即在该页面节点下渲染树。&lt;br/&gt;单位：ms&lt;br/&gt;默认值：0。

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

自定义切换动画具体内容。

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;ArcSwiperContentTransitionProxy&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperContentAnimatedTransition-transition: Callback<ArcSwiperContentTransitionProxy>--><!--Device-ArcSwiperContentAnimatedTransition-transition: Callback<ArcSwiperContentTransitionProxy>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

