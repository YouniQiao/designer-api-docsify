# InputEventInterceptResult

Defines the input event intercept result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export declare interface InputEventInterceptResult--><!--Device-unnamed-export declare interface InputEventInterceptResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
action: InputEventInterceptAction
```

Event intercept decision. - CONTINUE: Allows the event to continue to be delivered to the UI framework. - BLOCK: Blocks the event from being delivered, the event will not enter the UI framework.

**Type:** [InputEventInterceptAction](../../apis-arkui/arkts-apis/arkts-arkui-inputeventinterceptaction-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputEventInterceptResult-action: InputEventInterceptAction--><!--Device-InputEventInterceptResult-action: InputEventInterceptAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

