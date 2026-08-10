# WindowAnimationConfig

窗口动画参数配置。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-window-interface WindowAnimationConfig--><!--Device-window-interface WindowAnimationConfig-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## curve

```TypeScript
curve: WindowAnimationCurve
```

动画曲线类型。

**Type:** [WindowAnimationCurve](arkts-arkui-window-windowanimationcurve-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-WindowAnimationConfig-curve: WindowAnimationCurve--><!--Device-WindowAnimationConfig-curve: WindowAnimationCurve-End-->

**System capability:** SystemCapability.Window.SessionManager

## duration

```TypeScript
duration?: long
```

动画播放的时长，单位毫秒（ms）。

默认值：0，最大值：3000。

根据动画曲线类型决定是否必填。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-WindowAnimationConfig-duration?: long--><!--Device-WindowAnimationConfig-duration?: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## param

```TypeScript
param?: WindowAnimationCurveParam
```

动画曲线参数，根据动画曲线类型决定是否必填。

**Type:** [WindowAnimationCurveParam](arkts-arkui-windowanimationcurveparam-t.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-WindowAnimationConfig-param?: WindowAnimationCurveParam--><!--Device-WindowAnimationConfig-param?: WindowAnimationCurveParam-End-->

**System capability:** SystemCapability.Window.SessionManager

