# ScrollOptions

滚动到指定位置的参数选项。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare interface ScrollOptions--><!--Device-unnamed-declare interface ScrollOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## animation

```TypeScript
animation?: ScrollAnimationOptions | boolean
```

动画配置。

&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;&lt;br&gt;目前List、Scroll、Grid和WaterFlow支持Boolean类型和ICurve。&lt;/p&gt;

 布尔类型启用默认弹簧动效。 [since 10 - 11] 布尔类型启用默认弹簧动效。 [since 12]

**Type:** [ScrollAnimationOptions](../arkts-apis/arkts-arkui-scroll-scrollanimationoptions-i.md) \| boolean

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

设置滚动目标位置是否可以超出边界。

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

水平滚动偏移量。

&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;&lt;br&gt;不支持设置百分比。&lt;br&gt;无动画滚动时，设置为小于0的值按0处理。有动画滚动时，默认停在起始位置。通过设置&lt;em&gt;animation&lt;/em&gt;参数，可以在滚动超出边界时启用回弹效果。&lt;br&gt;该参数仅在滚动轴为x轴时生效。&lt;/p&gt;

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

竖直滚动偏移量。

&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;&lt;br&gt;不支持设置百分比。&lt;br&gt;无动画滚动时，设置为小于0的值按0处理。有动画滚动时，默认停在起始位置。通过设置&lt;em&gt;animation&lt;/em&gt;参数，可以在滚动超出边界时启用回弹效果。&lt;br&gt;该参数仅在滚动轴为y轴时生效。&lt;/p&gt;

**Type:** number \| string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollOptions-yOffset: number | string--><!--Device-ScrollOptions-yOffset: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

