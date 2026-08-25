# Morpher

Defines the deformation of 3D models by adjusting the weights of different deformation targets to create dynamic effects.@interface Morpher

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUi.Graphics3D

## targets

```TypeScript
readonly targets: Record<string, double>
```

Used to store the names and weights of deformation targets. The weight value is usually within the range of [0.0, 1.0].

**Type:** ArkTS-Dyn: Record&lt;string, number&gt;  <br>ArkTS-Sta：Record&lt;string, double&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUi.Graphics3D
