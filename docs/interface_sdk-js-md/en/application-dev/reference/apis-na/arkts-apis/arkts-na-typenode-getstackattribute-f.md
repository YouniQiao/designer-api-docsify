# getStackAttribute

## getStackAttribute

```TypeScript
export function getStackAttribute(node: FrameNode): StackAttribute | undefined
```

Get the attribute instance of FrameNode to set attributes.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getStackAttribute(node: FrameNode): StackAttribute | undefined--><!--Device-typeNode-export function getStackAttribute(node: FrameNode): StackAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-na-framenode-c.md) | Yes | the target FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| StackAttribute | Return the attribute instance of FrameNode, and return undefined if it does not exist. |

