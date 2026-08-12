# CanvasParams

Defines the parameters of the **Canvas** component.

**Since:** 23

<!--Device-unnamed-declare interface CanvasParams--><!--Device-unnamed-declare interface CanvasParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageAIOptions

```TypeScript
imageAIOptions?: ImageAIOptions
```

AI image analysis options. You can configure the analysis type or bind an analyzer controller through this parameter.

**Type:** [ImageAIOptions](../arkts-apis/arkts-arkui-imageaioptions-i.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CanvasParams-imageAIOptions?: ImageAIOptions--><!--Device-CanvasParams-imageAIOptions?: ImageAIOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## unit

```TypeScript
unit?: LengthMetricsUnit
```

Indicates the unit mode employed by Canvas during drawing.&lt;br&gt;It can only be set when creating the **Canvas** component and cannot be modified afterwards.&lt;br&gt;Default value: **LengthMetricsUnit.DEFAULT**

**Type:** LengthMetricsUnit

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CanvasParams-unit?: LengthMetricsUnit--><!--Device-CanvasParams-unit?: LengthMetricsUnit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
