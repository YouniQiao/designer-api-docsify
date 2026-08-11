# Scene

Defines the 3d scene.

**Since:** 12

<!--Device-unnamed-export declare class Scene--><!--Device-unnamed-export declare class Scene-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## cloneNode

```TypeScript
cloneNode(node: Node, parent: Node, name: string): Node | null
```

Clones a node in the current scene. Cross-scene node cloning is not supported.

**Since:** 23

<!--Device-Scene-cloneNode(node: Node, parent: Node, name: string): Node | null--><!--Device-Scene-cloneNode(node: Node, parent: Node, name: string): Node | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes |
| parent | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) |

## createComponent

```TypeScript
createComponent(node: Node, name: string): Promise<SceneComponent>
```

Create a new component.

**Since:** 20

<!--Device-Scene-createComponent(node: Node, name: string): Promise<SceneComponent>--><!--Device-Scene-createComponent(node: Node, name: string): Promise<SceneComponent>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;SceneComponent&gt; |

## destroy

```TypeScript
destroy(): void
```

Destroys this scene and releases all scene resources.

**Since:** 12

<!--Device-Scene-destroy(): void--><!--Device-Scene-destroy(): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## getComponent

```TypeScript
getComponent(node: Node, name: string): SceneComponent | null
```

Obtains the component instance from a node based on the component name.

**Since:** 20

<!--Device-Scene-getComponent(node: Node, name: string): SceneComponent | null--><!--Device-Scene-getComponent(node: Node, name: string): SceneComponent | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SceneComponent](arkts-arkgraphics3d-scene-scenecomponent-i.md) |

## getDefaultRenderContext

```TypeScript
static getDefaultRenderContext(): RenderContext | null
```

Get default render context

**Since:** 20

<!--Device-Scene-static getDefaultRenderContext(): RenderContext | null--><!--Device-Scene-static getDefaultRenderContext(): RenderContext | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RenderContext](arkts-arkgraphics3d-scene-rendercontext-i.md) |

## getNodeByPath

```TypeScript
getNodeByPath(path: string, type?: NodeType): Node | null
```

Obtains a node by path.

**Since:** 12

<!--Device-Scene-getNodeByPath(path: string, type?: NodeType): Node | null--><!--Device-Scene-getNodeByPath(path: string, type?: NodeType): Node | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| type | [NodeType](arkts-arkgraphics3d-scenenodes-nodetype-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) |

## getResourceFactory

```TypeScript
getResourceFactory(): SceneResourceFactory
```

Obtains the scene resource factory.

**Since:** 12

<!--Device-Scene-getResourceFactory(): SceneResourceFactory--><!--Device-Scene-getResourceFactory(): SceneResourceFactory-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SceneResourceFactory](arkts-arkgraphics3d-scene-sceneresourcefactory-i.md) |

## importNode

```TypeScript
importNode(name: string, node: Node, parent: Node | null): Node
```

Import node into the scene. The original node may come from separate Scene.The node will be cloned and any modifications to the old node will not be visible after the import.

**Since:** 18

<!--Device-Scene-importNode(name: string, node: Node, parent: Node | null): Node--><!--Device-Scene-importNode(name: string, node: Node, parent: Node | null): Node-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes |
| parent | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) |

## importScene

```TypeScript
importScene(name: string, scene: Scene, parent: Node | null): Node
```

Import scene into the scene as a node. The node hierarchy will appear under the parent node.All animations from the scene will be duplicated in the scene.

**Since:** 18

<!--Device-Scene-importScene(name: string, scene: Scene, parent: Node | null): Node--><!--Device-Scene-importScene(name: string, scene: Scene, parent: Node | null): Node-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| scene | [Scene](arkts-arkgraphics3d-scene-c.md) | Yes |
| parent | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) |

## load

```TypeScript
static load(uri? : ResourceStr): Promise<Scene>
```

Loads a resource by path.This API uses a promise to return the result.

**Since:** 12

<!--Device-Scene-static load(uri? : ResourceStr): Promise<Scene>--><!--Device-Scene-static load(uri? : ResourceStr): Promise<Scene>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Scene](arkts-arkgraphics3d-scene-c.md)&gt; |

## renderFrame

```TypeScript
renderFrame(params?: RenderParameters): boolean
```

A new frame is rendered for all active camera.

**Since:** 15

<!--Device-Scene-renderFrame(params?: RenderParameters): boolean--><!--Device-Scene-renderFrame(params?: RenderParameters): boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [RenderParameters](arkts-arkgraphics3d-scene-renderparameters-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## animations

```TypeScript
get animations(): Animation[]
```

The animations of the scene.

**Type:** [Animation](arkts-arkgraphics3d-sceneresources-animation-i.md)[]

**Since:** 12

<!--Device-Scene-get animations(): Animation[]--><!--Device-Scene-get animations(): Animation[]-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## environment

```TypeScript
set environment(value: Environment)
```

The environment of the scene.

**Type:** [Environment](arkts-arkgraphics3d-sceneresources-environment-i.md)

**Since:** 12

<!--Device-Scene-set environment(value: Environment)--><!--Device-Scene-set environment(value: Environment)-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## renderConfiguration

```TypeScript
get renderConfiguration(): RenderConfiguration
```

render configuration settings

**Type:** [RenderConfiguration](arkts-arkgraphics3d-scene-renderconfiguration-i.md)

**Since:** 23

<!--Device-Scene-get renderConfiguration(): RenderConfiguration--><!--Device-Scene-get renderConfiguration(): RenderConfiguration-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## root

```TypeScript
get root(): Node | null
```

The root node of the scene.

**Type:** [Node](arkts-arkgraphics3d-scenenodes-node-i.md)

**Since:** 12

<!--Device-Scene-get root(): Node | null--><!--Device-Scene-get root(): Node | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D
