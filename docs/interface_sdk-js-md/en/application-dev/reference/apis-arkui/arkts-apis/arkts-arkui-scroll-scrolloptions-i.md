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

Animation configuration Anonymous Object Rectification.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;.&lt;br&gt;Currently, the &lt;em&gt;List&lt;/em&gt;, &lt;em&gt;Scroll&lt;/em&gt;, &lt;em&gt;Grid&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; support the&lt;em&gt;Boolean&lt;/em&gt; type and &lt;em&gt;ICurve&lt;/em&gt;.&lt;/p&gt;

**Type:** [ScrollAnimationOptions](arkts-arkui-scroll-scrollanimationoptions-i.md) \| boolean

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

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;This parameter cannot be set in percentage.&lt;br&gt;If the value is less than 0, the offset will be 0 for non-animated scrolling.Animated scrolling stops at the starting position by default.By setting the &lt;em&gt;animation&lt;/em&gt; parameter, you can enable a bounce effect when the scrolling goes beyond the boundary.&lt;br&gt;This parameter takes effect only when the scroll axis is the x-axis.&lt;/p&gt;

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

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;This parameter cannot be set in percentage.&lt;br&gt;If the value is less than 0, the offset will be 0 for non-animated scrolling.Animated scrolling stops at the starting position by default.By setting the &lt;em&gt;animation&lt;/em&gt; parameter, you can enable a bounce effect when the scrolling goes beyond the boundary.&lt;br&gt;This parameter takes effect only when the scroll axis is the y-axis.&lt;/p&gt;

**Type:** double \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollOptions-yOffset: double | string--><!--Device-ScrollOptions-yOffset: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

