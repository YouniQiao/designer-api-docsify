# Container

Container for defining scene nodes. It provides a way to group scene nodes into a hierarchy.@interface Container

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## append

```TypeScript
append(item: T): void
```

Appends a node to the container.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | T | Yes | Object of the T type. |

**Examples**

```TypeScript
import { Scene, Node } from '@kit.ArkGraphics3D';

function append(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let node : Node | null = result.getNodeByPath("rootNode/Scene/");
      if (node) {
        // Append a node. If the node is already in the children list, the total count does not change, but the operation is successful.
        result.root?.children.get(0)?.children.append(node);
      }
    }
  }).catch((error: Error) => {
    console.error('Scene load failed:', error);
  });
}
```

## clear

```TypeScript
clear(): void
```

Clears all nodes in the container.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

**Examples**

```TypeScript
import { Scene, Node } from '@kit.ArkGraphics3D';

function clear(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let node : Node | null = result.getNodeByPath("rootNode/Scene/");
      if (node) {
        //Clear all child nodes of the node.
        node.children.clear();
      }
    }
  }).catch((error: Error) => {
    console.error('Scene load failed:', error);
  });
}
```

## count

```TypeScript
count(): number
```

Obtains the number of nodes in the container.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

**Return value:**

| Type | Description |
| --- | --- |
| number | Number of nodes in the container. The value is a non-negative integer. |

**Examples**

```TypeScript
import { Container, Scene, Node } from '@kit.ArkGraphics3D';

function count(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let node : Node | null = result.getNodeByPath("rootNode_");
      if (node) {
        let container: Container<Node> = node.children;
        // Obtain the number of nodes in children.
        let count: number = container.count();
      }
    }
  });
}
```

## get

```TypeScript
get(index: number): T | null
```

Obtains a node of a given index. If no node is obtained, null is returned.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | Index of the node. The value is an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| T \| null | Object obtained. If no object is obtained, null is returned. |

**Examples**

```TypeScript
import { Scene, Node } from '@kit.ArkGraphics3D';

function get(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let node : Node | null = result.getNodeByPath("rootNode/Scene/");
      // Get node 0 from children.
      result.root?.children.get(0)?.children.insertAfter(node, null);
    }
  }).catch((error: Error) => {
    console.error('Scene load failed:', error);
  });
}
```

## insertAfter

```TypeScript
insertAfter(item: T, sibling: T | null): void
```

Inserts the object after the sibling node.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | T | Yes | Node to be inserted. |
| sibling | T \| null | Yes | Sibling node. |

**Examples**

```TypeScript
import { Scene, Node } from '@kit.ArkGraphics3D';

function insertAfter(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let node : Node | null = result.getNodeByPath("rootNode/Scene/");
      if (node) {
        // Insert a node after another. If the node is already in the children list, the total count does not change, but the operation is successful.
        result.root?.children.get(0)?.children.insertAfter(node, null);
      }
    }
  }).catch((error: Error) => {
    console.error('Scene load failed:', error);
  });
}
```

## remove

```TypeScript
remove(item: T): void
```

Removes a node.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | T | Yes | Node to remove. |

**Examples**

```TypeScript
import { Scene, Node } from '@kit.ArkGraphics3D';

function remove(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let node : Node | null = result.getNodeByPath("rootNode/Scene/");
      if (node) {
        // Call remove to remove a node.
        result.root?.children.remove(node);
      }
    }
  }).catch((error: Error) => {
    console.error('Scene load failed:', error);
  });
}
```
