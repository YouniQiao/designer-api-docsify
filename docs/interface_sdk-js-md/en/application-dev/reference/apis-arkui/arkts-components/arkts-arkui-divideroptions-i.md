# DividerOptions

分割线的信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface DividerOptions--><!--Device-unnamed-declare interface DividerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ResourceColor
```

分割线的颜色。

> 默认值：'#33000000'

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** '#33000000'

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DividerOptions-color?: ResourceColor--><!--Device-DividerOptions-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## endMargin

```TypeScript
endMargin?: Dimension
```

分割线与TextPicker侧边结束端的距离。

> 默认值：0

> 单位：默认为vp，也可指定单位为px。

> 取值范围：[0, +∞)，endMargin小于0时无效，最大值不得超过TextPicker列宽。不支持“百分比”类型。

> **说明：** 当startMargin + endMargin超过组件宽度时，会被置0。

**Type:** [Dimension](../arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 0

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DividerOptions-endMargin?: Dimension--><!--Device-DividerOptions-endMargin?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startMargin

```TypeScript
startMargin?: Dimension
```

分割线与TextPicker侧边起始端的距离。

> 默认值：0

> 单位：默认为vp，也可指定单位为px。

> 取值范围：[0, +∞)，startMargin小于0时无效，最大值不得超过TextPicker列宽。不支持“百分比”类型。

> **说明：**当startMargin + endMargin超过组件宽度时，会被置0。

**Type:** [Dimension](../arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 0

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DividerOptions-startMargin?: Dimension--><!--Device-DividerOptions-startMargin?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth?: Dimension
```

分割线的线宽。

> 默认值：2.0px

> 单位：默认为vp，也可指定单位为px。

> 取值范围：[0, +∞)，strokeWidth小于0取默认值，最大不得超过列高的一半。不支持“百分比”类型。

**Type:** [Dimension](../arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 2.0px

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DividerOptions-strokeWidth?: Dimension--><!--Device-DividerOptions-strokeWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

