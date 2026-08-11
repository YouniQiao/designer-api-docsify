# NavDestinationTransition

NavDestination animation protocol.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface NavDestinationTransition--><!--Device-unnamed-export declare interface NavDestinationTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## curve

```TypeScript
curve?: Curve
```

Define the curve of the transition animation.

**Type:** [Curve](arkts-arkui-curve-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationTransition-curve?: Curve--><!--Device-NavDestinationTransition-curve?: Curve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## delay

```TypeScript
delay?: int
```

Define the delay of the transition animation.The value range is all integers.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationTransition-delay?: int--><!--Device-NavDestinationTransition-delay?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: int
```

Define the limit duration of the transition animation.The value range is all integers.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationTransition-duration?: int--><!--Device-NavDestinationTransition-duration?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## event

```TypeScript
event: VoidCallback
```

Configure the custom transition event.

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationTransition-event: VoidCallback--><!--Device-NavDestinationTransition-event: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTransitionEnd

```TypeScript
onTransitionEnd?: VoidCallback
```

This method is called after the transition ends to notify whether the transition was successful.

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationTransition-onTransitionEnd?: VoidCallback--><!--Device-NavDestinationTransition-onTransitionEnd?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

