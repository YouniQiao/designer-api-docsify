# Scene

用于设置场景。Scene采用树状层次结构组织场景节点，根节点（root）作为场景的入口。

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## cloneNode

```TypeScript
cloneNode(node: Node, parent: Node, name: string): Node | null
```

在当前所在场景中克隆节点，不支持跨场景克隆节点。

**起始版本：** 23

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
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) \| null |

## createComponent

```TypeScript
createComponent(node: Node, name: string): Promise<SceneComponent>
```

在指定节点上创建新的组件，根据组件名称异步创建并附加到节点上，使用Promise异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | 是 |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SceneComponent](arkts-arkgraphics3d-scene-scenecomponent-i.md)&gt; |

## destroy

```TypeScript
destroy(): void
```

销毁场景，释放所有的场景资源。

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## getComponent

```TypeScript
getComponent(node: Node, name: string): SceneComponent | null
```

根据指定的组件名称，从给定节点上获取对应的组件实例。

**起始版本：** 20

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | 是 |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| [SceneComponent](arkts-arkgraphics3d-scene-scenecomponent-i.md) \| null |

## getDefaultRenderContext

```TypeScript
static getDefaultRenderContext(): RenderContext | null
```

获取当前图形对象所关联的渲染上下文。

**起始版本：** 20

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

| 类型 |
| --- |
| [RenderContext](arkts-arkgraphics3d-scene-rendercontext-i.md) \| null |

## getNodeByPath

```TypeScript
getNodeByPath(path: string, type?: NodeType): Node | null
```

通过路径获取节点。

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| type | [NodeType](arkts-arkgraphics3d-scenenodes-nodetype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) \| null |

## getResourceFactory

```TypeScript
getResourceFactory(): SceneResourceFactory
```

获取场景资源工厂对象。

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

| 类型 |
| --- |
| [SceneResourceFactory](arkts-arkgraphics3d-scene-sceneresourcefactory-i.md) |

## importNode

```TypeScript
importNode(name: string, node: Node, parent: Node | null): Node
```

一般用于从其他场景导入节点。

**起始版本：** 18

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

在当前场景中导入其他场景。

**起始版本：** 18

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

通过传入的资源路径加载资源，使用Promise异步回调。 调用后，应该在Scene使用完毕时调用destroy释放资源，否则可能导致资源泄漏。

**起始版本：** 12

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

通过该接口可以实现按需渲染，例如控制渲染帧率。

**起始版本：** 15

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

动画数组，用于保存3D场景中的动画对象。@return { Animation[] } @readonly

**类型：** [Animation](arkts-arkgraphics3d-sceneresources-animation-i.md)[]

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## environment

```TypeScript
set environment(value: Environment)
```

环境对象。

**类型：** [Environment](arkts-arkgraphics3d-sceneresources-environment-i.md)

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## renderConfiguration

```TypeScript
get renderConfiguration(): RenderConfiguration
```

渲染配置接口。

**类型：** [RenderConfiguration](arkts-arkgraphics3d-scene-renderconfiguration-i.md)

**起始版本：** 23

**系统能力：** SystemCapability.ArkUi.Graphics3D

## root

```TypeScript
get root(): Node | null
```

3D场景树根节点。@return { Node | null } @readonly

**类型：** [Node](arkts-arkgraphics3d-scenenodes-node-i.md)

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D
