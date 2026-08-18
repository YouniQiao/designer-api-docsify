# FrameNode

Defines FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class FrameNode--><!--Device-unnamed-export declare class FrameNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addComponentContent

```TypeScript
addComponentContent<T>(content: ComponentContent<T> | ReactiveComponentContent): void
```

Mount ComponentContent to FrameNode. On API 26.0.0 and above, It can also mount ComponentContent and ReactiveComponentContent to FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-addComponentContent<T>(content: ComponentContent<T> | ReactiveComponentContent): void--><!--Device-FrameNode-addComponentContent<T>(content: ComponentContent<T> | ReactiveComponentContent): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [ComponentContent](../../apis-arkui/arkts-apis/arkts-arkui-componentcontent-c.md)&lt;T&gt; \| [ReactiveComponentContent](../../apis-arkui/arkts-apis/arkts-arkui-componentcontent-reactivecomponentcontent-c.md) | Yes | Newly added ComponentContent.<br>**Since:** 23 - 24 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100021](../../apis-arkui/errorcode-node.md#100021-framenode-not-modifiable) | The FrameNode is not modifiable. |

## addSupportedUIStates

```TypeScript
addSupportedUIStates(uiStates: int, statesChangeHandler: UIStatesChangeHandler, excludeInner?: boolean): void
```

Sets the polymorphic style states supported by the component. To improve efficiency, you need to pass the states of interest and their corresponding handler functions. When the state changes, the handler function will be executed. You can update the UI style based on the current state in the callback. For certain types of control nodes, the system has default style handling for some states (e.g., the button component has default style changes for the PRESSED state). When using this method to customize state handling for such components, the system's default style changes will be applied first, followed by the custom styles. The final effect is a combination of both. You can set `excludeInner` to `true` to disable the system's default style handling, though this depends on system implementation. When calling this method, the provided `handler` function will be executed immediately. You do not need to explicitly register a handler for the NORMAL state. If you register handlers for non-NORMAL states, the system will automatically call the handler when the state reverts to NORMAL, allowing you to restore the UI style.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-addSupportedUIStates(uiStates: int, statesChangeHandler: UIStatesChangeHandler, excludeInner?: boolean): void--><!--Device-FrameNode-addSupportedUIStates(uiStates: int, statesChangeHandler: UIStatesChangeHandler, excludeInner?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiStates | int | Yes | The target UI states the node needs to handle. Multiple states can be combined using the OR operation, e.g., `targetUIStates = UIState.PRESSED \| UIState.FOCUSED`. |
| statesChangeHandler | [UIStatesChangeHandler](../../apis-arkui/arkts-apis/arkts-arkui-uistateschangehandler-t.md) | Yes | The handler function for UI state changes. |
| excludeInner | boolean | No | =false] - A flag to disable the system's default style handling for states. |

## adoptChild

```TypeScript
adoptChild(child: FrameNode): void
```

The current node adopts the target child node. The node being adopted must not have an existing parent node. This operation does not actually append it as a child, but only allows it to receive life-cycle callbacks as if it were a child.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-adoptChild(child: FrameNode): void--><!--Device-FrameNode-adoptChild(child: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| child | [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Yes | the target node being adopted. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100021](../../apis-arkui/errorcode-node.md#100021-framenode-not-modifiable) | The current FrameNode is not modifiable. |
| [100025](../../apis-arkui/errorcode-node.md#100025-invalid-parameter-value) | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'child' is invalid: it cannot be disposed." |
| [100026](../../apis-arkui/errorcode-node.md#100026-the-instance-object-used-to-call-the-api-has-been-unbound-from-the-backend-entity-node) | The current FrameNode has been disposed. |

## appendChild

```TypeScript
appendChild(node: FrameNode): void
```

Add child to the end of the FrameNode's children. If this FrameNode is not modifiable, an exception is thrown. When appendChild is called, typeNode validates the type or number of child nodes. If the validation fails, an exception is thrown. For specific limitations, see typeNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-appendChild(node: FrameNode): void--><!--Device-FrameNode-appendChild(node: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Yes | The node will be added. The child node cannot be one created declaratively, which is not modifiable. Only declarative nodes obtained from a BuilderNode can be used as child nodes. If the child node does not meet the specifications, an exception is thrown. The FrameNode cannot have a parent node. Otherwise, an exception is thrown. The node cannot be adopted. Otherwise, an exception is thrown. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100021](../../apis-arkui/errorcode-node.md#100021-framenode-not-modifiable) | The FrameNode is not modifiable. |
| [100025](../../apis-arkui/errorcode-node.md#100025-invalid-parameter-value) | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'node' is invalid: it cannot be adopted." |

## cancelAnimations

```TypeScript
cancelAnimations(properties: AnimationPropertyType[]): boolean
```

Request to cancel all animations on specified properties. It blocks synchronously to wait for the cancellation result. If the cancellation is successful, the corresponding properties on the node are restored to the cancelled value.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-cancelAnimations(properties: AnimationPropertyType[]): boolean--><!--Device-FrameNode-cancelAnimations(properties: AnimationPropertyType[]): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| properties | [AnimationPropertyType](arkts-na-enums-animationpropertytype-e.md)[] | Yes | animation property types to cancel. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | whether the cancel operation is successful. For example, if ipc fails, canceling the animation fails. |

## clearChildren

```TypeScript
clearChildren(): void
```

Clear children of the current FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-clearChildren(): void--><!--Device-FrameNode-clearChildren(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100021](../../apis-arkui/errorcode-node.md#100021-framenode-not-modifiable) | The FrameNode is not modifiable. |

## constructor

```TypeScript
constructor(uiContext: UIContext, options?: FrameNodeOptions)
```

Constructor.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-constructor(uiContext: UIContext, options?: FrameNodeOptions)--><!--Device-FrameNode-constructor(uiContext: UIContext, options?: FrameNodeOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiContext | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode |
| options | [FrameNodeOptions](arkts-na-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation<br>**Since:** 26.0.0 |

## convertPosition

```TypeScript
convertPosition(position: NodePosition, targetNode: FrameNode): NodePosition
```

Converts a point's coordinates from the current node's coordinate system to the target node's coordinate system.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-convertPosition(position: NodePosition, targetNode: FrameNode): NodePosition--><!--Device-FrameNode-convertPosition(position: NodePosition, targetNode: FrameNode): NodePosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | [NodePosition](arkts-na-nodeposition-t.md) | Yes | The point's coordinates in the current node's local coordinate system. |
| targetNode | [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Yes | The destination node whose coordinate system will be used for conversion. |

**Return value:**

| Type | Description |
| --- | --- |
| [NodePosition](arkts-na-nodeposition-t.md) | The converted coordinates in the target node's local coordinate system. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100025](../../apis-arkui/errorcode-node.md#100025-invalid-parameter-value) | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'targetNode' is invalid: it cannot be disposed." |
| [100024](../../apis-arkui/errorcode-node.md#100024-no-common-ancestor-node-between-nodes) | The current FrameNode and the target FrameNode do not have a common ancestor node. |

## convertPositionFromWindow

```TypeScript
convertPositionFromWindow(positionByWindow: NodePosition): NodePosition
```

Converts a point's coordinates from the current window's coordinate system to the current node's coordinate system.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-convertPositionFromWindow(positionByWindow: NodePosition): NodePosition--><!--Device-FrameNode-convertPositionFromWindow(positionByWindow: NodePosition): NodePosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| positionByWindow | [NodePosition](arkts-na-nodeposition-t.md) | Yes | The point's coordinates in the current window's coordinate system. |

**Return value:**

| Type | Description |
| --- | --- |
| [NodePosition](arkts-na-nodeposition-t.md) | The converted coordinates in the current node's local coordinate system. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100026](../../apis-arkui/errorcode-node.md#100026-the-instance-object-used-to-call-the-api-has-been-unbound-from-the-backend-entity-node) | The current FrameNode has been disposed. |
| [100028](../../apis-arkui/errorcode-node.md#100028-current-node-is-not-on-the-main-node-tree) | The current FrameNode is not on the main tree. |

## convertPositionToWindow

```TypeScript
convertPositionToWindow(positionByLocal: NodePosition): NodePosition
```

Converts a point's coordinates from the current node's coordinate system to the current window's coordinate system.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-convertPositionToWindow(positionByLocal: NodePosition): NodePosition--><!--Device-FrameNode-convertPositionToWindow(positionByLocal: NodePosition): NodePosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| positionByLocal | [NodePosition](arkts-na-nodeposition-t.md) | Yes | The point's coordinates in the current node's local coordinate system. |

**Return value:**

| Type | Description |
| --- | --- |
| [NodePosition](arkts-na-nodeposition-t.md) | The converted coordinates in the current window's coordinate system. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100026](../../apis-arkui/errorcode-node.md#100026-the-instance-object-used-to-call-the-api-has-been-unbound-from-the-backend-entity-node) | The current FrameNode has been disposed. |
| [100028](../../apis-arkui/errorcode-node.md#100028-current-node-is-not-on-the-main-node-tree) | The current FrameNode is not on the main tree. |

## createAnimation

```TypeScript
createAnimation(property: AnimationPropertyType, startValue: double[] | undefined, endValue: double[], param: AnimateParam): boolean
```

create property animation in FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-createAnimation(property: AnimationPropertyType, startValue: double[] | undefined, endValue: double[], param: AnimateParam): boolean--><!--Device-FrameNode-createAnimation(property: AnimationPropertyType, startValue: double[] | undefined, endValue: double[], param: AnimateParam): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| property | [AnimationPropertyType](arkts-na-enums-animationpropertytype-e.md) | Yes | enumeration of property that produces the animation. |
| startValue | double[] \| undefined | Yes | start value of animation. Undefined means that the last final value is used as the starting value of the animation, and it is recommended to set undefined if the property already has a value. |
| endValue | double[] | Yes | end value of animation. |
| param | AnimateParam | Yes | param of animation. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | whether the createAnimation operation is successful. For example, if the array lengths of startValue and endValue do not match the data lengths required by type, creating animation fails. |

## createFrameNodes

```TypeScript
static createFrameNodes(uiContext: UIContext, count: int): FrameNode[]
```

Create a specified number of FrameNode objects and return them.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-static createFrameNodes(uiContext: UIContext, count: int): FrameNode[]--><!--Device-FrameNode-static createFrameNodes(uiContext: UIContext, count: int): FrameNode[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiContext | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode |
| count | int | Yes | the number of FrameNode objects to create. Returns an empty array if count &lt;= 0 or is not an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md)[] | the array of created FrameNode objects. |

## dispose

```TypeScript
dispose(): void
```

Dispose the FrameNode immediately.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-dispose(): void--><!--Device-FrameNode-dispose(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disposeTree

```TypeScript
disposeTree(): void
```

Detach from parent and dispose all child recursively.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-disposeTree(): void--><!--Device-FrameNode-disposeTree(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getChild

```TypeScript
getChild(index: int, expandMode?: ExpandMode | undefined): FrameNode | null
```

Get a child of the current FrameNode by index.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getChild(index: int, expandMode?: ExpandMode | undefined): FrameNode | null--><!--Device-FrameNode-getChild(index: int, expandMode?: ExpandMode | undefined): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index of the desired node in the children of FrameNode. |
| expandMode | [ExpandMode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-expandmode-e.md) \| undefined | No | The expand mode. Default value is ExpandMode.EXPAND. |

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Returns a FrameNode. When the required node does not exist, returns null. |

## getChildrenCount

```TypeScript
getChildrenCount(): int
```

Get the children count of the current FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getChildrenCount(): int--><!--Device-FrameNode-getChildrenCount(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the number of the children of the current FrameNode. |

## getChildrenCount

```TypeScript
getChildrenCount(countMode?: ChildrenCountMode): int
```

Get the children count of the current FrameNode with specified count mode.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getChildrenCount(countMode?: ChildrenCountMode): int--><!--Device-FrameNode-getChildrenCount(countMode?: ChildrenCountMode): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| countMode | [ChildrenCountMode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-childrencountmode-e.md) | No | The children count mode. Default value is ChildrenCountMode.ALL_EXPAND. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the number of children of the current FrameNode based on the count mode. |

## getCrossLanguageOptions

```TypeScript
getCrossLanguageOptions(): CrossLanguageOptions
```

Get the cross-language options of the target FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getCrossLanguageOptions(): CrossLanguageOptions--><!--Device-FrameNode-getCrossLanguageOptions(): CrossLanguageOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [CrossLanguageOptions](../../apis-arkui/arkts-apis/arkts-arkui-framenode-crosslanguageoptions-i.md) | Returns the cross-language options of the target FrameNode. |

## getCustomProperty

```TypeScript
getCustomProperty(name: string): CustomProperty
```

Get the custom property of the component corresponding to this FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getCustomProperty(name: string): CustomProperty--><!--Device-FrameNode-getCustomProperty(name: string): CustomProperty-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | the name of the custom property. |

**Return value:**

| Type | Description |
| --- | --- |
| CustomProperty | Returns the value of the custom property. |

## getFirstChild

```TypeScript
getFirstChild(): FrameNode | null
```

Get the first child of the current FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getFirstChild(): FrameNode | null--><!--Device-FrameNode-getFirstChild(): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Returns a FrameNode, which is first child of the current FrameNode. If current FrameNode does not have child node, returns null. If current FrameNode does not have child node, returns null. |

## getFirstChildIndexWithoutExpand

```TypeScript
getFirstChildIndexWithoutExpand(): int
```

Get the index of the current FrameNode's first child node which is on the tree.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getFirstChildIndexWithoutExpand(): int--><!--Device-FrameNode-getFirstChildIndexWithoutExpand(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the index of the current FrameNode's first child node which is on the tree. |

## getFrameNodeById

```TypeScript
getFrameNodeById(id: string): FrameNode | null
```

Get FrameNode by id.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getFrameNodeById(id: string): FrameNode | null--><!--Device-FrameNode-getFrameNodeById(id: string): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | The id of FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | The first child node with the specified ID, or null if not found. |

## getFrameNodeByUniqueId

```TypeScript
getFrameNodeByUniqueId(id: int): FrameNode | null
```

Get FrameNode by uniqueId. Obtains the entity node, FrameNode, of a component on the component tree using its uniqueId. The return value depends on the type of component associated with the uniqueId. 1. If the uniqueId corresponds to a built-in component, the associated FrameNode is returned. 2. If the uniqueId corresponds to a custom component: If the component has rendered content, its root node is returned, with the type __Common__; if the component has no rendered content, the FrameNode of its first child component is returned. 3. If the uniqueId does not correspond to any component, null is returned.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getFrameNodeByUniqueId(id: int): FrameNode | null--><!--Device-FrameNode-getFrameNodeByUniqueId(id: int): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | int | Yes | The uniqueId of the FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | The FrameNode with the target uniqueId, or null if the frameNode is not existed. |

## getGlobalPositionOnDisplay

```TypeScript
getGlobalPositionOnDisplay(): NodePosition
```

Get the position of the node relative to unified display, in vp.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getGlobalPositionOnDisplay(): NodePosition--><!--Device-FrameNode-getGlobalPositionOnDisplay(): NodePosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NodePosition](arkts-na-nodeposition-t.md) | Returns position of the node relative to unified display, in vp. |

## getId

```TypeScript
getId(): string
```

Get the id of the FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getId(): string--><!--Device-FrameNode-getId(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns the id of the FrameNode. |

## getInspectorInfo

```TypeScript
getInspectorInfo(): Object
```

Get the inspector information of the FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getInspectorInfo(): Object--><!--Device-FrameNode-getInspectorInfo(): Object-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Object | Returns the inspector information of the FrameNode. |

## getInteractionEventBindingInfo

```TypeScript
getInteractionEventBindingInfo(eventType: EventQueryType): InteractionEventBindingInfo | undefined
```

Gets event binding information of the target node.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getInteractionEventBindingInfo(eventType: EventQueryType): InteractionEventBindingInfo | undefined--><!--Device-FrameNode-getInteractionEventBindingInfo(eventType: EventQueryType): InteractionEventBindingInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | [EventQueryType](arkts-na-enums-eventquerytype-e.md) | Yes | The interaction event type to be queried. |

**Return value:**

| Type | Description |
| --- | --- |
| [InteractionEventBindingInfo](../../apis-arkui/arkts-apis/arkts-arkui-framenode-interactioneventbindinginfo-i.md) | Returns one InteractionEventBindingInfo object indicating the event binding details if any interaction events binded on current node, returns undefined if no one binded on. |

## getLastChildIndexWithoutExpand

```TypeScript
getLastChildIndexWithoutExpand(): int
```

Get the index of the current FrameNode's last child node which is on the tree.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getLastChildIndexWithoutExpand(): int--><!--Device-FrameNode-getLastChildIndexWithoutExpand(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the index of the current FrameNode's last child node which is on the tree. |

## getLayoutPosition

```TypeScript
getLayoutPosition(): NodePosition
```

Get the offset to the parent of the FrameNode after layout, with unit PX.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getLayoutPosition(): NodePosition--><!--Device-FrameNode-getLayoutPosition(): NodePosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NodePosition](arkts-na-nodeposition-t.md) | Returns the offset to the parent of the FrameNode after layout, with unit PX. |

## getMeasuredSize

```TypeScript
getMeasuredSize(): Size
```

Get the size of the FrameNode after measure, with unit PX.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getMeasuredSize(): Size--><!--Device-FrameNode-getMeasuredSize(): Size-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Size](arkts-na-graphics-size-i.md) | Returns the size of the FrameNode after measure, with unit PX. |

## getNextSibling

```TypeScript
getNextSibling(): FrameNode | null
```

Get the next sibling node of the current FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getNextSibling(): FrameNode | null--><!--Device-FrameNode-getNextSibling(): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Returns a FrameNode. If current FrameNode does not have next sibling node, returns null. |

## getNodePropertyValue

```TypeScript
getNodePropertyValue(property: AnimationPropertyType): double[]
```

get property value from node.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getNodePropertyValue(property: AnimationPropertyType): double[]--><!--Device-FrameNode-getNodePropertyValue(property: AnimationPropertyType): double[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| property | [AnimationPropertyType](arkts-na-enums-animationpropertytype-e.md) | Yes | animation property type to get value. |

**Return value:**

| Type | Description |
| --- | --- |
| double[] | the property value on the node. |

## getNodeType

```TypeScript
getNodeType(): string
```

Get the type of the FrameNode. The type is the name of component, for example, the nodeType of Button is "Button", and the nodeType of custom component is "__Common__".

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getNodeType(): string--><!--Device-FrameNode-getNodeType(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns the type of the FrameNode. |

## getOpacity

```TypeScript
getOpacity(): double
```

Get the opacity of the FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getOpacity(): double--><!--Device-FrameNode-getOpacity(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double | Returns the opacity of the FrameNode. |

## getParent

```TypeScript
getParent(): FrameNode | null
```

Get the parent node of the current FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getParent(): FrameNode | null--><!--Device-FrameNode-getParent(): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Returns a FrameNode. If current FrameNode does not have parent node, returns null. |

## getPositionToParent

```TypeScript
getPositionToParent(): NodePosition
```

Get the position of the node relative to its parent.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getPositionToParent(): NodePosition--><!--Device-FrameNode-getPositionToParent(): NodePosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NodePosition](arkts-na-nodeposition-t.md) | Returns position of the node relative to its parent. |

## getPositionToParentWithTransform

```TypeScript
getPositionToParentWithTransform(): NodePosition
```

Get the position of the node relative to its parent with transform.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getPositionToParentWithTransform(): NodePosition--><!--Device-FrameNode-getPositionToParentWithTransform(): NodePosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NodePosition](arkts-na-nodeposition-t.md) | Returns position of the node relative to its parent with transform. |

## getPositionToScreen

```TypeScript
getPositionToScreen(): NodePosition
```

Get the position of the node relative to screen.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getPositionToScreen(): NodePosition--><!--Device-FrameNode-getPositionToScreen(): NodePosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NodePosition](arkts-na-nodeposition-t.md) | Returns position of the node relative to screen. |

## getPositionToScreenWithTransform

```TypeScript
getPositionToScreenWithTransform(): NodePosition
```

Get the position of the node relative to screen with transform.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getPositionToScreenWithTransform(): NodePosition--><!--Device-FrameNode-getPositionToScreenWithTransform(): NodePosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NodePosition](arkts-na-nodeposition-t.md) | Returns position of the node relative to screen with transform. |

## getPositionToWindow

```TypeScript
getPositionToWindow(): NodePosition
```

Get the position of the node relative to window.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getPositionToWindow(): NodePosition--><!--Device-FrameNode-getPositionToWindow(): NodePosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NodePosition](arkts-na-nodeposition-t.md) | Returns position of the node relative to window. |

## getPositionToWindowWithTransform

```TypeScript
getPositionToWindowWithTransform(): NodePosition
```

Get the position of the node relative to window with transform.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getPositionToWindowWithTransform(): NodePosition--><!--Device-FrameNode-getPositionToWindowWithTransform(): NodePosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NodePosition](arkts-na-nodeposition-t.md) | Returns position of the node relative to window with transform. |

## getPreviousSibling

```TypeScript
getPreviousSibling(): FrameNode | null
```

Get the previous sibling node of the current FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getPreviousSibling(): FrameNode | null--><!--Device-FrameNode-getPreviousSibling(): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Returns a FrameNode. If current FrameNode does not have previous sibling node, returns null. |

## getRenderNode

```TypeScript
getRenderNode(): RenderNode | null
```

Get the RenderNode in FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getRenderNode(): RenderNode | null--><!--Device-FrameNode-getRenderNode(): RenderNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RenderNode](arkts-na-rendernode-c.md) | Returns a RenderNode inside the FrameNode, or null if not contained. |

## getUniqueId

```TypeScript
getUniqueId(): int
```

Get the unique id of the FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getUniqueId(): int--><!--Device-FrameNode-getUniqueId(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the unique id of the FrameNode. |

## getUserConfigBorderWidth

```TypeScript
getUserConfigBorderWidth(): NodeEdges<LengthMetrics>
```

Get the user config border width of the FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getUserConfigBorderWidth(): NodeEdges<LengthMetrics>--><!--Device-FrameNode-getUserConfigBorderWidth(): NodeEdges<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NodeEdges](arkts-na-graphics-nodeedges-i.md)&lt;[LengthMetrics](arkts-na-graphics-lengthmetrics-c.md)&gt; | Returns the user config border width of the FrameNode. |

## getUserConfigMargin

```TypeScript
getUserConfigMargin(): NodeEdges<LengthMetrics>
```

Get the user config margin of the FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getUserConfigMargin(): NodeEdges<LengthMetrics>--><!--Device-FrameNode-getUserConfigMargin(): NodeEdges<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NodeEdges](arkts-na-graphics-nodeedges-i.md)&lt;[LengthMetrics](arkts-na-graphics-lengthmetrics-c.md)&gt; | Returns the user config margin of the FrameNode. |

## getUserConfigPadding

```TypeScript
getUserConfigPadding(): NodeEdges<LengthMetrics>
```

Get the user config padding of the FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getUserConfigPadding(): NodeEdges<LengthMetrics>--><!--Device-FrameNode-getUserConfigPadding(): NodeEdges<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NodeEdges](arkts-na-graphics-nodeedges-i.md)&lt;[LengthMetrics](arkts-na-graphics-lengthmetrics-c.md)&gt; | Returns the user config padding of the FrameNode. |

## getUserConfigSize

```TypeScript
getUserConfigSize(): SizeT<LengthMetrics>
```

Get the user config size of the FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-getUserConfigSize(): SizeT<LengthMetrics>--><!--Device-FrameNode-getUserConfigSize(): SizeT<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [SizeT](arkts-na-graphics-sizet-i.md)&lt;[LengthMetrics](arkts-na-graphics-lengthmetrics-c.md)&gt; | Returns the user config size of the FrameNode. |

## insertChildAfter

```TypeScript
insertChildAfter(child: FrameNode, sibling: FrameNode | null): void
```

Add child to the current FrameNode. If this FrameNode is not modifiable, an exception is thrown.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-insertChildAfter(child: FrameNode, sibling: FrameNode | null): void--><!--Device-FrameNode-insertChildAfter(child: FrameNode, sibling: FrameNode | null): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| child | [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Yes | The node will be added. The child node cannot be a declarative node, that is, a FrameNode that cannot be modified. Only declarative nodes obtained from a BuilderNode can be used as child nodes. If the child node does not meet the specifications, an exception is thrown. The child node cannot have a parent node. Otherwise, an exception is thrown. The child node cannot be adopted. Otherwise, an exception is thrown. |
| sibling | [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) \| null | Yes | The new node is added after this node. When sibling is null, insert node as the first children of the node. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100021](../../apis-arkui/errorcode-node.md#100021-framenode-not-modifiable) | The FrameNode is not modifiable. |
| [100025](../../apis-arkui/errorcode-node.md#100025-invalid-parameter-value) | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'child' is invalid: it cannot be adopted." |

## invalidate

```TypeScript
invalidate(): void
```

Invalidate the RenderNode in the FrameNode, which will cause a re-render of the RenderNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-invalidate(): void--><!--Device-FrameNode-invalidate(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## invalidateAttributes

```TypeScript
invalidateAttributes(): void
```

Triggers node updates in the current frame. When node attributes are modified after the current frame's build phase, the node updates will be deferred to the next frame. This function forces immediate node updates within the current frame to ensure rendering effects are applied synchronously.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-invalidateAttributes(): void--><!--Device-FrameNode-invalidateAttributes(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isAttached

```TypeScript
isAttached(): boolean
```

Get if the FrameNode is attached to the root node tree.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-isAttached(): boolean--><!--Device-FrameNode-isAttached(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns if the FrameNode is attached to the root node tree. |

## isClipToFrame

```TypeScript
isClipToFrame(): boolean
```

Get if the FrameNode is clip to frame.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-isClipToFrame(): boolean--><!--Device-FrameNode-isClipToFrame(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns if the FrameNode is clip to frame. |

## isDisposed

```TypeScript
isDisposed(): boolean
```

Get if the FrameNode is disposed.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-isDisposed(): boolean--><!--Device-FrameNode-isDisposed(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the FrameNode is disposed, false otherwise. |

## isInRenderState

```TypeScript
isInRenderState(): boolean
```

Get if the FrameNode is in the render state. A FrameNode is considered to be in the render state if its corresponding RenderNode is on the render tree.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-isInRenderState(): boolean--><!--Device-FrameNode-isInRenderState(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns whether the node is in the render state. True indicates it is in the render state, while false indicates it is not. |

## isMinimized

```TypeScript
isMinimized(): boolean
```

Get whether the current FrameNode is a minimized FrameNode.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-isMinimized(): boolean--><!--Device-FrameNode-isMinimized(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true when the current FrameNode is a minimized FrameNode, otherwise returns false. |

## isModifiable

```TypeScript
isModifiable(): boolean
```

Return a flag to indicate whether the current FrameNode can be modified. Indicates whether the FrameNode supports appendChild, insertChildAfter, removeChild, clearChildren.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-isModifiable(): boolean--><!--Device-FrameNode-isModifiable(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the FrameNode can be modified, otherwise return false. |

## isOnMainTree

```TypeScript
isOnMainTree(): boolean
```

Get if the FrameNode is attached to the root node tree.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-isOnMainTree(): boolean--><!--Device-FrameNode-isOnMainTree(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns if the FrameNode is attached to the root node tree. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100026](../../apis-arkui/errorcode-node.md#100026-the-instance-object-used-to-call-the-api-has-been-unbound-from-the-backend-entity-node) | The current FrameNode has been disposed. |

## isTransferred

```TypeScript
isTransferred(): boolean
```

Returns a flag indicating whether the current FrameNode was obtained through dynamic-static conversion, includes conversions in both directions: dynamic-to-static and static-to-dynamic.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-isTransferred(): boolean--><!--Device-FrameNode-isTransferred(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the FrameNode was converted between dynamic and static states, otherwise, returns false. |

## isVisible

```TypeScript
isVisible(): boolean
```

Get if the FrameNode is visible.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-isVisible(): boolean--><!--Device-FrameNode-isVisible(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns if the FrameNode is visible. |

## layout

```TypeScript
layout(position: NodePosition): void
```

This is called to assign position to the FrameNode and all of its descendants. The position is used to init the position of the frameNode, and the actual layout work of FrameNode is performed in onLayout or the default layout method.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-layout(position: NodePosition): void--><!--Device-FrameNode-layout(position: NodePosition): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | [NodePosition](arkts-na-nodeposition-t.md) | Yes | The position of the node, will be used when executed the layout method. |

## measure

```TypeScript
measure(constraint: LayoutConstraint): void
```

This is called to find out how big the FrameNode should be. The parent node supplies constraint information. The actual measurement work of the FrameNode is performed in onMeasure or the default measure method.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-measure(constraint: LayoutConstraint): void--><!--Device-FrameNode-measure(constraint: LayoutConstraint): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| constraint | [LayoutConstraint](../../apis-arkui/arkts-apis/arkts-arkui-framenode-layoutconstraint-i.md) | Yes | The layout constraint of the node, supplied by the parent node. |

## moveTo

```TypeScript
moveTo(targetParent: FrameNode, index?: int): void
```

Move node to the target Framenode as child. If this FrameNode is not modifiable, an exception is thrown. When targetParent is a typeNode, the API validates the type or number of child nodes. If the validation fails, an exception is thrown. For specific limitations, see typeNode. If this FrameNode is adopted, an exception is thrown. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Currently, only the following types of TypedFrameNode are supported for the movement operations: Stack, XComponent. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-moveTo(targetParent: FrameNode, index?: int): void--><!--Device-FrameNode-moveTo(targetParent: FrameNode, index?: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetParent | [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Yes | The target parent node. The target parent node must not be a declaratively created node, that is, a FrameNode that is not modifiable. If it does not meet the specifications, an exception is thrown. |
| index | int | No | The index which the node is moved to. If the value is a negative number or invalid, the node is moved to the end of the target parent node. Moves to the end of the target parent node by default. If the target FrameNode has n nodes, the value range for index is [0, n). <br>Default value: -1 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100021](../../apis-arkui/errorcode-node.md#100021-framenode-not-modifiable) | The FrameNode is not modifiable. |
| [100027](../../apis-arkui/errorcode-node.md#100027-the-current-node-has-been-adopted-as-a-child-node) | The current node has been adopted. |

## onDraw

```TypeScript
onDraw(context: DrawContext): void
```

Draw Method. Executed when the current FrameNode is rendering its content.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-onDraw(context: DrawContext): void--><!--Device-FrameNode-onDraw(context: DrawContext): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [DrawContext](arkts-na-graphics-drawcontext-c.md) | Yes | The DrawContext will be used when executed draw method. |

## onLayout

```TypeScript
onLayout(position: NodePosition): void
```

Method to assign a position to the FrameNode and each of its children. Use this method to override the default layout method.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-onLayout(position: NodePosition): void--><!--Device-FrameNode-onLayout(position: NodePosition): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | [NodePosition](arkts-na-nodeposition-t.md) | Yes | The position of the node, will be used when executed layout method. |

## onMeasure

```TypeScript
onMeasure(constraint: LayoutConstraint): void
```

Method to measure the FrameNode and its content to determine the measured size. Use this method to override the default measure method when measuring the FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-onMeasure(constraint: LayoutConstraint): void--><!--Device-FrameNode-onMeasure(constraint: LayoutConstraint): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| constraint | [LayoutConstraint](../../apis-arkui/arkts-apis/arkts-arkui-framenode-layoutconstraint-i.md) | Yes | The layout constraint of the node, will be used when executed measure method. |

## recycle

```TypeScript
recycle(): void
```

Recycle current FrameNode From JsFrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-recycle(): void--><!--Device-FrameNode-recycle(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## removeAdoptedChild

```TypeScript
removeAdoptedChild(child: FrameNode): void
```

Remove the target adopted child node.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-removeAdoptedChild(child: FrameNode): void--><!--Device-FrameNode-removeAdoptedChild(child: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| child | [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Yes | the target node being adopted. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100021](../../apis-arkui/errorcode-node.md#100021-framenode-not-modifiable) | The current FrameNode is not modifiable. |
| [100025](../../apis-arkui/errorcode-node.md#100025-invalid-parameter-value) | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'child' is invalid: it cannot be null." |
| [100026](../../apis-arkui/errorcode-node.md#100026-the-instance-object-used-to-call-the-api-has-been-unbound-from-the-backend-entity-node) | The current FrameNode has been disposed. |

## removeChild

```TypeScript
removeChild(node: FrameNode): void
```

Remove child from the current FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-removeChild(node: FrameNode): void--><!--Device-FrameNode-removeChild(node: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Yes | The node will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100021](../../apis-arkui/errorcode-node.md#100021-framenode-not-modifiable) | The FrameNode is not modifiable. |

## removeSupportedUIStates

```TypeScript
removeSupportedUIStates(uiStates: int): void
```

Removes the registered state handlers. When all states registered via `addSupportedUIStates` are removed, the corresponding `statesChangeHandler` will no longer be executed.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-removeSupportedUIStates(uiStates: int): void--><!--Device-FrameNode-removeSupportedUIStates(uiStates: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiStates | int | Yes | The target UI states to remove handlers from. |

## reuse

```TypeScript
reuse(): void
```

Reuse current FrameNode From JsFrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-reuse(): void--><!--Device-FrameNode-reuse(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setCrossLanguageOptions

```TypeScript
setCrossLanguageOptions(value: CrossLanguageOptions): void
```

Set the cross-language options of the target FrameNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-setCrossLanguageOptions(value: CrossLanguageOptions): void--><!--Device-FrameNode-setCrossLanguageOptions(value: CrossLanguageOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CrossLanguageOptions](../../apis-arkui/arkts-apis/arkts-arkui-framenode-crosslanguageoptions-i.md) | Yes | The cross-language options. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100022](../../apis-arkui/errorcode-node.md#100022-crosslanguage-common-attribute-configuration-not-supported) | The FrameNode cannot be set whether to support cross-language common attribute setting. |

## setLayoutPosition

```TypeScript
setLayoutPosition(position: NodePosition): void
```

Set the position to the parent of the FrameNode after layout, with unit PX.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-setLayoutPosition(position: NodePosition): void--><!--Device-FrameNode-setLayoutPosition(position: NodePosition): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | [NodePosition](arkts-na-nodeposition-t.md) | Yes | The position to the parent of the FrameNode after layout. |

## setMeasuredSize

```TypeScript
setMeasuredSize(size: Size): void
```

Set the size of the FrameNode after measure, with unit PX.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-setMeasuredSize(size: Size): void--><!--Device-FrameNode-setMeasuredSize(size: Size): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | [Size](arkts-na-graphics-size-i.md) | Yes | The size of the FrameNode after measure. |

## setNeedsLayout

```TypeScript
setNeedsLayout(): void
```

Mark the frame node as need layout.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNode-setNeedsLayout(): void--><!--Device-FrameNode-setNeedsLayout(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

