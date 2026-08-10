# TabContentAnimatedTransition

Tabs自定义切换动画相关信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TabContentAnimatedTransition--><!--Device-unnamed-export declare interface TabContentAnimatedTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timeout

```TypeScript
timeout?: int
```

Tabs自定义切换动画超时时间。从自定义动画开始切换计时，如果到达该时间后，开发者仍未调用[TabContentTransitionProxy](../arkts-components/arkts-arkui-tabcontenttransitionproxy-i.md/arkts-arkui-tabcontenttransitionproxy-i.md)的finishTransition接口通知Tabs组件自定义动画结束，那么组件就会认为此次自定义动画已结束，直接执行后续操作。单位为： ms，取值应为≥0的整数。 默认值： 1000。

**Type:** int

**Default:** 1000 ms

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabContentAnimatedTransition-timeout?: int--><!--Device-TabContentAnimatedTransition-timeout?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transition

```TypeScript
transition: Callback<TabContentTransitionProxy>
```

自定义切换动画具体内容。

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;TabContentTransitionProxy&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabContentAnimatedTransition-transition: Callback<TabContentTransitionProxy>--><!--Device-TabContentAnimatedTransition-transition: Callback<TabContentTransitionProxy>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

