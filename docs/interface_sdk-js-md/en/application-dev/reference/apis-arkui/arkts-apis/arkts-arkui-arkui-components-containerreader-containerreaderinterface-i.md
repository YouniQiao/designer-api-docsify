# ContainerReaderInterface

```TypeScript
export interface ContainerReaderInterface
```

**ContainerReader** is a container breakpoint component used to obtain breakpoint information based on container size in dynamic scenarios and perform responsive layout. This component returns the container's size and breakpoint in real time through [two-way binding](../../../ui/state-management/arkts-new-binding.md#two-way-binding-between-built-in-component-parameters), enabling you to create and lay out components based on container size.

> **NOTE:** 
> 
> - To use **ContainerReader**, the parent component of **ContainerReader** should not rely on its child components to determine its own size.
> 
> - Container breakpoints determine height and width breakpoint values based on the component's own actual size and breakpoint threshold array. The component size and breakpoint information only apply to the current component and its child components. Multiple containers on the same page can have their own independent breakpoint states.
> 
> - The size of the **ContainerReader** component is determined by its parent container and its own layout, and is not affected by its child components. Layout specifications under different parent containers: when the parent container is Flex, Column, or Row, the remaining space of **ContainerReader** is filled; when the parent container is of other types, the parent container is filled.
> 
> - The parameters of the **ContainerReader** API must use state variables combined with the two-way binding ([!! syntax](../../../ui/state-management/arkts-new-binding.md)) so that the frontend is promptly notified to refresh the UI when the backend calculates size changes.
> 
> - For more development guidance and complete examples on container breakpoints, see [Container Breakpoint (ContainerReader)](../../../ui/arkts-layout-development-container-reader.md).

**Since:** 26.0.0

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ContainerReader, ContainerReaderAttribute, BreakpointOptions } from '@kit.ArkUI';
```

## [[Call]]

```TypeScript
(value: ContainerReaderInfo): ContainerReaderAttribute
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
| value | [ContainerReaderInfo](arkts-arkui-arkui-components-containerreader-containerreaderinfo-i.md) | Yes | Container reader configuration options, including size data and breakpoint configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| [ContainerReaderAttribute](arkts-arkui-arkui-components-containerreader-containerreaderattribute-c.md) |  |
