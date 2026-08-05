# VignetteSettings

Defines vignette parameters.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface VignetteSettings--><!--Device-unnamed-export interface VignetteSettings-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## intensity

```TypeScript
intensity?: double
```

Controls how strong the dark or bright edges are. When intensity > 0, the edges darken and the center brightens, creating a classic vignette effect. When intensity < 0, the center darkens and the edges brighten, producing an reverse vignette effect.

**Type:** double

**Default:** 0.4

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-VignetteSettings-intensity?: double--><!--Device-VignetteSettings-intensity?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## roundness

```TypeScript
roundness?: double
```

Controls the roundness of vignette between [0, 1]. Lower value will make the vignette effect more square.

**Type:** double

**Default:** sqrt(0.5)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-VignetteSettings-roundness?: double--><!--Device-VignetteSettings-roundness?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

