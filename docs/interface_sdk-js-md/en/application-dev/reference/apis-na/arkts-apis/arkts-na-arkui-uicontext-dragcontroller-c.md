# DragController

class DragController

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class DragController--><!--Device-unnamed-export declare class DragController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## cancelDataLoading

```TypeScript
cancelDataLoading(key: string): void
```

Cancel the UDMF data sync process by passing in the data key as the identify, can only be used after the drop.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragController-cancelDataLoading(key: string): void--><!--Device-DragController-cancelDataLoading(key: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The data key returned by startDataLoading method. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [190004](../../apis-arkui/errorcode-drag-event.md#190004-operation-failed) | Operation failed. |

## createDragAction

```TypeScript
createDragAction(customArray: Array<CustomBuilder | DragItemInfo> | undefined,
    dragInfo: dragController.DragInfo): dragController.DragAction
```

Create one drag action object, which can be used for starting drag later or monitoring the drag status after drag started.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragController-createDragAction(customArray: Array<CustomBuilder | DragItemInfo> | undefined,    dragInfo: dragController.DragInfo): dragController.DragAction--><!--Device-DragController-createDragAction(customArray: Array<CustomBuilder | DragItemInfo> | undefined,    dragInfo: dragController.DragInfo): dragController.DragAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| customArray | Array&lt;CustomBuilder \| DragItemInfo&gt; \| undefined | Yes | Objects used for prompts displayed when the objects are dragged. |
| dragInfo | dragController.DragInfo | Yes | Information about the drag event. |

**Return value:**

| Type | Description |
| --- | --- |
| dragController.DragAction | one drag action object |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal handling failed. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |

## enableDropDisallowedBadge

```TypeScript
enableDropDisallowedBadge(enabled: boolean): void
```

Sets whether to enable the disallow badge icon show. Typically, when a component can receive or process data dragged by the user, or when it declares to the system that data should be processed in COPY way by returning DragBehavior.COPY, the system will display a plus sign together with the data number on the upper-left corner of the dragged object; if returning DragBehavior.MOVE to the system to declare that data should be processed in CUT way, the system will only display the data number on the upper-left corner of the dragged object. In some cases, when the system determines or the component explicitly declares that it cannot handle the data that the user is dragging, the system displays a badge icon in the same way as it does for DragBehavior.MOVE. So if you want to show the more clearly status, you can call this method on the UI instance in advance to force the system to display a clear prohibition icon on the upper left corner in such cases, and the user can clearly know that data cannot be dropped here.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragController-enableDropDisallowedBadge(enabled: boolean): void--><!--Device-DragController-enableDropDisallowedBadge(enabled: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Indicating enable the disallow status showing or not. |

## executeDrag

```TypeScript
executeDrag(custom: CustomBuilder | DragItemInfo | undefined, dragInfo: dragController.DragInfo,
    callback: AsyncCallback<dragController.DragEventParam>): void
```

Execute a drag event.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragController-executeDrag(custom: CustomBuilder | DragItemInfo | undefined, dragInfo: dragController.DragInfo,    callback: AsyncCallback<dragController.DragEventParam>): void--><!--Device-DragController-executeDrag(custom: CustomBuilder | DragItemInfo | undefined, dragInfo: dragController.DragInfo,    callback: AsyncCallback<dragController.DragEventParam>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| custom | CustomBuilder \| DragItemInfo \| undefined | Yes | Object used for prompts displayed when the object is dragged. |
| dragInfo | dragController.DragInfo | Yes | Information about the drag event. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;dragController.DragEventParam&gt; | Yes | Callback that contains the drag event information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal handling failed. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |

## executeDrag

```TypeScript
executeDrag(custom: CustomBuilder | DragItemInfo | undefined, dragInfo: dragController.DragInfo)
    : Promise<dragController.DragEventParam> | null
```

Execute a drag event.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragController-executeDrag(custom: CustomBuilder | DragItemInfo | undefined, dragInfo: dragController.DragInfo)    : Promise<dragController.DragEventParam> | null--><!--Device-DragController-executeDrag(custom: CustomBuilder | DragItemInfo | undefined, dragInfo: dragController.DragInfo)    : Promise<dragController.DragEventParam> | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| custom | CustomBuilder \| DragItemInfo \| undefined | Yes | Object used for prompts displayed when the object is dragged. |
| dragInfo | dragController.DragInfo | Yes | Information about the drag event. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;dragController.DragEventParam&gt; \| null | A Promise with the drag event information. Null will be returned if the parameters' checking failed or some internal errors occur, for example: the runtime environment is broken. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal handling failed. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |

## getDragPreview

```TypeScript
getDragPreview(): dragController.DragPreview
```

Get a drag preview object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragController-getDragPreview(): dragController.DragPreview--><!--Device-DragController-getDragPreview(): dragController.DragPreview-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| dragController.DragPreview | A drag preview object. |

## notifyDragStartRequest

```TypeScript
notifyDragStartRequest(requestStatus: dragController.DragStartRequestStatus): void
```

Notify the drag start request to specific pending or continue.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragController-notifyDragStartRequest(requestStatus: dragController.DragStartRequestStatus): void--><!--Device-DragController-notifyDragStartRequest(requestStatus: dragController.DragStartRequestStatus): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| requestStatus | dragController.DragStartRequestStatus | Yes | Status about the drag start behavior. |

## setDragEventStrictReportingEnabled

```TypeScript
setDragEventStrictReportingEnabled(enable: boolean): void
```

Enable drag event strict reporting for drag enter and leave notification in nested situation. For example, the parent and child both register the onDragEnter/onDragLeave events, if this flag is enabled, the parent will be notified with leave event, and the child will notified with enter event at the same time, when user drag action is passing through the parent and enter the scope of the child. Please be noted, the default value of the flag is false, it means, for the same situation, the parent will not receive the leave notification, just the child can get the enter event, which is not fully strict.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragController-setDragEventStrictReportingEnabled(enable: boolean): void--><!--Device-DragController-setDragEventStrictReportingEnabled(enable: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Indicating enable drag event strict reporting or not. |

