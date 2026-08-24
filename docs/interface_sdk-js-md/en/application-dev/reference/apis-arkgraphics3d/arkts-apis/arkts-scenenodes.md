# SceneNodes

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [Camera](arkts-arkgraphics3d-scenenodes-camera-i.md) | Camera node, which inherits from Node.@extends Node @interface Camera |
| [Container](arkts-arkgraphics3d-scenenodes-container-i.md) | Container for defining scene nodes. It provides a way to group scene nodes into a hierarchy.@interface Container |
| [DirectionalLight](arkts-arkgraphics3d-scenenodes-directionallight-i.md) | Directional light, which inherits from Light.@extends Light @interface DirectionalLight |
| [Geometry](arkts-arkgraphics3d-scenenodes-geometry-i.md) | Geometric node type that holds renderable mesh data and supports optional deformation features. It inherits from Node.@extends Node @interface Geometry |
| [LayerMask](arkts-arkgraphics3d-scenenodes-layermask-i.md) | Defines the layer mask of a node.@interface LayerMask |
| [Light](arkts-arkgraphics3d-scenenodes-light-i.md) | Light node, which inherits from Node.@extends Node @interface Light |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | The 3D scene consists of nodes in a tree hierarchy, where each node implements a Node interface. This class inherits from SceneResource.@extends SceneResource @interface Node |
| [SpotLight](arkts-arkgraphics3d-scenenodes-spotlight-i.md) | Spotlight, which inherits from Light.A spotlight emits a conical beam of light in a specific direction, with the intensity of the light decaying according to the angles defined by the innerAngle and outerAngle parameters. Like a point light, a spotlight's intensity also diminishes with distance from the source. |

### Enums

| Name | Description |
| --- | --- |
| [LightType](arkts-arkgraphics3d-scenenodes-lighttype-e.md) | Enumerates the light types.@enum { int } |
| [NodeType](arkts-arkgraphics3d-scenenodes-nodetype-e.md) | Enumerates the node types.@enum { int } |

