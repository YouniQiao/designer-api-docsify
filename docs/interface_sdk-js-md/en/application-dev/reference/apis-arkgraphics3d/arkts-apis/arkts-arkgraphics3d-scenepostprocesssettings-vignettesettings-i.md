# VignetteSettings

定义暗角参数.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface VignetteSettings--><!--Device-unnamed-export interface VignetteSettings-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## intensity

```TypeScript
intensity?: double
```

控制暗边或亮边的强度.当intensity > 0时，边缘变暗且中心变亮，创建经典暗角效果.当intensity < 0时，中心变暗且边缘变亮，产生反向暗角效果.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Default:** 0.4

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-VignetteSettings-intensity?: double--><!--Device-VignetteSettings-intensity?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## roundness

```TypeScript
roundness?: double
```

控制暗角在[0, 1]之间的圆度.较低的值将使暗角效果更接近方形.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Default:** sqrt(0.5)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-VignetteSettings-roundness?: double--><!--Device-VignetteSettings-roundness?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

