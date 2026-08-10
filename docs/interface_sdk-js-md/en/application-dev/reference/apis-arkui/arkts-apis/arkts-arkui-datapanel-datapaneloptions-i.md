# DataPanelOptions

数据面板选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface DataPanelOptions--><!--Device-unnamed-export declare interface DataPanelOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## max

```TypeScript
max?: double
```

max大于0时，表示数据的最大值。  
- max小于等于0时，max等于value数组各项的和，按比例显示。  
默认值：100。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataPanelOptions-max?: double--><!--Device-DataPanelOptions-max?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type?: DataPanelType
```

数据面板的类型（不支持动态修改）。默认值：DataPanelType.Circle。

**Type:** [DataPanelType](../arkts-components/arkts-arkui-datapaneltype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataPanelOptions-type?: DataPanelType--><!--Device-DataPanelOptions-type?: DataPanelType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## values

```TypeScript
values: double[]
```

数据值列表，最多包含9个数据，大于9个数据则取前9个数据。若数据值小于0则置为0。

**Type:** double[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataPanelOptions-values: double[]--><!--Device-DataPanelOptions-values: double[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

