# OnVisibleIndexesChangeCallback

```TypeScript
declare type OnVisibleIndexesChangeCallback = (start: number, end: number) => void
```

懒加载布局容器[LazyColumnLayout](../arkts-apis/arkts-arkui-arkui-components-arklazycolumnlayout-con.md#lazycolumnlayout)、 LazyVGridLayout、 [LazyVWaterFlowLayout](../arkts-apis/arkts-arkui-arkui-components-arklazywaterflowlayout-con.md#lazyvwaterflowlayout)所显示的子组件索引发生变化时的回调 类型。

> **说明：**&gt;
> - 当懒加载布局容器没有子组件时，start和end都返回-1。&gt;
> - 当懒加载布局容器在可视区域内无子组件时，start和end都返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 是 |
| end | number | 是 |
