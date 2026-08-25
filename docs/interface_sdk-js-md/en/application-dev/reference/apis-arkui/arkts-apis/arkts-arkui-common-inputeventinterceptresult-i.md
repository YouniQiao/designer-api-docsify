# InputEventInterceptResult

Defines the input event intercept result.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
action: InputEventInterceptAction
```

Event intercept decision. - CONTINUE: Allows the event to continue to be delivered to the UI framework. - BLOCK: Blocks the event from being delivered, the event will not enter the UI framework.

**Type:** [InputEventInterceptAction](arkts-arkui-inputeventinterceptaction-e.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
