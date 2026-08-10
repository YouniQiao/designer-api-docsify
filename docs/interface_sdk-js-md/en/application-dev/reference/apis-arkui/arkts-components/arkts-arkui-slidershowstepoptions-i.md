# SliderShowStepOptions

Slider刻度点的无障碍文本信息映射集。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-unnamed-declare interface SliderShowStepOptions--><!--Device-unnamed-declare interface SliderShowStepOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stepsAccessibility

```TypeScript
stepsAccessibility?: Map<number, SliderStepItemAccessibility>
```

刻度点无障碍文本映射集，供屏幕阅读器等工具读取，增强无障碍功能。 

Key取值范围：[0, INT32_MAX]，当Key设定为负数和小数时，设定项不生效。 

默认值：{}

**Type:** Map&lt;number, SliderStepItemAccessibility&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SliderShowStepOptions-stepsAccessibility?: Map<number, SliderStepItemAccessibility>--><!--Device-SliderShowStepOptions-stepsAccessibility?: Map<number, SliderStepItemAccessibility>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

