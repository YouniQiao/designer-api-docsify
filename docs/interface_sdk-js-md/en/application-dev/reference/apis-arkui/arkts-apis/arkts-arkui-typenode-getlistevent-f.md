# getListEvent

## getListEvent

```TypeScript
export function getListEvent(node: FrameNode): UIListEvent | undefined
```

获取List节点的事件实例。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getListEvent(node: FrameNode): UIListEvent | undefined--><!--Device-typeNode-export function getListEvent(node: FrameNode): UIListEvent | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 目标FrameNode |

**Return value:**

| Type | Description |
| --- | --- |
| [UIListEvent](../arkts-components/arkts-arkui-uilistevent-i.md) | Return the event instance of FrameNode, and return undefined if it does not exist. |

