# BarMode

Declare the graphic format of the bar chart.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum BarMode--><!--Device-unnamed-export declare enum BarMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Scrollable

```TypeScript
Scrollable = 0
```

The width of each tab is determined by the actual layout. The tabs are scrollable in the following case: In horizontal layout, the total width exceeds the tab bar width; in vertical layout, the total height exceeds the tab bar height.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BarMode-Scrollable = 0--><!--Device-BarMode-Scrollable = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Fixed

```TypeScript
Fixed = 1
```

The width of each tab is determined by equally dividing the number of tabs by the bar width (or bar height in the vertical layout).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BarMode-Fixed = 1--><!--Device-BarMode-Fixed = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

