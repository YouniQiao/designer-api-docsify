# UIStatesChangeHandler

```TypeScript
declare type UIStatesChangeHandler = (node: FrameNode, currentUIStates: int) => void
```

UI状态变化处理函数，返回当前UI状态，值为结果的所有当前状态枚举值或计算，并且可以确定状态通过执行&操作，如下。如果(currentStates & UIState.PRESSED == UIState.PRESSED)但是，请注意，对于正常的状态检查，应该直接使用equal。如果(currentStates == UIState.NORMAL)。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare type UIStatesChangeHandler = (node: FrameNode, currentUIStates: int) => void--><!--Device-unnamed-declare type UIStatesChangeHandler = (node: FrameNode, currentUIStates: int) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 触发UI状态变化的节点。 |
| currentUIStates | int | Yes | 回调触发时当前的UI状态。可以通过位与运算判断当前包含哪些[UIState](arkts-arkui-framenode-uistate-e.md)状态。位与运算方法：if (currentState & UIState.PRESSED == UIState.PRESSED)。一般的UIState状态检查可以直接判断：if (currentState == UIState.PRESSED)。 <br>取值限定为整数。 |

