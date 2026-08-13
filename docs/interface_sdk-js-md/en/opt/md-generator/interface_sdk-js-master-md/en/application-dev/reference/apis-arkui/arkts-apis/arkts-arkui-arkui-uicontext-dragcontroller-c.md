# DragController

Provides APIs for initiating drag actions. When receiving a gesture event, such as a touch or long-press event, an application can initiate a drag action and carry drag information therein. > **NOTE：**> > In the following API examples, you must first use [getDragController()](arkts-arkui-arkui-uicontext-uicontext-c.md#getDragController) in > **UIContext** to obtain a **DragController** instance, and then call the APIs using the obtained instance.

**Since:** 11

**Deprecated since:** -1

<!--Device-unnamed-export class DragController--><!--Device-unnamed-export class DragController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CustomKeyboardContinueFeature, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from '@kit.ArkUI';
```

## cancelDataLoading

```TypeScript
cancelDataLoading(key: string): void
```

Cancels the data loading initiated by the [startDataLoading](../arkts-components/arkts-arkui-dragevent-i.md#startDataLoading) API. This API can be called only after the drag is released.

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-DragController-cancelDataLoading(key: string): void--><!--Device-DragController-cancelDataLoading(key: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [190004](../errorcode-drag-event.md#190004-operation-failed) |

## createDragAction

```TypeScript
createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: dragController.DragInfo): dragController.DragAction
```

Creates a drag action object for initiating drag and drop operations. You need to explicitly specify one or more drag previews, the drag data, and the drag handle point. If a drag operation initiated by an existing drag action object is not completed, no new object can be created, and calling the API will throw an exception. After the lifecycle of the drag action object ends, the callback functions registered on this object become invalid. Therefore, it is necessary to hold this object within a longer scope and replace the old value with a new object returned by **createDragAction** before each drag initiation. > **NOTE：**> > For optimal drag and drop performance, limit the number of drag previews.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DragController-createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: dragController.DragInfo): dragController.DragAction--><!--Device-DragController-createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: dragController.DragInfo): dragController.DragAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| customArray | Array&lt;[CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| [DragItemInfo](../arkts-components/arkts-arkui-dragiteminfo-i.md)&gt; | Yes |
| dragInfo | dragController.DragInfo | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| dragController.DragAction |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## enableDropDisallowedBadge

```TypeScript
enableDropDisallowedBadge(enabled: boolean): void
```

Specifies whether to enable the display of a disallowed badge when dragged content is incompatible with a component 's configured [allowDrop](../arkts-components/arkts-arkui-commonmethod-c.md#allowDrop) types. When a component can accept or process dragged data or returns **DragBehavior.COPY** to indicate copy mode processing, the drag preview shows a plus icon with data count badge. When the component returns **DragBehavior.MOVE** to indicate cut mode processing, only the data count badge appears. When this feature is enabled, the system automatically displays a disallowed badge during drag operations if the dragged data types are incompatible with the target component's allowed drop types. This API currently does not support [UIExtension](arkts-arkui-uiextension.md#@ohos.arkui.uiExtension).

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DragController-enableDropDisallowedBadge(enabled: boolean): void--><!--Device-DragController-enableDropDisallowedBadge(enabled: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

## executeDrag

```TypeScript
executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo,
    callback: AsyncCallback<dragController.DragEventParam>): void
```

Initiates a drag action, with the object to be dragged and the drag information passed in. This API uses a callback to return the drag event result.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DragController-executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo,    callback: AsyncCallback<dragController.DragEventParam>): void--><!--Device-DragController-executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo,    callback: AsyncCallback<dragController.DragEventParam>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| custom | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| [DragItemInfo](../arkts-components/arkts-arkui-dragiteminfo-i.md) | Yes |
| dragInfo | dragController.DragInfo | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;dragController.DragEventParam&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## executeDrag

```TypeScript
executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo)
    : Promise<dragController.DragEventParam>
```

Initiates a drag action, with the object to be dragged and the drag information passed in. This API uses a promise to return the drag event result.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DragController-executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo)    : Promise<dragController.DragEventParam>--><!--Device-DragController-executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo)    : Promise<dragController.DragEventParam>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| custom | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| [DragItemInfo](../arkts-components/arkts-arkui-dragiteminfo-i.md) | Yes |
| dragInfo | dragController.DragInfo | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;{ event: DragEvent, extraParams: string |
| Promise & lt;dragController.DragEventParam & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getDragPreview

```TypeScript
getDragPreview(): dragController.DragPreview
```

Obtains the **DragPreview** object, which represents the preview displayed during a drag operation.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DragController-getDragPreview(): dragController.DragPreview--><!--Device-DragController-getDragPreview(): dragController.DragPreview-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| dragController.DragPreview |

## notifyDragStartRequest

```TypeScript
notifyDragStartRequest(requestStatus: dragController.DragStartRequestStatus): void
```

Controls whether the application can initiate a drag operation.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-DragController-notifyDragStartRequest(requestStatus: dragController.DragStartRequestStatus): void--><!--Device-DragController-notifyDragStartRequest(requestStatus: dragController.DragStartRequestStatus): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| requestStatus | dragController.DragStartRequestStatus | Yes |

## setDragEventStrictReportingEnabled

```TypeScript
setDragEventStrictReportingEnabled(enable: boolean): void
```

Sets whether the **onDragLeave** callback of the parent component is triggered when an item is dragged from the parent to the child component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DragController-setDragEventStrictReportingEnabled(enable: boolean): void--><!--Device-DragController-setDragEventStrictReportingEnabled(enable: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |
