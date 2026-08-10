# getLoadingProgressAttribute

## getLoadingProgressAttribute

```TypeScript
export function getLoadingProgressAttribute(node: FrameNode): LoadingProgressAttribute | undefined
```

获取FrameNode的属性实例来设置属性。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getLoadingProgressAttribute(node: FrameNode): LoadingProgressAttribute | undefined--><!--Device-typeNode-export function getLoadingProgressAttribute(node: FrameNode): LoadingProgressAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 目标FrameNode。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LoadingProgressAttribute](../arkts-components/arkts-arkui-loadingprogress-attribute.md) | Return the attribute instance of FrameNode, and return undefined if it does not exist. |

