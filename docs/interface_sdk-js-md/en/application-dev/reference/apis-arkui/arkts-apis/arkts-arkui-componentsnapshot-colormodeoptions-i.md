# ColorModeOptions

Defines the color mode used for current snapshot taking.By default, the system draws snapshot in sRGB mode. Therefore, snapshot for components with wide color display mode enabled will lose some effect. If you know the color space used in the component to be taken snapshot,you can specify the colorSpace parameter and set isAuto to false, for achieving the expected screenshot effect.But it is difficult to know which color space is used by the component to be taken. Therefore, in general,you can just set isAuto to true for letting the system to determine the color space to use based on the actual situation automaticly. When isAuto is set to true, value set by the colorSpace field will be ignored.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-componentSnapshot-export interface ColorModeOptions--><!--Device-componentSnapshot-export interface ColorModeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { componentSnapshot } from '@kit.ArkUI';
```

## colorSpace

```TypeScript
colorSpace?: colorSpaceManager.ColorSpace
```

Set one specific color space which want to be used.

**Type:** colorSpaceManager.ColorSpace

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorModeOptions-colorSpace?: colorSpaceManager.ColorSpace--><!--Device-ColorModeOptions-colorSpace?: colorSpaceManager.ColorSpace-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isAuto

```TypeScript
isAuto?: boolean
```

Indicate that if the system should decide the color space automatically.If set this to true, the one specified by colorSpace parameter will be ignored.

When setting isAuto to true, it is recommended to also set the waitUntilRenderFinished field in SnapshotOptions to true to ensure that the system can properly detect the mode being used.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorModeOptions-isAuto?: boolean--><!--Device-ColorModeOptions-isAuto?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

