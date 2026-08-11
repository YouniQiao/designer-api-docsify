# Scene

定义3D场景.

**起始版本：** 12

<!--Device-unnamed-export declare class Scene--><!--Device-unnamed-export declare class Scene-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## cloneNode

```TypeScript
cloneNode(node: Node, parent: Node, name: string): Node | null
```

克隆以输入节点为根节点的节点或子树

**起始版本：** 23

<!--Device-Scene-cloneNode(node: Node, parent: Node, name: string): Node | null--><!--Device-Scene-cloneNode(node: Node, parent: Node, name: string): Node | null-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | 是 |
| parent | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | 是 |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) |

## createComponent

```TypeScript
createComponent(node: Node, name: string): Promise<SceneComponent>
```

创建新组件.

**起始版本：** 20

<!--Device-Scene-createComponent(node: Node, name: string): Promise<SceneComponent>--><!--Device-Scene-createComponent(node: Node, name: string): Promise<SceneComponent>-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | 是 |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;SceneComponent&gt; |

## destroy

```TypeScript
destroy(): void
```

释放所有原生场景资源. 所有TS引用将变为undefined.

**起始版本：** 12

<!--Device-Scene-destroy(): void--><!--Device-Scene-destroy(): void-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## getComponent

```TypeScript
getComponent(node: Node, name: string): SceneComponent | null
```

通过名称获取组件.

**起始版本：** 20

<!--Device-Scene-getComponent(node: Node, name: string): SceneComponent | null--><!--Device-Scene-getComponent(node: Node, name: string): SceneComponent | null-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | 是 |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| [SceneComponent](arkts-arkgraphics3d-scene-scenecomponent-i.md) |

## getDefaultRenderContext

```TypeScript
static getDefaultRenderContext(): RenderContext | null
```

获取默认渲染上下文

**起始版本：** 20

<!--Device-Scene-static getDefaultRenderContext(): RenderContext | null--><!--Device-Scene-static getDefaultRenderContext(): RenderContext | null-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

| 类型 |
| --- |
| [RenderContext](arkts-arkgraphics3d-scene-rendercontext-i.md) |

## getNodeByPath

```TypeScript
getNodeByPath(path: string, type?: NodeType): Node | null
```

通过路径获取节点.

**起始版本：** 12

<!--Device-Scene-getNodeByPath(path: string, type?: NodeType): Node | null--><!--Device-Scene-getNodeByPath(path: string, type?: NodeType): Node | null-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| type | [NodeType](arkts-arkgraphics3d-scenenodes-nodetype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) |

## getResourceFactory

```TypeScript
getResourceFactory(): SceneResourceFactory
```

获取资源工厂.

**起始版本：** 12

<!--Device-Scene-getResourceFactory(): SceneResourceFactory--><!--Device-Scene-getResourceFactory(): SceneResourceFactory-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

| 类型 |
| --- |
| [SceneResourceFactory](arkts-arkgraphics3d-scene-sceneresourcefactory-i.md) |

## importNode

```TypeScript
importNode(name: string, node: Node, parent: Node | null): Node
```

将节点导入场景. 原始节点可能来自另一个场景.节点将被克隆，导入后对旧节点的修改将不可见.

**起始版本：** 18

<!--Device-Scene-importNode(name: string, node: Node, parent: Node | null): Node--><!--Device-Scene-importNode(name: string, node: Node, parent: Node | null): Node-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | 是 |
| parent | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) \| null | 是 |

**返回值：**

| 类型 |
| --- |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) |

## importScene

```TypeScript
importScene(name: string, scene: Scene, parent: Node | null): Node
```

将场景作为节点导入场景. 节点层级将出现在父节点下.场景中的所有动画将被复制.

**起始版本：** 18

<!--Device-Scene-importScene(name: string, scene: Scene, parent: Node | null): Node--><!--Device-Scene-importScene(name: string, scene: Scene, parent: Node | null): Node-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| scene | [Scene](arkts-arkgraphics3d-scene-c.md) | 是 |
| parent | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) \| null | 是 |

**返回值：**

| 类型 |
| --- |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) |

## load

```TypeScript
static load(uri? : ResourceStr): Promise<Scene>
```

通过传入的资源路径加载资源，使用Promise异步回调。调用后，应该在Scene使用完毕时调用[destroy](arkts-arkgraphics3d-scene-c.md#destroy)释放资源，否则可能导致资源泄漏。

**起始版本：** 12

<!--Device-Scene-static load(uri? : ResourceStr): Promise<Scene>--><!--Device-Scene-static load(uri? : ResourceStr): Promise<Scene>-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Scene](arkts-arkgraphics3d-scene-c.md)&gt; |

## renderFrame

```TypeScript
renderFrame(params?: RenderParameters): boolean
```

为所有活动相机渲染新帧.

**起始版本：** 15

<!--Device-Scene-renderFrame(params?: RenderParameters): boolean--><!--Device-Scene-renderFrame(params?: RenderParameters): boolean-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [RenderParameters](arkts-arkgraphics3d-scene-renderparameters-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

## animations

```TypeScript
get animations(): Animation[]
```

场景的动画.

**类型：** [Animation](arkts-arkgraphics3d-sceneresources-animation-i.md)[]

**起始版本：** 12

<!--Device-Scene-get animations(): Animation[]--><!--Device-Scene-get animations(): Animation[]-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## environment

```TypeScript
set environment(value: Environment)
```

场景的环境.

**类型：** [Environment](arkts-arkgraphics3d-sceneresources-environment-i.md)

**起始版本：** 12

<!--Device-Scene-set environment(value: Environment)--><!--Device-Scene-set environment(value: Environment)-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## renderConfiguration

```TypeScript
get renderConfiguration(): RenderConfiguration
```

渲染配置设置

**类型：** [RenderConfiguration](arkts-arkgraphics3d-scene-renderconfiguration-i.md)

**起始版本：** 23

<!--Device-Scene-get renderConfiguration(): RenderConfiguration--><!--Device-Scene-get renderConfiguration(): RenderConfiguration-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## root

```TypeScript
get root(): Node | null
```

场景的根节点.

**类型：** [Node](arkts-arkgraphics3d-scenenodes-node-i.md)

**起始版本：** 12

<!--Device-Scene-get root(): Node | null--><!--Device-Scene-get root(): Node | null-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D
