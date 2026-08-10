# DisplayPhysicalResolution

设备的显示模式以及对应的物理屏幕分辨率信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-display-interface DisplayPhysicalResolution--><!--Device-display-interface DisplayPhysicalResolution-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## foldDisplayMode

```TypeScript
foldDisplayMode: FoldDisplayMode
```

设备的显示模式，非折叠设备时值为0。

**Type:** [FoldDisplayMode](arkts-arkui-display-folddisplaymode-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DisplayPhysicalResolution-foldDisplayMode: FoldDisplayMode--><!--Device-DisplayPhysicalResolution-foldDisplayMode: FoldDisplayMode-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## physicalHeight

```TypeScript
physicalHeight: long
```

设备的高度，单位为px，该参数为大于0的整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DisplayPhysicalResolution-physicalHeight: long--><!--Device-DisplayPhysicalResolution-physicalHeight: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## physicalWidth

```TypeScript
physicalWidth: long
```

设备的宽度，单位为px，该参数为大于0的整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DisplayPhysicalResolution-physicalWidth: long--><!--Device-DisplayPhysicalResolution-physicalWidth: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

