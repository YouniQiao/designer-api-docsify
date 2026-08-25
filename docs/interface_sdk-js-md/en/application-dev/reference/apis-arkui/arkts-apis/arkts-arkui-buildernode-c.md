# BuilderNode

The **BuilderNode** module provides APIs for a BuilderNode – a custom node that can be used to mount built-in components. A BuilderNode can be used only as a leaf node. For details, see [BuilderNode Development](../../../ui/arkts-user-defined-arktsNode-builderNode.md). For best practices, see [Dynamic Component Creation: Dynamically Adding, Updating, and Deleting Components](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-ui-dynamic-operations#section153921947151012).Compared with **BuilderNode**, **ReactiveBuilderNode** can generate a component tree through the stateless UI method @Builder with multiple parameters.

> **NOTE：**&gt;
> - If the root node of the provided Builder is a syntax node (
> [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md)/
> [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md)/
> [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)/
> [ContentSlot](../../../ui/rendering-control/arkts-rendering-control-contentslot.md)...),
> Span, ContainerSpan,
> SymbolSpan, or a custom component, an additional
> FrameNode is generated and displayed as BuilderProxyNode in the node tree. This structural
> change affects the propagation of certain events. For details, see
> [BuilderProxyNode in BuilderNode Causes Tree Structure Changes](../../../ui/arkts-user-defined-arktsNode-builderNode.md#builderproxynode-in-buildernode-causes-tree-structure-changes).&gt;
> - If you encounter display issues when reusing a BuilderNode across pages, see
> [Cross-Page Reuse Considerations](../../../ui/arkts-user-defined-arktsNode-builderNode.md#cross-page-reuse-considerations)
> for guidance.&gt;
> - **BuilderNode** is not available in DevEco Studio Previewer.&gt;
> - Custom components under **BuilderNode** can use the [@Prop](../../../ui/state-management/arkts-prop.md)
> decorator. The [@Link](../../../ui/state-management/arkts-link.md) decorator cannot be used to synchronize
> external data and status across **BuilderNode** boundaries.&gt;
> - If a BuilderNode contains custom components as child nodes, these custom components cannot use the
> [@Reusable](../../../ui/state-management/arkts-reusable.md) decorator. For details, see
> [Using the @Reusable Decorator with BuilderNode Child Components](../../../ui/arkts-user-defined-arktsNode-builderNode.md#using-the-reusable-decorator-with-buildernode-child-components).&gt;
> - Since API version 12, custom components can receive
> [LocalStorage](../../../ui/state-management/arkts-localstorage.md) instances. You can use LocalStorage related
> decorators such as [@LocalStorageProp](../../../ui/state-management/arkts-localstorage.md#localstorageprop) and
> [@LocalStorageLink](../../../ui/state-management/arkts-localstorage.md#localstoragelink) by
> [passing LocalStorage instances](../../../ui/state-management/arkts-localstorage.md#providing-a-custom-component-with-access-to-a-localstorage-instance).&gt;
> - Since API version 20, when configured with [BuildOptions](arkts-arkui-buildernode-buildoptions-i.md), custom components within a
> BuilderNode can access the host page's [@Provide](../../../ui/state-management/arkts-provide-and-consume.md) data
> through their [@Consume](../../../ui/state-management/arkts-provide-and-consume.md) decorated attributes.&gt;
> - The behavior of other decorators is undefined. Avoid using those decorators.&gt;
> - [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md) can be used only in custom
> components.&gt;
> - BuilderNode objects do not support JSON serialization.

**Since:** 11

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## build

```TypeScript
build(builder: WrappedBuilder<Args>, arg?: Object): void
```

Creates a component tree based on the passed object and holds the root node of the component tree. The stateless UI method [@Builder](../../../ui/state-management/arkts-builder.md) has at most one root node.Custom components are allowed.

> **NOTE：**

> - When nesting @Builder, ensure that the input objects for the inner and outer @Builder methods are consistent.&gt;
> - The outermost @Builder supports only one input parameter.&gt;
> - The build parameter uses the pass-by-value semantics. To implement state updates, you must explicitly use the
> [update](#update) API.&gt;
> - To operate objects in a BuilderNode, ensure that the reference to the BuilderNode is not garbage collected.
> When a BuilderNode object is garbage collected by the virtual machine, the associated
> FrameNode and [RenderNode](arkts-arkui-rendernode-c.md) objects are also dereferenced from
> the backend node tree. This means that any FrameNode objects obtained from a BuilderNode will no longer
> correspond to any actual node if the BuilderNode is garbage collected.&gt;
> - The BuilderNode object maintains references to its underlying entity nodes. When the BuilderNode frontend
> object is no longer required for managing backend nodes, call the [dispose](#dispose) API to
> release node references and unbind frontend and backend nodes.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| builder | [WrappedBuilder](../arkts-components/arkts-arkui-wrappedbuilder-c.md)&lt;Args&gt; | Yes |
| arg | Object | No |

## build

```TypeScript
build(builder: WrappedBuilder<Args>, arg: Object, options: BuildOptions): void
```

Creates a component tree based on the passed object and holds the root node of the component tree. The stateless UI method [@Builder](../../../ui/state-management/arkts-builder.md) has at most one root node.Custom components are allowed. Compared with the [build(builder: WrappedBuilder\&lt;Args&gt;, arg?: Object)](#build) API, this API can use the builder configuration parameters to determine whether @Builder can be nested with @ Builder.

> **NOTE：**

> - For details about the creation and update using @Builder, see
> [@Builder](../../../ui/state-management/arkts-builder.md).&gt;
> - The outermost @Builder supports only one input parameter.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| builder | [WrappedBuilder](../arkts-components/arkts-arkui-wrappedbuilder-c.md)&lt;Args&gt; | Yes |
| arg | Object | Yes |
| options | [BuildOptions](arkts-arkui-buildernode-buildoptions-i.md) | Yes |

## constructor

```TypeScript
constructor(uiContext: UIContext, options?: RenderOptions)
```

When content generated by BuilderNode is embedded within another RenderNode for display, the **selfIdealSize** parameter in **RenderOptions** must be explicitly specified. Otherwise, the layout constraints for the parent component in Builder default to [0, 0]. In this case, if **selfIdealSize** is not set, the root node of the subtree in BuilderNode will have a size of [0, 0].

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| options | [RenderOptions](arkts-arkui-buildernode-renderoptions-i.md) | No |

## dispose

```TypeScript
dispose(): void
```

Immediately releases the reference relationship between this BuilderNode object and its [entity node](../../../ui/arkts-user-defined-node.md#basic-concepts). For details about the scenarios involving BuilderNode unbinding, see [Canceling the Reference to the Entity Node](../../../ui/arkts-user-defined-arktsNode-builderNode.md#canceling-the-reference-to-the-entity-node).

> **NOTE：**&gt;
> After calling **dispose()**, the BuilderNode object cancels its reference to the backend entity node. If the
> frontend object BuilderNode cannot be released, memory leaks may occur. To avoid this, be sure to call
> **dispose()** on the BuilderNode when you no longer need it. This reduces the complexity of reference
> relationships and lowers the risk of memory leaks. For details, see
> [Memory Leak Caused by Circular Reference Between BuilderNode Frontend and Backend](../../../ui/arkts-user-defined-node-faq.md#memory-leak-caused-by-circular-reference-between-buildernode-frontend-and-backend).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getFrameNode

```TypeScript
getFrameNode(): FrameNode | null
```

Obtains the FrameNode from the BuilderNode. The FrameNode is generated only after the BuilderNode executes the build operation.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) \| null |

## inheritFreezeOptions

```TypeScript
inheritFreezeOptions(enabled: boolean): void
```

Sets whether the current **BuilderNode** object inherits the freeze policy from its parent component's custom components. When inheritance is disabled (set to **false**), the object's freeze policy is set to **false**, which means its associated node remains unfrozen even in an inactive state.

> **NOTE：**&gt;
> When **inheritFreezeOptions** is set to **true** for **BuilderNode** and the parent component is a custom
> component, BuilderNode, ComponentContent, ReactiveBuilderNode, or ReactiveComponentContent, the freeze policy of
> the parent component is inherited. If the child component is a custom component, its freeze policy is not
> transferred to the child component.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

## isDisposed

```TypeScript
isDisposed(): boolean
```

Checks whether this BuilderNode object has released its reference to its backend entity node. Frontend nodes maintain references to corresponding backend entity nodes. After a node calls the **dispose** API to release this reference, subsequent API calls may cause crashes or return default values. This API facilitates validation of node validity prior to operations, thereby mitigating risks in scenarios where calls after disposal are required.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## postInputEvent

```TypeScript
postInputEvent(event: InputEventType): boolean
```

Dispatches the specified input event to the target node.  
**offsetA** indicates the BuilderNode's offset relative to its parent component, **offsetB** the hit position's offset relative to the BuilderNode, **offsetC** the composite offset (offsetA + offsetB) passed to the window in **postInputEvent**.

> **NOTE：**&gt;
> - The passed coordinates must be converted to the unit of px. The sample code below demonstrates how to perform
> such coordinate conversion.&gt;
> - Mouse left-click events are automatically converted to touch events. Avoid binding both touch and mouse events
> at the outer layer, as this may cause coordinate offsets. This is because the **SourceType** remains unchanged
> during event conversion. For details, see onTouch.&gt;
> - When an [axis event](../arkts-components/arkts-arkui-axisevent-i.md) event is injected, it cannot trigger
> rotation gestures, because the axis event does not include rotation
> axis information.&gt;
> - A forwarded event undergoes touch testing in the target component's subtree and triggers corresponding
> gestures. The original event also triggers gestures in the source component tree. There is no guaranteed outcome
> for gesture competition between these two types of gestures.&gt;
> - For developer-constructed events, mandatory fields must be assigned values, such as the **touches** field for
> touch events and the **scrollStep** field for axis events Ensure the completeness of the event, for example, both
> **DOWN** and **UP** [TouchType](arkts-arkui-touchtype-e.md) states must be included for a touch event to prevent undefined
> behavior.&gt;
> - [webview](../../apis-arkweb/arkts-apis/arkts-web-webview.md) has already handled coordinate system transformation, so events can
> be dispatched.&gt;
> - The **postTouchEvent** API needs to provide the gesture coordinates relative to the local coordinates of the
> target component, and the **postInputEvent** API needs to provide the gesture coordinates relative to the window
> coordinates of the target component.&gt;
> - Avoid forwarding a single event multiple times.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [InputEventType](arkts-arkui-inputeventtype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## postInputEventWithStrategy

```TypeScript
postInputEventWithStrategy(event: InputEventType, competitionStrategy?: CompetitionStrategy): boolean
```

Posts an event containing a competition strategy to the target UI component node.Before calling this API, you need to convert the value of **event** to the corresponding event and convert the coordinates in the **window** parameter in **event**. **offsetA** indicates the offset of the builderNode relative to the parent component, **offsetB** indicates the offset of the hit position relative to the builderNode, and **offsetC** is the sum of **offsetA** and **offsetB**. The value of **offsetC** is used as the value of the **window** parameter in **event** and passed to the **postInputEventWithStrategy** method. For details, see the following sample code.

> **NOTE：**&gt;
> - The passed coordinates must be converted to the unit of px. The sample code below demonstrates how to perform
> such coordinate conversion.&gt;
> - When processing a mouse left-click event, the system converts the event to a touch event. When forwarding the
> event, do not bind the touch event and mouse event at the outer layer at the same time, as this may cause
> coordinate offsets. This is because [TouchType](arkts-arkui-touchtype-e.md) does not change during the event conversion. For
> details about the specifications, see onTouch.&gt;
> - When an [axis event](../arkts-components/arkts-arkui-axisevent-i.md) event is injected, it cannot trigger
> rotation gestures, because the axis event does not include rotation
> axis information.&gt;
> - The forwarded event is posted to the target component and its child components for processing, and triggers the
> corresponding gesture. You can use input parameters to control whether the gestures of the current component and
> the target component are in a competitive relationship.&gt;
> - If the event is converted to a developer-constructed event, mandatory fields must be assigned values, for
> example, the **touches** field of a touch event and the **scrollStep** field of an axis event. Ensure the
> completeness of the event. For example, [TouchType](arkts-arkui-touchtype-e.md) of a touch event must contain both the
> **DOWN** and **UP** fields to prevent program exceptions or unexpected crashes.&gt;
> - The same event can be forwarded multiple times.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [InputEventType](arkts-arkui-inputeventtype-t.md) | Yes |
| competitionStrategy | [CompetitionStrategy](arkts-arkui-competitionstrategy-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## postTouchEvent

```TypeScript
postTouchEvent(event: TouchEvent): boolean
```

Posts a raw touch event to the FrameNode created by this BuilderNode.  
**postTouchEvent** dispatches the event from a middle node in the component tree downwards. To ensure the event is dispatched correctly, it needs to be transformed into the coordinate system of the parent component, as shown in the figure below.  
**OffsetA** indicates the offset of the BuilderNode relative to the parent component. You can obtain this offset by calling [getPositionToParent](arkts-arkui-framenode-c.md#getpositiontoparent) in the FrameNode. **OffsetB** indicates the offset of the touch point relative to the BuilderNode. You can obtain this offset from the TouchEvent object. **OffsetC** is the sum of **OffsetA** and **OffsetB**. It represents the final offset that you need to pass to **postTouchEvent**.

> **NOTE：**&gt;
> - The coordinates you pass in need to be converted to pixel values (px). If the BuilderNode has any affine
> transformations applied to it, they must be taken into account and combined with the touch event coordinates.&gt;
> - In [Webview](../../apis-arkweb/arkts-apis/arkts-web-webview.md), coordinate system transformations are already handled
> internally, so you can directly dispatch the touch event without additional adjustments.&gt;
> - The **postTouchEvent** API can be called only once for the same timestamp.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [TouchEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-touchevent-touchevent-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## recycle

```TypeScript
recycle(): void
```

Triggers recycling of custom components under this BuilderNode. Component recycling is part of the component reuse mechanism. For details, see [@Reusable Decorator: Reusing V1 Components](../../../ui/state-management/arkts-reusable.md). Since API version 26.0.0, custom components in **BuilderNode** support V2 component reuse. For details, see [@ReusableV2 Decorator: Reusing Components](../../../ui/state-management/arkts-new-reusableV2.md).

> **NOTE：**&gt;
> The BuilderNode completes the reuse event transfer between internal and external custom components through
> **reuse** and **recycle**. For specific usage scenarios, see
> [Implementing Node Reuse with the BuilderNode reuse and recycle APIs](../../../ui/arkts-user-defined-arktsNode-builderNode.md#implementing-node-reuse-with-the-buildernode-reuse-and-recycle-apis).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reuse

```TypeScript
reuse(param?: Object): void
```

Triggers component reuse for custom components under this BuilderNode. For details about component reuse, see [@Reusable Decorator: Reusing V1 Components](../../../ui/state-management/arkts-reusable.md). For details about the scenarios involving BuilderNode unbinding, see [Canceling the Reference to the Entity Node](../../../ui/arkts-user-defined-arktsNode-builderNode.md#canceling-the-reference-to-the-entity-node). Since API version 26.0.0, custom components in **BuilderNode** support V2 component reuse. For details, see [@ReusableV2 Decorator: Reusing Components](../../../ui/state-management/arkts-new-reusableV2.md).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | Object | No |

## update

```TypeScript
update(arg: Object): void
```

Updates this BuilderNode using the provided parameter, which must be of the same type as the input parameter passed to the [build](#build) API. When updating a custom component, define the variables used in the component as [@Prop](../../../ui/state-management/arkts-prop.md) decorated properties.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arg | Object | Yes |

## updateConfiguration

```TypeScript
updateConfiguration(): void
```

Transfers a system environment change event and triggers full update of a node. For details about system environment changes, see [@ohos.app.ability.Configuration (Environment Variables)](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-configuration-configuration-i.md).

> **NOTE：**&gt;
> The **updateConfiguration** API is used to instruct an object to update, with the system environment used for
> the update being determined by the changes in the application's current system environment.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
