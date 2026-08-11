# Node

The 3D scene consists of nodes in a tree hierarchy, where each node implements a Node interface.

**Inheritance/Implementation:** Node extends [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface Node extends SceneResource--><!--Device-unnamed-export interface Node extends SceneResource-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## getNodeByPath

```TypeScript
getNodeByPath(path: string): Node | null
```

Obtains a node by path. If no node is obtained, null is returned.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Node-getNodeByPath(path: string): Node | null--><!--Device-Node-getNodeByPath(path: string): Node | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Path in the scene node tree. Each layer is separated by a slash (/). |

**Return value:**

| Type | Description |
| --- | --- |
| [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Returns the node object. |

## children

```TypeScript
readonly children: Container<Node>
```

Child node of the node and null if it does not exist.This is a read-only property, indicating that you cannot directly replace the entire children container.However, you can operate the child nodes using container methods like [append](arkts-arkgraphics3d-scenenodes-container-i.md#append),  
[insertAfter](arkts-arkgraphics3d-scenenodes-container-i.md#insertafter), [remove](arkts-arkgraphics3d-scenenodes-container-i.md#remove), or [clear](arkts-arkgraphics3d-scenenodes-container-i.md#clear).If the node being appended or inserted already exists in the container, it is removed first and then reinserted.As a result, the total number of child nodes remains unchanged, making the operation seem ineffective.The count increases only when a new node is added.

**Type:** [Container](arkts-arkgraphics3d-scenenodes-container-i.md)&lt;[Node](arkts-arkgraphics3d-scenenodes-node-i.md)&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Node-readonly children: Container<Node>--><!--Device-Node-readonly children: Container<Node>-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## layerMask

```TypeScript
readonly layerMask: LayerMask
```

Layer mask of a node.

**Type:** [LayerMask](arkts-arkgraphics3d-scenenodes-layermask-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Node-readonly layerMask: LayerMask--><!--Device-Node-readonly layerMask: LayerMask-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## nodeType

```TypeScript
readonly nodeType: NodeType
```

Node type.

**Type:** [NodeType](arkts-arkgraphics3d-scenenodes-nodetype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Node-readonly nodeType: NodeType--><!--Device-Node-readonly nodeType: NodeType-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## parent

```TypeScript
readonly parent: Node | null
```

Parent node of the node and null if it does not exist.

**Type:** [Node](arkts-arkgraphics3d-scenenodes-node-i.md) \| null

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Node-readonly parent: Node | null--><!--Device-Node-readonly parent: Node | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## path

```TypeScript
readonly path: string
```

Node path.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Node-readonly path: string--><!--Device-Node-readonly path: string-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## position

```TypeScript
position: Position3
```

Node position, in scene units of the world coordinate system (for example, cm, m, or km).

**Type:** [Position3](arkts-arkgraphics3d-position3-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Node-position: Position3--><!--Device-Node-position: Position3-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## rotation

```TypeScript
rotation: Quaternion
```

Rotation angle of a node.

**Type:** [Quaternion](arkts-arkgraphics3d-scenetypes-quaternion-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Node-rotation: Quaternion--><!--Device-Node-rotation: Quaternion-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## scale

```TypeScript
scale: Scale3
```

Node scale.

**Type:** [Scale3](arkts-arkgraphics3d-scale3-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Node-scale: Scale3--><!--Device-Node-scale: Scale3-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## visible

```TypeScript
visible: boolean
```

Whether a node is visible. true if visible, false otherwise.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Node-visible: boolean--><!--Device-Node-visible: boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

