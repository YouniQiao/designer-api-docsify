# BoidsSimPlugin (System API)

Boids simulation plugin, providing static methods for obtaining the boids simulation world.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare class BoidsSimPlugin--><!--Device-unnamed-export declare class BoidsSimPlugin-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## getDefaultBoidsSimWorld

```TypeScript
static getDefaultBoidsSimWorld(scene: Scene): BoidsSimWorld | null
```

Gets the Boids simulation world instance associated with the specified scene.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimPlugin-static getDefaultBoidsSimWorld(scene: Scene): BoidsSimWorld | null--><!--Device-BoidsSimPlugin-static getDefaultBoidsSimWorld(scene: Scene): BoidsSimWorld | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scene | [Scene](arkts-arkgraphics3d-scene-c-sys.md) | Yes | Object of the target scene. |

**Return value:**

| Type | Description |
| --- | --- |
| [BoidsSimWorld](arkts-arkgraphics3d-sceneboidssim-boidssimworld-c-sys.md) | Returns the Boids simulation world instance, or null if it does not exist. |

