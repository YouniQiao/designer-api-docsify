# getListEvent

## getListEvent

```TypeScript
export function getListEvent(node: FrameNode): UIListEvent | undefined
```

Get the event instance of List node.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getListEvent(node: FrameNode): UIListEvent | undefined--><!--Device-typeNode-export function getListEvent(node: FrameNode): UIListEvent | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Yes | the target FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| UIListEvent \| undefined | Return the event instance of FrameNode, and return undefined if it does not exist. |

