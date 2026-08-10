# TabContentAnimatedTransition

Tabs自定义切换动画相关信息。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface TabContentAnimatedTransition--><!--Device-unnamed-declare interface TabContentAnimatedTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timeout

```TypeScript
timeout?: number
```

自定义切换动画超时时间。如果到达该时间后，开发者仍未调用[TabContentTransitionProxy](arkts-arkui-tabcontenttransitionproxy-i.md)的finishTransition接口通知Tabs组件自定义动画结束，那么组件就会认为此次自定义动画已结束，直接执行后续操作。

默认值：1000

单位：ms

取值范围：[0, +∞)。设置为小于0的值时，按默认值显示。

**Type:** number

**Default:** 1000 ms

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-TabContentAnimatedTransition-timeout?: number--><!--Device-TabContentAnimatedTransition-timeout?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transition

```TypeScript
transition: Callback<TabContentTransitionProxy>
```

自定义切换动画具体内容。

**Type:** [Callback](arkts-arkui-callback-i.md)&lt;TabContentTransitionProxy&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-TabContentAnimatedTransition-transition: Callback<TabContentTransitionProxy>--><!--Device-TabContentAnimatedTransition-transition: Callback<TabContentTransitionProxy>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

