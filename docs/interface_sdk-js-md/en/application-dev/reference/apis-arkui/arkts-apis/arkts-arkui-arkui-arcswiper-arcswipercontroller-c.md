# ArcSwiperController

ArcSwiper容器组件的控制器，可以将此对象绑定至ArcSwiper组件，实现控制ArcSwiper翻页等功能。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class ArcSwiperController--><!--Device-unnamed-export declare class ArcSwiperController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcSwiperAttribute, ArcSwiper, ArcDirection, ArcSwiperController, ArcDotIndicator } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor()
```

ArcSwiperController的构造函数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperController-constructor()--><!--Device-ArcSwiperController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## finishAnimation

```TypeScript
finishAnimation(handler?: FinishAnimationHandler): void
```

停止播放动画。默认无回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperController-finishAnimation(handler?: FinishAnimationHandler): void--><!--Device-ArcSwiperController-finishAnimation(handler?: FinishAnimationHandler): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [FinishAnimationHandler](arkts-arkui-finishanimationhandler-t.md) | No | 动画结束的回调。&lt;br&gt;默认值：不传入时无回调 |

## showNext

```TypeScript
showNext(): void
```

翻至下一页。翻页带动效切换过程，时长通过[duration](arkts-arkui-arkui-arcswiper-arcswiperattribute-c.md#duration)指定。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperController-showNext(): void--><!--Device-ArcSwiperController-showNext(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## showPrevious

```TypeScript
showPrevious(): void
```

翻至上一页。翻页带动效切换过程，时长通过[duration](arkts-arkui-arkui-arcswiper-arcswiperattribute-c.md#duration)指定。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperController-showPrevious(): void--><!--Device-ArcSwiperController-showPrevious(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

