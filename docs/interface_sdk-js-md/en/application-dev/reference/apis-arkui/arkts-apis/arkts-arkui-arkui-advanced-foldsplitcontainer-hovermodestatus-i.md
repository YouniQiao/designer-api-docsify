# HoverModeStatus

Provides information about the device or application's folding, rotation, and window state.

**Since:** 12

<!--Device-unnamed-export interface HoverModeStatus--><!--Device-unnamed-export interface HoverModeStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { HoverModeStatus, ExtraRegionPosition, OnHoverStatusChangeHandler, ExpandedRegionLayoutOptions, FoldSplitContainer, HoverModeRegionLayoutOptions, FoldedRegionLayoutOptions, PresetSplitRatio } from '@kit.ArkUI';
```

## appRotation

```TypeScript
appRotation: number
```

Rotation angle of the application.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HoverModeStatus-appRotation: number--><!--Device-HoverModeStatus-appRotation: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## foldStatus

```TypeScript
foldStatus: display.FoldStatus
```

Fold status of the device.

**Type:** display.FoldStatus

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HoverModeStatus-foldStatus: display.FoldStatus--><!--Device-HoverModeStatus-foldStatus: display.FoldStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isHoverMode

```TypeScript
isHoverMode: boolean
```

Whether the application is in the hover state. The value **true** means that the application is in the hover state, and **false** means the opposite.

**Type:** boolean

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HoverModeStatus-isHoverMode: boolean--><!--Device-HoverModeStatus-isHoverMode: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowStatusType

```TypeScript
windowStatusType: window.WindowStatusType
```

Window mode.

**Type:** window.WindowStatusType

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-HoverModeStatus-windowStatusType: window.WindowStatusType--><!--Device-HoverModeStatus-windowStatusType: window.WindowStatusType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

