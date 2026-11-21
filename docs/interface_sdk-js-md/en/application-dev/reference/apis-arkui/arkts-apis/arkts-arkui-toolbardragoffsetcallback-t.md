# ToolBarDragOffsetCallback

```TypeScript
export declare type ToolBarDragOffsetCallback = (x: number, y: number) => void
```

Defines the callback for the drag offset relative to the ToolBarContainer container.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-unnamed-export declare type ToolBarDragOffsetCallback = (x: number, y: number) => void--><!--Device-unnamed-export declare type ToolBarDragOffsetCallback = (x: number, y: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | Yes | Offset along the X-axis, in vp. |
| y | number | Yes | Offset along the Y-axis, in vp. |
