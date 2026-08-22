# NavigationAnimatedTransition

Navigation transition animation protocol.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface NavigationAnimatedTransition--><!--Device-unnamed-export declare interface NavigationAnimatedTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isInteractive

```TypeScript
isInteractive?: boolean
```

Indicates whether it is an interactive transition. Default value: false.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAnimatedTransition-isInteractive?: boolean--><!--Device-NavigationAnimatedTransition-isInteractive?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTransitionEnd

```TypeScript
onTransitionEnd?: (success: boolean) => void
```

This method is called after the transition ends to notify whether the transition was successful.

**Type:** (success: boolean) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAnimatedTransition-onTransitionEnd?: (success: boolean) => void--><!--Device-NavigationAnimatedTransition-onTransitionEnd?: (success: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timeout

```TypeScript
timeout?: int
```

Define the limit duration of the transition animation. Unit: ms, The value must be an integer greater than or equal to 0, The default timeout period for non-interactive animations is 1000 ms. There is no default value for interactive animations.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAnimatedTransition-timeout?: int--><!--Device-NavigationAnimatedTransition-timeout?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transition

```TypeScript
transition: (transitionProxy: NavigationTransitionProxy) => void
```

Configure the animations associated with custom transition.

**Type:** (transitionProxy: NavigationTransitionProxy) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationAnimatedTransition-transition: (transitionProxy: NavigationTransitionProxy) => void--><!--Device-NavigationAnimatedTransition-transition: (transitionProxy: NavigationTransitionProxy) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

