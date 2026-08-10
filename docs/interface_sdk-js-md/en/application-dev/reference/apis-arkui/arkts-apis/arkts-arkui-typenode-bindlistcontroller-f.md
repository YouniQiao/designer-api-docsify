# bindListController

## bindListController

```TypeScript
export function bindListController(node: FrameNode, controller: Scroller): void
```

绑定FrameNode的控制器。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function bindListController(node: FrameNode, controller: Scroller): void--><!--Device-typeNode-export function bindListController(node: FrameNode, controller: Scroller): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 目标FrameNode。 |
| controller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | Yes | the controller which is bind to 目标FrameNode。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100023 | Parameter error. Possible causes: 1. The component type of the node is incorrect. 2. The node is null or undefined. 3. The controller is null or undefined. |

