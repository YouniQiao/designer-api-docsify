# StartAnimationSystemParams (System API)

启动动画配置，仅对全屏应用生效。

不同应用间跳转场景不生效，仍保持系统默认动效。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-window-interface StartAnimationSystemParams--><!--Device-window-interface StartAnimationSystemParams-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## animationConfig

```TypeScript
animationConfig?: WindowAnimationConfig
```

窗口动画参数配置。默认动画曲线为WindowAnimationCurve.LINEAR，duration为0。

**Type:** [WindowAnimationConfig](arkts-arkui-window-windowanimationconfig-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-StartAnimationSystemParams-animationConfig?: WindowAnimationConfig--><!--Device-StartAnimationSystemParams-animationConfig?: WindowAnimationConfig-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## type

```TypeScript
type: AnimationType
```

窗口动画类型。

**Type:** [AnimationType](arkts-arkui-window-animationtype-e-sys.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-StartAnimationSystemParams-type: AnimationType--><!--Device-StartAnimationSystemParams-type: AnimationType-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

