# BackgroundBrightnessOptions

Define BackgroundBrightness Options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface BackgroundBrightnessOptions--><!--Device-unnamed-export declare interface BackgroundBrightnessOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lightUpDegree

```TypeScript
lightUpDegree: double
```

Light up degree. A greater degree indicates a greater increase in brightness.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundBrightnessOptions-lightUpDegree: double--><!--Device-BackgroundBrightnessOptions-lightUpDegree: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rate

```TypeScript
rate: double
```

Brightness change rate. A higher rate means that brightness decreases more quickly. If **rate** is set to **0**, **lightUpDegree** will not take effect, meaning no brightening effect will occur.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundBrightnessOptions-rate: double--><!--Device-BackgroundBrightnessOptions-rate: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

