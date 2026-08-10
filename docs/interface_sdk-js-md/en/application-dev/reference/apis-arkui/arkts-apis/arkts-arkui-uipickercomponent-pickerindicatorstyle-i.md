# PickerIndicatorStyle

选中项指示器样式的参数说明。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface PickerIndicatorStyle--><!--Device-unnamed-export declare interface PickerIndicatorStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

选中项背景的颜色。

默认值：'sys.color.comp_background_tertiary'

**说明：**

当type为PickerIndicatorType.BACKGROUND时生效。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerIndicatorStyle-backgroundColor?: ResourceColor--><!--Device-PickerIndicatorStyle-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderRadius

```TypeScript
borderRadius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses
```

选中项背景的边框圆角半径。

默认值：{ value:12, unit:LengthUnit.vp }，即四个圆角半径均为12vp。

取值范围：取选中项的宽和高之中较小的边长为x，最大不超过x的一半。当取值小于0时，使用默认值；当取值大于最大值时，使用最大值。

**说明：**

1. 当type为PickerIndicatorType.BACKGROUND时生效。2. [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)：统一设置四个圆角半径的大小和单位。3. [BorderRadiuses](arkts-arkui-borderradiuses-t.md)：单独设置四个圆角半径的大小（单位为vp）。4. [LocalizedBorderRadiuses](arkts-arkui-units-localizedborderradiuses-i.md)：单独设置四个圆角半径的大小和单位。

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| BorderRadiuses \| LocalizedBorderRadiuses

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerIndicatorStyle-borderRadius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses--><!--Device-PickerIndicatorStyle-borderRadius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dividerColor

```TypeScript
dividerColor?: ResourceColor
```

分割线的颜色。

默认值：'sys.color.comp_divider'

**说明：**

当type为PickerIndicatorType.DIVIDER时生效。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerIndicatorStyle-dividerColor?: ResourceColor--><!--Device-PickerIndicatorStyle-dividerColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## endMargin

```TypeScript
endMargin?: LengthMetrics
```

分割线与UIPickerComponent容器侧边结束端的距离。

默认值：0

单位：与LengthMetrics一致。

取值范围：startMargin与endMargin之和不得超过UIPickerComponent容器的宽度。设置小于0或startMargin与endMargin之和超过UIPickerComponent容器的宽度时，使用默认值。不支持“百分比”类型。

**说明：**

当type为PickerIndicatorType.DIVIDER时生效。

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerIndicatorStyle-endMargin?: LengthMetrics--><!--Device-PickerIndicatorStyle-endMargin?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startMargin

```TypeScript
startMargin?: LengthMetrics
```

分割线与UIPickerComponent容器侧边起始端的距离。

默认值：0

单位：与LengthMetrics一致。

取值范围：startMargin与endMargin之和不得超过UIPickerComponent容器的宽度。设置小于0或startMargin与endMargin之和超过UIPickerComponent容器的宽度时，使用默认值。不支持“百分比”类型。

**说明：**

当type为PickerIndicatorType.DIVIDER时生效。

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerIndicatorStyle-startMargin?: LengthMetrics--><!--Device-PickerIndicatorStyle-startMargin?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth?: LengthMetrics
```

分割线的线宽。

默认值：2.0px

单位：与LengthMetrics一致。

取值范围：[0, 选中项高度的一半（即20vp）]。strokeWidth小于0或大于选中项高度的一半时使用默认值。不支持“百分比”类型。

**说明：**

1. 当type为PickerIndicatorType.DIVIDER时生效。2. 通过LengthMetrics.resource方式设置时，使用非长度属性的值会按照0vp处理。

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerIndicatorStyle-strokeWidth?: LengthMetrics--><!--Device-PickerIndicatorStyle-strokeWidth?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: PickerIndicatorType
```

选中项指示器的类型。

默认值：PickerIndicatorType.BACKGROUND

当type的值为小数时，使用向下取整后的整数；当type的值不在PickerIndicatorType枚举范围内时，使用默认值。

**Type:** [PickerIndicatorType](arkts-arkui-uipickercomponent-pickerindicatortype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PickerIndicatorStyle-type: PickerIndicatorType--><!--Device-PickerIndicatorStyle-type: PickerIndicatorType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

