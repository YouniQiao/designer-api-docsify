# BrightnessBlenderParam (System API)

BrightnessBlender的参数列表，用于配置提亮效果的各项属性，包括灰度调整系数、饱和度和混合比例等参数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface BrightnessBlenderParam--><!--Device-unnamed-export declare interface BrightnessBlenderParam-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## cubicRate

```TypeScript
cubicRate: double
```

灰度调整的三阶系数。 取值范围为[-20, 20]，超出边界会在实现时自动截断。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-BrightnessBlenderParam-cubicRate: double--><!--Device-BrightnessBlenderParam-cubicRate: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## degree

```TypeScript
degree: double
```

灰度调整的比例。 取值范围为[-20, 20]，超出边界会在实现时自动截断。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-BrightnessBlenderParam-degree: double--><!--Device-BrightnessBlenderParam-degree: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## fraction

```TypeScript
fraction: double
```

提亮效果的混合比例。 取值范围为[0, 1]，超出边界会在实现时自动截断。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-BrightnessBlenderParam-fraction: double--><!--Device-BrightnessBlenderParam-fraction: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## linearRate

```TypeScript
linearRate: double
```

灰度调整的线性系数。 取值范围为[-20, 20]，超出边界会在实现时自动截断。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-BrightnessBlenderParam-linearRate: double--><!--Device-BrightnessBlenderParam-linearRate: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## negativeCoefficient

```TypeScript
negativeCoefficient: [double, double, double]
```

基于基准饱和度的RGB负向调整参数。 每个number的取值范围为[-20, 20]，超出边界会在实现时自动截断。

**Type:** ArkTS-Dyn: [number, number, number]  <br>ArkTS-Sta：[double, double, double]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-BrightnessBlenderParam-negativeCoefficient: [double, double, double]--><!--Device-BrightnessBlenderParam-negativeCoefficient: [double, double, double]-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## positiveCoefficient

```TypeScript
positiveCoefficient: [double, double, double]
```

基于基准饱和度的RGB正向调整参数。 每个number的取值范围为[-20, 20]，超出边界会在实现时自动截断。

**Type:** ArkTS-Dyn: [number, number, number]  <br>ArkTS-Sta：[double, double, double]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-BrightnessBlenderParam-positiveCoefficient: [double, double, double]--><!--Device-BrightnessBlenderParam-positiveCoefficient: [double, double, double]-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## quadraticRate

```TypeScript
quadraticRate: double
```

灰度调整的二阶系数。 取值范围为[-20, 20]，超出边界会在实现时自动截断。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-BrightnessBlenderParam-quadraticRate: double--><!--Device-BrightnessBlenderParam-quadraticRate: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## saturation

```TypeScript
saturation: double
```

提亮的基准饱和度。 取值范围为[0, 20]，超出边界会在实现时自动截断。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-BrightnessBlenderParam-saturation: double--><!--Device-BrightnessBlenderParam-saturation: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

