# OnItemDragStartCallback

```TypeScript
export type OnItemDragStartCallback = (event: ItemDragInfo, itemIndex: int) => (CustomBuilder | undefined)
```

Defines the callback type used in onItemDragStart.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [ItemDragInfo](arkts-arkui-common-itemdraginfo-i.md) | 是 |
| itemIndex | int | 是 |

**返回值：**

| 类型 |
| --- |
| (CustomBuilder \| undefined) |
