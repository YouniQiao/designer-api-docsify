# WindowAnimationConfig

Describes the configuration for window animation.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-window-interface WindowAnimationConfig--><!--Device-window-interface WindowAnimationConfig-End-->

**System capability:** SystemCapability.Window.SessionManager

## curve

```TypeScript
curve: WindowAnimationCurve
```

Type of animation curve.

**Type:** WindowAnimationCurve

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-WindowAnimationConfig-curve: WindowAnimationCurve--><!--Device-WindowAnimationConfig-curve: WindowAnimationCurve-End-->

**System capability:** SystemCapability.Window.SessionManager

## duration

```TypeScript
duration?: long
```

Duration for playing the animation, in milliseconds (ms).

The default value is 0, and the maximum value is 3000.

Whether it is required depends on the animation curve type.

**Type:** long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-WindowAnimationConfig-duration?: long--><!--Device-WindowAnimationConfig-duration?: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## param

```TypeScript
param?: WindowAnimationCurveParam
```

Parameters for the animation curve. Whether it is required depends on the animation curve type.

**Type:** WindowAnimationCurveParam

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-WindowAnimationConfig-param?: WindowAnimationCurveParam--><!--Device-WindowAnimationConfig-param?: WindowAnimationCurveParam-End-->

**System capability:** SystemCapability.Window.SessionManager

