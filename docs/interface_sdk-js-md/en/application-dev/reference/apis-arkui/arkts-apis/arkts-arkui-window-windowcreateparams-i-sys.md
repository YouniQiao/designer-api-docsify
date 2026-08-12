# WindowCreateParams

Describes the window parameters during application startup.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-window-interface WindowCreateParams--><!--Device-window-interface WindowCreateParams-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## isWindowLimitsForcible

```TypeScript
isWindowLimitsForcible?: boolean
```

Whether to override system window limits.If true, the main window of the current ability can set a window limit that exceeds system restrictions.

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowCreateParams-isWindowLimitsForcible?: boolean--><!--Device-WindowCreateParams-isWindowLimitsForcible?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## systemAnimationParams

```TypeScript
systemAnimationParams?: StartAnimationSystemParams
```

Describes the start animation configuration. This API works only for full-screen applications.

The configuration does not take effect for inter-application transitions, where the default animation of the system is used.

**Type:** [StartAnimationSystemParams](arkts-arkui-window-startanimationsystemparams-i-sys.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-WindowCreateParams-systemAnimationParams?: StartAnimationSystemParams--><!--Device-WindowCreateParams-systemAnimationParams?: StartAnimationSystemParams-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

