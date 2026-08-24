# NodeController

The **NodeController** module provides APIs for managing custom nodes, such as creating, showing, and updating custom nodes, and APIs for mounting custom nodes to a NodeContainer component.

> **NOTE：**&gt;
> - NodeController objects do not support JSON serialization.

**Since:** 11

<!--Device-unnamed-export abstract class NodeController--><!--Device-unnamed-export abstract class NodeController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToAppear

```TypeScript
aboutToAppear?(): void
```

Called after the NodeContainer component bound to this **NodeController** instance is attached and about to appear.

> **NOTE：**&gt;
> For details about the callback timing, see onAppear.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeController-aboutToAppear?(): void--><!--Device-NodeController-aboutToAppear?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToDisappear

```TypeScript
aboutToDisappear?(): void
```

Called when the NodeContainer component bound to this **NodeController** instance is destroyed.

> **NOTE：**&gt;
> For details about the callback timing, see onDisAppear.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeController-aboutToDisappear?(): void--><!--Device-NodeController-aboutToDisappear?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToResize

```TypeScript
aboutToResize?(size: Size): void
```

Called when the NodeContainer component bound to this **NodeController** instance is resized.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeController-aboutToResize?(size: Size): void--><!--Device-NodeController-aboutToResize?(size: Size): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | Size | Yes | Width and height of the component, in vp. |

## makeNode

```TypeScript
abstract makeNode(uiContext: UIContext): FrameNode | null
```

Called when the NodeContainer component bound to this **NodeController** instance is created. This callback returns a node, which will be mounted to the **NodeContainer**.This callback can also be invoked through the **rebuild()** method of **NodeController**.

> **NOTE：**&gt;
> NodeContainer does not support cross-instance reuse. If
> NodeContainer is reused across instances and
> [NodeController](../../apis-default/arkts-apis/arkts-nodecontroller-c.md) of NodeContainer
> triggers the [makeNode](../../apis-default/arkts-apis/arkts-nodecontroller-c.md#makenode) callback method, the
> [UIContext](../../apis-default/arkts-apis/arkts-arkui-uicontext-uicontext-c.md) object in the input parameter may be undefined. In this case, you need
> to check whether the [UIContext](../../apis-default/arkts-apis/arkts-arkui-uicontext-uicontext-c.md) object in the input parameter is undefined, which
> prevents the [invalid UIContext](../../../ui/arkts-wrong-uicontext-debug.md#identifying-uicontext-errors) when
> the input parameter is used.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeController-abstract makeNode(uiContext: UIContext): FrameNode | null--><!--Device-NodeController-abstract makeNode(uiContext: UIContext): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiContext | [UIContext](../../apis-default/arkts-apis/arkts-arkui-uicontext-uicontext-c.md) | Yes | UI context of the bound NodeContainer component. |

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](../../apis-default/arkts-apis/arkts-framenode-c.md) \| null | FrameNode** object, which will be mounted to the placeholder node of the [NodeContainer]{ |

## onAttach

```TypeScript
onAttach?(): void
```

Called when the NodeContainer component bound to this **NodeController** instance is attached to the main node tree.

> **NOTE：**&gt;
> For details about the callback timing, see onAttach.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-NodeController-onAttach?(): void--><!--Device-NodeController-onAttach?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onBind

```TypeScript
onBind?(containerId: number): void
```

Called after this **NodeController** instance is bound to a NodeContainer component.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-NodeController-onBind?(containerId: number): void--><!--Device-NodeController-onBind?(containerId: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| containerId | number | Yes | ID of the NodeContainer component to which the **NodeController** instance is bound. |

## onDetach

```TypeScript
onDetach?(): void
```

Called when the NodeContainer component bound to this **NodeController** instance is detached from the main node tree.

> **NOTE：**&gt;
> For details about the callback timing, see onDetach.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-NodeController-onDetach?(): void--><!--Device-NodeController-onDetach?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTouchEvent

```TypeScript
onTouchEvent?(event: TouchEvent): void
```

Called when the NodeContainer component bound to this **NodeController** instance receives a touch event.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeController-onTouchEvent?(event: TouchEvent): void--><!--Device-NodeController-onTouchEvent?(event: TouchEvent): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | TouchEvent | Yes | Touch event. |

## onUnbind

```TypeScript
onUnbind?(containerId: number): void
```

Called after this **NodeController** instance is unbound from a NodeContainer component.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-NodeController-onUnbind?(containerId: number): void--><!--Device-NodeController-onUnbind?(containerId: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| containerId | number | Yes | ID of the NodeContainer component from which the **NodeController** instance is unbound. |

## onWillBind

```TypeScript
onWillBind?(containerId: number): void
```

Called when this **NodeController** instance is about to be bound to a NodeContainer component.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-NodeController-onWillBind?(containerId: number): void--><!--Device-NodeController-onWillBind?(containerId: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| containerId | number | Yes | ID of the NodeContainer component to which the **NodeController** instance is about to be bound. |

## onWillUnbind

```TypeScript
onWillUnbind?(containerId: number): void
```

Called when this **NodeController** instance is about to be unbound from a NodeContainer component.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-NodeController-onWillUnbind?(containerId: number): void--><!--Device-NodeController-onWillUnbind?(containerId: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| containerId | number | Yes | ID of the NodeContainer component from which the **NodeController** instance is about to be unbound. |

## rebuild

```TypeScript
rebuild(): void
```

Instructs the NodeContainer component bound to this **NodeController** instance to call the [makeNode](../../apis-default/arkts-apis/arkts-nodecontroller-c.md#makenode) API again to change child nodes.

> **NOTE：**&gt;
> Since the **rebuild** API is actively called by the application and is tied to the UI, you need to ensure that
> the UI context is valid at the time of the call, that is, it must be consistent with the UI context of the bound
> NodeContainer.&gt;
> In cases where the [UI context is unclear](../../../ui/arkts-global-interface.md#ambiguous-ui-context), for
> example, during event callbacks, you can use the
> [runScopedTask](../../apis-default/arkts-apis/arkts-arkui-uicontext-uicontext-c.md#runscopedtask) method of
> [UIContext](../../apis-default/arkts-apis/arkts-arkui-uicontext-uicontext-c.md) to explicitly define the UI context at the time of the call.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeController-rebuild(): void--><!--Device-NodeController-rebuild(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

