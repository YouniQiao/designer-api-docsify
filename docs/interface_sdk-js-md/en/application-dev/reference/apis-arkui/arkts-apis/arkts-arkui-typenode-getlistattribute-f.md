# getListAttribute

## getListAttribute

```TypeScript
export function getListAttribute(node: FrameNode): ListAttribute | undefined
```

获取属性实例用于设置属性

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getListAttribute(node: FrameNode): ListAttribute | undefined--><!--Device-typeNode-export function getListAttribute(node: FrameNode): ListAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 目标FrameNode |

**Return value:**

| Type | Description |
| --- | --- |
| [ListAttribute](../arkts-components/arkts-arkui-list-attribute.md) | Return the attribute instance of FrameNode, and return undefined if it does not exist. |

