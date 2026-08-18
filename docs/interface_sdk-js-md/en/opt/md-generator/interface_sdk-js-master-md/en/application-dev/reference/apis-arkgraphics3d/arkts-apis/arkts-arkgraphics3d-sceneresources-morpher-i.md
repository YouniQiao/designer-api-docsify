# Morpher

Defines the deformation of 3D models by adjusting the weights of different deformation targets to create dynamic effects.

**Since:** 23

<!--Device-unnamed-export interface Morpher--><!--Device-unnamed-export interface Morpher-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## targets

```TypeScript
readonly targets: Record<string, number>
```

Used to store the names and weights of deformation targets. The weight value is usually within the range of [0.0, 1.0].

**Type:** [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, number&gt;

**Since:** 23

<!--Device-Morpher-readonly targets: Record<string, double>--><!--Device-Morpher-readonly targets: Record<string, double>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D
