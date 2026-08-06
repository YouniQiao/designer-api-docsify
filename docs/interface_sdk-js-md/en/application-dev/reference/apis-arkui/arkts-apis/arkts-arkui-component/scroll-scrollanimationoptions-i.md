# ScrollAnimationOptions

Provides parameters for customizing scroll animations.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ScrollAnimationOptions--><!--Device-unnamed-export declare interface ScrollAnimationOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## canOverScroll

```TypeScript
canOverScroll?: boolean
```

Whether to enable overscroll.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_.\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_ Scrolling can exceed the boundary and initiate a bounce animation when this parameter is set to \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_true\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_,and the component's \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_edgeEffect\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_ attribute is set to EdgeEffect.Spring.\_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollAnimationOptions-canOverScroll?: boolean--><!--Device-ScrollAnimationOptions-canOverScroll?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## curve

```TypeScript
curve?: Curve | ICurve
```

Scrolling curve.

**Type:** Curve \| ICurve

**Default:** Curve.Ease

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollAnimationOptions-curve?: Curve | ICurve--><!--Device-ScrollAnimationOptions-curve?: Curve | ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: int
```

Scrolling duration.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_.The value should be an integer.\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_A value less than 0 evaluates to the default value.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_

**Type:** int

**Default:** 1000

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollAnimationOptions-duration?: int--><!--Device-ScrollAnimationOptions-duration?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

