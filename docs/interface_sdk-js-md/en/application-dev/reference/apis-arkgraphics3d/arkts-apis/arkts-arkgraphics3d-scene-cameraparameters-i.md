# CameraParameters

相机创建参数. 可用于定义相机创建的额外选项.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface CameraParameters--><!--Device-unnamed-export interface CameraParameters-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## msaa

```TypeScript
msaa?: boolean
```

选择是否启用MSAA.

**Type:** boolean

**Default:** false

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-CameraParameters-msaa?: boolean--><!--Device-CameraParameters-msaa?: boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## renderingPipeline

```TypeScript
renderingPipeline?: RenderingPipelineType
```

选择初始渲染管线类型.

**Type:** [RenderingPipelineType](arkts-arkgraphics3d-scenetypes-renderingpipelinetype-e.md)

**Default:** RenderingPipelineType.FORWARD_LIGHTWEIGHT 前向轻量级渲染管线

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-CameraParameters-renderingPipeline?: RenderingPipelineType--><!--Device-CameraParameters-renderingPipeline?: RenderingPipelineType-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

