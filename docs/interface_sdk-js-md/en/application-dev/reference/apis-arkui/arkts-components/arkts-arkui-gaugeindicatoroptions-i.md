# GaugeIndicatorOptions

数据量规图表指针选项。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface GaugeIndicatorOptions--><!--Device-unnamed-declare interface GaugeIndicatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: ResourceStr
```

图标资源路径。

**说明：**

不配置则使用系统默认样式，系统默认样式为三角形指针。

仅支持使用svg格式的图标，若使用其他格式，则使用默认的三角形样式指针。

**Type:** [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md)

**Default:** system style.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-GaugeIndicatorOptions-icon?: ResourceStr--><!--Device-GaugeIndicatorOptions-icon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: Dimension
```

指针距离圆环外边的间距。

默认值：8

单位：vp 

**说明：**

不支持百分比。

对于默认的三角形样式指针，为黑色三角形到圆环外边的间距。

若设置值小于0，则使用默认值。

若设置值大于圆环半径，则使用默认值。

**Type:** [Dimension](../arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 8vp

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-GaugeIndicatorOptions-space?: Dimension--><!--Device-GaugeIndicatorOptions-space?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

