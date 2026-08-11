# FrameNode

**FrameNode** represents an entity node in the component tree. It can be used by a  
[NodeController](arkts-arkui-nodecontroller-c.md) to mount a [BuilderNode](arkts-arkui-buildernode-c.md) (that holds the FrameNode) to a [NodeContainer](../../apis-arkui/arkts-components/arkts-arkui-node_container-i) or mount a  
[RenderNode](arkts-arkui-rendernode-c.md) to another FrameNode.&lt;!--RP2--&gt;&lt;!--RP2End--&gt;

> **NOTE：**
> 
> - **FrameNode** is not available in DevEco Studio Previewer.
> 
> - FrameNodes cannot be dragged.
> 
> - FrameNode objects do not support JSON serialization.
> 
> - When the API of the [FrameNode](arkts-arkui-framenode-c.md) object is invoked in the scenario of
> [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context), you are advised to use the
> [runScopedTask](arkts-arkui-arkui-uicontext-uicontext-c.md#runscopedtask) API of
> [UIContext](arkts-arkui-uicontext.md) to specify the UI context. For details, see
> [Executing the Closure Bound to a UI Instance](../../../ui/arkts-global-interface.md#executing-the-closure-bound-to-a-ui-instance).
> 
> - In the FrameNode APIs, only the mandatory parameters of the [Optional](../arkts-components/arkts-arkui-optional-t.md/arkts-arkui-optional-t.md) type can be set to null or
> undefined.

**Since:** 11

<!--Device-unnamed-export class FrameNode--><!--Device-unnamed-export class FrameNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addComponentContent

```TypeScript
addComponentContent<T>(content: ComponentContent<T> | ReactiveComponentContent<T>): void
```

Adds component content. The current node must be modifiable, which means the return value of  
[isModifiable](arkts-arkui-framenode-c.md#ismodifiable) must be **true**. If the node is not modifiable, an exception is thrown.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-addComponentContent<T>(content: ComponentContent<T> | ReactiveComponentContent<T>): void--><!--Device-FrameNode-addComponentContent<T>(content: ComponentContent<T> | ReactiveComponentContent<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [ComponentContent](arkts-arkui-componentcontent-c.md)&lt;T&gt; \| [ReactiveComponentContent&lt;T&gt;](arkts-arkui-componentcontent-reactivecomponentcontent-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |

## addSupportedUIStates

```TypeScript
addSupportedUIStates(uiStates: number, statesChangeHandler: UIStatesChangeHandler, excludeInner?: boolean): void
```

Adds the polymorphic style states supported by the component.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FrameNode-addSupportedUIStates(uiStates: number, statesChangeHandler: UIStatesChangeHandler, excludeInner?: boolean): void--><!--Device-FrameNode-addSupportedUIStates(uiStates: number, statesChangeHandler: UIStatesChangeHandler, excludeInner?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uiStates | number | Yes | UI states of the target node to be processed. &lt;br&gt;Multiple states can be specified simultaneously using bitwise OR operations, for example, **targetUIStates = UIState.PRESSED  \|
| statesChangeHandler | [UIStatesChangeHandler](arkts-arkui-uistateschangehandler-t.md) | Yes |
| excludeInner | boolean | No |

## adoptChild

```TypeScript
adoptChild(child: FrameNode): void
```

Adopts the target node as an affiliated node. The adopted node must not have an existing parent. This API is not used to add a node as a child node. Instead, it only allows the node to receive lifecycle callbacks of the corresponding child node.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FrameNode-adoptChild(child: FrameNode): void--><!--Device-FrameNode-adoptChild(child: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| child | [FrameNode](arkts-arkui-framenode-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |
| [100025](../errorcode-node.md#100025-invalid-parameter-value) |
| [100026](../errorcode-node.md#100026-the-instance-object-used-to-call-the-api-has-been-unbound-from-the-backend-entity-node) |

## appendChild

```TypeScript
appendChild(node: FrameNode): void
```

Appends a child node to the end of this FrameNode. If this FrameNode is not modifiable, an exception is thrown.When **appendChild** is called, [typeNode](arkts-arkui-typenode-n.md) validates the type or number of child nodes. If the validation fails, an exception is thrown. For specific limitations, see [typeNode](arkts-arkui-typenode-n.md).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-appendChild(node: FrameNode): void--><!--Device-FrameNode-appendChild(node: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |
| [100025](../errorcode-node.md#100025-invalid-parameter-value) |

## cancelAnimations

```TypeScript
cancelAnimations(properties: AnimationPropertyType[]): boolean
```

Cancels all animations for specified properties on the FrameNode. This API executes synchronously in the node's owning thread and blocks until cancellation completes. Upon successful cancellation, the node's property values revert to their current display state at the time of cancellation.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FrameNode-cancelAnimations(properties: AnimationPropertyType[]): boolean--><!--Device-FrameNode-cancelAnimations(properties: AnimationPropertyType[]): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| properties | [AnimationPropertyType](arkts-arkui-animationpropertytype-e.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## clearChildren

```TypeScript
clearChildren(): void
```

Clears all child nodes of this FrameNode. If this FrameNode is not modifiable, an exception is thrown.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-clearChildren(): void--><!--Device-FrameNode-clearChildren(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Error codes:**

| Error Code ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |

## constructor

```TypeScript
constructor(uiContext: UIContext)
```

A constructor used to create a FrameNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-constructor(uiContext: UIContext)--><!--Device-FrameNode-constructor(uiContext: UIContext)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |

## convertPosition

```TypeScript
convertPosition(position: Position, targetNode: FrameNode): Position
```

Converts a coordinate point from this node's coordinate system to the target node's coordinate system.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FrameNode-convertPosition(position: Position, targetNode: FrameNode): Position--><!--Device-FrameNode-convertPosition(position: Position, targetNode: FrameNode): Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | [Position](arkts-arkui-position-t.md) | Yes |
| targetNode | [FrameNode](arkts-arkui-framenode-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Position](arkts-arkui-position-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [100025](../errorcode-node.md#100025-invalid-parameter-value) |
| [100024](../errorcode-node.md#100024-no-common-ancestor-node-between-nodes) |

## convertPositionFromWindow

```TypeScript
convertPositionFromWindow(positionByWindow: Position): Position
```

Converts the coordinates of a point from the coordinate system of the window where the current node is located to the coordinate system of the current node.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FrameNode-convertPositionFromWindow(positionByWindow: Position): Position--><!--Device-FrameNode-convertPositionFromWindow(positionByWindow: Position): Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| positionByWindow | [Position](arkts-arkui-position-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Position](arkts-arkui-position-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [100026](../errorcode-node.md#100026-the-instance-object-used-to-call-the-api-has-been-unbound-from-the-backend-entity-node) |
| [100028](../errorcode-node.md#100028-current-node-is-not-on-the-main-node-tree) |

## convertPositionToWindow

```TypeScript
convertPositionToWindow(positionByLocal: Position): Position
```

Converts the coordinates of a point from the coordinate system of the current node to the coordinate system of the window where the current node is located.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FrameNode-convertPositionToWindow(positionByLocal: Position): Position--><!--Device-FrameNode-convertPositionToWindow(positionByLocal: Position): Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| positionByLocal | [Position](arkts-arkui-position-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Position](arkts-arkui-position-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [100026](../errorcode-node.md#100026-the-instance-object-used-to-call-the-api-has-been-unbound-from-the-backend-entity-node) |
| [100028](../errorcode-node.md#100028-current-node-is-not-on-the-main-node-tree) |

## createAnimation

```TypeScript
createAnimation(property: AnimationPropertyType, startValue: Optional<number[]>, endValue: number[], param: AnimateParam): boolean
```

Creates a property animation for the FrameNode.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FrameNode-createAnimation(property: AnimationPropertyType, startValue: Optional<number[]>, endValue: number[], param: AnimateParam): boolean--><!--Device-FrameNode-createAnimation(property: AnimationPropertyType, startValue: Optional<number[]>, endValue: number[], param: AnimateParam): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| property | [AnimationPropertyType](arkts-arkui-animationpropertytype-e.md) | Yes |
| startValue | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;number[]&gt; | Yes |
| endValue | number[] | Yes |
| param | [AnimateParam](../arkts-components/arkts-arkui-animateparam-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## createFrameNodes

```TypeScript
static createFrameNodes(uiContext: UIContext, count: number): FrameNode[]
```

Creates a specified number of FrameNodes in batches and returns a FrameNode array.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-FrameNode-static createFrameNodes(uiContext: UIContext, count: number): FrameNode[]--><!--Device-FrameNode-static createFrameNodes(uiContext: UIContext, count: number): FrameNode[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| count | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md)[] |

## dispose

```TypeScript
dispose(): void
```

Immediately releases the reference to the underlying FrameNode entity.

> **NOTE：**
> 
> - After the **dispose** API is called, the FrameNode object no longer corresponds to any entity FrameNode. In
> this case, attempts to call certain query APIs, such as [getMeasuredSize](arkts-arkui-framenode-c.md#getmeasuredsize) and
> [getLayoutPosition](arkts-arkui-framenode-c.md#getlayoutposition), will result in a JS crash in the application.
> 
> - To check whether the current FrameNode object corresponds to an entity FrameNode, you can use
> [getUniqueId](arkts-arkui-framenode-c.md#getuniqueid) API. A **UniqueId** value greater than 0 indicates that the object is
> associated with an entity FrameNode.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-dispose(): void--><!--Device-FrameNode-dispose(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disposeTree

```TypeScript
disposeTree(): void
```

Traverses down the tree and recursively releases the subtree with this node as the root.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-disposeTree(): void--><!--Device-FrameNode-disposeTree(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getChild

```TypeScript
getChild(index: number): FrameNode | null
```

Obtains the child node in the specified position of this node.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getChild(index: number): FrameNode | null--><!--Device-FrameNode-getChild(index: number): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) |

## getChild

```TypeScript
getChild(index: number, expandMode?: ExpandMode): FrameNode | null
```

Obtains a child node at a specified index from this FrameNode, with optional support for specifying the expansion mode of the child node.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FrameNode-getChild(index: number, expandMode?: ExpandMode): FrameNode | null--><!--Device-FrameNode-getChild(index: number, expandMode?: ExpandMode): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| expandMode | [ExpandMode](arkts-arkui-framenode-expandmode-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) |

## getChildrenCount

```TypeScript
getChildrenCount(): number
```

Obtains the number of child nodes of this FrameNode.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getChildrenCount(): number--><!--Device-FrameNode-getChildrenCount(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getChildrenCount

```TypeScript
getChildrenCount(countMode?: ChildrenCountMode): number
```

Obtains the number of child nodes of this FrameNode based on the specified counting mode.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-FrameNode-getChildrenCount(countMode?: ChildrenCountMode): int--><!--Device-FrameNode-getChildrenCount(countMode?: ChildrenCountMode): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| countMode | [ChildrenCountMode](arkts-arkui-framenode-childrencountmode-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getCrossLanguageOptions

```TypeScript
getCrossLanguageOptions(): CrossLanguageOptions
```

Obtains the cross-language access options for this FrameNode. For example, for nodes created using ArkTS, this API can obtain whether non-ArkTS languages are allowed to set the properties of these nodes and perform operations on the cross-language component tree. Since API version 26.0.0, this API can obtain whether non-ArkTS languages are allowed to perform operations on the component tree.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FrameNode-getCrossLanguageOptions(): CrossLanguageOptions--><!--Device-FrameNode-getCrossLanguageOptions(): CrossLanguageOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CrossLanguageOptions](arkts-arkui-framenode-crosslanguageoptions-i.md) |

## getCustomProperty

```TypeScript
getCustomProperty(name: string): Object | undefined
```

Obtains the component's custom property by its name.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getCustomProperty(name: string): Object | undefined--><!--Device-FrameNode-getCustomProperty(name: string): Object | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Object |

## getFirstChild

```TypeScript
getFirstChild(): FrameNode | null
```

Obtains the first child node of this FrameNode.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getFirstChild(): FrameNode | null--><!--Device-FrameNode-getFirstChild(): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) |

## getFirstChildIndexWithoutExpand

```TypeScript
getFirstChildIndexWithoutExpand(): number
```

Obtains the sequence number of the first child node of this node that is in the main node tree. The child node sequence numbers are calculated based on all child nodes.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FrameNode-getFirstChildIndexWithoutExpand(): number--><!--Device-FrameNode-getFirstChildIndexWithoutExpand(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getFrameNodeById

```TypeScript
getFrameNodeById(id: string): FrameNode | null
```

Searches for all child nodes layer by layer from the current node (which is used as the root node) and returns the first node that matches the specified ID. The search sequence is as follows: Search for direct child nodes first,then level-2 child nodes, and so on. The search stops as soon as a matching node is found.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-FrameNode-getFrameNodeById(id: string): FrameNode | null--><!--Device-FrameNode-getFrameNodeById(id: string): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) |

## getFrameNodeByUniqueId

```TypeScript
getFrameNodeByUniqueId(id: number): FrameNode | null
```

Searches for and returns the child node with the specified unique ID (which can be obtained using the  
[getUniqueId](arkts-arkui-framenode-c.md#getuniqueid) API) under the current node (which is used as the root node).

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-FrameNode-getFrameNodeByUniqueId(id: int): FrameNode | null--><!--Device-FrameNode-getFrameNodeByUniqueId(id: int): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) |

## getGlobalPositionOnDisplay

```TypeScript
getGlobalPositionOnDisplay(): Position
```

Obtains the position offset of this FrameNode relative to the global display, in vp.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FrameNode-getGlobalPositionOnDisplay(): Position--><!--Device-FrameNode-getGlobalPositionOnDisplay(): Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Position](arkts-arkui-position-t.md) |

## getId

```TypeScript
getId(): string
```

Obtains the node ID set by the user, which is the same as the value of the  
[component ID](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getId(): string--><!--Device-FrameNode-getId(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getInspectorInfo

```TypeScript
getInspectorInfo(): Object
```

Obtains the structure information of the node, which is consistent with what is found in DevEco Studio's built-in &lt;!--RP1--&gt;ArkUI Inspector &lt;!--RP1End--&gt;tool.

> **NOTE：**
> 
> The **getInspectorInfo** API is designed for debugging purposes to obtain information about all nodes. Frequent
> calls to this API may cause performance degradation.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getInspectorInfo(): Object--><!--Device-FrameNode-getInspectorInfo(): Object-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Object |

## getInteractionEventBindingInfo

```TypeScript
getInteractionEventBindingInfo(eventType: EventQueryType): InteractionEventBindingInfo | undefined
```

Obtains the event binding information for the target node. Returns **undefined** if the specified interaction event type is not bound to the component node.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-FrameNode-getInteractionEventBindingInfo(eventType: EventQueryType): InteractionEventBindingInfo | undefined--><!--Device-FrameNode-getInteractionEventBindingInfo(eventType: EventQueryType): InteractionEventBindingInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventType | [EventQueryType](arkts-arkui-eventquerytype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [InteractionEventBindingInfo](arkts-arkui-framenode-interactioneventbindinginfo-i.md) |

## getLastChildIndexWithoutExpand

```TypeScript
getLastChildIndexWithoutExpand(): number
```

Obtains the sequence number of the last child node of this node that is in the main node tree. The child node sequence numbers are calculated based on all child nodes.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FrameNode-getLastChildIndexWithoutExpand(): number--><!--Device-FrameNode-getLastChildIndexWithoutExpand(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getLayoutPosition

```TypeScript
getLayoutPosition(): Position
```

Obtains the position offset of this FrameNode relative to the parent component after layout, in px. The offset is the result of the parent component's layout on this node; therefore, the **offset** attribute that takes effect after layout and the **position** attribute that does not participate in layout do not affect this offset value.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getLayoutPosition(): Position--><!--Device-FrameNode-getLayoutPosition(): Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Position](arkts-arkui-position-t.md) |

## getMeasuredSize

```TypeScript
getMeasuredSize(): Size
```

Obtains the measured size of this FrameNode, in px.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getMeasuredSize(): Size--><!--Device-FrameNode-getMeasuredSize(): Size-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Size](arkts-arkui-graphics-size-i.md) |

## getNextSibling

```TypeScript
getNextSibling(): FrameNode | null
```

Obtains the next sibling node of this FrameNode.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getNextSibling(): FrameNode | null--><!--Device-FrameNode-getNextSibling(): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) |

## getNodePropertyValue

```TypeScript
getNodePropertyValue(property: AnimationPropertyType): number[]
```

Obtains the property value of the FrameNode.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FrameNode-getNodePropertyValue(property: AnimationPropertyType): number[]--><!--Device-FrameNode-getNodePropertyValue(property: AnimationPropertyType): number[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| property | [AnimationPropertyType](arkts-arkui-animationpropertytype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

## getNodeType

```TypeScript
getNodeType(): string
```

Obtains the type of the node. For built-in components, the node type corresponds to the component name. For example, the node type of the [Button](../../apis-arkui/arkts-components/arkts-arkui-button-i) component is **Button**. For custom components that implement rendering, the node type is **__Common__**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getNodeType(): string--><!--Device-FrameNode-getNodeType(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getOpacity

```TypeScript
getOpacity(): number
```

Obtains the opacity of the node. The minimum value is 0, and the maximum value is 1.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getOpacity(): number--><!--Device-FrameNode-getOpacity(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getParent

```TypeScript
getParent(): FrameNode | null
```

Obtains the parent node of this FrameNode.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getParent(): FrameNode | null--><!--Device-FrameNode-getParent(): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) |

## getPositionToParent

```TypeScript
getPositionToParent(): Position
```

Obtains the position offset of this FrameNode relative to the parent component, in vp.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getPositionToParent(): Position--><!--Device-FrameNode-getPositionToParent(): Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Position](arkts-arkui-position-t.md) |

## getPositionToParentWithTransform

```TypeScript
getPositionToParentWithTransform(): Position
```

Obtains the position offset of a FrameNode relative to its drawing-enabled parent component, in vp. Drawing attributes include [transform](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#transform) and  
[translate](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#translate). This API returns the upper left corner coordinates after component layout.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getPositionToParentWithTransform(): Position--><!--Device-FrameNode-getPositionToParentWithTransform(): Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Position](arkts-arkui-position-t.md) |

## getPositionToScreen

```TypeScript
getPositionToScreen(): Position
```

Obtains the position offset of this FrameNode relative to the screen, in vp.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getPositionToScreen(): Position--><!--Device-FrameNode-getPositionToScreen(): Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Position](arkts-arkui-position-t.md) |

## getPositionToScreenWithTransform

```TypeScript
getPositionToScreenWithTransform(): Position
```

Obtains the position offset of a FrameNode relative to the drawing-enabled screen, in vp. Drawing attributes include [transform](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#transform) and  
[translate](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#translate). This API returns the upper left corner coordinates after component layout.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getPositionToScreenWithTransform(): Position--><!--Device-FrameNode-getPositionToScreenWithTransform(): Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Position](arkts-arkui-position-t.md) |

## getPositionToWindow

```TypeScript
getPositionToWindow(): Position
```

Obtains the position offset of this FrameNode relative to the window, in vp.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getPositionToWindow(): Position--><!--Device-FrameNode-getPositionToWindow(): Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Position](arkts-arkui-position-t.md) |

## getPositionToWindowWithTransform

```TypeScript
getPositionToWindowWithTransform(): Position
```

Obtains the position offset of a FrameNode relative to the drawing-enabled window, in vp. Drawing attributes include [transform](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#transform) and  
[translate](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#translate). This API returns the upper left corner coordinates after component layout.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getPositionToWindowWithTransform(): Position--><!--Device-FrameNode-getPositionToWindowWithTransform(): Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Position](arkts-arkui-position-t.md) |

## getPreviousSibling

```TypeScript
getPreviousSibling(): FrameNode | null
```

Obtains the previous sibling node of this FrameNode.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getPreviousSibling(): FrameNode | null--><!--Device-FrameNode-getPreviousSibling(): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) |

## getRenderNode

```TypeScript
getRenderNode(): RenderNode | null
```

Obtains the [RenderNode](arkts-arkui-rendernode-c.md) held by the FrameNode.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getRenderNode(): RenderNode | null--><!--Device-FrameNode-getRenderNode(): RenderNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RenderNode](arkts-arkui-rendernode-c.md) |

## getUniqueId

```TypeScript
getUniqueId(): number
```

Obtains the system-assigned unique ID of the node.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getUniqueId(): number--><!--Device-FrameNode-getUniqueId(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getUserConfigBorderWidth

```TypeScript
getUserConfigBorderWidth(): Edges<LengthMetrics>
```

Obtains the border width set by the user.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getUserConfigBorderWidth(): Edges<LengthMetrics>--><!--Device-FrameNode-getUserConfigBorderWidth(): Edges<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Edges](arkts-arkui-graphics-edges-i.md)&lt;[LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)&gt; |

## getUserConfigMargin

```TypeScript
getUserConfigMargin(): Edges<LengthMetrics>
```

Obtains the margin set by the user.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getUserConfigMargin(): Edges<LengthMetrics>--><!--Device-FrameNode-getUserConfigMargin(): Edges<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Edges](arkts-arkui-graphics-edges-i.md)&lt;[LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)&gt; |

## getUserConfigPadding

```TypeScript
getUserConfigPadding(): Edges<LengthMetrics>
```

Obtains the padding set by the user.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getUserConfigPadding(): Edges<LengthMetrics>--><!--Device-FrameNode-getUserConfigPadding(): Edges<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Edges](arkts-arkui-graphics-edges-i.md)&lt;[LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)&gt; |

## getUserConfigSize

```TypeScript
getUserConfigSize(): SizeT<LengthMetrics>
```

Obtains the width and height set by the user.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-getUserConfigSize(): SizeT<LengthMetrics>--><!--Device-FrameNode-getUserConfigSize(): SizeT<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SizeT](arkts-arkui-graphics-sizet-i.md)&lt;[LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)&gt; |

## insertChildAfter

```TypeScript
insertChildAfter(child: FrameNode, sibling: FrameNode | null): void
```

Inserts a child node after the specified child node of this FrameNode. If this FrameNode is not modifiable, an exception is thrown.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-insertChildAfter(child: FrameNode, sibling: FrameNode | null): void--><!--Device-FrameNode-insertChildAfter(child: FrameNode, sibling: FrameNode | null): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| child | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| sibling | [FrameNode](arkts-arkui-framenode-c.md) \| null | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |
| [100025](../errorcode-node.md#100025-invalid-parameter-value) |

## invalidate

```TypeScript
invalidate(): void
```

Invalidates this FrameNode to trigger a re-rendering of the self-drawing content.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-invalidate(): void--><!--Device-FrameNode-invalidate(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## invalidateAttributes

```TypeScript
invalidateAttributes(): void
```

Forces immediate node property updates in this frame.

By default, property modifications applied after the build phase are deferred until the next frame.

This API ensures rendering synchronization by triggering immediate property updates.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-FrameNode-invalidateAttributes(): void--><!--Device-FrameNode-invalidateAttributes(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isAttached

```TypeScript
isAttached(): boolean
```

Obtains whether the node is mounted to the main node tree.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-isAttached(): boolean--><!--Device-FrameNode-isAttached(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isClipToFrame

```TypeScript
isClipToFrame(): boolean
```

Checks whether the node is clipped to the component area. This API returns **true** after the  
[dispose](arkts-arkui-framenode-c.md#dispose) API is called to release the reference to the FrameNode.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-isClipToFrame(): boolean--><!--Device-FrameNode-isClipToFrame(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isDisposed

```TypeScript
isDisposed(): boolean
```

Checks whether this FrameNode object has released its reference to its backend entity node. Frontend nodes maintain references to corresponding backend entity nodes. After a node calls the **dispose** API to release this reference,subsequent API calls may cause crashes or return default values. This API facilitates validation of node validity prior to operations, thereby mitigating risks in scenarios where calls after disposal are required.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FrameNode-isDisposed(): boolean--><!--Device-FrameNode-isDisposed(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isInRenderState

```TypeScript
isInRenderState(): boolean
```

Checks whether this node is in render state. A node is considered to be in render state when its corresponding RenderNode is present in the render tree.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FrameNode-isInRenderState(): boolean--><!--Device-FrameNode-isInRenderState(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isModifiable

```TypeScript
isModifiable(): boolean
```

Checks whether this FrameNode is modifiable.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-isModifiable(): boolean--><!--Device-FrameNode-isModifiable(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isOnMainTree

```TypeScript
isOnMainTree(): boolean
```

Queries whether a node is mounted to the main node tree.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FrameNode-isOnMainTree(): boolean--><!--Device-FrameNode-isOnMainTree(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [100026](../errorcode-node.md#100026-the-instance-object-used-to-call-the-api-has-been-unbound-from-the-backend-entity-node) |

## isTransferred

```TypeScript
isTransferred(): boolean
```

Returns a flag indicating whether the current FrameNode was obtained through dynamic-static conversion,includes conversions in both directions: dynamic-to-static and static-to-dynamic.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FrameNode-isTransferred(): boolean--><!--Device-FrameNode-isTransferred(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isVisible

```TypeScript
isVisible(): boolean
```

Obtains whether the node is visible.

> **NOTE：**
> 
> The visibility of a node is determined by the **visibility** attribute of the component.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-isVisible(): boolean--><!--Device-FrameNode-isVisible(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## layout

```TypeScript
layout(position: Position): void
```

Lays out this FrameNode, specifying the layout positions for the FrameNode and its child nodes. If the layout method is overridden, the overridden method is called. It is recommended that this API be called in  
[onLayout](arkts-arkui-framenode-c.md#onlayout).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-layout(position: Position): void--><!--Device-FrameNode-layout(position: Position): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | [Position](arkts-arkui-position-t.md) | Yes |

## measure

```TypeScript
measure(constraint: LayoutConstraint): void
```

Measures this FrameNode and calculates its size based on the layout constraints of the parent container. If the measurement method is overridden, the overridden method is called. It is recommended that this API be called in  
[onMeasure](arkts-arkui-framenode-c.md#onmeasure).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-measure(constraint: LayoutConstraint): void--><!--Device-FrameNode-measure(constraint: LayoutConstraint): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| constraint | [LayoutConstraint](arkts-arkui-framenode-layoutconstraint-i.md) | Yes |

## moveTo

```TypeScript
moveTo(targetParent: FrameNode, index?: number): void
```

Moves this FrameNode to a specified position within the target FrameNode. If this FrameNode is not modifiable, an exception is thrown. When **targetParent** is a [typeNode](arkts-arkui-typenode-n.md), the API validates the type or number of child nodes. If the validation fails, an exception is thrown. For specific limitations, see  
[typeNode](arkts-arkui-typenode-n.md).

> **NOTE：**
> 
> Currently, only the following types of [TypedFrameNode](arkts-arkui-framenode-typedframenode-i.md) are supported for the movement
> operations: [Stack](arkts-arkui-typenode-stack-t.md), [XComponent](arkts-arkui-typenode-xcomponent-t.md). This API does not work for
> other node types.
> 
> This API only supports [BuilderNode](arkts-arkui-buildernode-c.md) with root components of these types:
> [Stack](../../apis-arkui/arkts-components/arkts-arkui-stack-i), [XComponent](../../apis-arkui/arkts-components/arkts-arkui-xcomponent-i),
> [EmbeddedComponent](../../apis-arkui/arkts-components/arkts-arkui-embedded_component-i). This API does not work for other
> component types.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-FrameNode-moveTo(targetParent: FrameNode, index?: number): void--><!--Device-FrameNode-moveTo(targetParent: FrameNode, index?: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| targetParent | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| index | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |
| [100027](../errorcode-node.md#100027-the-current-node-has-been-adopted-as-a-child-node) |

## onDraw

```TypeScript
onDraw?(context: DrawContext): void
```

Implements custom drawing for the FrameNode. This API overrides the default drawing behavior and is invoked during FrameNode content rendering.

Note: The Canvas provided in the [DrawContext](arkts-arkui-graphics-drawcontext-c.md) parameter is a temporary command-recording canvas, not the actual rendering canvas of the node. For usage instructions, see  
[Adjusting the Transformation Matrix of the Custom Drawing Canvas](../../../ui/arkts-user-defined-arktsNode-frameNode.md#adjusting-the-transformation-matrix-of-the-custom-drawing-canvas).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-onDraw?(context: DrawContext): void--><!--Device-FrameNode-onDraw?(context: DrawContext): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [DrawContext](arkts-arkui-graphics-drawcontext-c.md) | Yes |

## onLayout

```TypeScript
onLayout(position: Position): void
```

Called when this FrameNode needs to determine its layout. This API provides custom layout and overrides the default layout method. It can be used to specify how the FrameNode and its child nodes are positioned and sized within the layout.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-onLayout(position: Position): void--><!--Device-FrameNode-onLayout(position: Position): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | [Position](arkts-arkui-position-t.md) | Yes |

## onMeasure

```TypeScript
onMeasure(constraint: LayoutConstraint): void
```

Called when this FrameNode needs to determine its size. This API provides custom measurement and overrides the default measurement method.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-onMeasure(constraint: LayoutConstraint): void--><!--Device-FrameNode-onMeasure(constraint: LayoutConstraint): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| constraint | [LayoutConstraint](arkts-arkui-framenode-layoutconstraint-i.md) | Yes |

## recycle

```TypeScript
recycle(): void
```

Triggers child component recycling in global reuse scenarios and fully releases FrameNode backend resources for reuse. This ensures efficient resource reclamation and reuse.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-FrameNode-recycle(): void--><!--Device-FrameNode-recycle(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## removeAdoptedChild

```TypeScript
removeAdoptedChild(child: FrameNode): void
```

Removes a previously-adopted affiliated node.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FrameNode-removeAdoptedChild(child: FrameNode): void--><!--Device-FrameNode-removeAdoptedChild(child: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| child | [FrameNode](arkts-arkui-framenode-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |
| [100025](../errorcode-node.md#100025-invalid-parameter-value) |
| [100026](../errorcode-node.md#100026-the-instance-object-used-to-call-the-api-has-been-unbound-from-the-backend-entity-node) |

## removeChild

```TypeScript
removeChild(node: FrameNode): void
```

Deletes the specified child node from this FrameNode. If this FrameNode is not modifiable, an exception is thrown.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-removeChild(node: FrameNode): void--><!--Device-FrameNode-removeChild(node: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) |

## removeSupportedUIStates

```TypeScript
removeSupportedUIStates(uiStates: number): void
```

Removes the state processing registration from the component.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FrameNode-removeSupportedUIStates(uiStates: number): void--><!--Device-FrameNode-removeSupportedUIStates(uiStates: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uiStates | number | Yes | UI states to be removed. &lt;br&gt;Multiple states can be specified simultaneously using bitwise OR operations, for example, **targetUIStates = UIState.PRESSED  \|

## reuse

```TypeScript
reuse(): void
```

Triggers child component reuse in global reuse scenarios to recycle FrameNode backend resources and improve resource utilization. To ensure adequate resource availability, call this API after the **recycle** API has been executed.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-FrameNode-reuse(): void--><!--Device-FrameNode-reuse(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setCrossLanguageOptions

```TypeScript
setCrossLanguageOptions(options: CrossLanguageOptions): void
```

Sets the cross-language access options for this FrameNode. For example, for nodes created using ArkTS, this API can set whether non-ArkTS languages are allowed to set the attributes of these nodes. Since API version 26.0.0, this API can set whether non-ArkTS languages are allowed to perform operations on the component tree. If the current FrameNode is not modifiable or does not support setting cross-language access options, an exception will be thrown.

> **NOTE：**
> 
> Currently, the cross-ArkTS language access option can only be configured for the following components:
> [Scroll](arkts-arkui-typenode-scroll-t.md), [Swiper](arkts-arkui-typenode-swiper-t.md), [List](arkts-arkui-typenode-list-t.md),
> [ListItem](arkts-arkui-typenode-listitem-t.md), [ListItemGroup](arkts-arkui-typenode-listitemgroup-t.md),
> [WaterFlow](arkts-arkui-typenode-waterflow-t.md), [FlowItem](arkts-arkui-typenode-flowitem-t.md), [Grid](arkts-arkui-typenode-grid-t.md),
> [GridItem](arkts-arkui-typenode-griditem-t.md), [TextInput](arkts-arkui-typenode-textinput-t.md), [TextArea](arkts-arkui-typenode-textarea-t.md),
> [Column](arkts-arkui-typenode-column-t.md), [Row](arkts-arkui-typenode-row-t.md), [Stack](arkts-arkui-typenode-stack-t.md),
> [Flex](arkts-arkui-typenode-flex-t.md), [RelativeContainer](arkts-arkui-typenode-relativecontainer-t.md),
> [Progress](arkts-arkui-typenode-progress-t.md), [LoadingProgress](arkts-arkui-typenode-loadingprogress-t.md),
> [Image](arkts-arkui-typenode-image-t.md), [Button](arkts-arkui-typenode-button-t.md), [CheckBox](arkts-arkui-typenode-checkbox-t.md),
> [Radio](arkts-arkui-typenode-radio-t.md), [Slider](arkts-arkui-typenode-slider-t.md), [Toggle](arkts-arkui-typenode-toggle-t.md), and
> [TypedFrameNode](arkts-arkui-framenode-typedframenode-i.md) of the [XComponent](arkts-arkui-typenode-xcomponent-t.md) type.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FrameNode-setCrossLanguageOptions(options: CrossLanguageOptions): void--><!--Device-FrameNode-setCrossLanguageOptions(options: CrossLanguageOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [CrossLanguageOptions](arkts-arkui-framenode-crosslanguageoptions-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100022](../errorcode-node.md#100022-crosslanguage-common-attribute-configuration-not-supported) |

## setLayoutPosition

```TypeScript
setLayoutPosition(position: Position): void
```

Sets the position of this FrameNode after layout. The default unit is PX.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-setLayoutPosition(position: Position): void--><!--Device-FrameNode-setLayoutPosition(position: Position): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | [Position](arkts-arkui-position-t.md) | Yes |

## setMeasuredSize

```TypeScript
setMeasuredSize(size: Size): void
```

Sets the measured size of this FrameNode. The default unit is PX. If the configured width or height values are negative, they are automatically set to 0.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-setMeasuredSize(size: Size): void--><!--Device-FrameNode-setMeasuredSize(size: Size): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | [Size](arkts-arkui-graphics-size-i.md) | Yes |

## setNeedsLayout

```TypeScript
setNeedsLayout(): void
```

Marks this FrameNode as needing layout, so that it will be relaid out in the next frame.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-setNeedsLayout(): void--><!--Device-FrameNode-setNeedsLayout(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## commonEvent

```TypeScript
get commonEvent(): UICommonEvent
```

Obtains the **UICommonEvent** object held in this FrameNode to set basic events. The set basic events will compete with declaratively defined events for event handling without overriding them. If both event callbacks are registered, the declaratively defined event callback takes precedence.

In scenarios involving **LazyForEach**, where nodes may be destroyed and reconstructed, you need to reset or re-attach event listeners to the newly created nodes to ensure they respond to events correctly.

**Type:** [UICommonEvent](../arkts-components/arkts-arkui-uicommonevent-i.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameNode-get commonEvent(): UICommonEvent--><!--Device-FrameNode-get commonEvent(): UICommonEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gestureEvent

```TypeScript
get gestureEvent(): UIGestureEvent
```

Obtains the **UIGestureEvent** object held by this FrameNode, which is used to set gesture events bound to the component. Gesture events set using the **gestureEvent** API will not override gestures bound using the  
[gesture binding API](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md). If both APIs are used to set gestures, the gesture binding API takes precedence.

**Type:** [UIGestureEvent](../arkts-components/arkts-arkui-uigestureevent-i.md)

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-FrameNode-get gestureEvent(): UIGestureEvent--><!--Device-FrameNode-get gestureEvent(): UIGestureEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
