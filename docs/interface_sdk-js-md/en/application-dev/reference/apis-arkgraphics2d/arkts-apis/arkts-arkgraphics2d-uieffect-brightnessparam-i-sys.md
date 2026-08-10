# BrightnessParam (System API)

材质提亮参数的详细说明。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-uiEffect-interface BrightnessParam--><!--Device-uiEffect-interface BrightnessParam-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## cubicCoeff

```TypeScript
cubicCoeff : double
```

灰度调整三阶系数。取值范围为[-1, 1]，小于-1时取值为-1，大于1时取值为1，值越大，灰度调整效果越强。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-BrightnessParam-cubicCoeff : double--><!--Device-BrightnessParam-cubicCoeff : double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## fraction

```TypeScript
fraction : double
```

提亮效果混合比例。取值范围为[0, 1]，小于0时取值为0，大于1时取值为1，值越大，提亮效果越弱。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-BrightnessParam-fraction : double--><!--Device-BrightnessParam-fraction : double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## lightUpDegree

```TypeScript
lightUpDegree : double
```

灰度调整比例。取值范围为[-1, 1]，小于-1时取值为-1，大于1时取值为1，值越大，灰度调整效果越强。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-BrightnessParam-lightUpDegree : double--><!--Device-BrightnessParam-lightUpDegree : double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## negRgb

```TypeScript
negRgb : [double, double, double]
```

基于基准饱和度的负向调整系数。取值范围为[-1, 1]，小于-1时取值为-1，大于1时取值为1，值越大饱和度越低。

**Type:** ArkTS-Dyn: [number, number, number]  <br>ArkTS-Sta：[double, double, double]

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-BrightnessParam-negRgb : [double, double, double]--><!--Device-BrightnessParam-negRgb : [double, double, double]-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## posRgb

```TypeScript
posRgb : [double, double, double]
```

基于基准饱和度的正向调整系数。取值范围为[-1, 1]，小于-1时取值为-1，大于1时取值为1，值越大饱和度越高。

**Type:** ArkTS-Dyn: [number, number, number]  <br>ArkTS-Sta：[double, double, double]

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-BrightnessParam-posRgb : [double, double, double]--><!--Device-BrightnessParam-posRgb : [double, double, double]-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## quadCoeff

```TypeScript
quadCoeff : double
```

灰度调整二阶系数。取值范围为[-1, 1]，小于-1时取值为-1，大于1时取值为1，值越大，灰度调整效果越强。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-BrightnessParam-quadCoeff : double--><!--Device-BrightnessParam-quadCoeff : double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## rate

```TypeScript
rate : double
```

灰度调整线性系数。取值范围为[-1, 1]，小于-1时取值为-1，大于1时取值为1，值越大，灰度调整效果越强。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-BrightnessParam-rate : double--><!--Device-BrightnessParam-rate : double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## saturation

```TypeScript
saturation : double
```

提亮基准饱和度。取值范围为[0, 1]，小于0时取值为0，大于1时取值为1，值越大基准饱和度越高。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-BrightnessParam-saturation : double--><!--Device-BrightnessParam-saturation : double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

