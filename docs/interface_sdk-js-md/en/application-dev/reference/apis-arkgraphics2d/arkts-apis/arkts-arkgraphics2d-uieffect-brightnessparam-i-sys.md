# BrightnessParam (System API)

Detailed description of the material brightness parameters.

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

Third-order coefficient for grayscale adjustment. The value range is [-1, 1]. Values less than -1 are treated as -1; values greater than 1 are treated as 1. A larger value results in a stronger grayscale adjustment effect.

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

Blending ratio for the brightness effect. The value range is [0, 1]. Values less than 0 are treated as 0;values greater than 1 are treated as 1. A larger value indicates a weaker brightness effect.

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

Grayscale adjustment ratio. The value range is [-1, 1]. Values less than -1 are treated as -1;values greater than 1 are treated as 1. A larger value results in a stronger grayscale adjustment effect.

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

Negative adjustment coefficients based on the base saturation. The value range for each number is [-1, 1].Values less than -1 are treated as -1; values greater than 1 are treated as 1.A larger value indicates lower saturation.

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

Positive adjustment coefficients based on the base saturation. The value range for each number is [-1, 1].Values less than -1 are treated as -1; values greater than 1 are treated as 1.A larger value indicates higher saturation.

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

Second-order coefficient for grayscale adjustment. The value range is [-1, 1]. Values less than -1 are treated as -1; values greater than 1 are treated as 1. A larger value results in a stronger grayscale adjustment effect.

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

Linear coefficient for grayscale adjustment. The value range is [-1, 1]. Values less than -1 are treated as -1;values greater than 1 are treated as 1. A larger value results in a stronger grayscale adjustment effect.

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

Base saturation for brightness. The value range is [0, 1]. Values less than 0 are treated as 0;values greater than 1 are treated as 1. A larger value indicates a higher base saturation.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-BrightnessParam-saturation : double--><!--Device-BrightnessParam-saturation : double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

