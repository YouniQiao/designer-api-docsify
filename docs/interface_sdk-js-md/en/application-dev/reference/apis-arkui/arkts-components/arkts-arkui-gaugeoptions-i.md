# GaugeOptions

数据量规图表选项。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-interface GaugeOptions--><!--Device-unnamed-interface GaugeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## max

```TypeScript
max?: number
```

当前数据段最大值。

默认值：100

**说明：**

不传入时默认最大值为100。

min大于max时使用默认值0和100。

max和min支持负数。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-GaugeOptions-max?: number--><!--Device-GaugeOptions-max?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## min

```TypeScript
min?: number
```

当前数据段最小值。

默认值：0

**说明：**

不传入时默认最小值为0。

min大于max时使用默认值0和100。

max和min支持负数。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-GaugeOptions-min?: number--><!--Device-GaugeOptions-min?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: number
```

量规图的当前数据值，即图中指针指向位置。用于组件创建时量规图初始值的预置。

默认值：0

**说明：**

value不在min和max范围内时使用min作为默认值。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-GaugeOptions-value: number--><!--Device-GaugeOptions-value: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

