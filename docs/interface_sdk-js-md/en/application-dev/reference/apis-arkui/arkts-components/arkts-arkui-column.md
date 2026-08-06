# Column

The **Column** component lays out child components vertically.
> **NOTE**
>
> If no height or width is set for the **Column** component, the component automatically adapts to the size of its
> child components in the main axis and cross axis respectively.
>
> **Child Components**
>
> Supported

## Column

```TypeScript
Column(options?: ColumnOptions)
```

Creates a vertical linear layout container. You can set the spacing between child components.
    **NOTE**  
    
    Excessive component nesting (either too deep a hierarchy or too many nested components) incurs significant  
    performance overhead. For performance purposes, you are advised to remove redundant nodes to simplify the  
    component tree, use layout boundaries to reduce redundant layout calculations, properly apply rendering control  
    syntax and layout component methods to minimize unnecessary re-renders and computations. For details about the  
    best practices, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_  
    .

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ColumnInterface-(options?: ColumnOptions): ColumnAttribute--><!--Device-ColumnInterface-(options?: ColumnOptions): ColumnAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Vertical spacing between two adjacent child components. The value can be of the number or string type. |

## Column

```TypeScript
Column(options?: ColumnOptions | ColumnOptionsV2)
```

Creates a vertical linear layout container. You can set the spacing between child components.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-ColumnInterface-(options?: ColumnOptions | ColumnOptionsV2): ColumnAttribute--><!--Device-ColumnInterface-(options?: ColumnOptions | ColumnOptionsV2): ColumnAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| ColumnOptionsV2 | No | Vertical spacing between two adjacent child components. The value can be of the number, string, or Resource type.  |

## Summary

