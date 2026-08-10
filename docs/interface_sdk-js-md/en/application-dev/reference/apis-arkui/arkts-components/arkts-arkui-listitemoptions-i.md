# ListItemOptions

ListItem组件参数。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface ListItemOptions--><!--Device-unnamed-declare interface ListItemOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: ListItemStyle
```

设置List组件卡片样式。默认值：ListItemStyle.NONE设置为ListItemStyle.NONE时无样式。设置为ListItemStyle.CARD时，建议配合ListItemGroup的ListItemGroupStyle.CARD同时使用，显示默认卡片样式。卡片样式下，ListItem默认规格：高度48vp，宽度100%，左右内边距8vp。如果需要实现ListItem高度自适应，可以把height设置为undefined。卡片样式下，为卡片内的列表选项提供了默认的focus、hover、press、selected和disable样式。当设置为ListItemStyle.CARD时，List的listDirection属性值须为Axis.Vertical，如果设置为Axis.Horizontal，会导致显示混乱；List属性alignListItem默认为ListItemAlign.Center，居中对齐显示。

**Type:** [ListItemStyle](arkts-arkui-listitemstyle-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ListItemOptions-style?: ListItemStyle--><!--Device-ListItemOptions-style?: ListItemStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

