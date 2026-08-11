# Camera

Defines camera.

**Inheritance/Implementation:** Camera extends [Node](arkts-arkgraphics3d-scenenodes-node-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface Camera extends Node--><!--Device-unnamed-export interface Camera extends Node-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## getProjectionMatrix

```TypeScript
getProjectionMatrix(): Mat4x4
```

Get the projection matrix of this camera.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Camera-getProjectionMatrix(): Mat4x4--><!--Device-Camera-getProjectionMatrix(): Mat4x4-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Return value:**

| Type | Description |
| --- | --- |
| [Mat4x4](arkts-arkgraphics3d-scenetypes-mat4x4-i.md) | the projection matrix of this camera |

## getViewMatrix

```TypeScript
getViewMatrix(): Mat4x4
```

Get the view matrix of this camera.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Camera-getViewMatrix(): Mat4x4--><!--Device-Camera-getViewMatrix(): Mat4x4-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Return value:**

| Type | Description |
| --- | --- |
| [Mat4x4](arkts-arkgraphics3d-scenetypes-mat4x4-i.md) | the view matrix of this camera |

## raycast

```TypeScript
raycast(viewPosition: Vec2, params: RaycastParameters): Promise<RaycastResult[]>
```

Casts a ray from a specific position on the screen to detect and retrieve information about all hit 3D objects.This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Camera-raycast(viewPosition: Vec2, params: RaycastParameters): Promise<RaycastResult[]>--><!--Device-Camera-raycast(viewPosition: Vec2, params: RaycastParameters): Promise<RaycastResult[]>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| viewPosition | [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md) | Yes | Normalized screen coordinates. The value range is [0, 1], where (0,0) corresponds to the top-left corner of the Component3D component, and (1,1) corresponds to the bottom-right corner. |
| params | [RaycastParameters](arkts-arkgraphics3d-scene-raycastparameters-i.md) | Yes | Configuration parameters for raycasting, such as detection range and filtered nodes. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[RaycastResult](arkts-arkgraphics3d-scene-raycastresult-i.md)[]&gt; | An array of hit objects sorted by distance (from nearest to farthest). If no objects are hit, an empty array is returned. |

## clearColor

```TypeScript
clearColor: Color | null
```

Color after the render target is cleared.

**Type:** [Color](arkts-arkgraphics3d-scenetypes-color-i.md) \| null

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Camera-clearColor: Color | null--><!--Device-Camera-clearColor: Color | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## effects

```TypeScript
readonly effects: Container<Effect>
```

Post-processing effects applied to the camera output.

**Type:** [Container](arkts-arkgraphics3d-scenenodes-container-i.md)&lt;[Effect](arkts-arkgraphics3d-sceneresources-effect-i.md)&gt;

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-Camera-readonly effects: Container<Effect>--><!--Device-Camera-readonly effects: Container<Effect>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## enabled

```TypeScript
enabled: boolean
```

Whether the camera is enabled. true if enabled, false otherwise.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Camera-enabled: boolean--><!--Device-Camera-enabled: boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## farPlane

```TypeScript
farPlane: double
```

Far plane. The unit is the scene unit (such as cm, m, and km) in the world coordinate system.The value is greater than that of nearPlane.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Camera-farPlane: double--><!--Device-Camera-farPlane: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## fov

```TypeScript
fov: double
```

Field of view. The unit is radian (rad).The value ranges from 0 to π radians.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Camera-fov: double--><!--Device-Camera-fov: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## msaa

```TypeScript
msaa?: boolean
```

Whether Multisample Anti-Aliasing (MSAA) is enabled. true if enabled, false otherwise.The default value is false.

**Type:** boolean

**Default:** false

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-Camera-msaa?: boolean--><!--Device-Camera-msaa?: boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## nearPlane

```TypeScript
nearPlane: double
```

Near plane. The unit is the scene unit (such as cm, m, and km) in the world coordinate system.The value is greater than 0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Camera-nearPlane: double--><!--Device-Camera-nearPlane: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## postProcess

```TypeScript
postProcess: PostProcessSettings | null
```

Post-processing settings.

**Type:** [PostProcessSettings](arkts-arkgraphics3d-scenepostprocesssettings-postprocesssettings-i.md) \| null

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Camera-postProcess: PostProcessSettings | null--><!--Device-Camera-postProcess: PostProcessSettings | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## renderingPipeline

```TypeScript
renderingPipeline?: RenderingPipelineType
```

Rendering pipeline type. If this parameter is not set, the lightweight forward rendering pipeline is used by default.(If the FORWARD_LIGHTWEIGHT pipeline is selected, certain features are unavailable.)

**Type:** [RenderingPipelineType](arkts-arkgraphics3d-scenetypes-renderingpipelinetype-e.md)

**Default:** RenderingPipelineType.FORWARD_LIGHTWEIGHT

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-Camera-renderingPipeline?: RenderingPipelineType--><!--Device-Camera-renderingPipeline?: RenderingPipelineType-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

