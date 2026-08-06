# graphics3d/SceneResources(Defines 3D resource related interfaces)

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [Animation](sceneresources-animation-i.md) | Animation resource. |
| [Blend](sceneresources-blend-i.md) | Blend interface. |
| [Effect](sceneresources-effect-i.md) | Effect resource. |
| [Environment](sceneresources-environment-i.md) | Environment resource. |
| [Image](sceneresources-image-i.md) | Image resource. |
| [ImageStream](sceneresources-imagestream-i.md) | ImageStream resource. |
| [Material](sceneresources-material-i.md) | Material resource. |
| [MaterialProperty](sceneresources-materialproperty-i.md) | Material property interface. |
| [Mesh](sceneresources-mesh-i.md) | The mesh instance owned by the mesh node |
| [MeshResource](sceneresources-meshresource-i.md) | The mesh data description resource for the geometry node |
| [MetallicRoughnessMaterial](sceneresources-metallicroughnessmaterial-i.md) | Physically-based metallic roughness material resource. |
| [Morpher](sceneresources-morpher-i.md) | Defines Morpher interface for specifying morph targets for Node's geometry. |
| [OcclusionMaterial](sceneresources-occlusionmaterial-i.md) | Occlusion material resource |
| [RenderSort](sceneresources-rendersort-i.md) | Render sort Layer. Within a render slot a layer can define a sort layer order.There are 0-63 values available (0 first, 63 last). Default id value is 32.1. Typical use case is to set render sort layer to objects which render with depth test without depth write.2. Typical use case is to always render character and/or camera object first to cull large parts of the view.3. Sort e.g. plane layers. |
| [Sampler](sceneresources-sampler-i.md) | Sampler interface |
| [SceneResource](sceneresources-sceneresource-i.md) | Define scene resource extended by other 3d resource. |
| [Shader](sceneresources-shader-i.md) | Shader resource. |
| [ShaderMaterial](sceneresources-shadermaterial-i.md) | Shader material resource. |
| [SubMesh](sceneresources-submesh-i.md) | Sub mesh resource. |
| [UnlitMaterial](sceneresources-unlitmaterial-i.md) | Unlit material resource |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [UnlitShadowAlphaMaterial](sceneresources-unlitshadowalphamaterial-i-sys.md) | Unlit shadow alpha material resource |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [CullMode](sceneresources-cullmode-e.md) | The enum of PBR material cull mode. |
| [EnvironmentBackgroundType](sceneresources-environmentbackgroundtype-e.md) | The enum of environment background type. |
| [MaterialType](sceneresources-materialtype-e.md) | The enum of material type. |
| [PolygonMode](sceneresources-polygonmode-e.md) | The enum of polygon mode. |
| [SamplerAddressMode](sceneresources-sampleraddressmode-e.md) | Addressing mode for Sampler |
| [SamplerFilter](sceneresources-samplerfilter-e.md) | Sampler filter Mode |
| [SceneResourceType](sceneresources-sceneresourcetype-e.md) | The enum of SceneResource type. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [MaterialType](sceneresources-materialtype-e-sys.md) | The enum of material type. |
<!--DelEnd-->

