# GridRow

栅格布局可以为布局提供规律性的结构，解决多尺寸多设备的动态布局问题，保证不同设备上各个模块的布局一致性。

栅格容器组件，仅可以和栅格子组件([GridCol]{@link ./grid_col})在栅格布局场景中使用。

支持根据设备尺寸和断点动态调整列数与间距，实现响应式布局。

> **说明：**
>
> 该组件从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 子组件

可以包含GridCol子组件。

## GridRow

```TypeScript
GridRow(option?: GridRowOptions)
```

栅格行布局容器。仅可以和栅格子组件在栅格布局场景中使用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-GridRowInterface-(option?: GridRowOptions): GridRowAttribute--><!--Device-GridRowInterface-(option?: GridRowOptions): GridRowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [GridRowOptions](../arkts-apis/arkts-arkui-gridrow-gridrowoptions-i.md) | No |  |

## Summary

- [BreakPoints](arkts-arkui-gridrow-breakpoints-i.md)
- [GridRowColumnOption](arkts-arkui-gridrow-gridrowcolumnoption-i.md)
- [GridRowOptions](arkts-arkui-gridrow-gridrowoptions-i.md)
- [GridRowSizeOption](arkts-arkui-gridrow-gridrowsizeoption-i.md)
- [GutterOption](arkts-arkui-gridrow-gutteroption-i.md)
- [BreakpointsReference](arkts-arkui-gridrow-breakpointsreference-e.md)
- [GridRowDirection](arkts-arkui-gridrow-gridrowdirection-e.md)
