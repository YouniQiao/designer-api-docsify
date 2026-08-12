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

Whether to enable overscroll.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;.&lt;br&gt; Scrolling can exceed the boundary and initiate a bounce animation when this parameter is set to &lt;em&gt;true&lt;/em&gt;,and the component's &lt;em&gt;edgeEffect&lt;/em&gt; attribute is set to EdgeEffect.Spring.&lt;/p&gt;

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

**Type:** [Curve](arkts-arkui-curve-e.md) \| [ICurve](../arkts-components/arkts-arkui-icurve-i.md)

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

Scrolling duration.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;.The value should be an integer.&lt;br&gt;A value less than 0 evaluates to the default value.&lt;/p&gt;

**Type:** int

**Default:** 1000

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollAnimationOptions-duration?: int--><!--Device-ScrollAnimationOptions-duration?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

