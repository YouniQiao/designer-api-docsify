# Scene

Describes a scene.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## cloneNode

```TypeScript
cloneNode(node: Node, parent: Node, name: string): Node | null
```

Clones a node in the current scene. Cross-scene node cloning is not supported.

**Since:** 23

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
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) \| null |

## createComponent

```TypeScript
createComponent(node: Node, name: string): Promise<SceneComponent>
```

Creates a component and attaches it to a node. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SceneComponent](arkts-arkgraphics3d-scene-scenecomponent-i.md)&gt; |

## destroy

```TypeScript
destroy(): void
```

Destroys this scene and releases all scene resources.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## getComponent

```TypeScript
getComponent(node: Node, name: string): SceneComponent | null
```

Obtains the component instance from a node based on the component name.

**Since:** 20

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SceneComponent](arkts-arkgraphics3d-scene-scenecomponent-i.md) \| null |

## getDefaultRenderContext

```TypeScript
static getDefaultRenderContext(): RenderContext | null
```

Obtains the rendering context associated with the current graphics object.

**Since:** 20

**System capability:** SystemCapability.ArkUi.Graphics3D

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RenderContext](arkts-arkgraphics3d-scene-rendercontext-i.md) \| null |

## getNodeByPath

```TypeScript
getNodeByPath(path: string, type?: NodeType): Node | null
```

Obtains a node by path.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| type | [NodeType](arkts-arkgraphics3d-scenenodes-nodetype-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) \| null |

## getResourceFactory

```TypeScript
getResourceFactory(): SceneResourceFactory
```

Obtains the scene resource factory.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SceneResourceFactory](arkts-arkgraphics3d-scene-sceneresourcefactory-i.md) |

## importNode

```TypeScript
importNode(name: string, node: Node, parent: Node | null): Node
```

Generally used for importing nodes from other scenes.

**Since:** 18

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

Imports another scene into the current one.

**Since:** 18

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

Loads a resource by path. This API uses a promise to return the result.

**Since:** 12

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

Renders frames on demand, such as controlling the frame rate.

**Since:** 15

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

Animation objects in the 3D scene.@return { Animation[] } @readonly

**Type:** [Animation](arkts-arkgraphics3d-sceneresources-animation-i.md)[]

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## environment

```TypeScript
set environment(value: Environment)
```

Environment object.

**Type:** [Environment](arkts-arkgraphics3d-sceneresources-environment-i.md)

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## renderConfiguration

```TypeScript
get renderConfiguration(): RenderConfiguration
```

Rendering configuration.

**Type:** [RenderConfiguration](arkts-arkgraphics3d-scene-renderconfiguration-i.md)

**Since:** 23

**System capability:** SystemCapability.ArkUi.Graphics3D

## root

```TypeScript
get root(): Node | null
```

Root node of the 3D scene tree.@return { Node | null } @readonly

**Type:** [Node](arkts-arkgraphics3d-scenenodes-node-i.md)

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D
