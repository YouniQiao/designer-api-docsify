# TransitionAnimation

Describes the window transition animation.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-window-interface TransitionAnimation--><!--Device-window-interface TransitionAnimation-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'window';
```

## config

```TypeScript
config: WindowAnimationConfig
```

Transition animation configuration.

**Type:** [WindowAnimationConfig](arkts-arkui-window-windowanimationconfig-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TransitionAnimation-config: WindowAnimationConfig--><!--Device-TransitionAnimation-config: WindowAnimationConfig-End-->

**System capability:** SystemCapability.Window.SessionManager

## opacity

```TypeScript
opacity?: double
```

Opacity of the window during the transition animation. If this parameter is set to **0**, the window is completely transparent. The default value is **1.0**. When the animation type is **WindowTransitionType.DESTROY** , this represents the opacity at the end of the animation. The value ranges from 0 to 1.0. The value is reset to **1.0** when the animation ends.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TransitionAnimation-opacity?: double--><!--Device-TransitionAnimation-opacity?: double-End-->

**System capability:** SystemCapability.Window.SessionManager

