# WindowCreateParams

应用启动时的窗口参数配置。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-window-interface WindowCreateParams--><!--Device-window-interface WindowCreateParams-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## isWindowLimitsForcible

```TypeScript
isWindowLimitsForcible?: boolean
```

是否覆盖系统窗口尺寸限制。如果为true，则当前主窗口可以设置超出系统限制的窗口尺寸限制。

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

启动动画配置，仅对全屏应用生效。

不同应用间跳转场景不生效，仍保持系统默认动效。

**Type:** [StartAnimationSystemParams](arkts-arkui-window-startanimationsystemparams-i-sys.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-WindowCreateParams-systemAnimationParams?: StartAnimationSystemParams--><!--Device-WindowCreateParams-systemAnimationParams?: StartAnimationSystemParams-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

