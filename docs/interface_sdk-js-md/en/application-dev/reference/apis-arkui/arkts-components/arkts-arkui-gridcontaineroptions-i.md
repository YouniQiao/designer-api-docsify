# GridContainerOptions

栅格栅格布局容器配置参数对象，用于设置GridContainer组件的列数、设备宽度类型、列间距和两侧间距。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** grid_col/GridColOptions

<!--Device-unnamed-declare interface GridContainerOptions--><!--Device-unnamed-declare interface GridContainerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## columns

```TypeScript
columns?: number | "auto"
```

当前布局总列数，number类型需为正整数。设置为number时使用固定列数布局；设置为'auto'时，系统根据设备宽度类型自动确定列数（XS为2列，SM为4列，MD为8列，LG为12列）。传入0或负数时视为未设置，系统自动确定列数。

默认值：'auto'

**Type:** number \| "auto"

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** grid_col/GridColOptions

<!--Device-GridContainerOptions-columns?: number | "auto"--><!--Device-GridContainerOptions-columns?: number | "auto"-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gutter

```TypeScript
gutter?: number | string
```

栅格布局列间距，不支持百分比。number类型默认单位为vp，取值范围[0, +∞)。不设置时根据设备宽度类型自动确定：XS为12vp，SM/MD/LG为24vp。

**Type:** number \| string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** grid_col/GridColOptions

<!--Device-GridContainerOptions-gutter?: number | string--><!--Device-GridContainerOptions-gutter?: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## margin

```TypeScript
margin?: number | string
```

栅格布局两侧间距，不支持百分比。number类型默认单位为vp，取值范围[0, +∞)。不设置时根据设备宽度类型自动确定：XS为12vp，SM为24vp，MD为32vp，LG为48vp。

**Type:** number \| string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** grid_col/GridColOptions

<!--Device-GridContainerOptions-margin?: number | string--><!--Device-GridContainerOptions-margin?: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## sizeType

```TypeScript
sizeType?: SizeType
```

设置设备宽度类型，用于响应式布局。

默认值：SizeType.Auto

**Type:** [SizeType](arkts-arkui-sizetype-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** grid_col/GridColOptions

<!--Device-GridContainerOptions-sizeType?: SizeType--><!--Device-GridContainerOptions-sizeType?: SizeType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

