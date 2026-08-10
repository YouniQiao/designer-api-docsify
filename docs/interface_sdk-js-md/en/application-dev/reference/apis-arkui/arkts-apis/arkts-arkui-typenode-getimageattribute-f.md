# getImageAttribute

## getImageAttribute

```TypeScript
export function getImageAttribute(node: FrameNode): ImageAttribute | undefined
```

Get the attribute instance of FrameNode to set attributes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getImageAttribute(node: FrameNode): ImageAttribute | undefined--><!--Device-typeNode-export function getImageAttribute(node: FrameNode): ImageAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | the target FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAttribute](../arkts-components/arkts-arkui-image-attribute.md) | Return the attribute instance of FrameNode, and return undefined if it does not exist. |

