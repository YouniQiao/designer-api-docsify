# OnVisibleIndexesChangeCallback

```TypeScript
declare type OnVisibleIndexesChangeCallback = (start: number, end: number) => void
```

懒加载布局容器[LazyColumnLayout](../../../reference/apis-arkui/arkui-ts/ts-container-lazycolumnlayout.md)、  
[LazyVGridLayout](./lazy_grid_layout)、  
[LazyVWaterFlowLayout](../../../reference/apis-arkui/arkui-ts/ts-container-lazyvwaterflowlayout.md)所显示的子组件索引发生变化时的回调类型。

> **说明：**
> 
> - 当懒加载布局容器没有子组件时，start和end都返回-1。
> 
> - 当懒加载布局容器在可视区域内无子组件时，start和end都返回-1。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type OnVisibleIndexesChangeCallback = (start: int, end: int) => void--><!--Device-unnamed-declare type OnVisibleIndexesChangeCallback = (start: int, end: int) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 是 |
| end | number | 是 |
