# @ohos.arkui.components.ContainerReader

## Modules to Import

```TypeScript
import { ContainerReader, ContainerReaderAttribute, BreakpointOptions } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ContainerReaderAttribute](arkts-arkui-arkui-components-containerreader-containerreaderattribute-c.md) | In addition to the [universal attributes](../arkts-components/arkts-arkui-commonmethod-c.md), the following attributes are supported: |

### Interfaces

| Name | Description |
| --- | --- |
| [BreakpointOptions](arkts-arkui-arkui-components-containerreader-breakpointoptions-i.md) | Defines the breakpoint configuration options, which are used to specify threshold parameters for container size analysis. |
| [ContainerReaderInfo](arkts-arkui-arkui-components-containerreader-containerreaderinfo-i.md) | Defines the configuration options for the **ContainerReader** component, used to specify parameters for reading container size and obtaining breakpoint values. The component size and breakpoint values cannot be changed through this parameter. |
| [ContainerReaderInterface](arkts-arkui-arkui-components-containerreader-containerreaderinterface-i.md) | **ContainerReader** is a container breakpoint component used to obtain breakpoint information based on container size in dynamic scenarios and perform responsive layout. This component returns the container's size and breakpoint in real time through [two-way binding](../../../ui/state-management/arkts-new-binding.md#two-way-binding-between-built-in-component-parameters), enabling you to create and lay out components based on container size. |

### Constants

| Name | Description |
| --- | --- |
| [ContainerReader](arkts-arkui-arkui-components-containerreader-con.md) | **ContainerReader** is a container breakpoint component used to obtain breakpoint information based on container size in dynamic scenarios and perform responsive layout. This component returns the container's size and breakpoint in real time through [two-way binding](../../../ui/state-management/arkts-new-binding.md#two-way-binding-between-built-in-component-parameters), enabling you to create and lay out components based on container size. |
| [ContainerReaderInstance](arkts-arkui-arkui-components-containerreader-con.md#containerreaderinstance) | Defines ContainerReader Component instance. Provides access to ContainerReader component methods for container dimension analysis and breakpoint detection. |

## Examples

```TypeScript
### Example 1: Switching Layout Direction Based on ContainerReader Width Breakpoint

This example demonstrates how the [ContainerReader](#containerreader-1) component obtains container size and breakpoint information through two-way binding, and switches the layout direction based on the width breakpoint.

The ContainerReader component is added since API version 26.0.0.
```

```TypeScript
### Example 2: Configuring Custom Breakpoints

This example demonstrates how to customize breakpoint thresholds via [breakpointConfig](arkts-arkui-arkui-components-containerreader-containerreaderattribute-c.md#breakpointconfig) to define various wide and narrow layout sizes, enabling more refined layout control.

The ContainerReader component and the breakpointConfig API are added since API version 26.0.0.

Tap the button to change the width of the parent container, which returns different width breakpoint values, thereby adjusting the layout direction.
```

```TypeScript
### Example 3: Dynamically Adjusting the Number of Columns Using the Width Breakpoint

This example demonstrates how to dynamically adjust the number of columns based on the width breakpoint obtained from ContainerReader, enabling adaptive layouts across multiple devices with varying column counts for different breakpoints.

The ContainerReader component is added since API version 26.0.0.
```
