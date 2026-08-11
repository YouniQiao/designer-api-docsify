# Shader

Shader resource, which inherits from [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md).

**Inheritance/Implementation:** Shader extends [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface Shader extends SceneResource--><!--Device-unnamed-export interface Shader extends SceneResource-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## setShaderInputs

ArkTS-Dyn:
```TypeScript
setShaderInputs(inputs: Record<string, number | Vec2 | Vec3 | Vec4 | Image>): void
```

ArkTS-Sta:
```TypeScript
setShaderInputs(inputs: Record<string, double | Vec2 | Vec3 | Vec4 | Image>): void
```

Sets the inputs for the shader. This API delivers better performance than directly setting the inputs property.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Shader-setShaderInputs(inputs: Record<string, double | Vec2 | Vec3 | Vec4 | Image>): void--><!--Device-Shader-setShaderInputs(inputs: Record<string, double | Vec2 | Vec3 | Vec4 | Image>): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inputs | ArkTS-Dyn: [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, number \| [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md) \| [Vec3](arkts-arkgraphics3d-scenetypes-vec3-i.md) \| [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md) \| Image&gt;  <br>ArkTS-Sta：[Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, double \| [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md) \| [Vec3](arkts-arkgraphics3d-scenetypes-vec3-i.md) \| [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md) \| Image&gt; | Yes | A mapping of strings to values for setting shader inputs. |

## inputs

```TypeScript
readonly inputs: Record<string, double | Vec2 | Vec3 | Vec4 | Image>
```

Inputs of the shader.

**Type:** ArkTS-Dyn: [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, number \| [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md) \| [Vec3](arkts-arkgraphics3d-scenetypes-vec3-i.md) \| [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md) \| Image&gt;  <br>ArkTS-Sta：[Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, double \| [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md) \| [Vec3](arkts-arkgraphics3d-scenetypes-vec3-i.md) \| [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md) \| Image&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Shader-readonly inputs: Record<string, double | Vec2 | Vec3 | Vec4 | Image>--><!--Device-Shader-readonly inputs: Record<string, double | Vec2 | Vec3 | Vec4 | Image>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

