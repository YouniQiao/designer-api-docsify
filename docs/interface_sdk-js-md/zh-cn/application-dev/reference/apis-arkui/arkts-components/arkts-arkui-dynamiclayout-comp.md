# DynamicLayout

动态布局容器组件，支持在运行时动态切换不同的布局算法，不改变子组件的状态。

> **说明：**

## 子组件

可以包含子组件。

## DynamicLayout

```TypeScript
DynamicLayout(algorithm: LayoutAlgorithm)
```

动态布局容器。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务中使用。

**卡片能力：** 从API版本24开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algorithm | [LayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-i.md) | 是 | 指定动态布局容器的布局算法。支持使用[RowLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-rowlayoutalgorithm-c.md)（水平线性布局，适用于水平排列场景）、[ColumnLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-columnlayoutalgorithm-c.md)（垂直线性布局，适用于垂直排列场景）、[StackLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-stacklayoutalgorithm-c.md)（堆叠布局，适用于层叠覆盖场景）、[GridLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-gridlayoutalgorithm-c.md)（网格布局，适用于规整网格场景）和[CustomLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-customlayoutalgorithm-c.md)（自定义布局，适用于复杂特殊布局场景）等布局算法实例，详见[LayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-i.md)。取非法值（如null、undefined或无效的布局算法对象）时，按照[StackLayoutAlgorithm](../arkts-apis/arkts-arkui-layoutalgorithm-stacklayoutalgorithm-c.md)布局子组件，子组件堆叠排列。 |

## 汇总

## 示例

```TypeScript
### 示例1（自定义布局算法实现瀑布流布局）

该示例展示如何重写onMeasure、onLayout函数，实现瀑布流布局展示商品列表的功能。瀑布流布局通过测量阶段计算子组件高度并记录每列累计高度，在布局阶段将子组件分配到当前高度最小的列，实现自动填充效果。

从API version 24开始，新增onMeasure、onLayout。


```

```TypeScript
### 示例2（切换布局算法）

该示例通过改变[@Local](../../../ui/state-management/arkts-new-local.md)装饰的LayoutAlgorithm类型变量，实现动态切换DynamicLayout组件布局算法的功能。示例展示如何切换布局算法为RowLayoutAlgorithm（水平线性布局）、ColumnLayoutAlgorithm（垂直线性布局）、StackLayoutAlgorithm（堆叠布局）和GridLayoutAlgorithm（网格布局）。

> 说明：
> 
> 示例中预置的layoutGravity属性仅在Stack布局算法下生效，在Row/Column布局算法下该属性不生效。

从API version 24开始，新增RowLayoutAlgorithm、ColumnLayoutAlgorithm、StackLayoutAlgorithm、GridLayoutAlgorithm。


```

```TypeScript
### 示例3（修改布局算法属性）

该示例通过修改RowLayoutAlgorithm的space和justifyContent属性，实现DynamicLayout组件布局效果刷新的功能。

从API version 24开始，新增space、justifyContent属性。
```
