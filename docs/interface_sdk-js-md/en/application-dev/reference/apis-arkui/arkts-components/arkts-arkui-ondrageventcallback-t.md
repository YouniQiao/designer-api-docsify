# OnDragEventCallback

```TypeScript
declare type OnDragEventCallback = (event: DragEvent, extraParams?: string) => void
```

拖拽事件的回调函数。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-unnamed-declare type OnDragEventCallback = (event: DragEvent, extraParams?: string) => void--><!--Device-unnamed-declare type OnDragEventCallback = (event: DragEvent, extraParams?: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [DragEvent](arkts-arkui-dragevent-i.md) | Yes | event为拖拽事件信息，包括拖拽点坐标。 |
| extraParams | string | No | extraParams为拖拽事件额外信息，需要解析为JSON格式。 |

