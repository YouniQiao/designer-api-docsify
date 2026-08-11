# getScrollAttribute

## getScrollAttribute

```TypeScript
export function getScrollAttribute(node: FrameNode): ScrollAttribute | undefined
```

Get the attribute instance of FrameNode to set attributes.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getScrollAttribute(node: FrameNode): ScrollAttribute | undefined--><!--Device-typeNode-export function getScrollAttribute(node: FrameNode): ScrollAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | the target FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| [ScrollAttribute](../arkts-components/arkts-arkui-scroll-attribute.md) | Return the attribute instance of FrameNode, and return undefined if it does not exist. |

