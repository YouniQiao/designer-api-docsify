# GridCol

The **GridCol** component must be used as a child component of the GridRow container. > **Child Components** > > This component can contain only one child component.

## GridCol

```TypeScript
GridCol(option?: GridColOptions)
```

Creates a **GridCol** component.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-GridColInterface-(option?: GridColOptions): GridColAttribute--><!--Device-GridColInterface-(option?: GridColOptions): GridColAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [GridColOptions](arkts-arkui-gridcoloptions-i.md) | No |  |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [GridColColumnOption](arkts-arkui-gridcolcolumnoption-i.md) | Describes the numbers of grid columns occupied by the **GridCol** component on devices with different width types. - In versions earlier than API version 20: When you configure **GridCol** column spans only at specific breakpoints, unconfigured breakpoints inherit values from the next smaller configured breakpoint. If no smaller breakpoint is configured, the default value of **1** is used. <!--code_no_check--> ```ts span: {xs:2, md:4, lg:8} // Equivalent to span: {xs:2, sm:2, md:4, lg:8, xl:8, xxl:8}. span: {md:4, lg:8} // Equivalent to span: {xs:1, sm:1, md:4, lg:8, xl:8, xxl:8}. ``` - Since API version 20: When you configure **GridCol** column spans only at specific breakpoints, unconfigured breakpoints inherit values from the next smaller configured breakpoint. If no smaller breakpoint exists, values are inherited from the next larger configured breakpoint. <!--code_no_check--> ```ts span: {xs:2, md:4, lg:8} // Equivalent to span: {xs:2, sm:2, md:4, lg:8, xl:8, xxl:8}. span: {md:4, lg:8} // Equivalent to span: {xs:4, sm:4, md:4, lg:8, xl:8, xxl:8}. ``` - Recommendation: Explicitly configure **GridCol** column spans for all required breakpoints to prevent unexpected layout behavior caused by automatic value inheritance. |
| [GridColOptions](arkts-arkui-gridcoloptions-i.md) | Defines the options of the **GridCol** component. The values of `span`, `offset`, and `order` attributes are inherited in the sequence of **xs**, **sm**, **md**, **lg**, **xl**, and **xxl**. If no value is set for a breakpoint, the value is obtained from the previous breakpoint. Since API version 20, inheritance of the **span** property follows rules detailed in [GridColColumnOption](arkts-arkui-gridcolcolumnoption-i.md). |

