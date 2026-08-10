# ColorMetricsStop

线性渐变颜色断点类型，用于描述渐进色颜色断点。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-declare interface ColorMetricsStop--><!--Device-unnamed-declare interface ColorMetricsStop-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color: ColorMetrics
```

线性渐变颜色断点的颜色值。

**Type:** [ColorMetrics](../arkts-apis/arkts-arkui-graphics-colormetrics-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ColorMetricsStop-color: ColorMetrics--><!--Device-ColorMetricsStop-color: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset: Length
```

线性渐变颜色断点的断点值，取值为0~1之间的比例值。小于0置为0，大于1置为1。 

**说明：**

如果传入字符串类型且内容为数字，则转换为对应的数值。例如'10vp'转换为10，'10%'转换为0.1。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ColorMetricsStop-offset: Length--><!--Device-ColorMetricsStop-offset: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

