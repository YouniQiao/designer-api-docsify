# ResponseRegion

由输入工具类型、触摸位置和大小组成的触摸热区。

> **说明：**
> 
> - 当父组件设置[clip](arkts-arkui-commonmethod-c.md#clip)为true时，子组件的响应会受到父组件触摸热区的影响，不在父组件触摸热区内的子组件无法响应手势和事件。
> 
> - 如果触摸热区未配置输入工具类型，触摸位置和大小均采用默认值。
> 
> - x和y的计算结果为正值时，分别代表向右偏移和向下偏移；当计算结果为负值时，分别代表向左偏移和向上偏移。
> 
> - width和height采用string类型时，string需采用小写字符否则不生效，支持calc()的动态计算。指定calc()的入参字符串格式为'宽高缩放比例 ± 宽高增量'，宽高缩放比例为百分比，宽高增量单位为px或
> vp。例如'calc(80% + 10vp)'中，80%为宽高缩放比例、10vp为宽高增量。width和height采用LengthMetrics类型且单位为percent时，相对于组件自身宽高进行计算，percent(1)代表1
> 00%。当计算结果为负值时，采用默认值。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-unnamed-declare interface ResponseRegion--><!--Device-unnamed-declare interface ResponseRegion-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: LengthMetrics | string
```

触摸热区的高度。

默认值：LengthMetrics.percent(1)

**Type:** [LengthMetrics](../arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) \| string

**Default:** LengthMetrics.percent(1)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ResponseRegion-height?: LengthMetrics | string--><!--Device-ResponseRegion-height?: LengthMetrics | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tool

```TypeScript
tool?: ResponseRegionSupportedTool
```

触摸热区适用的输入工具类型。

默认值：ResponseRegionSupportedTool.ALL

**Type:** [ResponseRegionSupportedTool](../arkts-apis/arkts-arkui-responseregionsupportedtool-e.md)

**Default:** ResponseRegionSupportedTool.ALL

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ResponseRegion-tool?: ResponseRegionSupportedTool--><!--Device-ResponseRegion-tool?: ResponseRegionSupportedTool-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: LengthMetrics | string
```

触摸热区的宽度。

默认值：LengthMetrics.percent(1)

**Type:** [LengthMetrics](../arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) \| string

**Default:** LengthMetrics.percent(1)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ResponseRegion-width?: LengthMetrics | string--><!--Device-ResponseRegion-width?: LengthMetrics | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## x

```TypeScript
x?: LengthMetrics
```

触摸点相对于组件左上角的x轴坐标。

默认值：LengthMetrics.vp(0)

**Type:** [LengthMetrics](../arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md)

**Default:** LengthMetrics.vp(0)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ResponseRegion-x?: LengthMetrics--><!--Device-ResponseRegion-x?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## y

```TypeScript
y?: LengthMetrics
```

触摸点相对于组件左上角的y轴坐标。

默认值：LengthMetrics.vp(0)

**Type:** [LengthMetrics](../arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md)

**Default:** LengthMetrics.vp(0)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ResponseRegion-y?: LengthMetrics--><!--Device-ResponseRegion-y?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

