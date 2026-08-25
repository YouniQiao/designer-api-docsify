# ScrollOptions

Provides parameters for scrolling to a specific position in a scrollable container.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## animation

```TypeScript
animation?: ScrollAnimationOptions | boolean
```

Animation configuration Anonymous Object Rectification. <p>&lt;strong&gt;NOTE&lt;/strong&gt;. <br>Currently, the &lt;em&gt;List&lt;/em&gt;, &lt;em&gt;Scroll&lt;/em&gt;, &lt;em&gt;Grid&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; support the &lt;em&gt;Boolean&lt;/em&gt; type and &lt;em&gt;ICurve&lt;/em&gt;. </p>

**Type:** [ScrollAnimationOptions](arkts-arkui-scroll-scrollanimationoptions-i.md) \| boolean

**Default:** ScrollAnimationOptions: { duration: 1000, curve: Curve.Ease, canOverScroll: false }

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## canOverScroll

```TypeScript
canOverScroll?: boolean
```

Set whether the scroll target position can over the boundary.

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## xOffset

```TypeScript
xOffset: double | string
```

Horizontal scrolling offset. Anonymous Object Rectification.<p>&lt;strong&gt;NOTE&lt;/strong&gt; <br>This parameter cannot be set in percentage. <br>If the value is less than 0, the offset will be 0 for non-animated scrolling. Animated scrolling stops at the starting position by default. By setting the &lt;em&gt;animation&lt;/em&gt; parameter, you can enable a bounce effect when the scrolling goes beyond the boundary. <br>This parameter takes effect only when the scroll axis is the x-axis. </p>

**Type:** double \| string

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## yOffset

```TypeScript
yOffset: double | string
```

Vertical scrolling offset. Anonymous Object Rectification.<p>&lt;strong&gt;NOTE&lt;/strong&gt; <br>This parameter cannot be set in percentage. <br>If the value is less than 0, the offset will be 0 for non-animated scrolling. Animated scrolling stops at the starting position by default. By setting the &lt;em&gt;animation&lt;/em&gt; parameter, you can enable a bounce effect when the scrolling goes beyond the boundary. <br>This parameter takes effect only when the scroll axis is the y-axis. </p>

**Type:** double \| string

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
