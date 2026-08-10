# RenderingContextSettings

用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class RenderingContextSettings--><!--Device-unnamed-export declare class RenderingContextSettings-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(antialias?: boolean)
```

构造CanvasRenderingContext2D对象，支持配置开启抗锯齿。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderingContextSettings-constructor(antialias?: boolean)--><!--Device-RenderingContextSettings-constructor(antialias?: boolean)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| antialias | boolean | No | 表明canvas是否开启抗锯齿。&lt;br&gt;异常值undefined按默认值处理。 &lt;br&gt;false：表示不开启抗锯齿功能，true：表示开启抗锯齿。&lt;br&gt;默认值：false |

## antialias

```TypeScript
set antialias(antialias: boolean | undefined)
```

表明canvas是否开启抗锯齿。&lt;br&gt;异常值undefined按默认值处理。&lt;br&gt;false：表示不开启抗锯齿功能，true：表示开启抗锯齿。&lt;br&gt;默认值：false

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderingContextSettings-set antialias(antialias: boolean | undefined)--><!--Device-RenderingContextSettings-set antialias(antialias: boolean | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

