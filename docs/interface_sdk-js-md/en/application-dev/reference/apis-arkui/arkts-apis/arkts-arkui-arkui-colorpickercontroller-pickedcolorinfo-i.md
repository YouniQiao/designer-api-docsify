# PickedColorInfo

```TypeScript
export interface PickedColorInfo
```

Global color picking result object, containing the basic information of the picked color.

**Since:** 26.1.0

<!--Device-unnamed-export interface PickedColorInfo--><!--Device-unnamed-export interface PickedColorInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { colorPickerController, PickedColorInfo } from '@kit.ArkUI';
```

## brightness

```TypeScript
brightness?: number
```

Color brightness, in nit. Available when the picked pixel is HDR content. Unit: nit. Default value: 0.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PickedColorInfo-brightness?: number--><!--Device-PickedColorInfo-brightness?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color: common2D.Color
```

Color value.

**Type:** [common2D.Color](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-common2d-color-i.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PickedColorInfo-color: common2D.Color--><!--Device-PickedColorInfo-color: common2D.Color-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## colorSpace

```TypeScript
colorSpace: colorSpaceManager.ColorSpace
```

Color space.

**Type:** [colorSpaceManager.ColorSpace](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-colorspacemanager-colorspace-e.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PickedColorInfo-colorSpace: colorSpaceManager.ColorSpace--><!--Device-PickedColorInfo-colorSpace: colorSpaceManager.ColorSpace-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timestamp

```TypeScript
timestamp: number
```

Timestamp, elapsed time since system startup, in ms. Unit: ms.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PickedColorInfo-timestamp: number--><!--Device-PickedColorInfo-timestamp: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
