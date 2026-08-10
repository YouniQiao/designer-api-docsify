# NavDestinationTransition

NavDestination自定义动画接口。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface NavDestinationTransition--><!--Device-unnamed-export declare interface NavDestinationTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## curve

```TypeScript
curve?: Curve
```

动画的曲线类型，默认值为[Curve.EaseInOut](arkts-arkui-curve-t.md)。

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

转场动画的延迟。取值范围为全体整数，单位：ms。 默认值： 0（毫秒）。

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

转场动画的持续时间。取值范围为全体整数，单位：ms。 默认值： 1000（毫秒）。

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

指定转场动效的闭包函数，系统会根据闭包中对组件UI状态的修改，生成对应的过渡动画。参见  
[animateTo](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#animateto)中的event。

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

转场动画结束时的回调函数。

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavDestinationTransition-onTransitionEnd?: VoidCallback--><!--Device-NavDestinationTransition-onTransitionEnd?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

