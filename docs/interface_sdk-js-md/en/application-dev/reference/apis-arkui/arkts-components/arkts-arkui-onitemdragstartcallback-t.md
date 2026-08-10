# OnItemDragStartCallback

```TypeScript
declare type OnItemDragStartCallback = (event: ItemDragInfo, itemIndex: number) => CustomBuilder
```

开始拖拽列表或网格元素时触发的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-declare type OnItemDragStartCallback = (event: ItemDragInfo, itemIndex: number) => CustomBuilder--><!--Device-unnamed-declare type OnItemDragStartCallback = (event: ItemDragInfo, itemIndex: number) => CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [ItemDragInfo](../arkts-apis/arkts-arkui-common-itemdraginfo-i.md) | Yes | 拖拽点的信息。 |
| itemIndex | number | Yes | 被拖拽列表元素索引值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CustomBuilder](arkts-arkui-custombuilder-t.md) | 返回CustomBuilder用于构建被拖拽元素的拖拽图。返回void表示不能拖拽。 |

