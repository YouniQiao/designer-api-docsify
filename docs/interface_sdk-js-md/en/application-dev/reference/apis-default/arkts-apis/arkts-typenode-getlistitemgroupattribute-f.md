# getListItemGroupAttribute

## getListItemGroupAttribute

```TypeScript
export function getListItemGroupAttribute(node: FrameNode): ListItemGroupAttribute | undefined
```

Get the attribute instance of FrameNode to set attributes.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getListItemGroupAttribute(node: FrameNode): ListItemGroupAttribute | undefined--><!--Device-typeNode-export function getListItemGroupAttribute(node: FrameNode): ListItemGroupAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-framenode-c.md) | Yes | the target FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| ListItemGroupAttribute \| undefined | Return the attribute instance of FrameNode, and return undefined if it does not exist. |

