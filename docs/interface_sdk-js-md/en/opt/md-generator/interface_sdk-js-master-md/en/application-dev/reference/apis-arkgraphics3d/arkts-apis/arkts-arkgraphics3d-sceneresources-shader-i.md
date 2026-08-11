# Shader

Shader resource, which inherits from [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md).

**Inheritance/Implementation:** Shader extends [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md)

**Since:** 12

<!--Device-unnamed-export interface Shader extends SceneResource--><!--Device-unnamed-export interface Shader extends SceneResource-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## setShaderInputs

```TypeScript
setShaderInputs(inputs: Record<string, number | Vec2 | Vec3 | Vec4 | Image>): void
```

Sets the inputs for the shader. This API delivers better performance than directly setting the inputs property.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Shader-setShaderInputs(inputs: Record<string, double | Vec2 | Vec3 | Vec4 | Image>): void--><!--Device-Shader-setShaderInputs(inputs: Record<string, double | Vec2 | Vec3 | Vec4 | Image>): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [inputs](#inputs) | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, number \| [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md) \| [Vec3](arkts-arkgraphics3d-scenetypes-vec3-i.md) \| [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md) \| [Image&gt;](arkts-arkgraphics3d-sceneresources-image-i.md) | Yes |

## inputs

```TypeScript
readonly inputs: Record<string, number | Vec2 | Vec3 | Vec4 | Image>
```

Inputs of the shader.

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, number \| [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md) \| [Vec3](arkts-arkgraphics3d-scenetypes-vec3-i.md) \| [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md) \| Image&gt;

**Since:** 12

<!--Device-Shader-readonly inputs: Record<string, double | Vec2 | Vec3 | Vec4 | Image>--><!--Device-Shader-readonly inputs: Record<string, double | Vec2 | Vec3 | Vec4 | Image>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D
