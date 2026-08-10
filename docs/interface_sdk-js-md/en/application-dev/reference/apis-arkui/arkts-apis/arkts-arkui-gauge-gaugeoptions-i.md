# GaugeOptions

数据量规图表选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface GaugeOptions--><!--Device-unnamed-export interface GaugeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## max

```TypeScript
max?: double
```

当前数据段最大值。默认值：100。&lt;br&gt;**说明：**max小于min时使用默认值0和100。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GaugeOptions-max?: double--><!--Device-GaugeOptions-max?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## min

```TypeScript
min?: double
```

当前数据段最小值。默认值：0。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GaugeOptions-min?: double--><!--Device-GaugeOptions-min?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: double | undefined
```

量规图的当前数据值，即图中指针指向位置。用于组件创建时量规图初始值的预置。

默认值：0

**说明：**

value不在min和max范围内时使用min作为默认值。

**Type:** double \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GaugeOptions-value: double | undefined--><!--Device-GaugeOptions-value: double | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

