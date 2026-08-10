# NavDestinationTransition

NavDestination自定义动画接口。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

<!--Device-unnamed-declare interface NavDestinationTransition--><!--Device-unnamed-declare interface NavDestinationTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## curve

```TypeScript
curve?: Curve
```

动画的曲线类型，默认值为[Curve.EaseInOut](../arkts-apis/arkts-arkui-curve-t.md/arkts-arkui-curve-t.md)。

**Type:** [Curve](../arkts-apis/arkts-arkui-curve-e.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-NavDestinationTransition-curve?: Curve--><!--Device-NavDestinationTransition-curve?: Curve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## delay

```TypeScript
delay?: number
```

转场动画的延迟。

取值范围：[0, +∞)

默认值：0（毫秒）

单位：ms

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-NavDestinationTransition-delay?: number--><!--Device-NavDestinationTransition-delay?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: number
```

转场动画的持续时间。

取值范围：[0, +∞)

默认值：1000（毫秒）

单位：ms

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-NavDestinationTransition-duration?: number--><!--Device-NavDestinationTransition-duration?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## event

```TypeScript
event: Callback<void>
```

指定转场动效的闭包函数，系统会根据闭包中对组件UI状态的修改，生成对应的过渡动画。参见[animateTo](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md/arkts-arkui-arkui-uicontext-uicontext-c.md#animatetoimmediately)中的event。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-NavDestinationTransition-event: Callback<void>--><!--Device-NavDestinationTransition-event: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTransitionEnd

```TypeScript
onTransitionEnd?: Callback<void>
```

转场动画结束时的回调函数。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-NavDestinationTransition-onTransitionEnd?: Callback<void>--><!--Device-NavDestinationTransition-onTransitionEnd?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

