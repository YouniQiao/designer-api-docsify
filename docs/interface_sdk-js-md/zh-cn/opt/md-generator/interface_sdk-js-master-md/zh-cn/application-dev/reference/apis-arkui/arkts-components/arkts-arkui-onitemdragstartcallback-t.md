# OnItemDragStartCallback

```TypeScript
declare type OnItemDragStartCallback = (event: ItemDragInfo, itemIndex: number) => CustomBuilder
```

开始拖拽列表或网格元素时触发的回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type OnItemDragStartCallback = (event: ItemDragInfo, itemIndex: number) => CustomBuilder--><!--Device-unnamed-declare type OnItemDragStartCallback = (event: ItemDragInfo, itemIndex: number) => CustomBuilder-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [ItemDragInfo](arkts-arkui-itemdraginfo-i.md) | 是 |
| itemIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| [CustomBuilder](arkts-arkui-custombuilder-t.md) |
