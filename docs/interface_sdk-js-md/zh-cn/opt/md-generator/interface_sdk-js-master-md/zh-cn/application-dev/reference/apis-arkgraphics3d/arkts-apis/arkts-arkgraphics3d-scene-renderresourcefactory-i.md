# RenderResourceFactory

渲染资源工厂，用于创建可在共享RenderContext的场景间共享的资源。

**起始版本：** 20

<!--Device-unnamed-export interface RenderResourceFactory--><!--Device-unnamed-export interface RenderResourceFactory-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## createImage

```TypeScript
createImage(params: SceneResourceParameters): Promise<Image>
```

创建图像.

**起始版本：** 20

<!--Device-RenderResourceFactory-createImage(params: SceneResourceParameters): Promise<Image>--><!--Device-RenderResourceFactory-createImage(params: SceneResourceParameters): Promise<Image>-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [SceneResourceParameters](arkts-arkgraphics3d-scene-sceneresourceparameters-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Image](arkts-arkgraphics3d-sceneresources-image-i.md)&gt; |

## createImageStream

```TypeScript
createImageStream(params: SceneResourceParameters): Promise<ImageStream>
```

创建图像流.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RenderResourceFactory-createImageStream(params: SceneResourceParameters): Promise<ImageStream>--><!--Device-RenderResourceFactory-createImageStream(params: SceneResourceParameters): Promise<ImageStream>-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [SceneResourceParameters](arkts-arkgraphics3d-scene-sceneresourceparameters-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ImageStream](arkts-arkgraphics3d-sceneresources-imagestream-i.md)&gt; |

## createMesh

```TypeScript
createMesh(params: SceneResourceParameters, geometry: GeometryDefinition): Promise<MeshResource>
```

从顶点数组创建网格.

**起始版本：** 20

<!--Device-RenderResourceFactory-createMesh(params: SceneResourceParameters, geometry: GeometryDefinition): Promise<MeshResource>--><!--Device-RenderResourceFactory-createMesh(params: SceneResourceParameters, geometry: GeometryDefinition): Promise<MeshResource>-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [SceneResourceParameters](arkts-arkgraphics3d-scene-sceneresourceparameters-i.md) | 是 |
| geometry | [GeometryDefinition](arkts-arkgraphics3d-scenetypes-geometrydefinition-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[MeshResource](arkts-arkgraphics3d-sceneresources-meshresource-i.md)&gt; |

## createSampler

```TypeScript
createSampler(params:SceneResourceParameters): Promise<Sampler>
```

创建采样器.

**起始版本：** 20

<!--Device-RenderResourceFactory-createSampler(params:SceneResourceParameters): Promise<Sampler>--><!--Device-RenderResourceFactory-createSampler(params:SceneResourceParameters): Promise<Sampler>-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [SceneResourceParameters](arkts-arkgraphics3d-scene-sceneresourceparameters-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Sampler](arkts-arkgraphics3d-sceneresources-sampler-i.md)&gt; |

## createScene

```TypeScript
createScene(uri?: ResourceStr): Promise<Scene>
```

从指定的资源URI创建一个新的场景。如果不指定URI，则创建一个空场景，使用Promise异步回调。

**起始版本：** 20

<!--Device-RenderResourceFactory-createScene(uri?: ResourceStr): Promise<Scene>--><!--Device-RenderResourceFactory-createScene(uri?: ResourceStr): Promise<Scene>-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Scene&gt; |

## createShader

```TypeScript
createShader(params: SceneResourceParameters): Promise<Shader>
```

创建着色器.

**起始版本：** 20

<!--Device-RenderResourceFactory-createShader(params: SceneResourceParameters): Promise<Shader>--><!--Device-RenderResourceFactory-createShader(params: SceneResourceParameters): Promise<Shader>-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [SceneResourceParameters](arkts-arkgraphics3d-scene-sceneresourceparameters-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Shader](arkts-arkgraphics3d-sceneresources-shader-i.md)&gt; |
