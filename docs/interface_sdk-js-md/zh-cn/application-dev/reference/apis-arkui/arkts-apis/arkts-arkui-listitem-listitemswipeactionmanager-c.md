# ListItemSwipeActionManager

ListItem划出菜单的管理器。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## collapse

```TypeScript
static collapse(node: FrameNode): void
```

收起指定ListItem的划出菜单。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100023](../errorcode-node.md#100023-参数错误) |
| [106203](../errorcode-node.md#106203-传入的节点未挂载到组件树上) |

## expand

```TypeScript
static expand(node: FrameNode, direction: ListItemSwipeActionDirection): void
```

展开指定ListItem的划出菜单。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | 是 |
| direction | [ListItemSwipeActionDirection](arkts-arkui-listitem-listitemswipeactiondirection-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100023](../errorcode-node.md#100023-参数错误) |
| [106203](../errorcode-node.md#106203-传入的节点未挂载到组件树上) |
