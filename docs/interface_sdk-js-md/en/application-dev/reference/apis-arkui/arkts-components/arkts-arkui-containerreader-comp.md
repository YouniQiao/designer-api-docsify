# ContainerReader

**ContainerReader** is a container breakpoint component used to obtain breakpoint information based on container size in dynamic scenarios and perform responsive layout. This component returns the container's size and breakpoint in real time through [two-way binding](../../../ui/state-management/arkts-new-binding.md#two-way-binding-between-built-in-component-parameters), enabling you to create and lay out components based on container size.

> **NOTE** > > - To use **ContainerReader**, the parent component of **ContainerReader** should not rely on its child components > to determine its own size. > > - Container breakpoints determine height and width breakpoint values based on the component's own actual size and > breakpoint threshold array. The component size and breakpoint information only apply to the current component and > its child components. Multiple containers on the same page can have their own independent breakpoint states. > > - The size of the **ContainerReader** component is determined by its parent container and its own layout, and is > not affected by its child components. Layout specifications under different parent containers: when the parent > container is [Flex](arkts-arkui-flex-comp.md#flex), [Column](arkts-arkui-column-comp.md#column), or > [Row](arkts-arkui-row-comp.md#row), the remaining space of **ContainerReader** is filled; when the parent > container is of other types, the parent container is filled. > > - The parameters of the **ContainerReader** API must use state variables combined with the two-way binding ( > [!! syntax](../../../ui/state-management/arkts-new-binding.md)) so that the frontend is promptly notified to > refresh the UI when the backend calculates size changes. > > - For more development guidance and complete examples on container breakpoints, see > [Container Breakpoint (ContainerReader)](../../../ui/arkts-layout-development-container-reader.md).

## Child Components

Supported

## ContainerReader

```TypeScript
ContainerReader(value: ContainerReaderInfo)
```

Creates a **ContainerReader** component and configures container reader parameters.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ContainerReaderInfo](arkts-arkui-containerreader-comp-containerreaderinfo-i.md) | Yes | Container reader configuration options, including size data and breakpoint configuration. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [BreakpointOptions](arkts-arkui-containerreader-comp-breakpointoptions-i.md) | Defines the breakpoint configuration options, which are used to specify threshold parameters for container size analysis. |
| [ContainerReaderInfo](arkts-arkui-containerreader-comp-containerreaderinfo-i.md) | Defines the configuration options for the **ContainerReader** component, used to specify parameters for reading container size and obtaining breakpoint values. The component size and breakpoint values cannot be changed through this parameter. |

## Examples

```TypeScript
### Example 1: Switching Layout Direction Based on ContainerReader Width Breakpoint

This example demonstrates how the [ContainerReader](#containerreader-1) component obtains container size and breakpoint information through two-way binding, and switches the layout direction based on the width breakpoint.

The ContainerReader component is added since API version 26.0.0.
```

```TypeScript
### Example 2: Configuring Custom Breakpoints

This example demonstrates how to customize breakpoint thresholds via [breakpointConfig](arkts-arkui-containerreader-comp-attribute.md#breakpointconfig) to define various wide and narrow layout sizes, enabling more refined layout control.

The ContainerReader component and the breakpointConfig API are added since API version 26.0.0.

Tap the button to change the width of the parent container, which returns different width breakpoint values, thereby adjusting the layout direction.
```

```TypeScript
### Example 3: Dynamically Adjusting the Number of Columns Using the Width Breakpoint

This example demonstrates how to dynamically adjust the number of columns based on the width breakpoint obtained from ContainerReader, enabling adaptive layouts across multiple devices with varying column counts for different breakpoints.

The ContainerReader component is added since API version 26.0.0.
```
