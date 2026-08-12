# SceneTypes(Defines 3D basic types)

## Summary

### Classes

| Name | Description |
| --- | --- |
| [CubeGeometry](arkts-arkgraphics3d-scenetypes-cubegeometry-c.md) | Define a rectangular cuboid. |
| [CustomGeometry](arkts-arkgraphics3d-scenetypes-customgeometry-c.md) | An array of vertices and their data defining a custom geometric shape. |
| [CylinderGeometry](arkts-arkgraphics3d-scenetypes-cylindergeometry-c.md) | A cylinder geometry type that inherits from [GeometryDefinition](arkts-arkgraphics3d-scenetypes-geometrydefinition-c.md#GeometryDefinition).  > **NOTE：** >  > You must ensure that all three parameters are set correctly. > Invalid values may prevent cylinder creation or cause undefined behavior. |
| [GeometryDefinition](arkts-arkgraphics3d-scenetypes-geometrydefinition-c.md) | Define a geometric shape for mesh creation. |
| [PlaneGeometry](arkts-arkgraphics3d-scenetypes-planegeometry-c.md) | Define a plane. |
| [SphereGeometry](arkts-arkgraphics3d-scenetypes-spheregeometry-c.md) | Define a sphere. |

### Interfaces

| Name | Description |
| --- | --- |
| [Aabb](arkts-arkgraphics3d-scenetypes-aabb-i.md) | Axis aligned boundary box used to determine whether two objects in space are overlapping. |
| [Color](arkts-arkgraphics3d-scenetypes-color-i.md) | Color in RGBA format. It consists of four components: red, green, blue, and alpha. |
| [Mat4x4](arkts-arkgraphics3d-scenetypes-mat4x4-i.md) | A camera matrix, which is a mathematical tool for transforming 3D world coordinates into 2D image coordinates. |
| [Quaternion](arkts-arkgraphics3d-scenetypes-quaternion-i.md) | A mathematical notation for representing spatial rotations of elements in 3D space.Compared with Euler angles, a quaternion has advantages in numerical stability and avoiding the gimbal lock problem. |
| [Rect](arkts-arkgraphics3d-scenetypes-rect-i.md) | Rectangle in a plane. |
| [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md) | A two-dimensional vector used to represent a point or a direction in 2D space.It consists of two components: x and y. |
| [Vec3](arkts-arkgraphics3d-scenetypes-vec3-i.md) | A three-dimensional vector used to represent a point, a direction, or a vector transformation in 3D space.It consists of three components: x, y, and z. |
| [Vec4](arkts-arkgraphics3d-scenetypes-vec4-i.md) | A four-dimensional vector used to represent a point, a direction, or a vector transformation in 4D space.It consists of four components: x, y, z, and w. The fourth component (w) enhances normalization and convenience for various calculations and transformations. |

### Enums

| Name | Description |
| --- | --- |
| [GeometryType](arkts-arkgraphics3d-scenetypes-geometrytype-e.md) | Types of geometric shapes. |
| [PrimitiveTopology](arkts-arkgraphics3d-scenetypes-primitivetopology-e.md) | How vertices in a sequence form triangles. |
| [RenderingPipelineType](arkts-arkgraphics3d-scenetypes-renderingpipelinetype-e.md) | The enum of rendering pipeline type. |
| [ShadowAlgorithmType](arkts-arkgraphics3d-scenetypes-shadowalgorithmtype-e.md) | the type of shadow algorithm |

### Types

| Name | Description |
| --- | --- |
| [Position3](arkts-arkgraphics3d-position3-t.md) | 3D position information, the unit is the scene unit in the world coordinate system (e.g., cm, m, km). |
| [Rotation3](arkts-arkgraphics3d-rotation3-t.md) | 3D rotation info as euler angles, the unit is radian. |
| [Scale3](arkts-arkgraphics3d-scale3-t.md) | 3D scale information. |

