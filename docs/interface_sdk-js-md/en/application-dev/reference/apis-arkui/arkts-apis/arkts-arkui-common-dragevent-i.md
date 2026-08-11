# DragEvent

DragEvent object description

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface DragEvent--><!--Device-unnamed-export declare interface DragEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## executeDropAnimation

```TypeScript
executeDropAnimation(customDropAnimation: VoidCallback): void
```

Setup one drop animation execution callback, which will be triggered by system when user drops.Use this way to implement the custom drop animation instead of doing it in onDrop, as the system will decide when to trigger the callback during the drop handling.  
[Note]: 1. Please set useCustomDropAnimation to true as well when using this method. 2. Do not implement the animation no-related logics in the callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-executeDropAnimation(customDropAnimation: VoidCallback): void--><!--Device-DragEvent-executeDropAnimation(customDropAnimation: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| customDropAnimation | [VoidCallback](arkts-arkui-voidcallback-t.md) | Yes | the custom drop animation function. |

## getData

```TypeScript
getData(): UnifiedData | undefined
```

Get dragData from DragEvent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-getData(): UnifiedData | undefined--><!--Device-DragEvent-getData(): UnifiedData | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UnifiedData](../arkts-components/arkts-arkui-unifieddata-t.md) | get dragData, undefined will be returned if the internal runtime environment is broken. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [190002](../errorcode-uicontext.md#190002-invalid-callback-function) | Data error. |
| [190001](../errorcode-uicontext.md#190001-invalid-uicontext-object) | Data not found. |

## getDisplayId

```TypeScript
getDisplayId(): int
```

Get the id of display which the drag event is occuring on.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-getDisplayId(): int--><!--Device-DragEvent-getDisplayId(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int |  |

## getDisplayX

```TypeScript
getDisplayX(): double
```

X coordinate of the touch point relative to the left edge of the device screen.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-getDisplayX(): double--><!--Device-DragEvent-getDisplayX(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## getDisplayY

```TypeScript
getDisplayY(): double
```

Y coordinate of the touch point relative to the upper edge of the device screen.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-getDisplayY(): double--><!--Device-DragEvent-getDisplayY(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## getDragSource

```TypeScript
getDragSource(): string
```

Retrieve the bundle information of the drag source application.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-getDragSource(): string--><!--Device-DragEvent-getDragSource(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## getGlobalDisplayX

```TypeScript
getGlobalDisplayX(): double
```

X coordinate of the point relative to the global display.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-getGlobalDisplayX(): double--><!--Device-DragEvent-getGlobalDisplayX(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## getGlobalDisplayY

```TypeScript
getGlobalDisplayY(): double
```

Y coordinate of the point relative to the global display.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-getGlobalDisplayY(): double--><!--Device-DragEvent-getGlobalDisplayY(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## getModifierKeyState

```TypeScript
getModifierKeyState?: ModifierKeyStateGetter
```

Query the modifier key press state, support 'ctrl'|'alt'|'shift'

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-getModifierKeyState?: ModifierKeyStateGetter--><!--Device-DragEvent-getModifierKeyState?: ModifierKeyStateGetter-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getPreviewRect

```TypeScript
getPreviewRect(): Rectangle
```

Get the rectangle of drag window.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-getPreviewRect(): Rectangle--><!--Device-DragEvent-getPreviewRect(): Rectangle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Rectangle](arkts-arkui-common-rectangle-i.md) | getPreview rectangle. |

## getResult

```TypeScript
getResult(): DragResult
```

Get dragEvent result from DragEvent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-getResult(): DragResult--><!--Device-DragEvent-getResult(): DragResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DragResult](../arkts-components/arkts-arkui-dragresult-e.md) | dragResult Data. |

## getSummary

```TypeScript
getSummary(): Summary | undefined
```

Get dragData summary from DragEvent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-getSummary(): Summary | undefined--><!--Device-DragEvent-getSummary(): Summary | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Summary](arkts-arkui-summary-t.md) | get Summary Data, undefined will be returned if the internal runtime environment is broken. |

## getVelocity

```TypeScript
getVelocity(): double
```

Get the velocity of drag gesture.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-getVelocity(): double--><!--Device-DragEvent-getVelocity(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double | get velocity. |

## getVelocityX

```TypeScript
getVelocityX(): double
```

Get the x axis velocity of drag gesture.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-getVelocityX(): double--><!--Device-DragEvent-getVelocityX(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double | get x axis velocity. |

## getVelocityY

```TypeScript
getVelocityY(): double
```

Get the y axis velocity of drag gesture.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-getVelocityY(): double--><!--Device-DragEvent-getVelocityY(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double | get y axis velocity. |

## getWindowX

```TypeScript
getWindowX(): double
```

X coordinate of the touch point relative to the left edge of the current window.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-getWindowX(): double--><!--Device-DragEvent-getWindowX(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## getWindowY

```TypeScript
getWindowY(): double
```

Y coordinate of the touch point relative to the left edge of the current window.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-getWindowY(): double--><!--Device-DragEvent-getWindowY(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## isRemote

```TypeScript
isRemote(): boolean
```

Call this method to determine whether the current drag operation is a cross-device drag.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-isRemote(): boolean--><!--Device-DragEvent-isRemote(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## setData

```TypeScript
setData(unifiedData: UnifiedData): void
```

Set dragData into DragEvent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-setData(unifiedData: UnifiedData): void--><!--Device-DragEvent-setData(unifiedData: UnifiedData): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| unifiedData | [UnifiedData](../arkts-components/arkts-arkui-unifieddata-t.md) | Yes | dragData. |

## setDataLoadParams

```TypeScript
setDataLoadParams(dataLoadParams: DataLoadParams): void
```

Use this method to provide a data representation to the system instead of directly providing a complete data object. When the user releases the drag over the target application, the system will use this data representation to request the actual data from drag source. This approach significantly improves the efficiency of initiating drag operations for large volumes of data and enhances the effectiveness of data reception. It is recommended to use this method instead of the setData method.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-setDataLoadParams(dataLoadParams: DataLoadParams): void--><!--Device-DragEvent-setDataLoadParams(dataLoadParams: DataLoadParams): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataLoadParams | [DataLoadParams](arkts-arkui-dataloadparams-t.md) | Yes | The data backend representation. |

## setResult

```TypeScript
setResult(dragResult: DragResult): void
```

Set dragEvent result to DragEvent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-setResult(dragResult: DragResult): void--><!--Device-DragEvent-setResult(dragResult: DragResult): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dragResult | [DragResult](../arkts-components/arkts-arkui-dragresult-e.md) | Yes | the return of dragEvent. |

## startDataLoading

```TypeScript
startDataLoading(options: DataSyncOptions): string | undefined
```

Request the drag data to be synchronized to caller, can be notified with the synchronization progress.Only can be used in onDrop event processing.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-startDataLoading(options: DataSyncOptions): string | undefined--><!--Device-DragEvent-startDataLoading(options: DataSyncOptions): string | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DataSyncOptions](../arkts-components/arkts-arkui-datasyncoptions-t.md) | Yes | the data sync options. |

**Return value:**

| Type | Description |
| --- | --- |
| string | The data key returned by system, which can be used as the identify of the request. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. |
| [190003](../errorcode-drag-event.md#190003-operation-not-allowed-in-the-current-phase) | Operation not allowed for current phase. |

## autoHideComponentUniqueIds

```TypeScript
autoHideComponentUniqueIds?: int | int[]
```

Set the uniqueId or uniqueId array of components that need to be automatically hidden during dragging.This property takes effect only in onDragStart. After the drag starts successfully, the system hides the target components before the drag preview window is shown. Developers need to restore component visibility in onDragEnd or onDrop based on service requirements.

**Type:** int \| int[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-autoHideComponentUniqueIds?: int | int[]--><!--Device-DragEvent-autoHideComponentUniqueIds?: int | int[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dragBehavior

```TypeScript
dragBehavior: DragBehavior
```

If copy is COPY, this DragEvent is a copy event.

**Type:** [DragBehavior](../arkts-components/arkts-arkui-dragbehavior-e.md)

**Default:** COPY

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-dragBehavior: DragBehavior--><!--Device-DragEvent-dragBehavior: DragBehavior-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## useCustomDropAnimation

```TypeScript
useCustomDropAnimation: boolean
```

If useCustomDropAnimation is true, System will not use drop animation.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragEvent-useCustomDropAnimation: boolean--><!--Device-DragEvent-useCustomDropAnimation: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

