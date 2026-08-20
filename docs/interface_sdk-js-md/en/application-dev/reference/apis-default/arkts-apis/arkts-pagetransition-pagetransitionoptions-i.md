# PageTransitionOptions

Defines pageTransition constructor parameters.

@interface PageTransitionOptions

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface PageTransitionOptions--><!--Device-unnamed-export declare interface PageTransitionOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## curve

```TypeScript
curve?: Curve | string | ICurve
```

PageTransition animation curve.

**Type:** [Curve](../../apis-arkui/arkts-apis/arkts-arkui-curve-e.md) \| string \| [ICurve](../../apis-arkui/arkts-components/arkts-arkui-icurve-i.md)

**Default:** Curve.Linear

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransitionOptions-duration?: int--><!--Device-PageTransitionOptions-duration?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type?: RouteType
```

RouteType in which the pageTransition can work.

**Type:** [RouteType](arkts-pagetransition-routetype-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransitionOptions-type?: RouteType--><!--Device-PageTransitionOptions-type?: RouteType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

