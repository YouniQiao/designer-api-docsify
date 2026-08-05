# ScrollOptions

Provides parameters for scrolling to a specific position in a scrollable container.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare interface ScrollOptions--><!--Device-unnamed-declare interface ScrollOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## animation

```TypeScript
animation?: ScrollAnimationOptions | boolean
```

Animation configuration Anonymous Object Rectification. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_ \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_Currently, the \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_List\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_, \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_Scroll\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_, \_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_Grid\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_, and \_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_WaterFlow\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_ support the \_\_\_HTML\_TAG\_DESC\_USD\_12\_\_\_Boolean\_\_\_HTML\_TAG\_DESC\_USD\_13\_\_\_ type and \_\_\_HTML\_TAG\_DESC\_USD\_14\_\_\_ICurve\_\_\_HTML\_TAG\_DESC\_USD\_15\_\_\_. \_\_\_HTML\_TAG\_DESC\_USD\_16\_\_\_ parameters and the boolean type enables default spring animation. [since 10 - 11] and the boolean type enables default spring animation. [since 12]

**Type:** ScrollAnimationOptions \| boolean

**Default:** ScrollAnimationOptions: { duration: 1000, curve: Curve.Ease, canOverScroll: false } [since 18]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollOptions-animation?: ScrollAnimationOptions | boolean--><!--Device-ScrollOptions-animation?: ScrollAnimationOptions | boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## canOverScroll

```TypeScript
canOverScroll?: boolean
```

Set whether the scroll target position can over the boundary.

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ScrollOptions-canOverScroll?: boolean--><!--Device-ScrollOptions-canOverScroll?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## xOffset

```TypeScript
xOffset: number | string
```

Horizontal scrolling offset. Anonymous Object Rectification. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_ \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_This parameter cannot be set in percentage. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_This parameter takes effect only when the scroll axis is the x-axis. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_Value range: Values less than 0 are treated as 0, and scrolling occurs without animation. Animated scrolling stops at the starting position by default. By setting the **animation** parameter, you can enable a bounce effect when the scrolling goes beyond the boundary. \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_If the parameter type is number, the unit is vp. \_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_

**Type:** number \| string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollOptions-xOffset: number | string--><!--Device-ScrollOptions-xOffset: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## yOffset

```TypeScript
yOffset: number | string
```

Vertical scrolling offset. Anonymous Object Rectification. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_ \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_This parameter cannot be set in percentage. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_This parameter takes effect only when the scroll axis is the y-axis. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_Value range: Values less than 0 are treated as 0, and scrolling occurs without animation. Animated scrolling stops at the starting position by default. By setting the **animation** parameter, you can enable a bounce effect when the scrolling goes beyond the boundary.\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_If the parameter type is number, the unit is vp. \_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_

**Type:** number \| string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollOptions-yOffset: number | string--><!--Device-ScrollOptions-yOffset: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

