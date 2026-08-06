# ScrollAnimationOptions

Provides parameters for customizing scroll animations.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface ScrollAnimationOptions--><!--Device-unnamed-declare interface ScrollAnimationOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## canOverScroll

```TypeScript
canOverScroll?: boolean
```

Whether to enable overscroll.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_ Scrolling can exceed the boundary and initiate a bounce animation when this parameter is set to \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_true\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_,and the component's \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_edgeEffect\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_ attribute is set to EdgeEffect.Spring.\_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_

**Type:** boolean

**Default:** false

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScrollAnimationOptions-canOverScroll?: boolean--><!--Device-ScrollAnimationOptions-canOverScroll?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## curve

```TypeScript
curve?: Curve | ICurve
```

Scrolling curve.

**Type:** Curve \| ICurve

**Default:** Curve.Ease

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScrollAnimationOptions-curve?: Curve | ICurve--><!--Device-ScrollAnimationOptions-curve?: Curve | ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: number
```

Scrolling duration.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_Scrolling duration.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_Default value: **1000**\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_Unit: ms\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_**NOTE**\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_A value less than 0 evaluates to the default value.\_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_

**Type:** number

**Default:** 1000

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScrollAnimationOptions-duration?: number--><!--Device-ScrollAnimationOptions-duration?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

