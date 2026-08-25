# ArcSwiperContentAnimatedTransition

Defines the swiper content animated transition options.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcSwiper, ArcSwiperAttribute, ArcDotIndicator, ArcDirection, ArcSwiperController } from '@kit.ArkUI';
```

## timeout

```TypeScript
timeout?: int
```

Defines the timeout of custom content transition animation after the page is moved out of the swiper. The unit is ms. If ArcSwiperContentTransitionProxy.finishTransition() is not invoked, use the timeout as animation end time.

**Type:** int

**Default:** 0ms

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## transition

```TypeScript
transition: Callback<ArcSwiperContentTransitionProxy>
```

Called when custom content transition animation start.

**Type:** Callback&lt;[ArcSwiperContentTransitionProxy](arkts-arkui-arkui-arcswiper-arcswipercontenttransitionproxy-i.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Circle
