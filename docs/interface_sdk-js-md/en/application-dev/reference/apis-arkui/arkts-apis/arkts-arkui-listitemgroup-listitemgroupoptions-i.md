# ListItemGroupOptions

ListItemGroup组件参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ListItemGroupOptions--><!--Device-unnamed-export declare interface ListItemGroupOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## footer

```TypeScript
footer?: CustomBuilder
```

设置ListItemGroup尾部组件。

**Type:** [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListItemGroupOptions-footer?: CustomBuilder--><!--Device-ListItemGroupOptions-footer?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## footerComponent

```TypeScript
footerComponent?: ComponentContentBase
```

使用ComponentContent类型参数设置ListItemGroup尾部组件。

**Type:** [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListItemGroupOptions-footerComponent?: ComponentContentBase--><!--Device-ListItemGroupOptions-footerComponent?: ComponentContentBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## footerStyle

```TypeScript
footerStyle?: ListItemGroupHeaderFooterStyle
```

设置ListItemGroup尾部样式。

**Type:** [ListItemGroupHeaderFooterStyle](arkts-arkui-listitemgroup-listitemgroupheaderfooterstyle-e.md)

**Default:** ListItemGroupHeaderFooterStyle.NONE

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListItemGroupOptions-footerStyle?: ListItemGroupHeaderFooterStyle--><!--Device-ListItemGroupOptions-footerStyle?: ListItemGroupHeaderFooterStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## header

```TypeScript
header?: CustomBuilder
```

设置ListItemGroup头部组件。

**Type:** [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListItemGroupOptions-header?: CustomBuilder--><!--Device-ListItemGroupOptions-header?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## headerComponent

```TypeScript
headerComponent?: ComponentContentBase
```

使用ComponentContent类型参数设置ListItemGroup头部组件。

**Type:** [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListItemGroupOptions-headerComponent?: ComponentContentBase--><!--Device-ListItemGroupOptions-headerComponent?: ComponentContentBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## headerStyle

```TypeScript
headerStyle?: ListItemGroupHeaderFooterStyle
```

设置ListItemGroup头部样式。

**Type:** [ListItemGroupHeaderFooterStyle](arkts-arkui-listitemgroup-listitemgroupheaderfooterstyle-e.md)

**Default:** ListItemGroupHeaderFooterStyle.NONE

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListItemGroupOptions-headerStyle?: ListItemGroupHeaderFooterStyle--><!--Device-ListItemGroupOptions-headerStyle?: ListItemGroupHeaderFooterStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: double | string
```

列表项间距。只作用于ListItem与ListItem之间，不作用于header与ListItem、footer与ListItem之间。

**Type:** double \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListItemGroupOptions-space?: double | string--><!--Device-ListItemGroupOptions-space?: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## spaceWidth

```TypeScript
spaceWidth?: Dimension
```

列表项间距。只作用于ListItem与ListItem之间，不作用于header与ListItem、footer与ListItem之间。&lt;p&gt;&lt;strong&gt;说明：&lt;/strong&gt;&lt;br/&gt;设置为负数或者大于等于List内容区长度时，按默认值显示。&lt;br/&gt;如果同时设置了spaceWidth和space，则spaceWidth优先生效。当spaceWidth为undefined或null时，space生效。&lt;/p&gt;。

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListItemGroupOptions-spaceWidth?: Dimension--><!--Device-ListItemGroupOptions-spaceWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: ListItemGroupStyle
```

设置List组件卡片样式。

**Type:** [ListItemGroupStyle](arkts-arkui-listitemgroup-listitemgroupstyle-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListItemGroupOptions-style?: ListItemGroupStyle--><!--Device-ListItemGroupOptions-style?: ListItemGroupStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

