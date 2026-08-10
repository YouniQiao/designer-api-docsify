# Configuration

创建子窗口或系统窗口时的参数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-window-interface Configuration--><!--Device-window-interface Configuration-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## defaultDensityEnabled

```TypeScript
defaultDensityEnabled?: boolean
```

是否使用系统默认Density，使用系统默认Density之后，窗口不会跟随系统显示大小变化重新布局。

当创建的系统窗口设置此参数为true时，表示当前窗口使用系统默认Density，且不会受到  
[setDefaultDensityEnabled()](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#setdefaultdensityenabled12)和[setCustomDensity()](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#setcustomdensity15)设置的主窗口以及  
[setDefaultDensityEnabled()](arkts-arkui-window-window-i-sys.md#setdefaultdensityenabled)设置的本窗口的相关影响。

当创建的系统窗口设置此参数为false时，表示当前窗口不使用系统默认Density，且会受到  
[setDefaultDensityEnabled()](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#setdefaultdensityenabled12)和[setCustomDensity()](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#setcustomdensity15)设置的主窗口以及  
[setDefaultDensityEnabled()](arkts-arkui-window-window-i-sys.md#setdefaultdensityenabled)设置的本窗口的相关影响。

默认为false。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Configuration-defaultDensityEnabled?: boolean--><!--Device-Configuration-defaultDensityEnabled?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## zIndex

```TypeScript
zIndex?: int
```

当前系统窗口的层级，仅在[WindowType](arkts-arkui-window-windowtype-e.md)为TYPE_DYNAMIC时生效。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Configuration-zIndex?: int--><!--Device-Configuration-zIndex?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

