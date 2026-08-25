# RenderNode

The **RenderNode** module provides APIs for creating a RenderNode in custom drawing settings with C APIs.

> **NOTE：**&gt;
> - Avoid modifying RenderNodes in BuilderNode. The FrameNode associated
> with BuilderNode is designed solely for mounting the BuilderNode as a child component. Modifying attributes or
> operations on the FrameNode's child nodes or their corresponding RenderNodes may lead to undefined behavior,
> including display, event handling, and stability issues.&gt;
> - RenderNode objects do not support JSON serialization.

**Since:** 11

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## appendChild

```TypeScript
appendChild(node: RenderNode): void
```

Appends a child node to this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [RenderNode](arkts-arkui-rendernode-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100025](../errorcode-node.md#100025-invalid-parameter-value) |

## clearChildren

```TypeScript
clearChildren(): void
```

Clears all child nodes of this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

Constructor used to create a RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dispose

```TypeScript
dispose(): void
```

Releases this RenderNode immediately.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## draw

```TypeScript
draw(context: DrawContext): void
```

Performs drawing. You need to implement this API. It is called when the RenderNode performs drawing.Note: The Canvas provided in the [DrawContext](arkts-arkui-graphics-drawcontext-c.md) parameter is a temporary command- recording canvas, not the actual rendering canvas of the node. For usage instructions, see [Adjusting the Transformation Matrix of the Custom Drawing Canvas](../../../ui/arkts-user-defined-arktsNode-renderNode.md#adjusting-the-transformation-matrix-of-the-custom-drawing-canvas).

> **NOTE：**&gt;
> During RenderNode initialization, the **draw** method is invoked twice. The first call occurs when the FrameNode
> is initially created, triggering the rendering process. The second call occurs when the modifier is initially
> set, which triggers drawing. All subsequent drawing processes are triggered by the modifier.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [DrawContext](arkts-arkui-graphics-drawcontext-c.md) | Yes |

## getChild

```TypeScript
getChild(index: number): RenderNode | null
```

Obtains the child node in the specified position of this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RenderNode](arkts-arkui-rendernode-c.md) \| null |

## getFirstChild

```TypeScript
getFirstChild(): RenderNode | null
```

Obtains the first child node of this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RenderNode](arkts-arkui-rendernode-c.md) \| null |

## getNextSibling

```TypeScript
getNextSibling(): RenderNode | null
```

Obtains the next sibling node of this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RenderNode](arkts-arkui-rendernode-c.md) \| null |

## getPreviousSibling

```TypeScript
getPreviousSibling(): RenderNode | null
```

Obtains the previous sibling node of this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RenderNode](arkts-arkui-rendernode-c.md) \| null |

## insertChildAfter

```TypeScript
insertChildAfter(child: RenderNode, sibling: RenderNode | null): void
```

Inserts a child node after the specified child node of this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [child](../arkts-components/arkts-arkui-nestedscrollinfo-i.md) | [RenderNode](arkts-arkui-rendernode-c.md) | Yes |
| sibling | [RenderNode](arkts-arkui-rendernode-c.md) \| null | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100025](../errorcode-node.md#100025-invalid-parameter-value) |

## invalidate

```TypeScript
invalidate(): void
```

Triggers the re-rendering of this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isDisposed

```TypeScript
isDisposed(): boolean
```

Checks whether this RenderNode object has released its reference to its backend entity node. Frontend nodes maintain references to corresponding backend entity nodes. After a node calls the **dispose** API to release this reference, subsequent API calls may cause crashes or return default values. This API facilitates validation of node validity prior to operations, thereby mitigating risks in scenarios where calls after disposal are required.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## removeChild

```TypeScript
removeChild(node: RenderNode): void
```

Deletes the specified child node from this RenderNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [RenderNode](arkts-arkui-rendernode-c.md) | Yes |

## backgroundBlur

```TypeScript
get backgroundBlur(): BackgroundBlur
```

Get the background blur effect.

**Type:** [BackgroundBlur](arkts-arkui-graphics-backgroundblur-i.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
get backgroundColor(): number
```

Get the background color of the RenderNode.

**Type:** number

**Default:** 0X00000000 [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
get borderColor(): Edges<number>
```

Get border color of the RenderNode.

**Type:** [Edges](arkts-arkui-graphics-edges-i.md)&lt;number&gt;

**Default:** 0XFF000000

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderRadius

```TypeScript
get borderRadius(): BorderRadiuses
```

Get border radius of the RenderNode.

**Type:** [BorderRadiuses](arkts-arkui-borderradiuses-t.md)

**Default:** 0

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderStyle

```TypeScript
get borderStyle(): Edges<BorderStyle>
```

Get border style of the RenderNode.

**Type:** [Edges](arkts-arkui-graphics-edges-i.md)&lt;[BorderStyle](arkts-arkui-borderstyle-e.md)&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
get borderWidth(): Edges<number>
```

Get border width of the RenderNode.

**Type:** [Edges](arkts-arkui-graphics-edges-i.md)&lt;number&gt;

**Default:** 0

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## clipToFrame

```TypeScript
get clipToFrame(): boolean
```

Get whether the RenderNode clip to frame.

**Type:** boolean

**Default:** true [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentBlur

```TypeScript
get contentBlur(): ContentBlur
```

Get the content blur effect.

**Type:** [ContentBlur](arkts-arkui-graphics-contentblur-i.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## foregroundBlur

```TypeScript
get foregroundBlur(): ForegroundBlur
```

Get the foreground blur effect.

**Type:** [ForegroundBlur](arkts-arkui-graphics-foregroundblur-i.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## frame

```TypeScript
get frame(): Frame
```

Get frame info of the RenderNode.

**Type:** [Frame](arkts-arkui-graphics-frame-i.md)

**Default:** Frame { x: 0, y: 0, width: 0, height: 0 } [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## label

```TypeScript
get label(): string
```

Get label of the RenderNode.

**Type:** string

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lengthMetricsUnit

```TypeScript
get lengthMetricsUnit(): LengthMetricsUnit
```

Get the length metrics unit of RenderNode.

**Type:** [LengthMetricsUnit](arkts-arkui-graphics-lengthmetricsunit-e.md)

**Default:** LengthMetricsUnit.DEFAULT

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## markNodeGroup

```TypeScript
get markNodeGroup(): boolean
```

Get whether to preferentially draw the node and its children.

**Type:** boolean

**Default:** false

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## opacity

```TypeScript
get opacity(): number
```

Get opacity of the RenderNode.

**Type:** number

**Default:** 1 [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pivot

```TypeScript
get pivot(): Pivot
```

Get pivot vector of the RenderNode.

**Type:** [Pivot](arkts-arkui-pivot-t.md)

**Default:** Pivot { x: 0.5, y: 0.5 } [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
get position(): Position
```

Get frame position of the RenderNode.

**Type:** [Position](arkts-arkui-position-t.md)

**Default:** Position { x: 0, y: 0 } [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rotation

```TypeScript
get rotation(): Rotation
```

Get rotation vector of the RenderNode.

**Type:** [Rotation](arkts-arkui-rotation-t.md)

**Default:** Rotation { x: 0, y: 0, z: 0 } [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
get scale(): Scale
```

Get scale vector of the RenderNode.

**Type:** [Scale](arkts-arkui-scale-t.md)

**Default:** Scale { x: 1, y: 1 } [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowAlpha

```TypeScript
get shadowAlpha(): number
```

Get shadow alpha of the RenderNode.

**Type:** number

**Default:** 0 [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowColor

```TypeScript
get shadowColor(): number
```

Get shadow color of the RenderNode.

**Type:** number

**Default:** 0X00000000 [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowElevation

```TypeScript
get shadowElevation(): number
```

Get shadow elevation of the RenderNode.

**Type:** number

**Default:** 0 [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowOffset

```TypeScript
get shadowOffset(): Offset
```

Get shadow offset of the RenderNode.

**Type:** [Offset](arkts-arkui-offset-t.md)

**Default:** Offset { x: 0, y: 0 } [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadowRadius

```TypeScript
get shadowRadius(): number
```

Get shadow radius of the RenderNode.

**Type:** number

**Default:** 0 [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shapeClip

```TypeScript
get shapeClip(): ShapeClip
```

Get shape clip of the RenderNode.

**Type:** [ShapeClip](arkts-arkui-graphics-shapeclip-c.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shapeMask

```TypeScript
get shapeMask(): ShapeMask
```

Get shape mask of the RenderNode.

**Type:** [ShapeMask](arkts-arkui-graphics-shapemask-c.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
get size(): Size
```

Get frame size of the RenderNode.

**Type:** Size

**Default:** Size { width: 0, height: 0 } [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transform

```TypeScript
get transform(): Matrix4
```

Get transform info of the RenderNode.

**Type:** [Matrix4](arkts-arkui-matrix4-t.md)

**Default:** Matrix4 [ 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ] [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## translation

```TypeScript
get translation(): Translation
```

Get translation vector of the RenderNode.

**Type:** [Translation](arkts-arkui-translation-t.md)

**Default:** Translation { x: 0, y: 0 } [since 11 - 11]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
