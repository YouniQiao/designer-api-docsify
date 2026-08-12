# TabContentAnimatedTransition

Defines the Tab Content animated transition options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TabContentAnimatedTransition--><!--Device-unnamed-export declare interface TabContentAnimatedTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timeout

```TypeScript
timeout?: int
```

Defines the timeout of custom content transition animation. The unit is ms.If TabContentTransitionProxy.finishTransition() is not invoked, use the timeout as animation end time.Unit: ms, The value must be an integer greater than or equal to 0. Default value: 1000.

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

Called when custom content transition animation start.Anonymous Object Rectification

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[TabContentTransitionProxy](arkts-arkui-tabs-tabcontenttransitionproxy-i.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabContentAnimatedTransition-transition: Callback<TabContentTransitionProxy>--><!--Device-TabContentAnimatedTransition-transition: Callback<TabContentTransitionProxy>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

