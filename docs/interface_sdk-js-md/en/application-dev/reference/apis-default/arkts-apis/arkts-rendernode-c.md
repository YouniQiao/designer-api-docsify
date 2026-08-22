# RenderNode

Defines RenderNode. Contains node tree operations and render property operations on node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class RenderNode--><!--Device-unnamed-export declare class RenderNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## appendChild

```TypeScript
appendChild(node: RenderNode): void
```

Add child to the end of the RenderNode's children.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-appendChild(node: RenderNode): void--><!--Device-RenderNode-appendChild(node: RenderNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [RenderNode](arkts-rendernode-c.md) | Yes | The node will be added. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100025](../../apis-arkui/errorcode-node.md#100025-invalid-parameter-value) | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'node' is invalid: its corresponding FrameNode cannot be adopted." |

## clearChildren

```TypeScript
clearChildren(): void
```

Clear children of the current RenderNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-clearChildren(): void--><!--Device-RenderNode-clearChildren(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-constructor()--><!--Device-RenderNode-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dispose

```TypeScript
dispose(): void
```

Dispose the RenderNode immediately.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-dispose(): void--><!--Device-RenderNode-dispose(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## draw

```TypeScript
draw(context: DrawContext): void
```

Draw Method. Executed when the associated RenderNode is onDraw.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-draw(context: DrawContext): void--><!--Device-RenderNode-draw(context: DrawContext): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [DrawContext](arkts-graphics-drawcontext-c.md) | Yes | The DrawContext will be used when executed draw method. |

## getChild

```TypeScript
getChild(index: int): RenderNode | null
```

Get a child of the current RenderNode by index.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-getChild(index: int): RenderNode | null--><!--Device-RenderNode-getChild(index: int): RenderNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index of the desired node in the children of RenderNode. |

**Return value:**

| Type | Description |
| --- | --- |
| [RenderNode](arkts-rendernode-c.md) \| null | Returns a RenderNode. When the required node does not exist, returns null. |

## getFirstChild

```TypeScript
getFirstChild(): RenderNode | null
```

Get the first child of the current RenderNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-getFirstChild(): RenderNode | null--><!--Device-RenderNode-getFirstChild(): RenderNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RenderNode](arkts-rendernode-c.md) \| null | Returns a RenderNode, which is first child of the current RenderNode. If current RenderNode does not have child node, returns null. |

## getNextSibling

```TypeScript
getNextSibling(): RenderNode | null
```

Get the next sibling node of the current RenderNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-getNextSibling(): RenderNode | null--><!--Device-RenderNode-getNextSibling(): RenderNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RenderNode](arkts-rendernode-c.md) \| null | Returns a RenderNode. If current RenderNode does not have next sibling node, returns null. |

## getPreviousSibling

```TypeScript
getPreviousSibling(): RenderNode | null
```

Get the previous sibling node of the current RenderNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-getPreviousSibling(): RenderNode | null--><!--Device-RenderNode-getPreviousSibling(): RenderNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RenderNode](arkts-rendernode-c.md) \| null | Returns a RenderNode. |

## insertChildAfter

```TypeScript
insertChildAfter(child: RenderNode, sibling: RenderNode | null): void
```

Add child to the current RenderNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-insertChildAfter(child: RenderNode, sibling: RenderNode | null): void--><!--Device-RenderNode-insertChildAfter(child: RenderNode, sibling: RenderNode | null): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| child | [RenderNode](arkts-rendernode-c.md) | Yes | The node will be added. |
| sibling | [RenderNode](arkts-rendernode-c.md) \| null | Yes | The new node is added after this node. When sibling is null, insert node as the first children of the node. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100025](../../apis-arkui/errorcode-node.md#100025-invalid-parameter-value) | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'child' is invalid: its corresponding FrameNode cannot be adopted." |

## invalidate

```TypeScript
invalidate(): void
```

Invalidate the RenderNode, which will cause a re-render of the RenderNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-invalidate(): void--><!--Device-RenderNode-invalidate(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isDisposed

```TypeScript
isDisposed(): boolean
```

Get if the RenderNode is disposed.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-isDisposed(): boolean--><!--Device-RenderNode-isDisposed(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the RenderNode is disposed, false otherwise. |

## removeChild

```TypeScript
removeChild(node: RenderNode): void
```

Remove child from the current RenderNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-removeChild(node: RenderNode): void--><!--Device-RenderNode-removeChild(node: RenderNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [RenderNode](arkts-rendernode-c.md) | Yes | The node will be removed. |

