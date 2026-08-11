# ListItemGroupOptions

Defines the list item group options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ListItemGroupOptions--><!--Device-unnamed-export declare interface ListItemGroupOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## footer

```TypeScript
footer?: CustomBuilder
```

Describes the ListItemGroup footer.

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

Describes the ListItemGroup footerComponent.

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

Describes the ListItemGroup footer style.

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

Describes the ListItemGroup header.

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

Describes the ListItemGroup headerComponent.

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

Describes the ListItemGroup header style.

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

Describes the ListItemGroup space.

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

Spacing between list items along the main axis.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;.&lt;br&gt;If this parameter is set to a negative number or a value greater than or equal to the length of the list content area, the default value is used.&lt;br&gt;If this parameter is set to a value less than the width of the list divider, the width of the list divider is used as the spacing.&lt;br&gt; Child components of &lt;em&gt;ListItemGroup&lt;/em&gt; whose &lt;em&gt;visibility&lt;/em&gt; attribute is set to &lt;em&gt;None&lt;/em&gt;are not displayed, but the spacing above and below them still takes effect.&lt;br&gt; If both spaceWidth and space are set, spaceWidth will take precedence.&lt;/p&gt;

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

Describes the ListItemGroup style.

**Type:** [ListItemGroupStyle](arkts-arkui-listitemgroup-listitemgroupstyle-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListItemGroupOptions-style?: ListItemGroupStyle--><!--Device-ListItemGroupOptions-style?: ListItemGroupStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

