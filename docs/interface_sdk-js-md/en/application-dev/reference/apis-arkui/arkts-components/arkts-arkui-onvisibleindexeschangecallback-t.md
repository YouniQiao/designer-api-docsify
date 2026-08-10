# OnVisibleIndexesChangeCallback

```TypeScript
declare type OnVisibleIndexesChangeCallback = (start: int, end: int) => void
```

懒加载布局容器[LazyColumnLayout](../../../reference/apis-arkui/arkui-ts/ts-container-lazycolumnlayout.md)、  
[LazyVGridLayout](./lazy_grid_layout)、  
[LazyVWaterFlowLayout](../../../reference/apis-arkui/arkui-ts/ts-container-lazyvwaterflowlayout.md)所显示的子组件索引发生变化时的回调类型。

> **说明：**
> 
> - 当懒加载布局容器没有子组件时，start和end都返回-1。
> 
> - 当懒加载布局容器在可视区域内无子组件时，start和end都返回-1。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-declare type OnVisibleIndexesChangeCallback = (start: int, end: int) => void--><!--Device-unnamed-declare type OnVisibleIndexesChangeCallback = (start: int, end: int) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | 可视区域起始位置的索引值。<br/>取值范围：[0, 子节点总数-1]，当没有子节点或所有子节点都在可视区域外时，返回-1。 |
| end | int | Yes | 可视区域终止位置的索引值。<br/>取值范围：[0, 子节点总数-1]，当没有子节点或所有子节点都在可视区域外时，返回-1。 |

