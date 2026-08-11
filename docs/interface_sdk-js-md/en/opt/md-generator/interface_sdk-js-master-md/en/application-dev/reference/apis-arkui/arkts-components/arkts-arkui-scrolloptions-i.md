# ScrollOptions

Provides parameters for scrolling to a specific position in a scrollable container.

**Since:** 18

<!--Device-unnamed-declare interface ScrollOptions--><!--Device-unnamed-declare interface ScrollOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## animation

```TypeScript
animation?: ScrollAnimationOptions | boolean
```

Animation configuration Anonymous Object Rectification.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;Currently, the &lt;em&gt;List&lt;/em&gt;, &lt;em&gt;Scroll&lt;/em&gt;, &lt;em&gt;Grid&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt;support the &lt;em&gt;Boolean&lt;/em&gt; type and &lt;em&gt;ICurve&lt;/em&gt;.&lt;/p&gt;

 parameters  and the boolean type enables default spring animation. [since 10 - 11] and the boolean type enables default spring animation. [since 12]

**Type:** [ScrollAnimationOptions](arkts-arkui-scrollanimationoptions-i.md) \| boolean

**Default:** ScrollAnimationOptions: { duration: 1000, curve: Curve.Ease, canOverScroll: false } [since 18]

**Since:** 10

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

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ScrollOptions-canOverScroll?: boolean--><!--Device-ScrollOptions-canOverScroll?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## xOffset

```TypeScript
xOffset: number | string
```

Horizontal scrolling offset.Anonymous Object Rectification.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;This parameter cannot be set in percentage.&lt;br&gt;This parameter takes effect only when the scroll axis is the x-axis.&lt;br&gt;Value range: Values less than 0 are treated as 0, and scrolling occurs without animation.Animated scrolling stops at the starting position by default.By setting the **animation** parameter, you can enable a bounce effect when the scrolling goes beyond the boundary.&lt;br&gt;If the parameter type is number, the unit is vp.&lt;/p&gt;

**Type:** number \| string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollOptions-xOffset: number | string--><!--Device-ScrollOptions-xOffset: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## yOffset

```TypeScript
yOffset: number | string
```

Vertical scrolling offset.Anonymous Object Rectification.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;This parameter cannot be set in percentage.&lt;br&gt;This parameter takes effect only when the scroll axis is the y-axis.&lt;br&gt;Value range: Values less than 0 are treated as 0, and scrolling occurs without animation.Animated scrolling stops at the starting position by default.By setting the **animation** parameter, you can enable a bounce effect when the scrolling goes beyond the boundary.&lt;br&gt;If the parameter type is number, the unit is vp.&lt;/p&gt;

**Type:** number \| string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollOptions-yOffset: number | string--><!--Device-ScrollOptions-yOffset: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
