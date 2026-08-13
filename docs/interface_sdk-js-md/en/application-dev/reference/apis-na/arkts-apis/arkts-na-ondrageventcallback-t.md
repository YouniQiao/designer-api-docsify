# OnDragEventCallback

```TypeScript
export type OnDragEventCallback = (event: DragEvent, extraParams?: string) => void
```

The event callback function for drag and drop common interfaces.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnDragEventCallback = (event: DragEvent, extraParams?: string) => void--><!--Device-unnamed-export type OnDragEventCallback = (event: DragEvent, extraParams?: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [DragEvent](arkts-na-common-dragevent-i.md) | Yes | the event object indicating current drag status. |
| extraParams | string | No | extra information set by user or system. |

