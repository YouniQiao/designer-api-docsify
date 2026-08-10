# PickerBackgroundStyle

选择器选中项的背景样式，包括选中项的背景颜色和边框圆角半径。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-unnamed-declare interface PickerBackgroundStyle--><!--Device-unnamed-declare interface PickerBackgroundStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderRadius

```TypeScript
borderRadius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses
```

选中项的边框圆角半径。

> 默认值：{ value:24, unit:LengthUnit.VP }，即四个圆角半径均为24vp。

> 单位：默认为vp，可通过LengthMetrics或LocalizedBorderRadiuses类型指定单位。

> **说明：**
> 
> 1. [LengthMetrics](../arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md/arkts-arkui-graphics-lengthmetrics-c.md)类型的value参数同时作用于四个圆角半径大小，
> unit参数用于设置单位。
> 2. [BorderRadiuses](../arkts-apis/arkts-arkui-borderradiuses-t.md/arkts-arkui-borderradiuses-t.md)类型可以设置四个不同值的圆角半径，所有单位固定为vp。
> 3. [LocalizedBorderRadiuses](../arkts-apis/arkts-arkui-units-localizedborderradiuses-i.md/arkts-arkui-units-localizedborderradiuses-i.md)类型可以设置四个不同值的圆角半径，并且可以单独设置每个圆角的单位。

**Type:** [LengthMetrics](../arkts-apis/arkts-arkui-lengthmetrics-t.md) \| BorderRadiuses \| LocalizedBorderRadiuses

**Default:** { value:24, unit:LengthUnit.VP }

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PickerBackgroundStyle-borderRadius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses--><!--Device-PickerBackgroundStyle-borderRadius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ResourceColor
```

选中项的背景颜色。

> 默认值：
> 
> 'sys.color.comp_background_tertiary'

> **说明：**未设置该属性时，使用默认值。

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** 'sys.color.comp_background_tertiary'

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PickerBackgroundStyle-color?: ResourceColor--><!--Device-PickerBackgroundStyle-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

