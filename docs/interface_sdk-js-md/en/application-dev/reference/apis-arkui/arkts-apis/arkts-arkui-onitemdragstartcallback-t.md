# OnItemDragStartCallback

```TypeScript
export type OnItemDragStartCallback = (event: ItemDragInfo, itemIndex: int) => (CustomBuilder | undefined)
```

Defines the callback type used in onItemDragStart.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnItemDragStartCallback = (event: ItemDragInfo, itemIndex: int) => (CustomBuilder | undefined)--><!--Device-unnamed-export type OnItemDragStartCallback = (event: ItemDragInfo, itemIndex: int) => (CustomBuilder | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [ItemDragInfo](arkts-arkui-common-itemdraginfo-i.md) | Yes | Information about the dragged item. |
| itemIndex | int | Yes | The index number of the dragged item. |

**Return value:**

| Type | Description |
| --- | --- |
| (CustomBuilder \| undefined) | - |

