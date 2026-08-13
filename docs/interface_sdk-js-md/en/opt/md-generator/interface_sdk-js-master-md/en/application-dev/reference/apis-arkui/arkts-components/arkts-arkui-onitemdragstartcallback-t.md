# OnItemDragStartCallback

```TypeScript
declare type OnItemDragStartCallback = (event: ItemDragInfo, itemIndex: number) => CustomBuilder
```

Defines the callback type used in onItemDragStart.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-declare type OnItemDragStartCallback = (event: ItemDragInfo, itemIndex: number) => CustomBuilder--><!--Device-unnamed-declare type OnItemDragStartCallback = (event: ItemDragInfo, itemIndex: number) => CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [ItemDragInfo](arkts-arkui-itemdraginfo-i.md) | Yes |
| itemIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CustomBuilder](arkts-arkui-custombuilder-t.md) |
