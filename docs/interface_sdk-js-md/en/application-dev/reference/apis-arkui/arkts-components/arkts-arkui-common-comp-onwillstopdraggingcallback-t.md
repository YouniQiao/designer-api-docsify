# OnWillStopDraggingCallback

```TypeScript
declare type OnWillStopDraggingCallback = (velocity: number) => void
```

Defines the callback invoked when the scrollable component is released.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| velocity | number | Yes | Scroll velocity. Positive for scrolling upward, negative for scrolling downward.<br>Unit: vp/s. |
