# GaugeIndicatorOptions

数据量规图表指针选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface GaugeIndicatorOptions--><!--Device-unnamed-export declare interface GaugeIndicatorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: ResourceStr
```

图标资源路径。

**说明：**

不配置则使用系统默认样式，系统默认样式为三角形指针。

仅支持使用svg格式的图标，若使用其他格式，则使用默认的三角形样式指针。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Default:** system style.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GaugeIndicatorOptions-icon?: ResourceStr--><!--Device-GaugeIndicatorOptions-icon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: Dimension
```

指针距离圆环外边的间距。(不支持百分比)。默认值：8vp。&lt;br&gt;**说明：**对于默认的三角形样式指针，间距为黑色三角形到圆环外边的间距。

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** 8vp

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GaugeIndicatorOptions-space?: Dimension--><!--Device-GaugeIndicatorOptions-space?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

