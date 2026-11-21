# ToolBarDockCallback

```TypeScript
export declare type ToolBarDockCallback = (area: DockArea, direction: Axis) => void
```

Defines the callback invoked when the toolbar docks to the specified area and direction.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-unnamed-export declare type ToolBarDockCallback = (area: DockArea, direction: Axis) => void--><!--Device-unnamed-export declare type ToolBarDockCallback = (area: DockArea, direction: Axis) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| area | [DockArea](arkts-arkui-arkui-advanced-toolbarcontainer-dockarea-e.md) | Yes | Area where the toolbar is docked. |
| direction | [Axis](arkts-arkui-axis-e.md) | Yes | Docking direction. |
