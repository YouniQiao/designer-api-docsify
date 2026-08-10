# ScrollAnimationOptions

自定义滚动动效的参数选项。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface ScrollAnimationOptions--><!--Device-unnamed-declare interface ScrollAnimationOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## canOverScroll

```TypeScript
canOverScroll?: boolean
```

是否启用过滚动。

&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;&lt;br&gt; 设置为&lt;em&gt;true&lt;/em&gt;时可以滚动超出边界并触发回弹动画，同时组件的&lt;em&gt;edgeEffect&lt;/em&gt;属性需设置为EdgeEffect.Spring。&lt;/p&gt;

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

滚动曲线。

**Type:** [Curve](../arkts-apis/arkts-arkui-curve-e.md) \| ICurve

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

滚动时长。

&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;&lt;br&gt;设置为小于0的值时，按默认值处理。&lt;/p&gt;

**Type:** number

**Default:** 1000

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScrollAnimationOptions-duration?: number--><!--Device-ScrollAnimationOptions-duration?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

