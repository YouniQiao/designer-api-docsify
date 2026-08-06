# InputEventInterceptResult

Input event interception result interface, used by the listener callback  
[InputEventListener]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to return the interception decision.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-unnamed-declare interface InputEventInterceptResult--><!--Device-unnamed-declare interface InputEventInterceptResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
action: InputEventInterceptAction
```

Input event interception action.

**CONTINUE**: The event is allowed to continue being passed to the UI framework.

**BLOCK**: The event is blocked from being passed to the UI framework.

**Type:** InputEventInterceptAction

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-InputEventInterceptResult-action: InputEventInterceptAction--><!--Device-InputEventInterceptResult-action: InputEventInterceptAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

