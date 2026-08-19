# NodeController

Defines the controller of the node container. Provides lifecycle callbacks for the associated NodeContainer and methods to control the child node of the NodeContainer.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare abstract class NodeController--><!--Device-unnamed-export declare abstract class NodeController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToAppear

```TypeScript
aboutToAppear(): void
```

AboutToAppear Method. Executed when the associated NodeContainer is aboutToAppear.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-aboutToAppear(): void--><!--Device-NodeController-aboutToAppear(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToDisappear

```TypeScript
aboutToDisappear(): void
```

AboutToDisappear Method. Executed before the associated NodeContainer is destroyed.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-aboutToDisappear(): void--><!--Device-NodeController-aboutToDisappear(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToResize

```TypeScript
aboutToResize(size: Size): void
```

AboutToResize Method. Executed when the associated NodeContainer performs the measure method.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-aboutToResize(size: Size): void--><!--Device-NodeController-aboutToResize(size: Size): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | [Size](../../apis-arkui/arkts-apis/arkts-arkui-graphics-size-i.md) | Yes | size used to resize |

## makeNode

```TypeScript
abstract makeNode(uiContext: UIContext): FrameNode | null
```

MakeNode Method. Used to build a node tree and return a FrameNode or null, and attach the return result to the associated NodeContainer. Executed when the associated NodeContainer is created or the rebuild function is called.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-abstract makeNode(uiContext: UIContext): FrameNode | null--><!--Device-NodeController-abstract makeNode(uiContext: UIContext): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiContext | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to makeNode |

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](arkts-na-framenode-c.md) \| null | Returns a FrameNode or null. |

## onAttach

```TypeScript
onAttach(): void
```

OnAttach Method. Executed when the associated NodeContainer is attached to the main tree.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-onAttach(): void--><!--Device-NodeController-onAttach(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onBind

```TypeScript
onBind(containerId: long): void
```

OnBind Method. Executed when the NodeController is bound to a NodeContainer.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-onBind(containerId: long): void--><!--Device-NodeController-onBind(containerId: long): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| containerId | long | Yes | the uniqueId of the NodeContainer. |

## onDetach

```TypeScript
onDetach(): void
```

OnDetach Method. Executed when the associated NodeContainer is detached from the main tree.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-onDetach(): void--><!--Device-NodeController-onDetach(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTouchEvent

```TypeScript
onTouchEvent(event: TouchEvent): void
```

OnTouchEvent Method. Executed when associated NodeContainer is touched.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-onTouchEvent(event: TouchEvent): void--><!--Device-NodeController-onTouchEvent(event: TouchEvent): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | TouchEvent | Yes | The TouchEvent when associated NodeContainer is touched. |

## onUnbind

```TypeScript
onUnbind(containerId: long): void
```

OnUnbind Method. Executed when the NodeController is unbound with the NodeContainer.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-onUnbind(containerId: long): void--><!--Device-NodeController-onUnbind(containerId: long): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| containerId | long | Yes | the uniqueId of the NodeContainer. |

## onWillBind

```TypeScript
onWillBind(containerId: long): void
```

OnWillBind Method. Executed before the NodeController is bound to a NodeContainer.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-onWillBind(containerId: long): void--><!--Device-NodeController-onWillBind(containerId: long): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| containerId | long | Yes | the uniqueId of the NodeContainer. |

## onWillUnbind

```TypeScript
onWillUnbind(containerId: long): void
```

OnWillUnbind Method. Executed before the NodeController is unbound with the NodeContainer.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-onWillUnbind(containerId: long): void--><!--Device-NodeController-onWillUnbind(containerId: long): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| containerId | long | Yes | the uniqueId of the NodeContainer. |

## rebuild

```TypeScript
rebuild(): void
```

Rebuild Method. Used to re-invoke the makeNode method.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NodeController-rebuild(): void--><!--Device-NodeController-rebuild(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

