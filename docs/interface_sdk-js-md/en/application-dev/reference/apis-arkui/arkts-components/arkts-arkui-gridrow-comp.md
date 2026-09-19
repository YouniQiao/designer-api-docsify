# GridRow

The responsive grid layout provides rules for layout design and resolves issues of dynamic layout across devices with different sizes, thereby ensuring layout consistency across layouts on different devices.

The **GridRow** component is used in a grid layout, together with its child component GridCol.

It supports dynamically adjusting the number of columns and gutter sizes based on device sizes and breakpoints to implement responsive layout.

## Child Components

This component can contain the **GridCol** child component.

## GridRow

```TypeScript
GridRow(option?: GridRowOptions)
```

Defines a grid row layout container. It can only be used with grid child components in grid layout scenarios.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [GridRowOptions](arkts-arkui-gridrowoptions-i.md) | No | Layout options of the grid row layout container. This parameter is passed when you need to customize the grid layout (such as setting the number of columns, gutter, breakpoint positions, and arrangement direction). If not passed, the default configuration is used. **GridRow** must be used together with GridCol child components. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [BreakPoints](arkts-arkui-breakpoints-i.md) | Sets breakpoints for the responsive grid container. For details about breakpoints, see [Breakpoints](../../../ui/arkts-layout-development-grid-layout.md#breakpoints). |
| [GridRowColumnOption](arkts-arkui-gridrowcolumnoption-i.md) | Describes the grid column number configuration for different device width types. |
| [GridRowOptions](arkts-arkui-gridrowoptions-i.md) | Defines layout options of the **GridRow** container. |
| [GridRowSizeOption](arkts-arkui-gridrowsizeoption-i.md) | Describes the gutter sizes for different device width types. |
| [GutterOption](arkts-arkui-gutteroption-i.md) | Provides the gutter options for the grid layout to define the spacing between child components in different directions. |

### Enums

| Name | Description |
| --- | --- |
| [BreakpointsReference](arkts-arkui-breakpointsreference-e.md) | Breakpoint reference of the grid container component. |
| [GridRowDirection](arkts-arkui-gridrowdirection-e.md) | Grid element arrangement direction. |

## Examples

```TypeScript
### Example 1: Basic Usage of Grid Layout

This example demonstrates the basic usage of the GridRow component.


```

```TypeScript
### Example 2: Basic Usage of AlignItems

This example demonstrates the effect of the GridCol component in different alignItems alignment modes.
```
