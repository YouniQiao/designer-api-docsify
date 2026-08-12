# Scene

Defines the 3d scene.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class Scene--><!--Device-unnamed-export declare class Scene-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## cloneNode

```TypeScript
cloneNode(node: Node, parent: Node, name: string): Node | null
```

Clones a node in the current scene. Cross-scene node cloning is not supported.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Scene-cloneNode(node: Node, parent: Node, name: string): Node | null--><!--Device-Scene-cloneNode(node: Node, parent: Node, name: string): Node | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | Node to be cloned. |
| parent | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | Target parent node of the cloned node in the current scene. The cloned node and the target parent node must belong to the same scene. |
| name | string | Yes | Name of the cloned node, which can be customized and has no special requirements. |

**Return value:**

| Type | Description |
| --- | --- |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Returns the cloned node. If the operation fails, null is returned. |

## Examples

```TypeScript
import { Scene, Node } from '@kit.ArkGraphics3D';

function CloneNode() {
  Scene.load().then(async (result: Scene | undefined) => {
    if (!result) {
      return;
    }
    // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
    Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"))
      .then(async (extScene: Scene) => {
        let extNode: Node | null = extScene.getNodeByPath("rootNode_/Unnamed Node 1/AnimatedCube");
        console.info("test cloneNode");
        let clone: Node | null = result.cloneNode(extNode, result.root, "scene");
        if (clone) {
          clone.position.x = 5;
        }
      });
  });
}
```

## createComponent

```TypeScript
createComponent(node: Node, name: string): Promise<SceneComponent>
```

Create a new component.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Scene-createComponent(node: Node, name: string): Promise<SceneComponent>--><!--Device-Scene-createComponent(node: Node, name: string): Promise<SceneComponent>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | The node the component is attached to |
| name | string | Yes | The name of the component to load. Valid names are defined by each plugin. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[SceneComponent](arkts-arkgraphics3d-scene-scenecomponent-i.md)&gt; | The newly added component. |

## Examples

```TypeScript
import { Scene, SceneComponent } from '@kit.ArkGraphics3D';

function createComponentTest(): Promise<SceneComponent> {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  return Scene.load($rawfile("gltf/DamagedHelmet/glTF/DamagedHelmet.glb"))
    .then(scene => {
      if (!scene) {
        return Promise.reject(new Error("Scene load failed"));
      }
      // RenderConfigurationComponent is an internal component of the engine. You do not need to install plugins when creating the component.
      return scene.createComponent(scene.root, "RenderConfigurationComponent");
    })
    .then(component => {
      if (!component) {
        return Promise.reject(new Error("createComponent failed"));
      }
      return component;
    });
}
```

## destroy

```TypeScript
destroy(): void
```

Destroys this scene and releases all scene resources.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Scene-destroy(): void--><!--Device-Scene-destroy(): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## Examples

```TypeScript
import { Scene } from '@kit.ArkGraphics3D';

function destroy(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
         // Destroy the scene.
        result.destroy();
    }
  });
}
```

## getComponent

```TypeScript
getComponent(node: Node, name: string): SceneComponent | null
```

Obtains the component instance from a node based on the component name.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Scene-getComponent(node: Node, name: string): SceneComponent | null--><!--Device-Scene-getComponent(node: Node, name: string): SceneComponent | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | Node to which the component is attached. |
| name | string | Yes | Name of the component to obtain. The value must be a system predefined or registered custom component name, and follow the naming conventions. |

**Return value:**

| Type | Description |
| --- | --- |
| [SceneComponent](arkts-arkgraphics3d-scene-scenecomponent-i.md) | SceneComponent object corresponding to the given name, or null if not found. |

## Examples

```TypeScript
import { Scene } from '@kit.ArkGraphics3D';

function getComponentTest() {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  Scene.load($rawfile("gltf/DamagedHelmet/glTF/DamagedHelmet.glb"))
    .then(async (result: Scene | undefined) => {
      if (!result) {
        console.error("Scene load failed");
        return;
      }
      console.info("TEST getComponentTest");
      let component = result.getComponent(result.root, "myComponent");
      if (component) {
        console.info("getComponent success");
      } else {
        console.warn("Component not found");
      }
    });
}
```

## getDefaultRenderContext

```TypeScript
static getDefaultRenderContext(): RenderContext | null
```

Get default render context

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Scene-static getDefaultRenderContext(): RenderContext | null--><!--Device-Scene-static getDefaultRenderContext(): RenderContext | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Return value:**

| Type | Description |
| --- | --- |
| [RenderContext](arkts-arkgraphics3d-scene-rendercontext-i.md) | The default RenderContext instance |

## Examples

```TypeScript
import { Scene, RenderContext } from '@kit.ArkGraphics3D';

function getDefaultRenderContextTest() {
  console.info("TEST getDefaultRenderContextTest");
  const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
  if (renderContext) {
    console.info("getDefaultRenderContext success");
  } else {
    console.error("RenderContext is null");
  }
}
```

## getNodeByPath

```TypeScript
getNodeByPath(path: string, type?: NodeType): Node | null
```

Obtains a node by path.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Scene-getNodeByPath(path: string, type?: NodeType): Node | null--><!--Device-Scene-getNodeByPath(path: string, type?: NodeType): Node | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Path in the scene node tree. Each layer is separated by a slash (/). |
| type | [NodeType](arkts-arkgraphics3d-scenenodes-nodetype-e.md) | No | Expected type of the node to be returned. The default value is null. |

**Return value:**

| Type | Description |
| --- | --- |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Returns the instance of the requested node. Returns null if not found or if the type of the found node does not match the passed parameter. |

## Examples

```TypeScript
import { Scene, Node } from '@kit.ArkGraphics3D';

function getNode(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
         // Search for a node in the specified path.
        let node : Node | null = result.getNodeByPath("rootNode_");
    }
  });
}
```

## getResourceFactory

```TypeScript
getResourceFactory(): SceneResourceFactory
```

Obtains the scene resource factory.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Scene-getResourceFactory(): SceneResourceFactory--><!--Device-Scene-getResourceFactory(): SceneResourceFactory-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Return value:**

| Type | Description |
| --- | --- |
| [SceneResourceFactory](arkts-arkgraphics3d-scene-sceneresourcefactory-i.md) | Scene resource factory. |

## Examples

```TypeScript
import { SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

function getFactory(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
         // Obtain a SceneResourceFactory object.
        let sceneFactory: SceneResourceFactory = result.getResourceFactory();
    }
  });
}
```

## importNode

```TypeScript
importNode(name: string, node: Node, parent: Node | null): Node
```

Import node into the scene. The original node may come from separate Scene.The node will be cloned and any modifications to the old node will not be visible after the import.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-Scene-importNode(name: string, node: Node, parent: Node | null): Node--><!--Device-Scene-importNode(name: string, node: Node, parent: Node | null): Node-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | The name of the newly created node. |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | The node to be imported. |
| parent | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) \| null | Yes | The parent node or null for root |

**Return value:**

| Type | Description |
| --- | --- |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | The newly created node. |

## Examples

```TypeScript
import { Scene } from '@kit.ArkGraphics3D';

function ImportNodeTest() {
  Scene.load().then(async (result: Scene | undefined) => {
    if (!result) {
      return;
    }
    // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
    Scene.load($rawfile("gltf/AnimatedCube/glTF/AnimatedCube.glb"))
      .then(async (extScene: Scene) => {
        let extNode = extScene.getNodeByPath("rootNode_/Unnamed Node 1/AnimatedCube");
        console.info("TEST ImportNodeTest");
        let node = result.importNode("scene", extNode, result.root);
        if (node) {
          node.position.x = 5;
        }
      });
  });
}
```

## importScene

```TypeScript
importScene(name: string, scene: Scene, parent: Node | null): Node
```

Import scene into the scene as a node. The node hierarchy will appear under the parent node.All animations from the scene will be duplicated in the scene.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-Scene-importScene(name: string, scene: Scene, parent: Node | null): Node--><!--Device-Scene-importScene(name: string, scene: Scene, parent: Node | null): Node-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | The name of the newly created node |
| scene | [Scene](arkts-arkgraphics3d-scene-c.md) | Yes | The scene to be imported. |
| parent | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) \| null | Yes | The parent node or null for root |

**Return value:**

| Type | Description |
| --- | --- |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | The newly created node. |

## Examples

```TypeScript
import { Scene } from '@kit.ArkGraphics3D';

function ImportSceneTest() {
  Scene.load().then(async (result: Scene | undefined) => {
    if (!result) {
      return;
    }
    // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
    let content = await result.getResourceFactory().createScene($rawfile("gltf/DamagedHelmet/glTF/DamagedHelmet.glb"))
    console.info("TEST ImportSceneTest");
    result.importScene("helmet", content, null);
  });
}
```

## load

```TypeScript
static load(uri? : ResourceStr): Promise<Scene>
```

Loads a resource by path.This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Scene-static load(uri? : ResourceStr): Promise<Scene>--><!--Device-Scene-static load(uri? : ResourceStr): Promise<Scene>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | ResourceStr | No | Path of the model file resource to load. The default value is undefined. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Scene](arkts-arkgraphics3d-scene-c.md)&gt; | Promise used to return the Scene object created. |

## Examples

Example 1: Load resources via rawfile (a relative path).

```TypeScript
import { Scene } from '@kit.ArkGraphics3D';

function loadModel(): void {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {});
}
```

Example 2: Load via an absolute path (from /data/storage/el2/base/files in the application sandbox directory).

```TypeScript
import { common } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';
import { Scene } from '@kit.ArkGraphics3D';

async loadModelFromAbsolutePath(): Promise<void> {
  // Obtain the application sandbox directory. (Scene.load can read only files written by the application itself, not files written by hdc/adb push.)
  const uiCtx = this.getUIContext().getHostContext() as common.UIAbilityContext;
  const appCtx = uiCtx.getApplicationContext();
  const filesDir = appCtx.filesDir; // /data/storage/el2/base/files

  // Read the model content from rawfile. (In practice, you can replace rawfile with data from other sources.)
  // Use a .glb file for easier copying and loading. If the file is in.gltf format, copy its .bin file and texture files to the same directory.
  const src = 'gltf/CubeWithFloor/glTF/AnimatedCube.glb';
  const load_uri = `${filesDir}/AnimatedCube.glb`;

  // Write the model file to the application sandbox directory to create a file accessible by Scene.load (absolute path).
  const rawData = await uiCtx.resourceManager.getRawFileContent(src);
  const file = fileIo.openSync(load_uri, fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC | fileIo.OpenMode.WRITE_ONLY);
  fileIo.writeSync(file.fd, rawData.buffer.slice(rawData.byteOffset, rawData.byteOffset + rawData.byteLength));
  fileIo.closeSync(file);

  // Load the model using the absolute path.
  Scene.load(load_uri).then((scene: Scene) => {
    // Handle the loaded scene.
  }).catch((error: string) => {
    console.error('Scene load failed: ' + error);
  });
}
```

## renderFrame

```TypeScript
renderFrame(params?: RenderParameters): boolean
```

A new frame is rendered for all active camera.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-Scene-renderFrame(params?: RenderParameters): boolean--><!--Device-Scene-renderFrame(params?: RenderParameters): boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [RenderParameters](arkts-arkgraphics3d-scene-renderparameters-i.md) | No | Rendering parameters |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if rendering was scheduled, false otherwise |

## Examples

```TypeScript
import { Scene } from '@kit.ArkGraphics3D';

function RenderFrameTest() {
  // Load scene resources, which supports .gltf and .glb formats. The path and file name can be customized based on the specific project resources.
  Scene.load($rawfile("gltf/DamagedHelmet/glTF/DamagedHelmet.glb"))
    .then(async (result: Scene | undefined) => {
      if (!result) {
        return;
      }
      console.info("TEST RenderFrameTest");
      result.renderFrame({ alwaysRender: true });
  });
}
```

## animations

```TypeScript
get animations(): Animation[]
```

The animations of the scene.

**Type:** [Animation](arkts-arkgraphics3d-sceneresources-animation-i.md)[]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Scene-get animations(): Animation[]--><!--Device-Scene-get animations(): Animation[]-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## environment

```TypeScript
set environment(value: Environment)
```

The environment of the scene.

**Type:** [Environment](arkts-arkgraphics3d-sceneresources-environment-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Scene-set environment(value: Environment)--><!--Device-Scene-set environment(value: Environment)-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## renderConfiguration

```TypeScript
get renderConfiguration(): RenderConfiguration
```

render configuration settings

**Type:** [RenderConfiguration](arkts-arkgraphics3d-scene-renderconfiguration-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Scene-get renderConfiguration(): RenderConfiguration--><!--Device-Scene-get renderConfiguration(): RenderConfiguration-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## root

```TypeScript
get root(): Node | null
```

The root node of the scene.

**Type:** [Node](arkts-arkgraphics3d-scenenodes-node-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Scene-get root(): Node | null--><!--Device-Scene-get root(): Node | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

