# DataPanelConfiguration

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](arkts-arkui-common-commonconfiguration-i.md)。

**Inheritance/Implementation:** DataPanelConfiguration extends [CommonConfiguration<DataPanelConfiguration>](CommonConfiguration<DataPanelConfiguration>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface DataPanelConfiguration extends CommonConfiguration<DataPanelConfiguration>--><!--Device-unnamed-export declare interface DataPanelConfiguration extends CommonConfiguration<DataPanelConfiguration>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxValue

```TypeScript
maxValue: double
```

DataPanel显示的最大值。

默认值：100。

**说明：**

如果小于或等于0，maxValue将被设为values数组中所有项的总和，并按比例显示。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataPanelConfiguration-maxValue: double--><!--Device-DataPanelConfiguration-maxValue: double-End-->

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

<!--Device-DataPanelConfiguration-values: double[]--><!--Device-DataPanelConfiguration-values: double[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

