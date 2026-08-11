# Node

定义Node接口.

**继承/实现关系：** Node extends [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md)

**起始版本：** 12

<!--Device-unnamed-export interface Node extends SceneResource--><!--Device-unnamed-export interface Node extends SceneResource-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## getNodeByPath

```TypeScript
getNodeByPath(path: string): Node | null
```

通过路径获取节点.

**起始版本：** 12

<!--Device-Node-getNodeByPath(path: string): Node | null--><!--Device-Node-getNodeByPath(path: string): Node | null-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [path](#path) | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) |

## children

```TypeScript
readonly children: Container<Node>
```

节点的子节点，不存在则为空值。为只读属性，表示不能替换整个children容器，但可以通过容器方法操作子节点（如[append](arkts-arkgraphics3d-scenenodes-container-i.md#append)、[insertAfter](arkts-arkgraphics3d-scenenodes-container-i.md#insertafter)、  
[remove](arkts-arkgraphics3d-scenenodes-container-i.md#remove)或[clear](arkts-arkgraphics3d-scenenodes-container-i.md#clear)）。如果append或insertAfter的节点已存在于容器中，容器会先移除该节点再插入，因此数量不会增加，看似“无效”；添加新节点才会真正增加子节点数量。

**类型：** [Container](arkts-arkgraphics3d-scenenodes-container-i.md)&lt;[Node](arkts-arkgraphics3d-scenenodes-node-i.md)&gt;

**起始版本：** 12

<!--Device-Node-readonly children: Container<Node>--><!--Device-Node-readonly children: Container<Node>-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## layerMask

```TypeScript
readonly layerMask: LayerMask
```

节点图层掩码.

**类型：** [LayerMask](arkts-arkgraphics3d-scenenodes-layermask-i.md)

**起始版本：** 12

<!--Device-Node-readonly layerMask: LayerMask--><!--Device-Node-readonly layerMask: LayerMask-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## nodeType

```TypeScript
readonly nodeType: NodeType
```

节点类型.

**类型：** [NodeType](arkts-arkgraphics3d-scenenodes-nodetype-e.md)

**起始版本：** 12

<!--Device-Node-readonly nodeType: NodeType--><!--Device-Node-readonly nodeType: NodeType-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## parent

```TypeScript
readonly parent: Node | null
```

节点的父节点.

**类型：** [Node](arkts-arkgraphics3d-scenenodes-node-i.md) \| null

**起始版本：** 12

<!--Device-Node-readonly parent: Node | null--><!--Device-Node-readonly parent: Node | null-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## path

```TypeScript
readonly path: string
```

节点路径.

**类型：** string

**起始版本：** 12

<!--Device-Node-readonly path: string--><!--Device-Node-readonly path: string-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## position

```TypeScript
position: Position3
```

节点位置, 单位为世界坐标系下的场景单位（例如cm、m、km等）.

**类型：** [Position3](arkts-arkgraphics3d-position3-t.md)

**起始版本：** 12

<!--Device-Node-position: Position3--><!--Device-Node-position: Position3-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## rotation

```TypeScript
rotation: Quaternion
```

节点旋转.

**类型：** [Quaternion](arkts-arkgraphics3d-scenetypes-quaternion-i.md)

**起始版本：** 12

<!--Device-Node-rotation: Quaternion--><!--Device-Node-rotation: Quaternion-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## scale

```TypeScript
scale: Scale3
```

节点缩放.

**类型：** [Scale3](arkts-arkgraphics3d-scale3-t.md)

**起始版本：** 12

<!--Device-Node-scale: Scale3--><!--Device-Node-scale: Scale3-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## visible

```TypeScript
visible: boolean
```

节点可见性标志.

**类型：** boolean

**起始版本：** 12

<!--Device-Node-visible: boolean--><!--Device-Node-visible: boolean-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D
