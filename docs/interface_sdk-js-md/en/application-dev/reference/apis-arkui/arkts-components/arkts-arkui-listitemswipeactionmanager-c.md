# ListItemSwipeActionManager

ListItem划出菜单的管理器。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-unnamed-declare class ListItemSwipeActionManager--><!--Device-unnamed-declare class ListItemSwipeActionManager-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## collapse

```TypeScript
static collapse(node: FrameNode): void
```

收起指定ListItem的划出菜单。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-ListItemSwipeActionManager-static collapse(node: FrameNode): void--><!--Device-ListItemSwipeActionManager-static collapse(node: FrameNode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](../arkts-apis/arkts-arkui-framenode-c.md) | Yes | ListItem节点对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100023 | The component type of the node is incorrect. |
| 106203 | The node not mounted to component tree. |

## expand

```TypeScript
static expand(node: FrameNode, direction: ListItemSwipeActionDirection): void
```

展开指定ListItem的划出菜单。

> **说明：**
> 
> - 如果List组件cachedCount属性show参数设置为true，List显示区域外已预加载完成的ListItem支持展开，否则List显示区域外节点不支持展开。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-ListItemSwipeActionManager-static expand(node: FrameNode, direction: ListItemSwipeActionDirection): void--><!--Device-ListItemSwipeActionManager-static expand(node: FrameNode, direction: ListItemSwipeActionDirection): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](../arkts-apis/arkts-arkui-framenode-c.md) | Yes | ListItem节点对象。 |
| direction | [ListItemSwipeActionDirection](../arkts-apis/arkts-arkui-listitem-listitemswipeactiondirection-e.md) | Yes | ListItem划出菜单的展开方向。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100023 | The component type of the node is incorrect. |
| 106203 | The node not mounted to component tree. |

