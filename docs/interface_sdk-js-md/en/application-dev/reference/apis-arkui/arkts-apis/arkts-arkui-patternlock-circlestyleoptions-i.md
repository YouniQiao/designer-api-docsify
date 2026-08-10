# CircleStyleOptions

圆环样式的参数说明。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface CircleStyleOptions--><!--Device-unnamed-export declare interface CircleStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ResourceColor
```

背景圆环颜色。默认值：'# 33182431'。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CircleStyleOptions-color?: ResourceColor--><!--Device-CircleStyleOptions-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableForeground

```TypeScript
enableForeground?: boolean
```

背景圆环是否显示在宫格圆点上层。true：背景圆环显示在宫格圆点上层，遮盖宫格圆点；false：背景圆环显示在宫格圆点下层，不遮盖宫格圆点。默认值：false。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CircleStyleOptions-enableForeground?: boolean--><!--Device-CircleStyleOptions-enableForeground?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableWaveEffect

```TypeScript
enableWaveEffect?: boolean
```

选中宫格圆点后的波浪效果开关。true：显示波浪效果；false：不显示波浪效果。默认值：true。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CircleStyleOptions-enableWaveEffect?: boolean--><!--Device-CircleStyleOptions-enableWaveEffect?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## radius

```TypeScript
radius?: LengthMetrics
```

背景圆环的半径。默认值：circleRadius的1.833（即11/6）倍。

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CircleStyleOptions-radius?: LengthMetrics--><!--Device-CircleStyleOptions-radius?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

