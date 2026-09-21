# LazyVWaterFlowLayout

定义LazyVWaterFlowLayout组件。

## LazyVWaterFlowLayout

```TypeScript
LazyVWaterFlowLayout()
```

构造懒加载垂直瀑布流属性。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 汇总

## 示例

```TypeScript
### 示例1（实现懒加载瀑布流布局）

通过[Scroll](ts-container-scroll.md)和LazyVWaterFlowLayout组件实现懒加载瀑布流布局。

MyDataSource实现了LazyForEach数据源接口[IDataSource](ts-rendering-control-lazyforeach.md#idatasource)，用于通过LazyForEach给LazyVWaterFlowLayout提供子组件。

从API版本26.0.0开始，新增支持LazyVWaterFlowLayout组件。
```

```TypeScript

```

```TypeScript
### 示例2（设置头部组件或尾部组件及吸附效果）

该示例通过[Scroll](ts-container-scroll.md)嵌套LazyVWaterFlowLayout，并通过[header](#header)、[footer](#footer)、[sticky](#sticky)实现瀑布流顶部和底部吸附效果。滚动过程中header吸附在可视区域顶部，footer吸附在可视区域底部。

从API版本26.0.0开始，新增支持header、footer和sticky属性。


```

```TypeScript
### 示例3（设置自适应列数）

该示例通过[columnsTemplate](#columnstemplate)设置repeat(auto-fill, track-size)和ItemFillPolicy，实现LazyVWaterFlowLayout列数自适应。

从API版本26.0.0开始，新增[columnsTemplate](#columnstemplate)接口。
```
