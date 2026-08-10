# TransitionAnimation

窗口转场动画配置。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-window-interface TransitionAnimation--><!--Device-window-interface TransitionAnimation-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## config

```TypeScript
config: WindowAnimationConfig
```

本次转场动画配置。

**Type:** [WindowAnimationConfig](arkts-arkui-window-windowanimationconfig-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TransitionAnimation-config: WindowAnimationConfig--><!--Device-TransitionAnimation-config: WindowAnimationConfig-End-->

**System capability:** SystemCapability.Window.SessionManager

## opacity

```TypeScript
opacity?: double
```

不透明度，转场动画作用的窗口属性，值为0时窗口完全透明，默认值为1.0。当动画类型为WindowTransitionType.DESTROY时，代表动画终点的不透明度。取值范围0~1.0，在动画结束时恢复为1.0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TransitionAnimation-opacity?: double--><!--Device-TransitionAnimation-opacity?: double-End-->

**System capability:** SystemCapability.Window.SessionManager

