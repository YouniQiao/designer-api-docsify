# NodeAdapter

Used for lazy loading of typeNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class NodeAdapter--><!--Device-unnamed-export declare class NodeAdapter-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attachNodeAdapter

```TypeScript
static attachNodeAdapter(adapter: NodeAdapter, node: FrameNode): boolean
```

Add a NodeAdapter to bind to the node.A node can only be bound to one NodeAdapter. Binding failure returns false.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-static attachNodeAdapter(adapter: NodeAdapter, node: FrameNode): boolean--><!--Device-NodeAdapter-static attachNodeAdapter(adapter: NodeAdapter, node: FrameNode): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| adapter | [NodeAdapter](arkts-arkui-framenode-nodeadapter-c.md) | Yes | Define lazy loading classes. |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | The bound FrameNode node. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Return the binding result. |

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-constructor()--><!--Device-NodeAdapter-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## detachNodeAdapter

```TypeScript
static detachNodeAdapter(node: FrameNode): void
```

Remove the bound NodeAdapter from the node.A node can only be bound to one NodeAdapter.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-static detachNodeAdapter(node: FrameNode): void--><!--Device-NodeAdapter-static detachNodeAdapter(node: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | Unbind the FrameNode node. |

## dispose

```TypeScript
dispose(): void
```

Dispose the NodeAdapter immediately.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-dispose(): void--><!--Device-NodeAdapter-dispose(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getAllAvailableItems

```TypeScript
getAllAvailableItems(): Array<FrameNode>
```

Obtain all data results.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-getAllAvailableItems(): Array<FrameNode>--><!--Device-NodeAdapter-getAllAvailableItems(): Array<FrameNode>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[FrameNode](arkts-arkui-framenode-c.md)&gt; | Return all valid FrameNode collections. |

## insertItem

```TypeScript
insertItem(start: int, count: int): void
```

Define data insertion operations.Insert a specified amount of data starting from the index value.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-insertItem(start: int, count: int): void--><!--Device-NodeAdapter-insertItem(start: int, count: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | Start Insert index values for data. |
| count | int | Yes | Insert the number of data. |

## isDisposed

```TypeScript
isDisposed(): boolean
```

Get if the NodeAdapter is disposed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-isDisposed(): boolean--><!--Device-NodeAdapter-isDisposed(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the NodeAdapter is disposed, false otherwise. |

## moveItem

```TypeScript
moveItem(from: int, to: int): void
```

Define data movement operations. Move data from the starting index to the ending index.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-moveItem(from: int, to: int): void--><!--Device-NodeAdapter-moveItem(from: int, to: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | int | Yes | Starting index value. |
| to | int | Yes | End index value. |

## onAttachToNode

```TypeScript
onAttachToNode(target: FrameNode): void
```

This callback will be triggered when a FrameNode is bound.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-onAttachToNode(target: FrameNode): void--><!--Device-NodeAdapter-onAttachToNode(target: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | [FrameNode](arkts-arkui-framenode-c.md) | Yes | The bound FrameNode node. |

## onCreateChild

```TypeScript
onCreateChild(index: int): FrameNode
```

Call this callback when loading for the first time or when a new node slides in.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-onCreateChild(index: int): FrameNode--><!--Device-NodeAdapter-onCreateChild(index: int): FrameNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Load the index value of the data. |

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](arkts-arkui-framenode-c.md) | Returns the FrameNode node that loads the node. |

## onDetachFromNode

```TypeScript
onDetachFromNode(): void
```

This callback will be triggered when the binding is released.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-onDetachFromNode(): void--><!--Device-NodeAdapter-onDetachFromNode(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDisposeChild

```TypeScript
onDisposeChild(id: int, node: FrameNode): void
```

Called when the child node is about to be destroyed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-onDisposeChild(id: int, node: FrameNode): void--><!--Device-NodeAdapter-onDisposeChild(id: int, node: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | int | Yes | The child node ID that is about to be destroyed. |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | The FrameNode node that is about to be destroyed. |

## onGetChildId

```TypeScript
onGetChildId(index: int): int
```

Call this callback when loading for the first time or when a new node slides in.Used to generate custom IDs,developers need to ensure the uniqueness of the IDs themselves.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-onGetChildId(index: int): int--><!--Device-NodeAdapter-onGetChildId(index: int): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Load the index value of the data. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returning the developer's custom ID requires the developer to ensure its uniqueness. |

## onUpdateChild

```TypeScript
onUpdateChild(id: int, node: FrameNode): void
```

Call this callback when reloading or reusing.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-onUpdateChild(id: int, node: FrameNode): void--><!--Device-NodeAdapter-onUpdateChild(id: int, node: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | int | Yes | The child node ID that is about to be reloaded. |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | Reused FrameNode nodes. |

## reloadAllItems

```TypeScript
reloadAllItems(): void
```

Define the operation of reloading all data.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-reloadAllItems(): void--><!--Device-NodeAdapter-reloadAllItems(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reloadItem

```TypeScript
reloadItem(start: int, count: int): void
```

Define the data reload operation.Reload a specified amount of data starting from the index value.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-reloadItem(start: int, count: int): void--><!--Device-NodeAdapter-reloadItem(start: int, count: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | Start loading index values for data. |
| count | int | Yes | Load the number of data. |

## removeItem

```TypeScript
removeItem(start: int, count: int): void
```

Define data deletion operations.Delete a specified amount of data starting from the index value.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-removeItem(start: int, count: int): void--><!--Device-NodeAdapter-removeItem(start: int, count: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | Start deleting index values for data. |
| count | int | Yes | Delete the number of data. |

## totalNodeCount

```TypeScript
get totalNodeCount(): int
```

Get the total number of node count.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeAdapter-get totalNodeCount(): int--><!--Device-NodeAdapter-get totalNodeCount(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

