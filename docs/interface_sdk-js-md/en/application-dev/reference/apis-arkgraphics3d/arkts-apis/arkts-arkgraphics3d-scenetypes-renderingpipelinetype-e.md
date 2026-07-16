# RenderingPipelineType

The enum of rendering pipeline type.

**Since:** 21

<!--Device-unnamed-export enum RenderingPipelineType--><!--Device-unnamed-export enum RenderingPipelineType-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## FORWARD_LIGHTWEIGHT

```TypeScript
FORWARD_LIGHTWEIGHT = 0
```

Lightweight forward pipeline which renders directly to back buffer.This pipeline can only do per-pixel effects (e.g. tonemapping) in the shader,complex effects (e.g. bloom) are not supported.

**Since:** 21

<!--Device-RenderingPipelineType-FORWARD_LIGHTWEIGHT = 0--><!--Device-RenderingPipelineType-FORWARD_LIGHTWEIGHT = 0-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## FORWARD

```TypeScript
FORWARD = 1
```

Forward pipeline for high quality rendering.Use this for complex visual effects (e.g. bloom).

**Since:** 21

<!--Device-RenderingPipelineType-FORWARD = 1--><!--Device-RenderingPipelineType-FORWARD = 1-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

