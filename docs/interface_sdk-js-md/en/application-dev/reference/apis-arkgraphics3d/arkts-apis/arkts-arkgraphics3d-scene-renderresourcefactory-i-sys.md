# RenderResourceFactory

渲染资源工厂，用于创建可在共享RenderContext的场景间共享的资源。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface RenderResourceFactory--><!--Device-unnamed-export interface RenderResourceFactory-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## createScene

```TypeScript
createScene(uri: ResourceStr, param: SceneLoadParams): Promise<Scene>
```

从SceneLoadParams创建新场景.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderResourceFactory-createScene(uri: ResourceStr, param: SceneLoadParams): Promise<Scene>--><!--Device-RenderResourceFactory-createScene(uri: ResourceStr, param: SceneLoadParams): Promise<Scene>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) | Yes | 创建场景的资源 |
| param | [SceneLoadParams](arkts-arkgraphics3d-scene-sceneloadparams-i-sys.md) | Yes | 场景加载参数 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Scene&gt; | 返回场景的Promise |

