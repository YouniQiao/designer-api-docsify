# getCheckboxAttribute

## getCheckboxAttribute

```TypeScript
export function getCheckboxAttribute(node: FrameNode): CheckboxAttribute | undefined
```

Get the attribute instance of FrameNode to set attributes.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getCheckboxAttribute(node: FrameNode): CheckboxAttribute | undefined--><!--Device-typeNode-export function getCheckboxAttribute(node: FrameNode): CheckboxAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-framenode-c.md) | Yes | the target FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| CheckboxAttribute \| undefined | Return the attribute instance of FrameNode, and return undefined if it does not exist. |

