# getTextAttribute

## getTextAttribute

```TypeScript
export function getTextAttribute(node: FrameNode): TextAttribute | undefined
```

获取FrameNode的属性实例来设置属性。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getTextAttribute(node: FrameNode): TextAttribute | undefined--><!--Device-typeNode-export function getTextAttribute(node: FrameNode): TextAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 目标FrameNode。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TextAttribute](../arkts-components/arkts-arkui-text-attribute.md) | Return the attribute instance of FrameNode, and return undefined if it does not exist. |

