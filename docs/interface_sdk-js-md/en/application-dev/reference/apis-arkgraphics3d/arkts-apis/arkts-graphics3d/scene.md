# graphics3d/Scene(Defines 3D scene related interfaces)

## Summary

### Classes

| Name | Description |
| --- | --- |
| [PCFConfig](scene-pcfconfig-c.md) | param config for pcf soft shadow |
| [Scene](scene-scene-c.md) | Defines the 3d scene. |
| [SoftShadowConfig](scene-softshadowconfig-c.md) | param config for soft shadow, control the algorithm type and its configuration |

<!--Del-->
### Classes（系统接口）

| Name | Description |
| --- | --- |
| [Scene](scene-scene-c-sys.md) | Defines the 3d scene. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [CameraParameters](scene-cameraparameters-i.md) | Camera creation parameters. Can be used to define extra options for camera creation. |
| [EffectParameters](scene-effectparameters-i.md) | The parameters for effect |
| [RaycastParameters](scene-raycastparameters-i.md) | How a raycast should be performed. |
| [RaycastResult](scene-raycastresult-i.md) | The result of a ray cast hit. |
| [RenderConfiguration](scene-renderconfiguration-i.md) | Global render configuration control |
| [RenderContext](scene-rendercontext-i.md) | Render context defines the context for all rendering resources. Resources within the same render context may be shared between scenes created within the same render context. |
| [RenderParameters](scene-renderparameters-i.md) | Defines parameters for manual rendering. |
| [RenderResourceFactory](scene-renderresourcefactory-i.md) | The render resource factory. RenderResourceFactory is used to create resources that can be shared across Scenes that share a RenderContext |
| [SceneComponent](scene-scenecomponent-i.md) | Define underlying scene component |
| [SceneNodeParameters](scene-scenenodeparameters-i.md) | The scene node parameters type. |
| [SceneResourceFactory](scene-sceneresourcefactory-i.md) | The scene resource factory. |
| [SceneResourceParameters](scene-sceneresourceparameters-i.md) | The scene resource parameters type. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [RenderResourceFactory](scene-renderresourcefactory-i-sys.md) | The render resource factory. RenderResourceFactory is used to create resources that can be shared across Scenes that share a RenderContext |
| [SceneLoadParams](scene-sceneloadparams-i-sys.md) | The parameters for loading a scene |
<!--DelEnd-->

