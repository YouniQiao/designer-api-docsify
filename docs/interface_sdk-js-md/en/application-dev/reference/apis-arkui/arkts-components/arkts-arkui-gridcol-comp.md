# GridCol

A column component in the grid layout system. It must be used as a child component of the grid container component (GridRow). It is suitable for responsive layout, multi-device adaptation, and other scenarios that require dynamic column width adjustment. It supports responsive breakpoint configuration, cross-column layout, offset, and sorting. Using the **GridCol** component enables quick implementation of responsive layouts, simplifying multi-device adaptation development.

## Child Components

This component can contain only one child component.

## GridCol

```TypeScript
GridCol(option?: GridColOptions)
```

Defines a grid column layout component. After creation, it participates in the layout calculation of the grid system as a child component of **GridRow**, based on the configured **span**, **offset**, and **order** attributes.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [GridColOptions](arkts-arkui-gridcoloptions-i.md) | No | Configuration options for the grid layout child component, which can be used to configure **span** (number of occupied columns), **offset** (number of offset columns), and **order** (sorting sequence). Pass this parameter when custom grid layout behavior is required (such as responsive column width, fixed offset position, and specified rendering order). This parameter can be omitted when the default grid layout is used. The default configuration is used when this parameter is not passed. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [GridColColumnOption](arkts-arkui-gridcolcolumnoption-i.md) | Describes the numbers of grid columns occupied by the **GridCol** component on devices with different width types. |
| [GridColOptions](arkts-arkui-gridcoloptions-i.md) | Defines the options of the **GridCol** component. |

## Examples

```TypeScript
This example demonstrates the basic usage of GridCol.
```
