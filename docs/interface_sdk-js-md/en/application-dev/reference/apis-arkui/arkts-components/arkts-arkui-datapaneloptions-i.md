# DataPanelOptions

数据面板选项。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare interface DataPanelOptions--><!--Device-unnamed-declare interface DataPanelOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## max

```TypeScript
max?: number
```

- max大于0时，表示数据的最大值。

- max小于等于0时，max等于values数据值列表各项的和，按比例显示。

不传入时默认值：100。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-DataPanelOptions-max?: number--><!--Device-DataPanelOptions-max?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type?: DataPanelType
```

数据面板的类型（不支持动态修改）。

可选值：DataPanelType.Line（线性数据面板，适合在有限空间内展示多段数据对比）、DataPanelType.Circle（环形数据面板，适合直观展示数据占比关系）。

不传入时默认值为DataPanelType.Circle。

**Type:** [DataPanelType](arkts-arkui-datapaneltype-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-DataPanelOptions-type?: DataPanelType--><!--Device-DataPanelOptions-type?: DataPanelType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## values

```TypeScript
values: number[]
```

数据值列表，数组长度范围[0, 9]，大于9个数据则取前9个数据。若数据值小于0则置为0。

**Type:** number[]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-DataPanelOptions-values: number[]--><!--Device-DataPanelOptions-values: number[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

