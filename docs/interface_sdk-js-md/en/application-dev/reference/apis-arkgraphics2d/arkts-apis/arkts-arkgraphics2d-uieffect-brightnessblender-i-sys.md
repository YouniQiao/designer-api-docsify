# BrightnessBlender (System API)

提亮混合器，用于将提亮效果添加到指定的组件上。在调用BrightnessBlender前，需要先通过createBrightnessBlender创建一个BrightnessBlender实例。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-uiEffect-interface BrightnessBlender--><!--Device-uiEffect-interface BrightnessBlender-End-->

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

<!--Device-BrightnessBlender-cubicRate: double--><!--Device-BrightnessBlender-cubicRate: double-End-->

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

<!--Device-BrightnessBlender-degree: double--><!--Device-BrightnessBlender-degree: double-End-->

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

<!--Device-BrightnessBlender-fraction: double--><!--Device-BrightnessBlender-fraction: double-End-->

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

<!--Device-BrightnessBlender-linearRate: double--><!--Device-BrightnessBlender-linearRate: double-End-->

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

<!--Device-BrightnessBlender-negativeCoefficient: [double, double, double]--><!--Device-BrightnessBlender-negativeCoefficient: [double, double, double]-End-->

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

<!--Device-BrightnessBlender-positiveCoefficient: [double, double, double]--><!--Device-BrightnessBlender-positiveCoefficient: [double, double, double]-End-->

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

<!--Device-BrightnessBlender-quadraticRate: double--><!--Device-BrightnessBlender-quadraticRate: double-End-->

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

<!--Device-BrightnessBlender-saturation: double--><!--Device-BrightnessBlender-saturation: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

