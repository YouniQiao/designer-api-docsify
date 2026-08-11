# SceneNodes(Defines 3D node related interfaces)

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [Camera](arkts-arkgraphics3d-scenenodes-camera-i.md) | Defines camera. |
| [Container](arkts-arkgraphics3d-scenenodes-container-i.md) | Defines a scene object container. |
| [DirectionalLight](arkts-arkgraphics3d-scenenodes-directionallight-i.md) | Defines directional light. |
| [Geometry](arkts-arkgraphics3d-scenenodes-geometry-i.md) | Geometric node type that holds renderable mesh data and supports optional deformation features. |
| [LayerMask](arkts-arkgraphics3d-scenenodes-layermask-i.md) | Defines the layer mask of the node. |
| [Light](arkts-arkgraphics3d-scenenodes-light-i.md) | Defines light interface. |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | The 3D scene consists of nodes in a tree hierarchy, where each node implements a Node interface. |
| [SpotLight](arkts-arkgraphics3d-scenenodes-spotlight-i.md) | Spotlight, which inherits from [Light](arkts-arkgraphics3d-scenenodes-light-i.md).  A spotlight emits a conical beam of light in a specific direction,with the intensity of the light decaying according to the angles defined by the innerAngle and outerAngle parameters.Like a point light, a spotlight's intensity also diminishes with distance from the source.  > **NOTE：** >  > Ensure that the innerAngle and outerAngle values are proper. > If the value set for outerAngle is greater than PI/2, it is forcibly set to PI/2 internally. > If the value set for outerAngle is less than innerAngle, it is forcibly set to innerAngle internally. |

### Enums

| Name | Description |
| --- | --- |
| [LightType](arkts-arkgraphics3d-scenenodes-lighttype-e.md) | The enum of light type. |
| [NodeType](arkts-arkgraphics3d-scenenodes-nodetype-e.md) | The enum of node type. |

