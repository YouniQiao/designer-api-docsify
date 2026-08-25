# ScrollAnimationOptions

Provides parameters for customizing scroll animations.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## canOverScroll

```TypeScript
canOverScroll?: boolean
```

Whether to enable overscroll. <p>&lt;strong&gt;NOTE&lt;/strong&gt;. <br> Scrolling can exceed the boundary and initiate a bounce animation when this parameter is set to &lt;em&gt;true&lt;/em&gt;, and the component's &lt;em&gt;edgeEffect&lt;/em&gt; attribute is set to EdgeEffect.Spring. </p>

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## curve

```TypeScript
curve?: Curve | ICurve
```

Scrolling curve.

**Type:** [Curve](arkts-arkui-curve-e.md) \| [ICurve](../arkts-components/arkts-arkui-icurve-i.md)

**Default:** Curve.Ease

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: int
```

Scrolling duration. <p>&lt;strong&gt;NOTE&lt;/strong&gt;. The value should be an integer. <br>A value less than 0 evaluates to the default value. </p>

**Type:** int

**Default:** 1000

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
