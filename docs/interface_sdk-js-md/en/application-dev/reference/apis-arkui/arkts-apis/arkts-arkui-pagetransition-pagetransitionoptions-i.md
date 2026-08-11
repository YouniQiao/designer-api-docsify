# PageTransitionOptions

Defines pageTransition constructor parameters.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface PageTransitionOptions--><!--Device-unnamed-export declare interface PageTransitionOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## curve

```TypeScript
curve?: Curve | string | ICurve
```

PageTransition animation curve.

**Type:** [Curve](arkts-arkui-curve-e.md) \| string \| ICurve

**Default:** Curve.Linear

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransitionOptions-curve?: Curve | string | ICurve--><!--Device-PageTransitionOptions-curve?: Curve | string | ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## delay

```TypeScript
delay?: int
```

PageTransition animation delay time, in ms.

**Type:** int

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransitionOptions-delay?: int--><!--Device-PageTransitionOptions-delay?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: int
```

PageTransition animation duration, in ms.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransitionOptions-duration?: int--><!--Device-PageTransitionOptions-duration?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type?: RouteType
```

RouteType in which the pageTransition can work.

**Type:** [RouteType](../arkts-components/arkts-arkui-routetype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransitionOptions-type?: RouteType--><!--Device-PageTransitionOptions-type?: RouteType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

