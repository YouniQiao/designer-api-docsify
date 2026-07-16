# SceneResources

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [Animation](arkts-arkgraphics3d-sceneresources-animation-i.md) | Animation resource. |
| [Blend](arkts-arkgraphics3d-sceneresources-blend-i.md) | Blend interface. |
| [Effect](arkts-arkgraphics3d-sceneresources-effect-i.md) | Effect resource. |
| [Environment](arkts-arkgraphics3d-sceneresources-environment-i.md) | Environment resource. |
| [Image](arkts-arkgraphics3d-sceneresources-image-i.md) | Image resource. |
| [ImageStream](arkts-arkgraphics3d-sceneresources-imagestream-i.md) | ImageStream resource. |
| [Material](arkts-arkgraphics3d-sceneresources-material-i.md) | Material resource. |
| [MaterialProperty](arkts-arkgraphics3d-sceneresources-materialproperty-i.md) | Material property interface. |
| [Mesh](arkts-arkgraphics3d-sceneresources-mesh-i.md) | The mesh instance owned by the mesh node |
| [MeshResource](arkts-arkgraphics3d-sceneresources-meshresource-i.md) | The mesh data description resource for the geometry node |
| [MetallicRoughnessMaterial](arkts-arkgraphics3d-sceneresources-metallicroughnessmaterial-i.md) | Physically-based metallic roughness material resource. |
| [Morpher](arkts-arkgraphics3d-sceneresources-morpher-i.md) | Defines Morpher interface for specifying morph targets for Node's geometry. |
| [OcclusionMaterial](arkts-arkgraphics3d-sceneresources-occlusionmaterial-i.md) | Occlusion material resource |
| [RenderSort](arkts-arkgraphics3d-sceneresources-rendersort-i.md) | Render sort Layer. Within a render slot a layer can define a sort layer order.There are 0-63 values available (0 first, 63 last). Default id value is 32.1. Typical use case is to set render sort layer to objects which render with depth test without depth write.2. Typical use case is to always render character and/or camera object first to cull large parts of the view.3. Sort e.g. plane layers. |
| [Sampler](arkts-arkgraphics3d-sceneresources-sampler-i.md) | Sampler interface |
| [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md) | Define scene resource extended by other 3d resource. |
| [Shader](arkts-arkgraphics3d-sceneresources-shader-i.md) | Shader resource. |
| [ShaderMaterial](arkts-arkgraphics3d-sceneresources-shadermaterial-i.md) | Shader material resource. |
| [SubMesh](arkts-arkgraphics3d-sceneresources-submesh-i.md) | Sub mesh resource. |
| [UnlitMaterial](arkts-arkgraphics3d-sceneresources-unlitmaterial-i.md) | Unlit material resource |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [UnlitShadowAlphaMaterial](arkts-arkgraphics3d-sceneresources-unlitshadowalphamaterial-i-sys.md) | Unlit shadow alpha material resource |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [CullMode](arkts-arkgraphics3d-sceneresources-cullmode-e.md) | The enum of PBR material cull mode. |
| [EnvironmentBackgroundType](arkts-arkgraphics3d-sceneresources-environmentbackgroundtype-e.md) | The enum of environment background type. |
| [MaterialType](arkts-arkgraphics3d-sceneresources-materialtype-e.md) | The enum of material type. |
| [PolygonMode](arkts-arkgraphics3d-sceneresources-polygonmode-e.md) | The enum of polygon mode. |
| [SamplerAddressMode](arkts-arkgraphics3d-sceneresources-sampleraddressmode-e.md) | Addressing mode for Sampler |
| [SamplerFilter](arkts-arkgraphics3d-sceneresources-samplerfilter-e.md) | Sampler filter Mode |
| [SceneResourceType](arkts-arkgraphics3d-sceneresources-sceneresourcetype-e.md) | The enum of SceneResource type. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [MaterialType](arkts-arkgraphics3d-sceneresources-materialtype-e-sys.md) | The enum of material type. |
<!--DelEnd-->

