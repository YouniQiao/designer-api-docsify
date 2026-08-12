# ArcSwiperContentTransitionProxy

The proxy object returned to the developer during the execution of the Swiper custom content transition animation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface ArcSwiperContentTransitionProxy--><!--Device-unnamed-export declare interface ArcSwiperContentTransitionProxy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcSwiperAttribute, ArcSwiper, ArcDirection, ArcSwiperController, ArcDotIndicator } from '@kit.ArkUI';
```

## finishTransition

```TypeScript
finishTransition(): void
```

Notifies Swiper page the custom content transition animation is complete.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperContentTransitionProxy-finishTransition(): void--><!--Device-ArcSwiperContentTransitionProxy-finishTransition(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## index

```TypeScript
index: int
```

The index value of the swiper content.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperContentTransitionProxy-index: int--><!--Device-ArcSwiperContentTransitionProxy-index: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## mainAxisLength

```TypeScript
mainAxisLength: double
```

the swiper main axis length for calculating position.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperContentTransitionProxy-mainAxisLength: double--><!--Device-ArcSwiperContentTransitionProxy-mainAxisLength: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## position

```TypeScript
position: double
```

the moving ratio of the swiper content from the start position of the swiper main axis.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperContentTransitionProxy-position: double--><!--Device-ArcSwiperContentTransitionProxy-position: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## selectedIndex

```TypeScript
selectedIndex: int
```

the index value of the swiper content selected before animation start.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperContentTransitionProxy-selectedIndex: int--><!--Device-ArcSwiperContentTransitionProxy-selectedIndex: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

