# Flex

The **Flex** component is a container that uses the flexible box model for layout. It provides an efficient mechanism for arranging and aligning child elements, as well as distributing available space among them.

For details, see [Flex Layout](../../../ui/arkts-layout-development-flex-layout.md).

> **NOTE** > > - The **Flex** component involves a secondary layout process during rendering. Therefore, in scenarios with strict > performance requirements, you are advised to use [Column](arkts-arkui-column-comp.md#column) or [Row](arkts-arkui-row-comp.md#row) instead. For best > practices, see the layout optimization guide - Proper Use of Layout Components. > > - When the main axis length of the **Flex** component is not set, it fills the parent container by default. If a > child component with position set is included, the **Flex** component will not fill > the parent container. When the main axis length of the [Column](arkts-arkui-column-comp.md#column) or [Row](arkts-arkui-row-comp.md#row) component is > not set, it follows the child node size by default. > > - When the **Flex**, **Column**, or **Row** component has no child nodes and no width or height is set, the default > width and height are **-1**. > > - The main axis length can be set to **auto** to make the **Flex** component adapt to the child component layout. > During adaptation, the **Flex** length is constrained by the constraintSize > attribute and the maximum and minimum lengths passed by the parent container, with the **constraintSize** attribute > taking higher priority.

## Child Components

This component can contain child components.

## Flex

```TypeScript
Flex(value?: FlexOptions)
```

Creates a **Flex** layout container for arranging and aligning child components in a flexible manner and distributing remaining space.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [FlexOptions](arkts-arkui-flex-comp-flexoptions-i.md) | No | Configuration options of the **Flex** container, used to set the layout direction, wrapping mode, alignment, and spacing of child components. If not passed, the default configuration is used. For details about the default values of each attribute, see [FlexOptions](arkts-arkui-flex-comp-flexoptions-i.md). |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [FlexOptions](arkts-arkui-flex-comp-flexoptions-i.md) | Describes the layout and alignment of child components within the **Flex** component. |
| [FlexSpaceOptions](arkts-arkui-flex-comp-flexspaceoptions-i.md) | Sets the spacing between child components along the main axis or cross axis of the **Flex** component. |

## Examples

```TypeScript
### Example 1: Setting the Child Component Layout Direction

This example demonstrates different layout directions for child components by setting the direction property.


```

```TypeScript
### Example 2: Implementing Single- and Multi-Line Layouts

This example demonstrates single-line and multi-line layouts for child components by setting the wrap property.


```

```TypeScript
### Example 3: Setting Alignment Along the Main Axis

This example demonstrates different alignment effects for child components along the main axis by setting the justifyContent property.


```

```TypeScript
### Example 4: Setting Alignment Along the Cross Axis

This example demonstrates different alignment effects for child components along the cross axis by setting the alignItems property.


```

```TypeScript
### Example 5: Setting Alignment of Multiple Lines

This example demonstrates different alignment effects for multiple lines of content by setting the alignContent property.


```

```TypeScript
### Example 6: Setting the Spacing Between Child Components Along the Main Axis or Cross Axis

This example sets the spacing along the main axis and cross axis for child components in single-line or multi-line arrangement by configuring the space attribute.


```

```TypeScript
### Example 7: Implementing a Flex Component with Adaptive Width

This example shows how the Flex component can automatically adjust to fit the layout of child components when the width is set to auto.
```
