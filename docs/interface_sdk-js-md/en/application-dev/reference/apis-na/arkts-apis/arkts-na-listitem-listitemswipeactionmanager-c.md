# ListItemSwipeActionManager

The swipe action manager.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare class ListItemSwipeActionManager--><!--Device-unnamed-export declare class ListItemSwipeActionManager-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## collapse

```TypeScript
static collapse(node: FrameNode): void
```

Collapse the swipe action

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListItemSwipeActionManager-static collapse(node: FrameNode): void--><!--Device-ListItemSwipeActionManager-static collapse(node: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-na-framenode-c.md) | Yes | The ListItem FrameNode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100023](../../apis-arkui/errorcode-node.md#100023-parameter-error) | The component type of the node is incorrect. |
| [106203](../../apis-arkui/errorcode-node.md#106203-passed-node-not-mounted-to-component-tree) | The node not mounted to component tree. |

## expand

```TypeScript
static expand(node: FrameNode, direction: ListItemSwipeActionDirection): void
```

Expand the swipe action

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListItemSwipeActionManager-static expand(node: FrameNode, direction: ListItemSwipeActionDirection): void--><!--Device-ListItemSwipeActionManager-static expand(node: FrameNode, direction: ListItemSwipeActionDirection): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-na-framenode-c.md) | Yes | The ListItem FrameNode. |
| direction | [ListItemSwipeActionDirection](arkts-na-listitem-listitemswipeactiondirection-e.md) | Yes | The direction to expand. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100023](../../apis-arkui/errorcode-node.md#100023-parameter-error) | The component type of the node is incorrect. |
| [106203](../../apis-arkui/errorcode-node.md#106203-passed-node-not-mounted-to-component-tree) | The node not mounted to component tree. |

