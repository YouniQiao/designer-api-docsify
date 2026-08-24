# DragAction

One drag action object for drag process@interface DragAction

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-dragController-interface DragAction--><!--Device-dragController-interface DragAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { dragController } from '@kit.ArkUI';
```

## offStatusChange

```TypeScript
offStatusChange(callback?: Callback<DragAndDropInfo>): void
```

Deregisters a callback for listening on drag status changes. This callback is not triggered when the drag status change.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragAction-offStatusChange(callback?: Callback<DragAndDropInfo>): void--><!--Device-DragAction-offStatusChange(callback?: Callback<DragAndDropInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DragAndDropInfo](arkts-arkui-dragcontroller-draganddropinfo-i.md)&gt; | No | with drag event and status information |

## onStatusChange

```TypeScript
onStatusChange(callback: Callback<DragAndDropInfo>): void
```

Registers a callback for listening on drag status changes. This callback is triggered when the drag status change.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragAction-onStatusChange(callback: Callback<DragAndDropInfo>): void--><!--Device-DragAction-onStatusChange(callback: Callback<DragAndDropInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DragAndDropInfo](arkts-arkui-dragcontroller-draganddropinfo-i.md)&gt; | Yes | with drag event and status information |

## startDrag

```TypeScript
startDrag(): Promise<void> | null
```

trigger drag action

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragAction-startDrag(): Promise<void> | null--><!--Device-DragAction-startDrag(): Promise<void> | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; \| null | A Promise can indicate the start result is returned, or null is returned if it's failed for some errors, for example: execution environment broken or excess parameters passed in. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../errorcode-internal.md#100001-internal-error) | Internal handling failed. |

