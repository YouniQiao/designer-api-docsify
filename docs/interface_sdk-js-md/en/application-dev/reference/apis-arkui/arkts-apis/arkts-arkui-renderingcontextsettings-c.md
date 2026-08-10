# RenderingContextSettings

用于配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare class RenderingContextSettings--><!--Device-unnamed-declare class RenderingContextSettings-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(antialias?: boolean)
```

构造RenderingContextSettings对象，支持配置开启抗锯齿。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-RenderingContextSettings-constructor(antialias?: boolean)--><!--Device-RenderingContextSettings-constructor(antialias?: boolean)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| antialias | boolean | No | 表明canvas是否开启抗锯齿。 &lt;br&gt;异常值undefined或null按默认值处理。 &lt;br&gt;true：表示开启抗锯齿，false：表示不开启抗锯齿功能。 &lt;br&gt;默认值：false &lt;br&gt;**说明：** &lt;br&gt;绘制文本默认开启抗锯齿效果，RenderingContextSettings的antialias无法影响绘制文本的抗锯齿效果，如需修改文本抗锯齿效果，请使用 [antialias&lt;sup&gt;24+&lt;/sup&gt;](../../../reference/apis-arkui/arkui-ts/ts-components-canvas-common-property.md#antialias24) 接口。 |

## antialias

```TypeScript
antialias?: boolean
```

表明canvas是否开启抗锯齿。

异常值undefined或null按默认值处理。

true：表示开启抗锯齿，false：表示不开启抗锯齿功能。

默认值：false

**说明：**

绘制文本默认开启抗锯齿效果，RenderingContextSettings的antialias无法影响绘制文本的抗锯齿效果，如需修改文本抗锯齿效果，请使用  
[antialias&lt;sup&gt;24+&lt;/sup&gt;](../../../reference/apis-arkui/arkui-ts/ts-components-canvas-common-property.md#antialias24)接口。

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-RenderingContextSettings-antialias?: boolean--><!--Device-RenderingContextSettings-antialias?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

