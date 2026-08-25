# DynamicNode

Define DynamicNode.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onMove

```TypeScript
onMove(handler: OnMoveHandler | undefined): this
```

Set the move action.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [OnMoveHandler](arkts-arkui-onmovehandler-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onMove

```TypeScript
onMove(handler: OnMoveHandler | undefined, eventHandler: ItemDragEventHandler): this
```

Set the move action.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [OnMoveHandler](arkts-arkui-onmovehandler-t.md) \| undefined | 是 |
| eventHandler | [ItemDragEventHandler](arkts-arkui-common-itemdrageventhandler-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |
