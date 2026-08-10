# bindTextAreaController

## bindTextAreaController

```TypeScript
export function bindTextAreaController(node: FrameNode, controller: TextAreaController): void
```

绑定TextArea节点的控制器。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function bindTextAreaController(node: FrameNode, controller: TextAreaController): void--><!--Device-typeNode-export function bindTextAreaController(node: FrameNode, controller: TextAreaController): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 目标节点。 |
| controller | [TextAreaController](../arkts-components/arkts-arkui-textareacontroller-c.md) | Yes | the controller which is bind to 目标节点。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100021 | The FrameNode is not modifiable. |
| 100023 | Parameter error. Possible causes: 1. The component type of the node is incorrect. 2. The node is null or undefined. 3. The controller is null or undefined. |

