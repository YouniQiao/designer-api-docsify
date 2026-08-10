# getCheckboxAttribute

## getCheckboxAttribute

```TypeScript
export function getCheckboxAttribute(node: FrameNode): CheckboxAttribute | undefined
```

获取FrameNode的属性实例以设置属性。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getCheckboxAttribute(node: FrameNode): CheckboxAttribute | undefined--><!--Device-typeNode-export function getCheckboxAttribute(node: FrameNode): CheckboxAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 目标FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| [CheckboxAttribute](../arkts-components/arkts-arkui-checkbox-attribute.md) | Return the attribute instance of FrameNode, and return undefined if it does not exist. |

