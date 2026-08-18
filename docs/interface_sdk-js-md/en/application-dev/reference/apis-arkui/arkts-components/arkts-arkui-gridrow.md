# GridRow

The responsive grid layout provides rules for layout design and resolves issues of dynamic layout across devices with different sizes, thereby ensuring layout consistency across layouts on different devices. The **GridRow** component is used in a grid layout, together with its child component GridCol. > **Child Components** > > This component can contain the **GridCol** child component.

## GridRow

```TypeScript
GridRow(option?: GridRowOptions)
```

Creates a **GridRow** container.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-GridRowInterface-(option?: GridRowOptions): GridRowAttribute--><!--Device-GridRowInterface-(option?: GridRowOptions): GridRowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [GridRowOptions](arkts-arkui-gridrowoptions-i.md) | No |  |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [BreakPoints](arkts-arkui-breakpoints-i.md) | Sets breakpoints for the responsive grid container. For details about breakpoints, see [Breakpoints](../../../ui/arkts-layout-development-grid-layout.md#breakpoints). <!--code_no_check--> |
| [GridRowColumnOption](arkts-arkui-gridrowcolumnoption-i.md) | Describes the numbers of grid columns for devices with different grid sizes. In versions earlier than API version 20: When **GridRow** column spans are configured only at specific breakpoints, unconfigured breakpoints inherit values from the next smaller configured breakpoint. If no smaller breakpoint exists, the default column count (12) is used for unconfigured breakpoints. <!--code_no_check--> Since API version 20: When **GridRow** column spans are configured only at specific breakpoints, unconfigured breakpoints inherit values from the next smaller configured breakpoint. If no smaller breakpoint exists, values are inherited from the next larger configured breakpoint. <!--code_no_check--> Recommendation: Explicitly configure **GridRow** column spans for all required breakpoints to prevent unexpected layout behavior caused by automatic value inheritance. The width of each column is the content area size of the **GridRow** component minus the gutter of the grid child components, and then divided by the total number of columns. For example, if **columns** is set to **12**, **gutter** is set to **10px**, and **padding** is set to **20px** for a **GridRow** component with a width of 800 px, the width of each column is (800 – 20 × 2 – 10 × 11)/12. |
| [GridRowOptions](arkts-arkui-gridrowoptions-i.md) | Defines layout options of the **GridRow** container. |
| [GridRowSizeOption](arkts-arkui-gridrowsizeoption-i.md) | Describes the gutter sizes for different device width types. |
| [GutterOption](arkts-arkui-gutteroption-i.md) | Provides the gutter options for the grid layout to define the spacing between child components in different directions. |

### Enums

| Name | Description |
| --- | --- |
| [BreakpointsReference](arkts-arkui-breakpointsreference-e.md) | Breakpoint reference of the grid container component. |
| [GridRowDirection](arkts-arkui-gridrowdirection-e.md) | Grid element arrangement direction. > **NOTE：**> > - Grid elements can be arranged only in the **Row** or **RowReverse** direction, but not in the **Column** or > **ColumnReverse** direction. > > - The location and size of a grid child component can be calculated only based on **span** and **offset**. If the > **span** values of child components add up to a number greater than the allowed number of columns, the grid will > automatically wrap lines. > > - If the **span** value of a single child component exceeds the maximum number of columns, the maximum number of > columns is used. > > - If a child component takes up more than the total number of columns according to its **offset** and **span** > settings, it will be placed in a new row. > > - Example: Item1: GridCol({ span: 6 }), Item2: GridCol({ span: 8, offset:11 }) > > > >  |

