# getTextAreaAttribute

## getTextAreaAttribute

```TypeScript
export function getTextAreaAttribute(node: FrameNode): TextAreaAttribute | undefined
```

获取FrameNode的属性实例来设置属性。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getTextAreaAttribute(node: FrameNode): TextAreaAttribute | undefined--><!--Device-typeNode-export function getTextAreaAttribute(node: FrameNode): TextAreaAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 目标FrameNode。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TextAreaAttribute](../arkts-components/arkts-arkui-textarea-attribute.md) | Return the attribute instance of FrameNode, and return undefined if it does not exist. |

