# getTextAreaAttribute

## getTextAreaAttribute

```TypeScript
export function getTextAreaAttribute(node: FrameNode): TextAreaAttribute | undefined
```

Get the attribute instance of FrameNode to set attributes.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getTextAreaAttribute(node: FrameNode): TextAreaAttribute | undefined--><!--Device-typeNode-export function getTextAreaAttribute(node: FrameNode): TextAreaAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-na-framenode-c.md) | Yes | the target FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| TextAreaAttribute \| undefined | Return the attribute instance of FrameNode, and return undefined if it does not exist. |

