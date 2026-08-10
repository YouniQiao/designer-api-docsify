# BoidsSimPlugin (System API)

群组模拟插件. 提供用于管理群组模拟组件的静态方法.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare class BoidsSimPlugin--><!--Device-unnamed-export declare class BoidsSimPlugin-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## getDefaultBoidsSimWorld

```TypeScript
static getDefaultBoidsSimWorld(scene: Scene): BoidsSimWorld | null
```

获取指定场景的默认群组模拟世界.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimPlugin-static getDefaultBoidsSimWorld(scene: Scene): BoidsSimWorld | null--><!--Device-BoidsSimPlugin-static getDefaultBoidsSimWorld(scene: Scene): BoidsSimWorld | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scene | [Scene](arkts-arkgraphics3d-scene-c-sys.md) | Yes | 要获取群组模拟世界的场景 |

**Return value:**

| Type | Description |
| --- | --- |
| [BoidsSimWorld](arkts-arkgraphics3d-sceneboidssim-boidssimworld-c-sys.md) | 返回群组模拟世界实例，若不存在则返回null。 |

