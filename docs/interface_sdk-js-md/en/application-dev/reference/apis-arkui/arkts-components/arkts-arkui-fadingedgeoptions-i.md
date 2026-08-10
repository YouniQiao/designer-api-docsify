# FadingEdgeOptions

[fadingEdge](../../../reference/apis-arkui/arkui-ts/ts-container-scrollable-common.md#fadingedge14)属性边缘渐隐参数对象。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

<!--Device-unnamed-declare interface FadingEdgeOptions--><!--Device-unnamed-declare interface FadingEdgeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fadingEdgeLength

```TypeScript
fadingEdgeLength?: LengthMetrics
```

设置边缘渐隐长度。默认值为32vp，设置小于0的值或undefined或不设置则取默认值。设置的长度超过容器高度的一半时，渐隐长度取容器高度的一半。

**Type:** [LengthMetrics](../arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md)

**Default:** 32vp

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-FadingEdgeOptions-fadingEdgeLength?: LengthMetrics--><!--Device-FadingEdgeOptions-fadingEdgeLength?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

