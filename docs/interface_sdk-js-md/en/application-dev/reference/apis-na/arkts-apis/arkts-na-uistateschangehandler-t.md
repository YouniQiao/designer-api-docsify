# UIStatesChangeHandler

```TypeScript
declare type UIStatesChangeHandler = (node: FrameNode, currentUIStates: int) => void
```

UI state change handling function, it returns the current UI states, the value is the result of all current state enumeration values or calculations, and you can determine the state by performing the & operation as follows。 if (currentStates & UIState.PRESSED == UIState.PRESSED) But, please be awared, for the normal state check, the equal should be used directly. if (currentStates == UIState.NORMAL)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare type UIStatesChangeHandler = (node: FrameNode, currentUIStates: int) => void--><!--Device-unnamed-declare type UIStatesChangeHandler = (node: FrameNode, currentUIStates: int) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Yes | Current node which is triggering the state change. |
| currentUIStates | int | Yes | Current UI states when the handler is triggered. |

