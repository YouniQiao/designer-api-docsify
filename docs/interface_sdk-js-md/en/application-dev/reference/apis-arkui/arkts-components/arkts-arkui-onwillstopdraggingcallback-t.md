# OnWillStopDraggingCallback

```TypeScript
declare type OnWillStopDraggingCallback = (velocity: number) => void
```

On scroll callback using in scrollable onWillStopDragging.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

<!--Device-unnamed-declare type OnWillStopDraggingCallback = (velocity: number) => void--><!--Device-unnamed-declare type OnWillStopDraggingCallback = (velocity: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| velocity | number | Yes | The veolicity of the scroll view at the moment the touch was released. |

