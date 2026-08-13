# ColumnSplitDividerStyle

Sets the distance between the child component and the upper and lower dividers. > **NOTE：**> > Similar to RowSplit, the dividers of **ColumnSplit** adjust the height of adjacent child > components. However, this adjustment is only applied to the extent that the resulting height stays within the > height limits of the child components. > > Universal attributes such as clip and margin are supported. > If **clip** is not set, the default value **true** is used.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-interface ColumnSplitDividerStyle--><!--Device-unnamed-interface ColumnSplitDividerStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## endMargin

```TypeScript
endMargin?: Dimension
```

Distance between the child component and the lower divider.&lt;br&gt;Default value: **0vp**&lt;br&gt;Invalid values are treated as the default value. In this case, the attribute value obtained by the [getInspectorByKey()](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-component-id.md#getinspectorbykey9)

**Type:** [Dimension](../arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 0

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ColumnSplitDividerStyle-endMargin?: Dimension--><!--Device-ColumnSplitDividerStyle-endMargin?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startMargin

```TypeScript
startMargin?: Dimension
```

Distance between the child component and the upper divider.&lt;br&gt;Default value: **0vp**&lt;br&gt;Invalid values are treated as the default value. In this case, the attribute value obtained by the [getInspectorByKey()](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-component-id.md#getinspectorbykey9)

**Type:** [Dimension](../arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 0

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ColumnSplitDividerStyle-startMargin?: Dimension--><!--Device-ColumnSplitDividerStyle-startMargin?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
