# bindTextInputController

## bindTextInputController

```TypeScript
export function bindTextInputController(node: FrameNode, controller: TextInputController): void
```

Bind the controller of FrameNode which type is TextInput.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function bindTextInputController(node: FrameNode, controller: TextInputController): void--><!--Device-typeNode-export function bindTextInputController(node: FrameNode, controller: TextInputController): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the target FrameNode. |
| controller | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the controller which is bind to the target FrameNode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100023](../errorcode-node.md#100023-parameter-error) | Parameter error. Possible causes: 1. The component type of the node is incorrect. 2. The node is null or undefined. 3. The controller is null or undefined. |
| [100021](../errorcode-node.md#100021-framenode-not-modifiable) | The FrameNode is not modifiable. |

