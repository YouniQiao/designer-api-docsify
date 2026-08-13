# getScrollEvent

## getScrollEvent

```TypeScript
export function getScrollEvent(node: FrameNode): UIScrollEvent | undefined
```

Get the event instance of Scroll node.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getScrollEvent(node: FrameNode): UIScrollEvent | undefined--><!--Device-typeNode-export function getScrollEvent(node: FrameNode): UIScrollEvent | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Yes | the target FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| UIScrollEvent | Return the event instance of FrameNode, and return undefined if it does not exist. |

