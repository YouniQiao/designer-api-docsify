# Camera

Camera node, which inherits from Node.@extends Node @interface Camera

**Inheritance/Implementation:** Camera extends [Node](arkts-arkgraphics3d-scenenodes-node-i.md)

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## getProjectionMatrix

```TypeScript
getProjectionMatrix(): Mat4x4
```

Obtains the projection matrix of the camera.

**Since:** 23

**System capability:** SystemCapability.ArkUi.Graphics3D

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Mat4x4](arkts-arkgraphics3d-scenetypes-mat4x4-i.md) |

## getViewMatrix

```TypeScript
getViewMatrix(): Mat4x4
```

Obtains the view matrix of the camera.

**Since:** 23

**System capability:** SystemCapability.ArkUi.Graphics3D

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Mat4x4](arkts-arkgraphics3d-scenetypes-mat4x4-i.md) |

## raycast

```TypeScript
raycast(viewPosition: Vec2, params: RaycastParameters): Promise<RaycastResult[]>
```

Casts a ray from a specific position on the screen to detect and retrieve information about all hit 3D objects. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| viewPosition | [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md) | Yes |
| params | [RaycastParameters](arkts-arkgraphics3d-scene-raycastparameters-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[RaycastResult](arkts-arkgraphics3d-scene-raycastresult-i.md)[]&gt; |

## clearColor

```TypeScript
clearColor: Color | null
```

Color after the render target is cleared.

**Type:** [Color](arkts-arkgraphics3d-scenetypes-color-i.md) \| null

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## effects

```TypeScript
readonly effects: Container<Effect>
```

Post-processing effects applied to the camera output.

**Type:** [Container](arkts-arkgraphics3d-scenenodes-container-i.md)&lt;[Effect](arkts-arkgraphics3d-sceneresources-effect-i.md)&gt;

**Since:** 21

**System capability:** SystemCapability.ArkUi.Graphics3D

## enabled

```TypeScript
enabled: boolean
```

Whether the camera is enabled. true if enabled, false otherwise.

**Type:** boolean

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## farPlane

```TypeScript
farPlane: number
```

Far plane. The unit is the scene unit (such as cm, m, and km) in the world coordinate system. The value is greater than that of nearPlane.

**Type:** number

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## fov

```TypeScript
fov: number
```

Field of view. The unit is radian (rad). The value ranges from 0 to π radians.

**Type:** number

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## msaa

```TypeScript
msaa?: boolean
```

Whether Multisample Anti-Aliasing (MSAA) is enabled. true if enabled, false otherwise. The default value is false.

**Type:** boolean

**Default:** false

**Since:** 22

**System capability:** SystemCapability.ArkUi.Graphics3D

## nearPlane

```TypeScript
nearPlane: number
```

Near plane. The unit is the scene unit (such as cm, m, and km) in the world coordinate system. The value is greater than 0.

**Type:** number

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## postProcess

```TypeScript
postProcess: PostProcessSettings | null
```

Post-processing settings.

**Type:** [PostProcessSettings](arkts-arkgraphics3d-scenepostprocesssettings-postprocesssettings-i.md) \| null

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## renderingPipeline

```TypeScript
renderingPipeline?: RenderingPipelineType
```

Rendering pipeline type. If this parameter is not set, the lightweight forward rendering pipeline is used by default. (If the FORWARD_LIGHTWEIGHT pipeline is selected, certain features are unavailable.)

**Type:** [RenderingPipelineType](arkts-arkgraphics3d-scenetypes-renderingpipelinetype-e.md)

**Default:** RenderingPipelineType.FORWARD_LIGHTWEIGHT

**Since:** 21

**System capability:** SystemCapability.ArkUi.Graphics3D
