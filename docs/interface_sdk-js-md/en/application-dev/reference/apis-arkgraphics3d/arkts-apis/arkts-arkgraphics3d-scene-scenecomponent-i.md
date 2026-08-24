# SceneComponent

Represents a basic scene component, which is used to describe the component information of a scene node, including the component name and its properties.@interface SceneComponent

**Since:** 23

<!--Device-unnamed-export interface SceneComponent--><!--Device-unnamed-export interface SceneComponent-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## name

```TypeScript
name: string
```

Name of the scene component, which is customizable.

**Type:** string

**Since:** 23

<!--Device-SceneComponent-name: string--><!--Device-SceneComponent-name: string-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## property

```TypeScript
readonly property: Record<string, string | double | Vec2 | Vec3 | Vec4 | SceneResource | boolean | double[] |
  string[] | SceneResource[] | Vec2[] | Vec3[] | Vec4[] | null | undefined>
```

A set of component properties stored in key-value pairs. It supports multiple basic and complex types to describe various properties of the scene component. The unit and value range depend on the specific scene component.

**Type:** Record&lt;string, string \| double \| [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md) \| [Vec3](arkts-arkgraphics3d-scenetypes-vec3-i.md) \| [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md) \| [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md) \| boolean \| double[] \| string[] \| [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md)[] \| [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md)[] \| [Vec3](arkts-arkgraphics3d-scenetypes-vec3-i.md)[] \| [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md)[] \| null \| undefined&gt;

**Since:** 23

<!--Device-SceneComponent-readonly property: Record<string, string | double | Vec2 | Vec3 | Vec4 | SceneResource | boolean | double[] |  string[] | SceneResource[] | Vec2[] | Vec3[] | Vec4[] | null | undefined>--><!--Device-SceneComponent-readonly property: Record<string, string | double | Vec2 | Vec3 | Vec4 | SceneResource | boolean | double[] |  string[] | SceneResource[] | Vec2[] | Vec3[] | Vec4[] | null | undefined>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

