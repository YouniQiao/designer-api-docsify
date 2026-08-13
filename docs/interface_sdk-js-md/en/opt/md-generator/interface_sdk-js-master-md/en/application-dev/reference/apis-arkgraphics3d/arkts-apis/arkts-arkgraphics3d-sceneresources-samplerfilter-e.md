# SamplerFilter

Enumerates the filtering modes of a sampler. The filtering mode determines the interpolation method used when sampling textures, controlling how final pixel colors are calculated during texture scaling or deformation.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-export enum SamplerFilter--><!--Device-unnamed-export enum SamplerFilter-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## NEAREST

```TypeScript
NEAREST = 0
```

Uses nearest-neighbor interpolation, which is fast but can result in jagged edges.

**Since:** 23

**Deprecated since:** -1

<!--Device-SamplerFilter-NEAREST = 0--><!--Device-SamplerFilter-NEAREST = 0-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## LINEAR

```TypeScript
LINEAR = 1
```

Uses linear interpolation, providing a smoother appearance but with a slight performance cost.

**Since:** 23

**Deprecated since:** -1

<!--Device-SamplerFilter-LINEAR = 1--><!--Device-SamplerFilter-LINEAR = 1-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D
