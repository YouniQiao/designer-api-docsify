# bindGridController

## bindGridController

```TypeScript
export function bindGridController(node: FrameNode, controller: Scroller): void
```

Bind the controller of FrameNode.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function bindGridController(node: FrameNode, controller: Scroller): void--><!--Device-typeNode-export function bindGridController(node: FrameNode, controller: Scroller): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Yes | the target FrameNode. |
| controller | Scroller | Yes | the controller which is bind to the target FrameNode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100023](../../apis-arkui/errorcode-node.md#100023-parameter-error) | Parameter error. Possible causes: 1. The component type of the node is incorrect. 2. The node is null or undefined. 3. The controller is null or undefined. |

