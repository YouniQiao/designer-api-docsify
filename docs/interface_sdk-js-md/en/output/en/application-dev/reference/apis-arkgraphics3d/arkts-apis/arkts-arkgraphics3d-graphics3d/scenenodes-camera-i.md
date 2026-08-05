# Camera

Defines camera.

**Inheritance/Implementation:** Camera extends [Node](scenenodes-node-i.md)

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
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | -- the projection matrix of this camera |

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
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | -- the view matrix of this camera |

## raycast

```TypeScript
raycast(viewPosition: Vec2, params: RaycastParameters): Promise<RaycastResult[]>
```

Casts a ray to a position on the screen and lists what the ray hits.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Camera-raycast(viewPosition: Vec2, params: RaycastParameters): Promise<RaycastResult[]>--><!--Device-Camera-raycast(viewPosition: Vec2, params: RaycastParameters): Promise<RaycastResult[]>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| viewPosition | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Position to cast in the normalized device coordinates. |
| params | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Options used to execute the ray cast. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_[]&gt; | - Promise used to return an array of hit results, sorted from the closest to the farthest. The array may be empty. |

## clearColor

```TypeScript
clearColor: Color | null
```

Background clear color (environment background overrides this color, BACKGROUND\_NONE is needed for this to actually take effect).

**Type:** Color \| null

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Camera-clearColor: Color | null--><!--Device-Camera-clearColor: Color | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## effects

```TypeScript
readonly effects: Container<Effect>
```

The effects to apply on the camera output.

**Type:** Container&lt;Effect&gt;

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-Camera-readonly effects: Container<Effect>--><!--Device-Camera-readonly effects: Container<Effect>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## enabled

```TypeScript
enabled: boolean
```

Whether the camera is enabled.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Camera-enabled: boolean--><!--Device-Camera-enabled: boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## farPlane

```TypeScript
farPlane: double
```

Far plane of the camera, the unit is the scene unit in the world coordinate system (e.g., cm, m, km).

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Camera-farPlane: double--><!--Device-Camera-farPlane: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## fov

```TypeScript
fov: double
```

Field of view of the camera, the unit is radian.

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Camera-fov: double--><!--Device-Camera-fov: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## msaa

```TypeScript
msaa?: boolean
```

Controls whether MSAA is enabled or not.

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

Near plane of the camera, the unit is the scene unit in the world coordinate system (e.g., cm, m, km).

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Camera-nearPlane: double--><!--Device-Camera-nearPlane: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## postProcess

```TypeScript
postProcess: PostProcessSettings | null
```

The post processing settings of the camera.

**Type:** PostProcessSettings \| null

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Camera-postProcess: PostProcessSettings | null--><!--Device-Camera-postProcess: PostProcessSettings | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## renderingPipeline

```TypeScript
renderingPipeline?: RenderingPipelineType
```

Controls the rendering pipeline. Note that if FORWARD\_LIGHTWEIGHT pipeline is selected, some features will be unavailable.

**Type:** RenderingPipelineType

**Default:** RenderingPipelineType.FORWARD_LIGHTWEIGHT

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-Camera-renderingPipeline?: RenderingPipelineType--><!--Device-Camera-renderingPipeline?: RenderingPipelineType-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

