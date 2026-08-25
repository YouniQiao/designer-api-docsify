# Shader

着色器，继承自SceneResource。@extends SceneResource @interface Shader

**继承/实现关系：** Shader extends [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md)

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## setShaderInputs

```TypeScript
setShaderInputs(inputs: Record<string, number | Vec2 | Vec3 | Vec4 | Image>): void
```

设置Shader的输入，该接口性能优于直接设置inputs属性。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [inputs](arkts-arkgraphics3d-sceneresources-shader-i.md) | Record & lt;string, number \ | [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md) \| [Vec3](arkts-arkgraphics3d-scenetypes-vec3-i.md) \| [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md) \| [Image](arkts-arkgraphics3d-sceneresources-image-i.md)&gt; | 是 |

## inputs

```TypeScript
readonly inputs: Record<string, number | Vec2 | Vec3 | Vec4 | Image>
```

着色器输入。

**类型：** Record&lt;string, number \| [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md) \| [Vec3](arkts-arkgraphics3d-scenetypes-vec3-i.md) \| [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md) \| [Image](arkts-arkgraphics3d-sceneresources-image-i.md)&gt;

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D
