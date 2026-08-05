# bindListController

## bindListController

```TypeScript
export function bindListController(node: FrameNode, controller: Scroller): void
```

Bind the controller of FrameNode.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function bindListController(node: FrameNode, controller: Scroller): void--><!--Device-typeNode-export function bindListController(node: FrameNode, controller: Scroller): void-End-->

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

