# Scene

Defines the 3d scene.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class Scene--><!--Device-unnamed-export declare class Scene-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## load

```TypeScript
static load(uri: ResourceStr, param: SceneLoadParams):Promise<Scene>
```

Create a new scene from a SceneLoadParams.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Scene-static load(uri: ResourceStr, param: SceneLoadParams):Promise<Scene>--><!--Device-Scene-static load(uri: ResourceStr, param: SceneLoadParams):Promise<Scene>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) | Yes | the resource of creating a scene |
| param | [SceneLoadParams](arkts-arkgraphics3d-scene-sceneloadparams-i-sys.md) | Yes | the params for scene load |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Scene](arkts-arkgraphics3d-scene-c-sys.md)&gt; | Promise used to return a scene |

