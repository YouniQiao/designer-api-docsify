# Tabs

通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。适用于应用底部导航栏、顶部页签切换、侧边栏导航等需要在不同内容视图间快速切换的场景。使用Tabs组件可以简化多视图导航的实现，提升用户切换效率。
> **说明：**
> - 该组件从API version 11开始，支持安全区域避让特性，其[expandSafeArea](arkts-arkui-commonmethod-c.md#expandsafearea)属性的默认值为expandSafeArea(> [SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])。开发者可通过重写该属性覆盖默认行为。对于API version 11之前的版本，则需配合expandSafeArea属性手动实现安全区域避> 让。

## 子组件

仅支持子组件TabContent，以及渲染控制类型 [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md)和 [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md)，不建议自定义组件作为子组件。并且if/else和ForEach下也仅支持 TabContent作为子组件，不建议自定义组件作为子组件。

> **说明：**&gt;
> Tabs子组件设置了通用属性visibility的值为None，或者设置值为Hidden时，对应子组件不显示，但依然会在视窗内占位。&gt;
> 已经显示的Tabs子组件TabContent后续隐藏时不会被销毁，若需要页面懒加载和释放，可以参考
> 示例13。&gt;
> Tabs设置height为auto时，可根据子组件高度自适应高度大小。设置
> width为auto时，可根据子组件宽度自适应宽度大小。

## Tabs

```TypeScript
Tabs(options?: TabsOptions)
```

创建Tabs容器。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | [类型](#类型) | 必填 |
| --- | --- | --- |
| options | [TabsOptions](arkts-arkui-tabsoptions-i.md) | 否 |

## 汇总

### 接口

| 名称 |
| --- |
| [DividerStyle](arkts-arkui-dividerstyle-i.md) |

### 类型

| 名称 |
| --- |

### 枚举

| 名称 |
| --- |
