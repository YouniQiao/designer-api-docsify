# NodeAdapter

Provides lazy loading capabilities for FrameNode data, implementing LazyForEach API functionality.

> **NOTE：**&gt;
> Negative input parameters are ignored and trigger no processing.

**Since:** 12

<!--Device-unnamed-declare class NodeAdapter--><!--Device-unnamed-declare class NodeAdapter-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attachNodeAdapter

```TypeScript
static attachNodeAdapter(adapter: NodeAdapter, node: FrameNode): boolean
```

Attaches a FrameNode to a NodeAdapter. Each node can be bound to only one NodeAdapter. Attempts to re-attach to a NodeAdapter that has already been attached to will fail and return **false**.

> **NOTE：**&gt;
> The following components can be bound: **Column**, **Row**, **Stack**, **GridRow**, **Flex**, **Swiper**,
> **RelativeContainer**, **List**, **ListItemGroup**, **WaterFlow**, and **Grid**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeAdapter-static attachNodeAdapter(adapter: NodeAdapter, node: FrameNode): boolean--><!--Device-NodeAdapter-static attachNodeAdapter(adapter: NodeAdapter, node: FrameNode): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| adapter | [NodeAdapter](../../apis-default/arkts-apis/arkts-framenode-nodeadapter-c.md) | Yes | NodeAdapter class for lazy loading. |
| node | [FrameNode](../../apis-default/arkts-apis/arkts-framenode-c.md) | Yes | FrameNode to be attached. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Attachment result. Returns **true** if the attachment is successful; returns **false** otherwise. |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **NodeAdapter** object.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeAdapter-constructor()--><!--Device-NodeAdapter-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## detachNodeAdapter

```TypeScript
static detachNodeAdapter(node: FrameNode): void
```

Detaches a FrameNode from its NodeAdapter.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeAdapter-static detachNodeAdapter(node: FrameNode): void--><!--Device-NodeAdapter-static detachNodeAdapter(node: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](../../apis-default/arkts-apis/arkts-framenode-c.md) | Yes | FrameNode to detach. |

## dispose

```TypeScript
dispose(): void
```

Disposes of this **NodeAdapter** object. Bindings, if any, of the object will be cleared before the object is disposed of.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeAdapter-dispose(): void--><!--Device-NodeAdapter-dispose(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
import { NodeController, FrameNode, BuilderNode } from '@kit.ArkUI';

@Component
struct TestComponent {
  build() {
    Column() {
      Text('This is a BuilderNode.')
        .fontSize(16)
        .fontWeight(FontWeight.Bold)
    }
    .width('100%')
    .backgroundColor(Color.Gray)
  }

  aboutToAppear() {
    console.info('aboutToAppear');
  }

  aboutToDisappear() {
    console.info('aboutToDisappear');
  }
}

@Builder
function buildComponent() {
  TestComponent()
}

// Implement a custom UI controller by extending NodeController.
class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;
  private builderNode: BuilderNode<[]> | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
    this.builderNode.build(new WrappedBuilder(buildComponent));

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.size = { width: 200, height: 200 };
      rootRenderNode.backgroundColor = 0xffd5d5d5;
      rootRenderNode.appendChild(this.builderNode!.getFrameNode()!.getRenderNode());
    }

    return this.rootNode;
  }

  disposeFrameNode() {
    if (this.rootNode !== null && this.builderNode !== null) {
      // Remove all child nodes from rootNode before clearing the reference relationships.
      this.rootNode.removeChild(this.builderNode.getFrameNode());
      // Release the reference between builderNode and FrameNode.
      this.builderNode.dispose();
      // Release the reference between rootNode and FrameNode.
      this.rootNode.dispose();
    }
  }

  removeBuilderNode() {
    const rootRenderNode = this.rootNode!.getRenderNode();
    if (rootRenderNode !== null && this.builderNode !== null && this.builderNode.getFrameNode() !== null) {
      rootRenderNode.removeChild(this.builderNode!.getFrameNode()!.getRenderNode());
    }
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column({ space: 4 }) {
      NodeContainer(this.myNodeController)
      Button('FrameNode dispose')
        .onClick(() => {
          this.myNodeController.disposeFrameNode();
        })
        .width('100%')
    }
  }
}
```

## getAllAvailableItems

```TypeScript
getAllAvailableItems(): Array<FrameNode>
```

Obtains all available items. Available nodes include both currently displayed and preloaded nodes. The number of preloaded nodes can be configured by adjusting the **cachedCount** property of the parent container, following the [usage constraints](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md#constraints) of **LazyForEach**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeAdapter-getAllAvailableItems(): Array<FrameNode>--><!--Device-NodeAdapter-getAllAvailableItems(): Array<FrameNode>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[FrameNode](../../apis-default/arkts-apis/arkts-framenode-c.md)&gt; | Array of items in the FrameNode. |

## insertItem

```TypeScript
insertItem(start: number, count: number): void
```

Inserts a specified number of items starting from a specific index.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeAdapter-insertItem(start: number, count: number): void--><!--Device-NodeAdapter-insertItem(start: number, count: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | number | Yes | Starting index of the items to insert. <br>Value range: 0, +∞). |
| count | number | Yes | Number of the items to insert. <br>Value range: [0, +∞). |

## isDisposed

```TypeScript
isDisposed(): boolean
```

Checks whether the NodeAdapter's backend reference has been released. Frontend nodes maintain references to corresponding backend entity nodes. After a node calls the **dispose** API to release this reference, subsequent API calls may cause crashes or return default values. This API facilitates validation of node validity prior to operations, thereby mitigating risks in scenarios where calls after disposal are required.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-NodeAdapter-isDisposed(): boolean--><!--Device-NodeAdapter-isDisposed(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the reference to the backend node is released. The value **true** means that the reference to backend node is released, and **false** means the opposite. |

**Examples**

See [FrameNode Validity Check Example.

See NodeAdapter Validity Check Example.

## moveItem

```TypeScript
moveItem(from: number, to: number): void
```

Moves items from the starting index to the ending index.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeAdapter-moveItem(from: number, to: number): void--><!--Device-NodeAdapter-moveItem(from: number, to: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | number | Yes | Original index from which the data will be moved. <br>Value range: [0, +∞). |
| to | number | Yes | Target index to which the data will be moved. <br>Value range: [0, +∞). |

## onAttachToNode

```TypeScript
onAttachToNode?(target: FrameNode): void
```

Called when a FrameNode is attached to the NodeAdapter.

> **NOTE：**&gt;
> In versions earlier than API version 26.0.0, this callback is triggered when the host node is attached to the
> main tree. If you set this callback by dynamically assigning a value, you can complete the setting after calling
> [attachNodeAdapter](../../apis-default/arkts-apis/arkts-framenode-nodeadapter-c.md#attachnodeadapter) and before the host node is attached to the main tree.
> In this case, you will receive this callback when the host node is attached to the main tree.&gt;
> In API version 26.0.0 and later, this callback is triggered immediately when the NodeAdapter is bound to the host
> node, instead of when the host node is attached to the main tree. In this case, the host node may not have been
> attached to the main tree. If the node on which the callback logic depends has been mounted (for example,
> accessing layout information or executing animation), you are advised to register
> onAppear in the callback and place the related logic in **onAppear** for
> execution. If you set this callback by dynamically assigning a value, complete the setting before calling
> [attachNodeAdapter](../../apis-default/arkts-apis/arkts-framenode-nodeadapter-c.md#attachnodeadapter). Otherwise, the callback may fail to be triggered.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeAdapter-onAttachToNode?(target: FrameNode): void--><!--Device-NodeAdapter-onAttachToNode?(target: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | [FrameNode](../../apis-default/arkts-apis/arkts-framenode-c.md) | Yes | FrameNode attached to the NodeAdapter. |

## onCreateChild

```TypeScript
onCreateChild?(index: number): FrameNode
```

Called during node initialization or when new child nodes are detected. When adding child components, follow the child component restrictions for declarative components. For example, **WaterFlow** only supports adding **FlowItem** child nodes. The parent node uses the child node's index and key to determine whether the node is being loaded for the first time or a new node is sliding into view.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeAdapter-onCreateChild?(index: number): FrameNode--><!--Device-NodeAdapter-onCreateChild?(index: number): FrameNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | Index of the loaded node. <br>Value range: [0, +∞). |

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](../../apis-default/arkts-apis/arkts-framenode-c.md) | FrameNode created by you. |

## onDetachFromNode

```TypeScript
onDetachFromNode?(): void
```

Called when detachment occurs.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeAdapter-onDetachFromNode?(): void--><!--Device-NodeAdapter-onDetachFromNode?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDisposeChild

```TypeScript
onDisposeChild?(id: number, node: FrameNode): void
```

Called when a child node is about to be disposed. Nodes that are neither displayed on the screen nor within the preload range are considered nodes about to be disposed.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeAdapter-onDisposeChild?(id: number, node: FrameNode): void--><!--Device-NodeAdapter-onDisposeChild?(id: number, node: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | number | Yes | ID of the child node to be disposed of. |
| node | [FrameNode](../../apis-default/arkts-apis/arkts-framenode-c.md) | Yes | FrameNode to be disposed of. |

## onGetChildId

```TypeScript
onGetChildId?(index: number): number
```

Called during node initialization or when new child nodes are detected. The **index** parameter enables custom ID generation. Ensure that IDs remain unique across different index values.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeAdapter-onGetChildId?(index: number): number--><!--Device-NodeAdapter-onGetChildId?(index: number): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | Index of the loaded node. <br>Value range: [0, +∞). |

**Return value:**

| Type | Description |
| --- | --- |
| number | Custom ID. Make sure the ID is unique. |

## onUpdateChild

```TypeScript
onUpdateChild?(id: number, node: FrameNode): void
```

Called when a loaded node is reused. Node reuse occurs when the key value of a cached node matches that of the node to be reused.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeAdapter-onUpdateChild?(id: number, node: FrameNode): void--><!--Device-NodeAdapter-onUpdateChild?(id: number, node: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | number | Yes | ID of the node to be reused. |
| node | [FrameNode](../../apis-default/arkts-apis/arkts-framenode-c.md) | Yes | FrameNode that is reused. |

## reloadAllItems

```TypeScript
reloadAllItems(): void
```

Reloads all items in this node. This API calls the OnDataReloaded API in **LazyForEach** to trigger component data refresh.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeAdapter-reloadAllItems(): void--><!--Device-NodeAdapter-reloadAllItems(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reloadItem

```TypeScript
reloadItem(start: number, count: number): void
```

Reloads a specified number of items starting from a specific index.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeAdapter-reloadItem(start: number, count: number): void--><!--Device-NodeAdapter-reloadItem(start: number, count: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | number | Yes | Starting index of the items to reload. <br>Value range: 0, +∞). |
| count | number | Yes | Number of the items to reload. <br>Value range: [0, +∞). |

## removeItem

```TypeScript
removeItem(start: number, count: number): void
```

Removes a specified number of items starting from a specific index.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeAdapter-removeItem(start: number, count: number): void--><!--Device-NodeAdapter-removeItem(start: number, count: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | number | Yes | Starting index of the items to remove. <br>Value range: [0, +∞). |
| count | number | Yes | Number of the items to remove. <br>Value range: [0, +∞). |

**Examples**

See the example for [NodeAdapter Usage Example.

