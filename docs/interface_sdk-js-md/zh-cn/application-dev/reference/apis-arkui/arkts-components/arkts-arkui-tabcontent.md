# TabContent

仅在[Tabs](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-customelement-i.md#tabs)中使用，对应一个切换页签的内容视图。
> **说明：**
> - 该组件默认设置了clip属性的值为true，若需要扩展内容区到组件外显示，需先关闭clip属性。

## 子组件

支持单个子组件。

> **说明：**&gt;
> 可内置系统组件和自定义组件，支持渲染控制类型（[if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md)、
> [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md)和
> [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)）。

## TabContent

```TypeScript
TabContent()
```

创建TabContent页签和内容。

> **说明：**&gt;
> TabContent组件仅能作为Tabs组件的子组件使用，否则会导致组件无法正常显示。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 汇总

### 接口

| 名称 |
| --- |
| [IndicatorStyle](arkts-arkui-indicatorstyle-i.md) |
| [LabelStyle](arkts-arkui-labelstyle-i.md) |

### 类型

| 名称 |
| --- |
| [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md) |

### 枚举

| 名称 |
| --- |
