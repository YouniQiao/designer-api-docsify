# LayerMask

Defines the layer mask of a node.

**Since:** 23

<!--Device-unnamed-export interface LayerMask--><!--Device-unnamed-export interface LayerMask-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## getEnabled

```TypeScript
getEnabled(index: int): boolean
```

Checks whether the mask is enabled for a layer of a given index.

**Since:** 23

<!--Device-LayerMask-getEnabled(index: int): boolean--><!--Device-LayerMask-getEnabled(index: int): boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Index of the layer. The value is an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for whether the layer mask is enabled. true if enabled, false otherwise. |

**Examples**

```TypeScript
import { Scene, Node } from '@kit.ArkGraphics3D';

function layerMask(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let node : Node | null = result.getNodeByPath("rootNode_");
      if (node) {
          // Obtain the enabled status of the mask.
          let enabled: boolean = node.layerMask.getEnabled(1);
      }
    }
  }).catch((error: Error) => {
    console.error('Scene load failed:', error);
  });
}
```

## setEnabled

```TypeScript
setEnabled(index: int, enabled: boolean): void
```

Enables the mask of a layer of a given index.

**Since:** 23

<!--Device-LayerMask-setEnabled(index: int, enabled: boolean): void--><!--Device-LayerMask-setEnabled(index: int, enabled: boolean): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Index of the layer. The value is an integer greater than or equal to 0. |
| enabled | boolean | Yes | Whether to enable the layer mask. true to enable, false otherwise. |

**Examples**

```TypeScript
import { Scene, Node } from '@kit.ArkGraphics3D';

function layerMask(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let node : Node | null = result.getNodeByPath("rootNode/Scene/");
      if (node) {
          // Set the enabled status of the mask.
          node.layerMask.setEnabled(1, true);
      }
    }
  }).catch((error: Error) => {
    console.error('Scene load failed:', error);
  });
}
```

