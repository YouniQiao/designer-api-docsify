# GridCol

栅格布局系统中的列组件，必须作为栅格容器组件([GridRow]{@link ./grid_row})的子组件使用。适用于响应式布局、多设备适配等需要动态调整列宽的场景。支持响应式断点配置、跨列布局、偏移和排序功能。使用GridCol
组件可以快速实现响应式布局，简化多设备适配的开发工作。

> **说明：**
>
> 该组件从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 子组件

可以包含单个子组件。

## GridCol

```TypeScript
GridCol(option?: GridColOptions)
```

栅格列布局组件。创建成功后，可根据配置的span、offset、order属性进行栅格布局，作为GridRow的子组件参与栅格系统的布局计算。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-GridColInterface-(option?: GridColOptions): GridColAttribute--><!--Device-GridColInterface-(option?: GridColOptions): GridColAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [GridColOptions](../arkts-apis/arkts-arkui-gridcol-gridcoloptions-i.md) | No |  |

## Summary

- [GridColColumnOption](arkts-arkui-gridcol-gridcolcolumnoption-i.md)
- [GridColOptions](arkts-arkui-gridcol-gridcoloptions-i.md)
