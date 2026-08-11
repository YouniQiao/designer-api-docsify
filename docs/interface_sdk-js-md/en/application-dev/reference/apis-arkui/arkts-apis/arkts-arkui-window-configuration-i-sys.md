# Configuration

Defines the parameters for creating a child window or system window.

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

Whether the window should use the default density of the system. If the default density is used, the window does not re-layout when the system display size changes.

If this parameter is set to **true** for a system window, the window uses the default density and is not affected by  
[setDefaultDensityEnabled()](arkts-arkui-window-windowstage-i.md#setdefaultdensityenabled)or [setCustomDensity()](@ohos.window:window.Window.setCustomDensity)settings for the main window or  
[setDefaultDensityEnabled()](arkts-arkui-window-windowstage-i.md#setdefaultdensityenabled)settings for the current window.

If this parameter is set to **false**, the window does not use the default density and is affected by those settings.

The default value is **false**.

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

Z-level of the system window. This parameter is valid only when [WindowType](arkts-arkui-window-windowtype-e.md) is set to  
**TYPE_DYNAMIC**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Configuration-zIndex?: int--><!--Device-Configuration-zIndex?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

