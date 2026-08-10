# SliderShowStepOptions

Slider刻度点的无障碍文本信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SliderShowStepOptions--><!--Device-unnamed-export declare interface SliderShowStepOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stepsAccessibility

```TypeScript
stepsAccessibility?: Map<double, SliderStepItemAccessibility>
```

用于设置刻度点提供辅助功能文本，供屏幕阅读器等工具读取，增强无障碍功能。 

Key取值范围：[0, INT32_MAX]，当Key设定为负数和小数时，设定项不生效。 

默认值：{}

**Type:** Map&lt;double, SliderStepItemAccessibility&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderShowStepOptions-stepsAccessibility?: Map<double, SliderStepItemAccessibility>--><!--Device-SliderShowStepOptions-stepsAccessibility?: Map<double, SliderStepItemAccessibility>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

