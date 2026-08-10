# ListItem

ListItem用于展示列表中的具体列表项，支持设置划出菜单、选中状态、鼠标框选和卡片样式等能力，必须配合List组件使用，适用于需要在列表中展示内容并对单个列表项进行交互操作（如滑动删除、选中标记）的场景。

> **说明：**
>
> - 该组件的父组件只能是[List]{@link ./list}或者[ListItemGroup]{@link ./list_item_group}。
>
> - 当ListItem配合[LazyForEach](docroot://ui/rendering-control/arkts-rendering-control-lazyforeach.md)使用时，ListItem子组件在
> ListItem创建时创建。配合[if/else](docroot://ui/rendering-control/arkts-rendering-control-ifelse.md)、
> [ForEach](docroot://ui/rendering-control/arkts-rendering-control-foreach.md)使用时，或父组件为List/ListItemGroup时，ListItem子组
> 件在ListItem布局时创建。

## 子组件

可以包含单个子组件。

## ListItem

```TypeScript
ListItem(value?: ListItemOptions)
```

创建ListItem组件。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-ListItemInterface-(value?: ListItemOptions): ListItemAttribute--><!--Device-ListItemInterface-(value?: ListItemOptions): ListItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ListItemOptions](../arkts-apis/arkts-arkui-listitem-listitemoptions-i.md) | No |  |

## ListItem

```TypeScript
ListItem(value?: string)
```

创建ListItem组件。

> **说明：**
> 
> 从API version 7开始支持，从API version 10开始废弃。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** <!--SUBSTITUTE_API-->listItem/ListItemInterface<!--/SUBSTITUTE_API-->

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListItemInterface-(value?: string): ListItemAttribute--><!--Device-ListItemInterface-(value?: string): ListItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string | No |  |

## Summary

- [ListItemOptions](arkts-arkui-listitem-listitemoptions-i.md)
- [SwipeActionItem](arkts-arkui-listitem-swipeactionitem-i.md)
- [SwipeActionOptions](arkts-arkui-listitem-swipeactionoptions-i.md)
- [EditMode](arkts-arkui-listitem-editmode-e.md)
- [ListItemStyle](arkts-arkui-listitem-listitemstyle-e.md)
- [ListItemSwipeActionDirection](arkts-arkui-listitem-listitemswipeactiondirection-e.md)
- [Sticky](arkts-arkui-listitem-sticky-e.md)
- [SwipeActionState](arkts-arkui-listitem-swipeactionstate-e.md)
- [SwipeEdgeEffect](arkts-arkui-listitem-swipeedgeeffect-e.md)
