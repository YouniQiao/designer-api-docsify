# getTextInputAttribute

## getTextInputAttribute

```TypeScript
export function getTextInputAttribute(node: FrameNode): TextInputAttribute | undefined
```

Get the attribute instance of FrameNode to set attributes.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getTextInputAttribute(node: FrameNode): TextInputAttribute | undefined--><!--Device-typeNode-export function getTextInputAttribute(node: FrameNode): TextInputAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | the target FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| TextInputAttribute | Return the attribute instance of FrameNode, and return undefined if it does not exist. |

