# DragEvent

Provides information about the drag event.

**Since:** 7

<!--Device-unnamed-declare interface DragEvent--><!--Device-unnamed-declare interface DragEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## executeDropAnimation

```TypeScript
executeDropAnimation(customDropAnimation: Callback<void>): void
```

Sets the execution function of the custom drop animation. This parameter is valid only when  
[useCustomDropAnimation](#useCustomDropAnimation) is set to **true**.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-DragEvent-executeDropAnimation(customDropAnimation: Callback<void>): void--><!--Device-DragEvent-executeDropAnimation(customDropAnimation: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| customDropAnimation | [Callback](arkts-arkui-callback-i.md)&lt;void&gt; | Yes |

## getData

```TypeScript
getData(): UnifiedData
```

Obtains drag-related data.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragEvent-getData(): UnifiedData--><!--Device-DragEvent-getData(): UnifiedData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UnifiedData](arkts-arkui-unifieddata-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [190002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-drag-event.md#190002-data-retrieval-error) |
| [190001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-drag-event.md#190001-data-not-found) |

## getDisplayId

```TypeScript
getDisplayId(): number
```

Obtains the ID of the screen where the current drag event occurs. This API is not supported in the  
[onDragEnd](arkts-arkui-commonmethod-c.md#onDragEnd) callback.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DragEvent-getDisplayId(): number--><!--Device-DragEvent-getDisplayId(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getDisplayX

```TypeScript
getDisplayX(): number
```

Obtains the x-coordinate of the drag point relative to the upper left corner of the screen.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragEvent-getDisplayX(): number--><!--Device-DragEvent-getDisplayX(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getDisplayY

```TypeScript
getDisplayY(): number
```

Obtains the y-coordinate of the drag point relative to the upper left corner of the screen.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragEvent-getDisplayY(): number--><!--Device-DragEvent-getDisplayY(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getDragSource

```TypeScript
getDragSource(): string
```

Obtains the package name of the drag source application.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DragEvent-getDragSource(): string--><!--Device-DragEvent-getDragSource(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getGlobalDisplayX

```TypeScript
getGlobalDisplayX(): number
```

Obtains the x-coordinate of the drag point relative to the upper left corner of the global screen.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DragEvent-getGlobalDisplayX(): number--><!--Device-DragEvent-getGlobalDisplayX(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getGlobalDisplayY

```TypeScript
getGlobalDisplayY(): number
```

Obtains the y-coordinate of the drag point relative to the upper left corner of the global screen.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DragEvent-getGlobalDisplayY(): number--><!--Device-DragEvent-getGlobalDisplayY(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getModifierKeyState

```TypeScript
getModifierKeyState?(keys: Array<string>): boolean
```

Obtains the pressed status of modifier keys.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-DragEvent-getModifierKeyState?(keys: Array<string>): boolean--><!--Device-DragEvent-getModifierKeyState?(keys: Array<string>): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keys | Array & lt;string & gt; | Yes | Obtains the pressed status of modifier keys. For details about the error message, see the following error codes. The following modifier keys are supported: 'Ctrl' \| 'Alt' \|

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getPreviewRect

```TypeScript
getPreviewRect(): Rectangle
```

Obtains the position of the drag preview relative to the current window and the preview size.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragEvent-getPreviewRect(): Rectangle--><!--Device-DragEvent-getPreviewRect(): Rectangle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Rectangle](arkts-arkui-rectangle-i.md) |

## getResult

```TypeScript
getResult(): DragResult
```

Obtains the drag result.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragEvent-getResult(): DragResult--><!--Device-DragEvent-getResult(): DragResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DragResult](arkts-arkui-dragresult-e.md) |

## getSummary

```TypeScript
getSummary(): Summary
```

Obtains a summary of drag data, including data type and size information. In a delayed drag scenario, only data type information can be obtained.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragEvent-getSummary(): Summary--><!--Device-DragEvent-getSummary(): Summary-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Summary](arkts-arkui-summary-t.md) |

## getVelocity

```TypeScript
getVelocity(): number
```

Obtains the dragging velocity along the main axis.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragEvent-getVelocity(): number--><!--Device-DragEvent-getVelocity(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getVelocityX

```TypeScript
getVelocityX(): number
```

Obtains the dragging velocity along the x-axis.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragEvent-getVelocityX(): number--><!--Device-DragEvent-getVelocityX(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getVelocityY

```TypeScript
getVelocityY(): number
```

Obtains the dragging velocity along the y-axis.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragEvent-getVelocityY(): number--><!--Device-DragEvent-getVelocityY(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getWindowX

```TypeScript
getWindowX(): number
```

Obtains the x-coordinate of the drag point relative to the upper left corner of the window.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragEvent-getWindowX(): number--><!--Device-DragEvent-getWindowX(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getWindowY

```TypeScript
getWindowY(): number
```

Obtains the y-coordinate of the drag point relative to the upper left corner of the window.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragEvent-getWindowY(): number--><!--Device-DragEvent-getWindowY(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getX

```TypeScript
getX(): number
```

Obtains the x-coordinate of the drag point relative to the upper left corner of the window, in vp.

> **NOTE：**

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [getWindowX](#getWindowX)

<!--Device-DragEvent-getX(): number--><!--Device-DragEvent-getX(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getY

```TypeScript
getY(): number
```

Obtains the y-coordinate of the drag point relative to the upper left corner of the window, in vp.

> **NOTE：**

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [getWindowY](#getWindowY)

<!--Device-DragEvent-getY(): number--><!--Device-DragEvent-getY(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## isRemote

```TypeScript
isRemote(): boolean
```

Checks whether the drag operation is cross-device.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DragEvent-isRemote(): boolean--><!--Device-DragEvent-isRemote(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## setData

```TypeScript
setData(unifiedData: UnifiedData): void
```

Sets drag-related data in **DragEvent**.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragEvent-setData(unifiedData: UnifiedData): void--><!--Device-DragEvent-setData(unifiedData: UnifiedData): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| unifiedData | [UnifiedData](arkts-arkui-unifieddata-t.md) | Yes |

## setDataLoadParams

```TypeScript
setDataLoadParams(dataLoadParams: DataLoadParams): void
```

Sets the parameters for deferred data loading from the drag source. This API provides data loading parameters to the system instead of directly providing complete data objects. When the user drops data on the target application,the system will use these parameters to request the actual data from the drag source. If this API is used together with [setData](#setData), the last called API takes precedence. This API takes effect only in the  
[onDragStart](arkts-arkui-commonmethod-c.md#onDragStart) callback.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DragEvent-setDataLoadParams(dataLoadParams: DataLoadParams): void--><!--Device-DragEvent-setDataLoadParams(dataLoadParams: DataLoadParams): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [dataLoadParams](../arkts-apis/arkts-arkui-dragcontroller-draginfo-i.md) | [DataLoadParams](arkts-arkui-dataloadparams-t.md) | Yes |

## setResult

```TypeScript
setResult(dragResult: DragResult): void
```

Sets the drag result in **DragEvent**.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragEvent-setResult(dragResult: DragResult): void--><!--Device-DragEvent-setResult(dragResult: DragResult): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dragResult | [DragResult](arkts-arkui-dragresult-e.md) | Yes |

## startDataLoading

```TypeScript
startDataLoading(options: DataSyncOptions): string
```

Asynchronously obtains drag data and notifies you of the current data synchronization progress. This API is only supported in the **onDrop** callback.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-DragEvent-startDataLoading(options: DataSyncOptions): string--><!--Device-DragEvent-startDataLoading(options: DataSyncOptions): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [DataSyncOptions](arkts-arkui-datasyncoptions-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [190003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-drag-event.md#190003-operation-not-allowed-in-the-current-phase) |

## autoHideComponentUniqueIds

```TypeScript
autoHideComponentUniqueIds?: number | number[]
```

Set the uniqueId or uniqueId array of components that need to be automatically hidden during dragging.This property takes effect only in onDragStart. After the drag starts successfully, the system hides the target components before the drag preview window is shown. Developers need to restore component visibility in onDragEnd or onDrop based on service requirements.

**Type:** number \| number[]

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-DragEvent-autoHideComponentUniqueIds?: int | int[]--><!--Device-DragEvent-autoHideComponentUniqueIds?: int | int[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dragBehavior

```TypeScript
dragBehavior: DragBehavior
```

Copy or paste mode.

Default value: **DragBehavior.COPY**

**Type:** [DragBehavior](arkts-arkui-dragbehavior-e.md)

**Default:** COPY

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragEvent-dragBehavior: DragBehavior--><!--Device-DragEvent-dragBehavior: DragBehavior-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## useCustomDropAnimation

```TypeScript
useCustomDropAnimation: boolean
```

Whether to disable the default drop animation when the dragging ends.

If this parameter is set to **true**, the default drop animation is disabled, and the custom one is used.

If this parameter is not set or is set to **false**, the default drop animation takes effect. When [setResult](#setResult)is set to **DRAG_SUCCESSFUL**, a shrink-out animation takes effect. Otherwise, an expand-out animation takes effect.

When the default drop animation is not disabled, avoid implementing custom animations to prevent conflicts.

Default value: **false**

**Type:** boolean

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragEvent-useCustomDropAnimation: boolean--><!--Device-DragEvent-useCustomDropAnimation: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
