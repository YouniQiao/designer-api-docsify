# ArcSwiperAttribute

Defines the Arc swiper attribute functions.

**Inheritance/Implementation:** ArcSwiperAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface ArcSwiperAttribute extends CommonMethod--><!--Device-unnamed-export declare interface ArcSwiperAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcSwiperAttribute, ArcSwiper, ArcDirection, ArcSwiperController, ArcDotIndicator } from 'kits/@kit.ArkUI';
```

## customContentTransition

```TypeScript
default customContentTransition(transition: ArcSwiperContentAnimatedTransition | undefined): this
```

Custom swiper content transition animation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default customContentTransition(transition: ArcSwiperContentAnimatedTransition | undefined): this--><!--Device-ArcSwiperAttribute-default customContentTransition(transition: ArcSwiperContentAnimatedTransition | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transition | [ArcSwiperContentAnimatedTransition](arkts-arkui-arkui-arcswiper-arcswipercontentanimatedtransition-i.md) \| undefined | Yes | custom content transition animation, undefined means clear transition. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## digitalCrownSensitivity

```TypeScript
default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this
```

Set the sensitivity of rotating crown.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this--><!--Device-ArcSwiperAttribute-default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensitivity | [CrownSensitivity](arkts-arkui-crownsensitivity-e.md) \| undefined | Yes | The sensitivity of rotating crown, default value is { MEDIUM }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## disableSwipe

```TypeScript
default disableSwipe(disabled: boolean | undefined): this
```

Set whether to disable sliding function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default disableSwipe(disabled: boolean | undefined): this--><!--Device-ArcSwiperAttribute-default disableSwipe(disabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| disabled | boolean \| undefined | Yes | The value indicates whether the sliding function is enabled, default value is { false }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## disableTransitionAnimation

```TypeScript
default disableTransitionAnimation(disabled: boolean | undefined): this
```

Custom swiper content transition animation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default disableTransitionAnimation(disabled: boolean | undefined): this--><!--Device-ArcSwiperAttribute-default disableTransitionAnimation(disabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| disabled | boolean \| undefined | Yes | the value indicates whether to disable the transition animation, default value is { false }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## duration

```TypeScript
default duration(duration: int | undefined): this
```

Set the animation duration of the switch in ms.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default duration(duration: int | undefined): this--><!--Device-ArcSwiperAttribute-default duration(duration: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| duration | int \| undefined | Yes | Duration of animation, default value is { 400ms }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## effectMode

```TypeScript
default effectMode(edgeEffect: EdgeEffect | undefined): this
```

Set effect when scrolling over edge.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default effectMode(edgeEffect: EdgeEffect | undefined): this--><!--Device-ArcSwiperAttribute-default effectMode(edgeEffect: EdgeEffect | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| edgeEffect | [EdgeEffect](arkts-arkui-edgeeffect-e.md) \| undefined | Yes | scrolling effect over edge, default value is { EdgeEffect.Spring }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## index

```TypeScript
default index(index: int | undefined): this
```

Set the index value of the displayed subcomponent.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default index(index: int | undefined): this--><!--Device-ArcSwiperAttribute-default index(index: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int \| undefined | Yes | The index value of the subcomponents to be displayed, default value is { 0 }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## indicator

```TypeScript
default indicator(style: ArcDotIndicator | boolean | undefined): this
```

Set whether the indicator is available or set the indicator style.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default indicator(style: ArcDotIndicator | boolean | undefined): this--><!--Device-ArcSwiperAttribute-default indicator(style: ArcDotIndicator | boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) \| boolean \| undefined | Yes | The style information of the indicator or whether to display the indicator, default value is { true }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onAnimationEnd

```TypeScript
default onAnimationEnd(handler: AnimationEndHandler | undefined): this
```

Called when the swiper animation has ended.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default onAnimationEnd(handler: AnimationEndHandler | undefined): this--><!--Device-ArcSwiperAttribute-default onAnimationEnd(handler: AnimationEndHandler | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [AnimationEndHandler](arkts-arkui-animationendhandler-t.md) \| undefined | Yes | The handler is used to listen for the animation has ended, undefined means clear handler. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onAnimationStart

```TypeScript
default onAnimationStart(handler: AnimationStartHandler | undefined): this
```

Called when the swiper animation has started.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default onAnimationStart(handler: AnimationStartHandler | undefined): this--><!--Device-ArcSwiperAttribute-default onAnimationStart(handler: AnimationStartHandler | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [AnimationStartHandler](arkts-arkui-animationstarthandler-t.md) \| undefined | Yes | The handler is used to listen for the animation has started, undefined means clear handler. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(handler: IndexChangedHandler | undefined): this
```

Called when the index value has changed.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default onChange(handler: IndexChangedHandler | undefined): this--><!--Device-ArcSwiperAttribute-default onChange(handler: IndexChangedHandler | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [IndexChangedHandler](arkts-arkui-indexchangedhandler-t.md) \| undefined | Yes | The handler is used to listen for index values that have changed, undefined means clear handler. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onGestureSwipe

```TypeScript
default onGestureSwipe(handler: GestureSwipeHandler | undefined): this
```

Called when swiping the switch using gestures.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default onGestureSwipe(handler: GestureSwipeHandler | undefined): this--><!--Device-ArcSwiperAttribute-default onGestureSwipe(handler: GestureSwipeHandler | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [GestureSwipeHandler](arkts-arkui-gestureswipehandler-t.md) \| undefined | Yes | The handler is used to listen for swiping through gestures, undefined means clear handler. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setArcSwiperOptions

```TypeScript
default setArcSwiperOptions(controller?: ArcSwiperController): this
```

Set arcSwiper options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default setArcSwiperOptions(controller?: ArcSwiperController): this--><!--Device-ArcSwiperAttribute-default setArcSwiperOptions(controller?: ArcSwiperController): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [ArcSwiperController](arkts-arkui-arkui-arcswiper-arcswipercontroller-c.md) | No | ArcSwiper constructor options |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns instance of ArcSwiperAttribute. |

## vertical

```TypeScript
default vertical(isVertical: boolean | undefined): this
```

Set whether to slide vertically.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default vertical(isVertical: boolean | undefined): this--><!--Device-ArcSwiperAttribute-default vertical(isVertical: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isVertical | boolean \| undefined | Yes | The value indicates whether to slide vertically, default value is { false }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

