# SystemBarTintState (System API)

当前系统栏回调信息集合。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-window-interface SystemBarTintState--><!--Device-window-interface SystemBarTintState-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## displayId

```TypeScript
displayId: long
```

当前窗口所在屏幕id，该参数应为整数。

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

当前已改变的所有系统栏信息。

**Type:** Array&lt;SystemBarRegionTint&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SystemBarTintState-regionTint: Array<SystemBarRegionTint>--><!--Device-SystemBarTintState-regionTint: Array<SystemBarRegionTint>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

