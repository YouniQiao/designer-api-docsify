# Row

The **Row** component lays out child components horizontally. > **NOTE** > > If no width or height is set for the **Row** component, the component automatically adapts to the size of its child > components in the main axis and cross axis respectively. > > **Child Components** > > Supported

## Row

```TypeScript
Row(options?: RowOptions)
```

Creates a horizontal linear layout container. You can set the spacing between child components. &gt; **NOTE：**&gt; &gt; Excessive component nesting (either too deep a hierarchy or too many nested components) incurs significant &gt; performance overhead. For performance purposes, you are advised to remove redundant nodes to simplify the &gt; component tree, use layout boundaries to reduce redundant layout calculations, properly apply rendering control &gt; syntax and layout component methods to minimize unnecessary re-renders and computations. For details about the &gt; best practices, see &gt; [Layout Optimization](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-improve-layout-performance) &gt; .

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-RowInterface-(options?: RowOptions): RowAttribute--><!--Device-RowInterface-(options?: RowOptions): RowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RowOptions](arkts-arkui-rowoptions-i.md) | No | Spacing between elements in the horizontal layout. The value can be of the number or string type. |

## Row

```TypeScript
Row(options?: RowOptions | RowOptionsV2)
```

Creates a horizontal linear layout container. You can set the spacing between child components.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-RowInterface-(options?: RowOptions | RowOptionsV2): RowAttribute--><!--Device-RowInterface-(options?: RowOptions | RowOptionsV2): RowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RowOptions](arkts-arkui-rowoptions-i.md) \| [RowOptionsV2](arkts-arkui-rowoptionsv2-i.md) | No | Spacing between elements in a horizontal layout. The value can be of the number, string, or Resource type. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [RowOptions](arkts-arkui-rowoptions-i.md) | Sets the spacing between child components of the **Row** component. &gt; **NOTE：**&gt; &gt; To standardize anonymous object definitions, the element definitions here have been revised in API version 18. &gt; While starting version information is preserved for historical anonymous objects, there may be cases where the &gt; outer element's @since version number is higher than inner element's. This does not affect interface usability. |
| [RowOptionsV2](arkts-arkui-rowoptionsv2-i.md) | Sets the spacing between child components of the **Row** component. &gt; **NOTE：**&gt; &gt; To standardize anonymous object definitions, the element definitions here have been revised in API version 18. &gt; While starting version information is preserved for historical anonymous objects, there may be cases where the &gt; outer element's @since version number is higher than inner element's. This does not affect interface usability. |

