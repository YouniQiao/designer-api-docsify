# ListItemGroupOptions

ListItemGroup组件参数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-declare interface ListItemGroupOptions--><!--Device-unnamed-declare interface ListItemGroupOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## footer

```TypeScript
footer?: CustomBuilder
```

设置ListItemGroup尾部组件。

**说明：**

可以放单个子组件或不放子组件，不设置时无尾部组件。该参数的优先级低于参数footerComponent。即同时设置footer和footerComponent时，以footerComponent设置的值为准。

**Type:** [CustomBuilder](arkts-arkui-custombuilder-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ListItemGroupOptions-footer?: CustomBuilder--><!--Device-ListItemGroupOptions-footer?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## footerComponent

```TypeScript
footerComponent?: ComponentContent
```

使用ComponentContent类型参数设置ListItemGroup尾部组件。

**说明：**

可以放单个子组件或不放子组件，不设置时无尾部组件。该参数的优先级高于参数footer。即同时设置footer和footerComponent时，以footerComponent设置的值为准。

同一个footerComponent不推荐同时给不同的ListItemGroup使用，否则会导致显示问题。

**Type:** [ComponentContent](../arkts-apis/arkts-arkui-componentcontent-c.md)

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-ListItemGroupOptions-footerComponent?: ComponentContent--><!--Device-ListItemGroupOptions-footerComponent?: ComponentContent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## footerStyle

```TypeScript
footerStyle?: ListItemGroupHeaderFooterStyle
```

设置ListItemGroup尾部样式。

默认值：ListItemGroupHeaderFooterStyle.NONE

设置为ListItemGroupHeaderFooterStyle.NONE时无样式。

设置为ListItemGroupHeaderFooterStyle.FLOATING时，尾部组件在滚动时悬浮显示。

**Type:** [ListItemGroupHeaderFooterStyle](../arkts-apis/arkts-arkui-listitemgroup-listitemgroupheaderfooterstyle-e.md)

**Default:** ListItemGroupHeaderFooterStyle.NONE

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ListItemGroupOptions-footerStyle?: ListItemGroupHeaderFooterStyle--><!--Device-ListItemGroupOptions-footerStyle?: ListItemGroupHeaderFooterStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## header

```TypeScript
header?: CustomBuilder
```

设置ListItemGroup头部组件。

**说明：**

可以放单个子组件或不放子组件，不设置时无头部组件。该参数的优先级低于参数headerComponent。即同时设置header和headerComponent时，以headerComponent设置的值为准。

**Type:** [CustomBuilder](arkts-arkui-custombuilder-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ListItemGroupOptions-header?: CustomBuilder--><!--Device-ListItemGroupOptions-header?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## headerComponent

```TypeScript
headerComponent?: ComponentContent
```

使用ComponentContent类型参数设置ListItemGroup头部组件。

**说明：**

可以放单个子组件或不放子组件，不设置时无头部组件。该参数的优先级高于参数header。即同时设置header和headerComponent时，以headerComponent设置的值为准。

同一个headerComponent不推荐同时给不同的ListItemGroup使用，否则会导致显示问题。

**Type:** [ComponentContent](../arkts-apis/arkts-arkui-componentcontent-c.md)

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-ListItemGroupOptions-headerComponent?: ComponentContent--><!--Device-ListItemGroupOptions-headerComponent?: ComponentContent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## headerStyle

```TypeScript
headerStyle?: ListItemGroupHeaderFooterStyle
```

设置ListItemGroup头部样式。

默认值：ListItemGroupHeaderFooterStyle.NONE

设置为ListItemGroupHeaderFooterStyle.NONE时无样式。

设置为ListItemGroupHeaderFooterStyle.FLOATING时，头部组件在滚动时悬浮显示。

**Type:** [ListItemGroupHeaderFooterStyle](../arkts-apis/arkts-arkui-listitemgroup-listitemgroupheaderfooterstyle-e.md)

**Default:** ListItemGroupHeaderFooterStyle.NONE

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ListItemGroupOptions-headerStyle?: ListItemGroupHeaderFooterStyle--><!--Device-ListItemGroupOptions-headerStyle?: ListItemGroupHeaderFooterStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: number | string
```

列表项间距。只作用于ListItem与ListItem之间，不作用于header与ListItem、footer与ListItem之间。

默认值：0

单位：vp

**说明：**

设置为负数或者大于等于List内容区长度时，按默认值显示。如果同时设置了spaceWidth和space，则spaceWidth优先生效。当spaceWidth为undefined或null时，space生效。

**Type:** number \| string

**Default:** 0

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ListItemGroupOptions-space?: number | string--><!--Device-ListItemGroupOptions-space?: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## spaceWidth

```TypeScript
spaceWidth?: Dimension
```

列表项间距。只作用于ListItem与ListItem之间，不作用于header与ListItem、footer与ListItem之间。

默认值：0

单位：vp

**说明：**

设置为负数或者大于等于List内容区长度时，按默认值显示。如果同时设置了spaceWidth和space，则spaceWidth优先生效。当spaceWidth为undefined或null时，space生效。

**Type:** [Dimension](../arkts-apis/arkts-arkui-dimension-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ListItemGroupOptions-spaceWidth?: Dimension--><!--Device-ListItemGroupOptions-spaceWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: ListItemGroupStyle
```

设置ListItemGroup组件卡片样式。

默认值：ListItemGroupStyle.NONE

设置为ListItemGroupStyle.NONE时无样式。

设置为ListItemGroupStyle.CARD时，建议配合[ListItem](./list_item)的ListItemStyle.CARD同时使用，显示默认卡片样式。

卡片样式下，ListItemGroup默认规格：左右外边距12vp，上下左右内边距4vp。

卡片样式下，为卡片内的列表选项提供了默认的focused、hover、pressed、selected和disabled样式。

**说明：**

当设置为ListItemGroupStyle.CARD时，List的listDirection属性值须为Axis.Vertical，如果设置为Axis.Horizontal，会导致显示混乱；List属性  
[alignListItem](../arkts-apis/arkts-arkui-list-listattribute-i.md/arkts-arkui-list-listattribute-i.md#alignlistitem)默认为ListItemAlign.Center，居中对齐显示。

**Type:** [ListItemGroupStyle](../arkts-apis/arkts-arkui-listitemgroup-listitemgroupstyle-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ListItemGroupOptions-style?: ListItemGroupStyle--><!--Device-ListItemGroupOptions-style?: ListItemGroupStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

