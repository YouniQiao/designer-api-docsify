# DividerOptions

分割线的信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface DividerOptions--><!--Device-unnamed-export declare interface DividerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ResourceColor
```

分割线的颜色。

默认值：'#33000000'

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** "#33000000"

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DividerOptions-color?: ResourceColor--><!--Device-DividerOptions-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## endMargin

```TypeScript
endMargin?: Dimension
```

分割线与TextPicker侧边结束端的距离。

默认值：0

单位：默认为vp，也可指定单位为px。

取值范围：endMargin小于0时无效，最大值不得超过TextPicker列宽。不支持“百分比”类型。

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DividerOptions-endMargin?: Dimension--><!--Device-DividerOptions-endMargin?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startMargin

```TypeScript
startMargin?: Dimension
```

分割线与TextPicker侧边起始端的距离。

默认值：0

单位：默认为vp，也可指定单位为px。

取值范围：startMargin小于0时无效，最大值不得超过TextPicker列宽。不支持“百分比”类型。

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DividerOptions-startMargin?: Dimension--><!--Device-DividerOptions-startMargin?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth?: Dimension
```

分割线的线宽。

默认值：2.0px

单位：默认为vp，也可指定单位为px。

取值范围：strokeWidth小于0取默认值，最大不得超过列高的一半。不支持“百分比”类型。

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** 2.0px

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DividerOptions-strokeWidth?: Dimension--><!--Device-DividerOptions-strokeWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

