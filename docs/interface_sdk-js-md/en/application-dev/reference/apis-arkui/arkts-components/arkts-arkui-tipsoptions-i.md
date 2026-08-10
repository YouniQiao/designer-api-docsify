# TipsOptions

悬浮气泡自定义参数。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

<!--Device-unnamed-declare interface TipsOptions--><!--Device-unnamed-declare interface TipsOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## appearingTime

```TypeScript
appearingTime?: number
```

设置悬浮气泡的显示时延。显示时延的最大值为4000ms，设置超过4000ms的值以4000ms为准。

默认值：700

单位：ms

**Type:** number

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-TipsOptions-appearingTime?: number--><!--Device-TipsOptions-appearingTime?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## appearingTimeWithContinuousOperation

```TypeScript
appearingTimeWithContinuousOperation?: number
```

多个组件连续弹出悬浮气泡时，悬浮气泡的显示时延。显示时延的最大值为4000ms，设置超过4000ms的值以4000ms为准。 

默认值：300

单位：ms

**Type:** number

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-TipsOptions-appearingTimeWithContinuousOperation?: number--><!--Device-TipsOptions-appearingTimeWithContinuousOperation?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowHeight

```TypeScript
arrowHeight?: Dimension
```

The height of the arrow.

**Type:** [Dimension](../arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 8.0_vp.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-TipsOptions-arrowHeight?: Dimension--><!--Device-TipsOptions-arrowHeight?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowPointPosition

```TypeScript
arrowPointPosition?: ArrowPointPosition
```

气泡箭头相对于父组件显示位置，气泡箭头在垂直和水平方向上有 “Start”、“Center”、“End”三个位置点可选。所有位置点均位于父组件区域范围内，不会超出父组件的边界范围，也不会覆盖圆角范围。

默认值：ArrowPointPosition.CENTER

**Type:** [ArrowPointPosition](../arkts-apis/arkts-arkui-arrowpointposition-e.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-TipsOptions-arrowPointPosition?: ArrowPointPosition--><!--Device-TipsOptions-arrowPointPosition?: ArrowPointPosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowWidth

```TypeScript
arrowWidth?: Dimension
```

The width of the arrow.

**Type:** [Dimension](../arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 16.0_vp.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-TipsOptions-arrowWidth?: Dimension--><!--Device-TipsOptions-arrowWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disappearingTime

```TypeScript
disappearingTime?: number
```

设置悬浮气泡的隐藏时延。隐藏时延的最大值为4000ms，设置超过4000ms的值以4000ms为准。

默认值：300

单位：ms

**Type:** number

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-TipsOptions-disappearingTime?: number--><!--Device-TipsOptions-disappearingTime?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disappearingTimeWithContinuousOperation

```TypeScript
disappearingTimeWithContinuousOperation?: number
```

多个组件连续弹出悬浮气泡时，悬浮气泡的隐藏时延。隐藏时延的最大值为4000ms，设置超过4000ms的值以4000ms为准。 

默认值：0

单位：ms

**Type:** number

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-TipsOptions-disappearingTimeWithContinuousOperation?: number--><!--Device-TipsOptions-disappearingTimeWithContinuousOperation?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableArrow

```TypeScript
enableArrow?: boolean
```

设置是否显示气泡箭头。

默认值：true

true：显示箭头；false：不显示箭头。

**说明：**

当页面可用空间无法让气泡完全避让时，气泡会覆盖到组件上并且不显示气泡箭头。

**Type:** boolean

**Default:** true

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-TipsOptions-enableArrow?: boolean--><!--Device-TipsOptions-enableArrow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showAtAnchor

```TypeScript
showAtAnchor?: TipsAnchorType
```

设置Tips跟随类型。

默认值：TipsAnchorType.TARGET

**说明：**

Tips的跟随类型为TipsAnchorType.CURSOR时，Tips不显示箭头。

**Type:** [TipsAnchorType](../arkts-apis/arkts-arkui-tipsanchortype-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TipsOptions-showAtAnchor?: TipsAnchorType--><!--Device-TipsOptions-showAtAnchor?: TipsAnchorType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

设置组件的系统材质。

默认值：undefined，会清除由该接口设置的材质效果。 

**说明：**

不同系统材质对应不同的属性影响效果，该接口影响背景色[backgroundColor](arkts-arkui-commonmethod-c.md#backgroundcolor)、边框颜色  
[borderColor](arkts-arkui-commonmethod-c.md#bordercolor)、边框宽度[borderWidth](arkts-arkui-commonmethod-c.md#borderwidth)、阴影  
[shadow](arkts-arkui-commonmethod-c.md#shadow)，不建议与上述接口一起使用。

**Type:** [SystemUiMaterial](../arkts-apis/arkts-arkui-systemuimaterial-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TipsOptions-systemMaterial?: SystemUiMaterial--><!--Device-TipsOptions-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

