# RenderNode

Defines RenderNode. Contains node tree operations and render property operations on node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class RenderNode--><!--Device-unnamed-export declare class RenderNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## appendChild

```TypeScript
appendChild(node: RenderNode): void
```

Add child to the end of the RenderNode's children.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-appendChild(node: RenderNode): void--><!--Device-RenderNode-appendChild(node: RenderNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The node will be added. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100025](../../errorcode-node.md#100025-invalid-parameter-value) | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'node' is invalid: its corresponding FrameNode cannot be adopted." |

## clearChildren

```TypeScript
clearChildren(): void
```

Clear children of the current RenderNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-clearChildren(): void--><!--Device-RenderNode-clearChildren(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-constructor()--><!--Device-RenderNode-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dispose

```TypeScript
dispose(): void
```

Dispose the RenderNode immediately.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-dispose(): void--><!--Device-RenderNode-dispose(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## draw

```TypeScript
draw(context: DrawContext): void
```

Draw Method. Executed when the associated RenderNode is onDraw.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-draw(context: DrawContext): void--><!--Device-RenderNode-draw(context: DrawContext): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The DrawContext will be used when executed draw method. |

## getChild

```TypeScript
getChild(index: int): RenderNode | null
```

Get a child of the current RenderNode by index.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | - Returns a RenderNode. When the required node does not exist, returns null. |

## getFirstChild

```TypeScript
getFirstChild(): RenderNode | null
```

Get the first child of the current RenderNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-getFirstChild(): RenderNode | null--><!--Device-RenderNode-getFirstChild(): RenderNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | - Returns a RenderNode, which is first child of the current RenderNode. |

## getNextSibling

```TypeScript
getNextSibling(): RenderNode | null
```

Get the next sibling node of the current RenderNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-getNextSibling(): RenderNode | null--><!--Device-RenderNode-getNextSibling(): RenderNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | - Returns a RenderNode. If current RenderNode does not have next |

## getPreviousSibling

```TypeScript
getPreviousSibling(): RenderNode | null
```

Get the previous sibling node of the current RenderNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-getPreviousSibling(): RenderNode | null--><!--Device-RenderNode-getPreviousSibling(): RenderNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | - Returns a RenderNode. |

## insertChildAfter

```TypeScript
insertChildAfter(child: RenderNode, sibling: RenderNode | null): void
```

Add child to the current RenderNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-insertChildAfter(child: RenderNode, sibling: RenderNode | null): void--><!--Device-RenderNode-insertChildAfter(child: RenderNode, sibling: RenderNode | null): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| child | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The node will be added. |
| sibling | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| null | Yes | The new node is added after this node. When sibling is null,insert node as the first children of the node. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100025](../../errorcode-node.md#100025-invalid-parameter-value) | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'child' is invalid: its corresponding FrameNode cannot be adopted." |

## invalidate

```TypeScript
invalidate(): void
```

Invalidate the RenderNode, which will cause a re-render of the RenderNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-invalidate(): void--><!--Device-RenderNode-invalidate(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isDisposed

```TypeScript
isDisposed(): boolean
```

Get if the RenderNode is disposed.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-isDisposed(): boolean--><!--Device-RenderNode-isDisposed(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - Returns true if the RenderNode is disposed, false otherwise. |

## removeChild

```TypeScript
removeChild(node: RenderNode): void
```

Remove child from the current RenderNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-removeChild(node: RenderNode): void--><!--Device-RenderNode-removeChild(node: RenderNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The node will be removed. |

## backgroundBlur

```TypeScript
get backgroundBlur(): BackgroundBlur
```

Get the background blur effect.

**Type:** BackgroundBlur

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get backgroundBlur(): BackgroundBlur--><!--Device-RenderNode-get backgroundBlur(): BackgroundBlur-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
get backgroundColor(): int
```

Get the background color of the RenderNode.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get backgroundColor(): int--><!--Device-RenderNode-get backgroundColor(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
get borderColor(): NodeEdges<int> | undefined
```

Get border color of the RenderNode.

**Type:** NodeEdges&lt;int&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get borderColor(): NodeEdges<int> | undefined--><!--Device-RenderNode-get borderColor(): NodeEdges<int> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderRadius

```TypeScript
get borderRadius(): NodeBorderRadiuses | undefined
```

Get border radius of the RenderNode.

**Type:** NodeBorderRadiuses

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get borderRadius(): NodeBorderRadiuses | undefined--><!--Device-RenderNode-get borderRadius(): NodeBorderRadiuses | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderStyle

```TypeScript
get borderStyle(): NodeEdges<BorderStyle> | undefined
```

Get border style of the RenderNode.

**Type:** NodeEdges&lt;BorderStyle&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get borderStyle(): NodeEdges<BorderStyle> | undefined--><!--Device-RenderNode-get borderStyle(): NodeEdges<BorderStyle> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
get borderWidth(): NodeEdges<double> | undefined
```

Get border width of the RenderNode.

**Type:** NodeEdges&lt;double&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get borderWidth(): NodeEdges<double> | undefined--><!--Device-RenderNode-get borderWidth(): NodeEdges<double> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## clipToFrame

```TypeScript
get clipToFrame(): boolean
```

Get whether the RenderNode clip to frame.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get clipToFrame(): boolean--><!--Device-RenderNode-get clipToFrame(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentBlur

```TypeScript
get contentBlur(): ContentBlur
```

Get the content blur effect.

**Type:** ContentBlur

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get contentBlur(): ContentBlur--><!--Device-RenderNode-get contentBlur(): ContentBlur-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## foregroundBlur

```TypeScript
get foregroundBlur(): ForegroundBlur
```

Get the foreground blur effect.

**Type:** ForegroundBlur

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get foregroundBlur(): ForegroundBlur--><!--Device-RenderNode-get foregroundBlur(): ForegroundBlur-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## frame

```TypeScript
get frame(): Frame
```

Get frame info of the RenderNode.

**Type:** Frame

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get frame(): Frame--><!--Device-RenderNode-get frame(): Frame-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## label

```TypeScript
get label(): string
```

Get label of the RenderNode.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get label(): string--><!--Device-RenderNode-get label(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lengthMetricsUnit

```TypeScript
get lengthMetricsUnit(): LengthMetricsUnit
```

Get the length metrics unit of RenderNode.

**Type:** LengthMetricsUnit

**Default:** LengthMetricsUnit.DEFAULT

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get lengthMetricsUnit(): LengthMetricsUnit--><!--Device-RenderNode-get lengthMetricsUnit(): LengthMetricsUnit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## markNodeGroup

```TypeScript
get markNodeGroup(): boolean
```

Get whether to preferentially draw the node and its children.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get markNodeGroup(): boolean--><!--Device-RenderNode-get markNodeGroup(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## opacity

```TypeScript
get opacity(): double
```

Get opacity of the RenderNode.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get opacity(): double--><!--Device-RenderNode-get opacity(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pivot

```TypeScript
get pivot(): Pivot
```

Get pivot vector of the RenderNode.

**Type:** Pivot

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get pivot(): Pivot--><!--Device-RenderNode-get pivot(): Pivot-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
get position(): NodePosition
```

Get frame position of the RenderNode.

**Type:** NodePosition

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get position(): NodePosition--><!--Device-RenderNode-get position(): NodePosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rotation

```TypeScript
get rotation(): Rotation
```

Get rotation vector of the RenderNode.

**Type:** Rotation

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get rotation(): Rotation--><!--Device-RenderNode-get rotation(): Rotation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
get scale(): Scale
```

Get scale vector of the RenderNode.

**Type:** Scale

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get scale(): Scale--><!--Device-RenderNode-get scale(): Scale-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowAlpha

```TypeScript
get shadowAlpha(): double
```

Get shadow alpha of the RenderNode.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get shadowAlpha(): double--><!--Device-RenderNode-get shadowAlpha(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowColor

```TypeScript
get shadowColor(): int
```

Get shadow color of the RenderNode.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get shadowColor(): int--><!--Device-RenderNode-get shadowColor(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowElevation

```TypeScript
get shadowElevation(): double
```

Get shadow elevation of the RenderNode.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get shadowElevation(): double--><!--Device-RenderNode-get shadowElevation(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowOffset

```TypeScript
get shadowOffset(): NodeOffset
```

Get shadow offset of the RenderNode.

**Type:** NodeOffset

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get shadowOffset(): NodeOffset--><!--Device-RenderNode-get shadowOffset(): NodeOffset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowRadius

```TypeScript
get shadowRadius(): double
```

Get shadow radius of the RenderNode.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get shadowRadius(): double--><!--Device-RenderNode-get shadowRadius(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shapeClip

```TypeScript
get shapeClip(): ShapeClip
```

Get shape clip of the RenderNode.

**Type:** ShapeClip

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get shapeClip(): ShapeClip--><!--Device-RenderNode-get shapeClip(): ShapeClip-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shapeMask

```TypeScript
get shapeMask(): ShapeMask | undefined
```

Get shape mask of the RenderNode.

**Type:** ShapeMask

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get shapeMask(): ShapeMask | undefined--><!--Device-RenderNode-get shapeMask(): ShapeMask | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
get size(): Size
```

Get frame size of the RenderNode.

**Type:** Size

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get size(): Size--><!--Device-RenderNode-get size(): Size-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transform

```TypeScript
get transform(): Matrix4
```

Get transform info of the RenderNode.

**Type:** Matrix4

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get transform(): Matrix4--><!--Device-RenderNode-get transform(): Matrix4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## translation

```TypeScript
get translation(): Translation
```

Get translation vector of the RenderNode.

**Type:** Translation

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderNode-get translation(): Translation--><!--Device-RenderNode-get translation(): Translation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

