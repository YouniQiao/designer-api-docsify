# CanvasParams

定义Canvas的具体配置参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface CanvasParams--><!--Device-unnamed-export declare interface CanvasParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageAIOptions

```TypeScript
imageAIOptions?: ImageAIOptions
```

给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。

**Type:** [ImageAIOptions](arkts-arkui-imageaioptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasParams-imageAIOptions?: ImageAIOptions--><!--Device-CanvasParams-imageAIOptions?: ImageAIOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## unit

```TypeScript
unit?: LengthMetricsUnit
```

用于描述Canvas绘制时所采用的单位模式。仅可在创建Canvas时设置，后续不可修改。默认值：LengthMetricsUnit.DEFAULT，undefined表示设置为默认值。

**Type:** [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasParams-unit?: LengthMetricsUnit--><!--Device-CanvasParams-unit?: LengthMetricsUnit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

