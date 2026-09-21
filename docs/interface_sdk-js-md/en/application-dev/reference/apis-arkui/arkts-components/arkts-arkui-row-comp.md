# Row

Defines a container that lays out child components horizontally. It supports setting the spacing between child components and the alignment mode, and is suitable for scenarios where multiple child components need to be arranged horizontally, such as toolbars, tab bars, and button groups.

> **NOTE** > > If no width or height is set for the **Row** component, it adapts to the size of child components in the main axis > or cross axis direction.

## Child Components

Supported

## Row

```TypeScript
Row(options?: RowOptions)
```

Creates a horizontal linear layout container. You can set the spacing between child components.

> **NOTE:** 
> 
> When using multi-component nesting in complex UIs, if layout components are nested too deeply or too many
> components are nested, additional overhead will be incurred. It is recommended to optimize performance by
> removing redundant nodes, using layout boundaries to reduce layout calculations, and properly adopting rendering
> control syntax and layout component methods.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RowOptions](arkts-arkui-row-comp-rowoptions-i.md) | No | Configuration object of the horizontal layout, used to set the spacing between child components (unit: vp). The **space** attribute supports values of the number or string type. Pass this parameter when you need to customize the spacing between child components. If this parameter is not passed, the default spacing is 0.<br> <br>**Note:** Since API version 9, the **space** attribute does not take effect when it is set to a negative value or when **justifyContent** is set to **FlexAlign.SpaceBetween**, **FlexAlign.SpaceAround**, or **FlexAlign.SpaceEvenly**. |

## Row

```TypeScript
Row(options?: RowOptions | RowOptionsV2)
```

Creates a horizontal linear layout container. You can set the spacing between child components.

> **NOTE:** 
> 
> When using multi-component nesting in complex UIs, if layout components are nested too deeply or too many
> components are nested, additional overhead will be incurred. It is recommended to optimize performance by
> removing redundant nodes, using layout boundaries to reduce layout calculations, and properly adopting rendering
> control syntax and layout component methods.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RowOptions](arkts-arkui-row-comp-rowoptions-i.md) &#124; [RowOptionsV2](arkts-arkui-row-comp-rowoptionsv2-i.md) | No | Configuration object of the horizontal layout, used to set the spacing between child components (in vp). The space property supports values of the number, string, or Resource type. If not set, the default spacing is 0.<br>**Note:** Since API version 9, this property does not take effect when space is a negative number or **justifyContent** is set to **FlexAlign.SpaceBetween**, **FlexAlign.SpaceAround**, or **FlexAlign.SpaceEvenly**. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [RowOptions](arkts-arkui-row-comp-rowoptions-i.md) | Sets the spacing between child components of the **Row** component. |
| [RowOptionsV2](arkts-arkui-row-comp-rowoptionsv2-i.md) | Sets the spacing between child components of the **Row** component. The spacing type **SpaceType** can be of the number, string, or Resource type. |

## Examples

```TypeScript
### Example 1: Setting the Layout Attributes of the Row Component

This example demonstrates the effect of setting the layout attributes (such as the spacing and alignment mode) of the Row component.
```

```TypeScript

```

```TypeScript
### Example 2: Configuring the Reverse Attribute

This example shows the effect after setting the reverse attribute of the Row component, demonstrating how to reverse the arrangement order of child components.
```
