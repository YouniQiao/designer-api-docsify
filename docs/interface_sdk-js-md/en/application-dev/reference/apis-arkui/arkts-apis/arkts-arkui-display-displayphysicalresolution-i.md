# DisplayPhysicalResolution

Describes the display mode of a device and the corresponding physical screen resolution information.

**Since:** 23

<!--Device-display-interface DisplayPhysicalResolution--><!--Device-display-interface DisplayPhysicalResolution-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## foldDisplayMode

```TypeScript
foldDisplayMode: FoldDisplayMode
```

Display mode of the device. The value is **0** for non-foldable devices.

**Type:** [FoldDisplayMode](arkts-arkui-display-folddisplaymode-e.md)

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-DisplayPhysicalResolution-foldDisplayMode: FoldDisplayMode--><!--Device-DisplayPhysicalResolution-foldDisplayMode: FoldDisplayMode-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## physicalHeight

```TypeScript
physicalHeight: long
```

Height of the device, in px. The value is an integer greater than 0.

**Type:** long

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-DisplayPhysicalResolution-physicalHeight: long--><!--Device-DisplayPhysicalResolution-physicalHeight: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## physicalWidth

```TypeScript
physicalWidth: long
```

Width of the device, in px. The value is an integer greater than 0.

**Type:** long

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-DisplayPhysicalResolution-physicalWidth: long--><!--Device-DisplayPhysicalResolution-physicalWidth: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

