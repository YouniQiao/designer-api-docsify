# DockCornerMode

```TypeScript
export enum DockCornerMode
```

Defines the snapping mode used when the floating toolbar is dragged to a corner.

**Since:** 26.1.0

<!--Device-unnamed-export enum DockCornerMode--><!--Device-unnamed-export enum DockCornerMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## EXPAND

```TypeScript
EXPAND = 1
```

Retains the drag direction without minimizing the toolbar.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DockCornerMode-EXPAND = 1--><!--Device-DockCornerMode-EXPAND = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## MINIMIZE

```TypeScript
MINIMIZE = 0
```

Snaps the toolbar to a corner and minimizes it; after the corner is clicked, the toolbar follows the edge where it is located.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DockCornerMode-MINIMIZE = 0--><!--Device-DockCornerMode-MINIMIZE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
