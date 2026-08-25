# Shader

Shader resource, which inherits from SceneResource.@extends SceneResource @interface Shader

**Inheritance/Implementation:** Shader extends [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md)

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## setShaderInputs

```TypeScript
setShaderInputs(inputs: Record<string, number | Vec2 | Vec3 | Vec4 | Image>): void
```

Sets the inputs for the shader. This API delivers better performance than directly setting the inputs property.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [inputs](arkts-arkgraphics3d-sceneresources-shader-i.md) | Record & lt;string, number \ | [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md) \| [Vec3](arkts-arkgraphics3d-scenetypes-vec3-i.md) \| [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md) \| [Image](arkts-arkgraphics3d-sceneresources-image-i.md)&gt; | Yes |

## inputs

```TypeScript
readonly inputs: Record<string, number | Vec2 | Vec3 | Vec4 | Image>
```

Inputs of the shader.

**Type:** Record&lt;string, number \| [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md) \| [Vec3](arkts-arkgraphics3d-scenetypes-vec3-i.md) \| [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md) \| [Image](arkts-arkgraphics3d-sceneresources-image-i.md)&gt;

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D
