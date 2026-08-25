# VignetteSettings

Describes the settings for vignette effects.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUi.Graphics3D

## intensity

```TypeScript
intensity?: double
```

Effect strength. The value range is [0, 1]. The value 0 indicates no vignetting effect, and the value 1 indicates maximum vignetting intensity. The default value is 0.4.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Default:** 0.4

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUi.Graphics3D

## roundness

```TypeScript
roundness?: double
```

Application scope. The value range is [0, 1]. When the value is 0, the application scope is minimized. When the value is 1, the application scope is global. The default value is sqrt(0.5).

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Default:** sqrt(0.5)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUi.Graphics3D
