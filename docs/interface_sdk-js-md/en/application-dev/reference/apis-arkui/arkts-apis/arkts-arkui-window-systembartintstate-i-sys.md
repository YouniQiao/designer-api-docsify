# SystemBarTintState (System API)

Describes the callback for the current system bar.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-window-interface SystemBarTintState--><!--Device-window-interface SystemBarTintState-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## displayId

```TypeScript
displayId: long
```

ID of the screen where the window is located. The value must be an integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SystemBarTintState-displayId: long--><!--Device-SystemBarTintState-displayId: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## regionTint

```TypeScript
regionTint: Array<SystemBarRegionTint>
```

All system bar information that has been changed.

**Type:** Array&lt;[SystemBarRegionTint](arkts-arkui-window-systembarregiontint-i-sys.md)&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SystemBarTintState-regionTint: Array<SystemBarRegionTint>--><!--Device-SystemBarTintState-regionTint: Array<SystemBarRegionTint>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

