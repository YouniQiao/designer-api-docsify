# Column

沿垂直方向布局的容器。适用于需要将多个子组件按垂直方向依次排列的场景，如列表项、表单项、卡片内容等。支持设置子组件间距、对齐方式等属性，能够快速实现垂直方向的线性布局。

> **说明：**
>
> 该组件从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
>
> Column未设置高度或宽度时，在主轴（垂直方向）或交叉轴（水平方向）方向上自适应子组件大小。

## 子组件

可以包含子组件。

## Column

```TypeScript
Column(options?: ColumnOptions)
```

创建垂直方向线性布局容器，可以设置子组件的间距。

> **说明：**
> 
> 在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考布局优化指导。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ColumnInterface-(options?: ColumnOptions): ColumnAttribute--><!--Device-ColumnInterface-(options?: ColumnOptions): ColumnAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ColumnOptions](arkts-arkui-columnoptions-i.md) | No | Column组件的间距配置选项。通过space属性设置纵向布局元素垂直方向间距。当需要为子组件设置固定垂直间距时传入此参数；省略时不设置子组件间距。 <br> |

## Column

```TypeScript
Column(options?: ColumnOptions | ColumnOptionsV2)
```

创建垂直方向线性布局容器，可以设置子组件的间距。

> **说明：**
> 
> 在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考布局优化指导。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-ColumnInterface-(options?: ColumnOptions | ColumnOptionsV2): ColumnAttribute--><!--Device-ColumnInterface-(options?: ColumnOptions | ColumnOptionsV2): ColumnAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ColumnOptions](arkts-arkui-columnoptions-i.md) \| ColumnOptionsV2 | No | Column组件的间距配置选项。通过space属性设置纵向布局元素垂直方向间距，space支持设置number、 string或Resource类型。当需要为子组件设置固定垂直间距时传入此参数；省略时不设置子组件间距。 |

## Summary

- [ColumnOptions](arkts-arkui-column-columnoptions-i.md)
- [ColumnOptionsV2](arkts-arkui-column-columnoptionsv2-i.md)
- [SpaceType](arkts-arkui-column-spacetype-t.md)
