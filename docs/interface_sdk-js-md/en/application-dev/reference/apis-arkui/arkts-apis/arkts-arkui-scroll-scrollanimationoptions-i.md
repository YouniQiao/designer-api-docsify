# ScrollAnimationOptions

自定义滚动动效的参数选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ScrollAnimationOptions--><!--Device-unnamed-export declare interface ScrollAnimationOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## canOverScroll

```TypeScript
canOverScroll?: boolean
```

设置滚动动画滚动到边界后，是否转换成越界回弹动画。&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;。&lt;br&gt;仅在设置为true，且组件的edgeEffect设置为EdgeEffect.Spring时，使用动画滚动到边界会转换为越界回弹动画，设置为false时，滚动到边界会直接停止动画，不会转换为越界回弹动画。&lt;/p&gt;

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

设置滚动曲线。

**Type:** [Curve](arkts-arkui-curve-e.md) \| ICurve

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

设置滚动时长。&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;。取值限定为整数。&lt;br&gt;设置为小于0的值时，按默认值显示。&lt;/p&gt;

**Type:** int

**Default:** 1000

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollAnimationOptions-duration?: int--><!--Device-ScrollAnimationOptions-duration?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

