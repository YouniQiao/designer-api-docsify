# Container

定义场景对象的容器。容器提供了一种将场景对象分组到层次结构中的方法。@interface Container

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

## append

```TypeScript
append(item: T): void
```

追加一个对象到容器。如果追加的对象已存在于容器中，容器会先移除该对象再插入，因此数量不会增加。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| item | T | 是 |

**示例**

```TypeScript
import { Scene, Node } from '@kit.ArkGraphics3D';

function append(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let node : Node | null = result.getNodeByPath("rootNode/Scene/");
      if (node) {
        // append 节点，如果node已经在children中，数量不会增加，但操作仍然生效
        result.root?.children.get(0)?.children.append(node);
      }
    }
  }).catch((err: Error) => {
    console.error(`Failed to load scene. Message: ${err.message}`);
  });
}
```

## clear

```TypeScript
clear(): void
```

清空容器内的所有对象。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**示例**

```TypeScript
import { Scene, Node } from '@kit.ArkGraphics3D';

function clear(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let node : Node | null = result.getNodeByPath("rootNode/Scene/");
      if (node) {
        // 清空 node 节点下的所有子节点
        node.children.clear();
      }
    }
  }).catch((err: Error) => {
    console.error(`Failed to load scene. Message: ${err.message}`);
  });
}
```

## count

ArkTS-Dyn:
```TypeScript
count(): number
```

ArkTS-Sta:
```TypeScript
count(): int
```

获取容器中对象的数量。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**示例**

```TypeScript
import { Container, Scene, Node } from '@kit.ArkGraphics3D';

function count(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let node : Node | null = result.getNodeByPath("rootNode_");
      if (node) {
        let container: Container<Node> = node.children;
        // 获取children中的节点数
        let count: number = container.count();
      }
    }
  });
}
```

## get

ArkTS-Dyn:
```TypeScript
get(index: number): T | null
```

ArkTS-Sta:
```TypeScript
get(index: int): T | null
```

获取特定下标对象，获取不到则返回空。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| T \| null |

**示例**

```TypeScript
import { Scene, Node } from '@kit.ArkGraphics3D';

function get(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let node : Node | null = result.getNodeByPath("rootNode/Scene/");
      if (node) {
        // 从children中get 0号节点
        result.root?.children.get(0)?.children.insertAfter(node, null);
      }
    }
  }).catch((err: Error) => {
    console.error(`Failed to load scene. Message: ${err.message}`);
  });
}
```

## insertAfter

```TypeScript
insertAfter(item: T, sibling: T | null): void
```

在兄弟节点后面插入对象。如果插入的对象已存在于容器中，容器会先移除该对象再插入，因此数量不会增加。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| item | T | 是 |
| sibling | T \| null | 是 |

**示例**

```TypeScript
import { Scene, Node } from '@kit.ArkGraphics3D';

function insertAfter(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let node : Node | null = result.getNodeByPath("rootNode/Scene/");
      if (node) {
        // insertAfter 节点，如果node已经在children中，数量不会增加，但操作仍然生效
        result.root?.children.get(0)?.children.insertAfter(node, null);
      }
    }
  }).catch((err: Error) => {
    console.error(`Failed to load scene. Message: ${err.message}`);
  });
}
```

## remove

```TypeScript
remove(item: T): void
```

移除指定对象。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| item | T | 是 |

**示例**

```TypeScript
import { Scene, Node } from '@kit.ArkGraphics3D';

function remove(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let node : Node | null = result.getNodeByPath("rootNode/Scene/");
      if (node) {
        // remove 节点
        result.root?.children.remove(node);
      }
    }
  }).catch((err: Error) => {
    console.error(`Failed to load scene. Message: ${err.message}`);
  });
}
```
