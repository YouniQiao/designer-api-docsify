# ScrollOptions

Provides parameters for scrolling to a specific position in a scrollable container.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ScrollOptions--><!--Device-unnamed-export declare interface ScrollOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## animation

```TypeScript
animation?: ScrollAnimationOptions | boolean
```

Animation configuration Anonymous Object Rectification.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_.\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_Currently, the \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_List\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_, \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_Scroll\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_, \_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_Grid\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_, and \_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_WaterFlow\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_ support the\_\_\_HTML\_TAG\_DESC\_USD\_12\_\_\_Boolean\_\_\_HTML\_TAG\_DESC\_USD\_13\_\_\_ type and \_\_\_HTML\_TAG\_DESC\_USD\_14\_\_\_ICurve\_\_\_HTML\_TAG\_DESC\_USD\_15\_\_\_.\_\_\_HTML\_TAG\_DESC\_USD\_16\_\_\_

**Type:** ScrollAnimationOptions \| boolean

**Default:** ScrollAnimationOptions: { duration: 1000, curve: Curve.Ease, canOverScroll: false }

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollOptions-animation?: ScrollAnimationOptions | boolean--><!--Device-ScrollOptions-animation?: ScrollAnimationOptions | boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## canOverScroll

```TypeScript
canOverScroll?: boolean
```

Set whether the scroll target position can over the boundary.

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollOptions-canOverScroll?: boolean--><!--Device-ScrollOptions-canOverScroll?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## xOffset

```TypeScript
xOffset: double | string
```

Horizontal scrolling offset.Anonymous Object Rectification.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_This parameter cannot be set in percentage.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_If the value is less than 0, the offset will be 0 for non-animated scrolling.Animated scrolling stops at the starting position by default.By setting the \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_animation\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_ parameter, you can enable a bounce effect when the scrolling goes beyond the boundary.\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_This parameter takes effect only when the scroll axis is the x-axis.\_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_

**Type:** double \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollOptions-xOffset: double | string--><!--Device-ScrollOptions-xOffset: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## yOffset

```TypeScript
yOffset: double | string
```

Vertical scrolling offset.Anonymous Object Rectification.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_This parameter cannot be set in percentage.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_If the value is less than 0, the offset will be 0 for non-animated scrolling.Animated scrolling stops at the starting position by default.By setting the \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_animation\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_ parameter, you can enable a bounce effect when the scrolling goes beyond the boundary.\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_This parameter takes effect only when the scroll axis is the y-axis.\_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_

**Type:** double \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollOptions-yOffset: double | string--><!--Device-ScrollOptions-yOffset: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

