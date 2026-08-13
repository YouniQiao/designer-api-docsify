# LayerMask

Defines the layer mask of the node.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-export interface LayerMask--><!--Device-unnamed-export interface LayerMask-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## getEnabled

```TypeScript
getEnabled(index: number): boolean
```

Checks whether the mask is enabled for a layer of a given index.

**Since:** 23

**Deprecated since:** -1

<!--Device-LayerMask-getEnabled(index: int): boolean--><!--Device-LayerMask-getEnabled(index: int): boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { Scene, Node } from '@kit.ArkGraphics3D';

function layerMask(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let node : Node | null = result.getNodeByPath("rootNode_");
      if (node) {
          // Obtain the enabling status of the mask. You can perform subsequent processing on the return value based on service requirements.
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
setEnabled(index: number, enabled: boolean): void
```

Enables the mask of a layer of a given index.

**Since:** 23

**Deprecated since:** -1

<!--Device-LayerMask-setEnabled(index: int, enabled: boolean): void--><!--Device-LayerMask-setEnabled(index: int, enabled: boolean): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| enabled | boolean | Yes |

## Examples

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
