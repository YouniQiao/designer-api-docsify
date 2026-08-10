# InputEventInterceptResult

输入事件拦截结果接口，用于监听器回调[InputEventListener](arkts-arkui-inputeventlistener-t.md)返回是否拦截的决策。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-unnamed-declare interface InputEventInterceptResult--><!--Device-unnamed-declare interface InputEventInterceptResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
action: InputEventInterceptAction
```

输入事件拦截动作。

CONTINUE：允许事件继续传递到UI框架。

BLOCK：阻止事件传递到UI框架。

**Type:** [InputEventInterceptAction](../arkts-apis/arkts-arkui-inputeventinterceptaction-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-InputEventInterceptResult-action: InputEventInterceptAction--><!--Device-InputEventInterceptResult-action: InputEventInterceptAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

