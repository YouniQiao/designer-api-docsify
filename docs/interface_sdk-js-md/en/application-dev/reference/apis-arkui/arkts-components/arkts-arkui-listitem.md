# ListItem

The ListItem component displays specific items in the list. It must be used together with List. > **NOTE** > > - This component is supported since API version 7. Updates will be marked with a superscript to indicate > their earliest API version. > > - The parent of this component can only be List or ListItemGroup. > > - When this component is used with LazyForEach, its child components are created when it is created. > When this component is used with if/else or ForEach, or when the parent component is List or ListItemGroup, > its child components are created when it is laid out.

## Child Components This component can contain a single child component.

## ListItem

```TypeScript
ListItem(value?: ListItemOptions)
```

Creates a ListItem component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-ListItemInterface-(value?: ListItemOptions): ListItemAttribute--><!--Device-ListItemInterface-(value?: ListItemOptions): ListItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ListItemOptions](arkts-arkui-listitemoptions-i.md) | No |  |

## ListItem

```TypeScript
ListItem(value?: string)
```

Creates a ListItem component.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** listItem/ListItemInterface

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListItemInterface-(value?: string): ListItemAttribute--><!--Device-ListItemInterface-(value?: string): ListItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string | No |  |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [ListItemOptions](arkts-arkui-listitemoptions-i.md) | Defines ListItem component configuration options. |
| [SwipeActionItem](arkts-arkui-swipeactionitem-i.md) | Describes the swipe action item. For a list in vertical layout, it refers to the delete option displayed on the left (or right) of the list item when the list item is swiped right (or left). For a list in horizontal layout, it refers to the delete option displayed below (or above) the list item when the list item is swiped up (or down). |
| [SwipeActionOptions](arkts-arkui-swipeactionoptions-i.md) | The top layer of the @builder function corresponding to start and end must be a single component. Otherwise, undefined behavior occurs. If the top layer of the @builder function is a statement such as if/else or ForEach, ensure that these statements can generate a single component. The swipe gesture works only in the list item area. If a swipe causes a child component to extend beyond the list item area, the portion outside the area does not respond to the swipe. |

### Enums

| Name | Description |
| --- | --- |
| [EditMode](arkts-arkui-editmode-e.md) | Enumerates the edit modes of list items. |
| [ListItemStyle](arkts-arkui-listitemstyle-e.md) | Enumerates the card styles of the List component. |
| [ListItemSwipeActionDirection](arkts-arkui-listitemswipeactiondirection-e.md) | Enumerates the swipe action menu display directions for ListItem components. |
| [Sticky](arkts-arkui-sticky-e.md) | Enumerates the sticky effects for list items. |
| [SwipeActionState](arkts-arkui-swipeactionstate-e.md) | Enumerates swipe states of list items. |
| [SwipeEdgeEffect](arkts-arkui-swipeedgeeffect-e.md) | Enumerates the edge effects. |

