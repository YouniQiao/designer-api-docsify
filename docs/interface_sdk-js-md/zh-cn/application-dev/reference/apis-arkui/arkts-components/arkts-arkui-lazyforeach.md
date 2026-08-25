# LazyForEach

> **说明**> 开发者指南见：[LazyForEach开发者指南](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)。
LazyForEach是一种懒加载渲染控制组件，从提供的数据源中按需迭代数据并创建相应组件。在大量子组件的场景下，LazyForEach与缓存列表项、动态预加载、组件复用等方法配合使用，可以进一步提升滑动帧率并降低应用内存占用。

## LazyForEach

```TypeScript
LazyForEach(
    dataSource: IDataSource,
    itemGenerator: (item: any, index: number) => void,
    keyGenerator?: (item: any, index: number) => string
  )
```

LazyForEach从提供的数据源中按需迭代数据，并在每次迭代过程中创建相应的组件。当在滚动容器中使用了LazyForEach，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会进行组件销毁回收以降低内存占 用。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | [类型](#类型) | 必填 |
| --- | --- | --- |
| dataSource | [IDataSource](arkts-arkui-idatasource-i.md) | 是 |
| itemGenerator | (item: any, index: number) = & gt; void | 是 |
| keyGenerator | (item: any, index: number) = & gt; string | 否 |

## LazyForEach

```TypeScript
LazyForEach(
    dataSource: IDataSource,
    itemGenerator: (item: any, index: number) => void,
    keyGenerator?: (item: any, index: number) => string,
    options?: LazyForEachOptions
  )
```

LazyForEach从提供的数据源中按需迭代数据，并在每次迭代过程中创建相应的组件。当在滚动容器中使用了LazyForEach，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会进行组件销毁回收以降低内存占 用。

> **说明：**&gt;
> 从API版本26.0.0开始，LazyForEach支持传入[LazyForEachOptions](arkts-arkui-lazyforeachoptions-i.md)，用于使能自定义组件冻结和配置内存优化策略、资源释放策略。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | [类型](#类型) | 必填 |
| --- | --- | --- |
| dataSource | [IDataSource](arkts-arkui-idatasource-i.md) | 是 |
| itemGenerator | (item: any, index: number) = & gt; void | 是 |
| keyGenerator | (item: any, index: number) = & gt; string | 否 |
| options | [LazyForEachOptions](arkts-arkui-lazyforeachoptions-i.md) | 否 |

## 汇总

### 接口

| 名称 |
| --- |

### 类型

| 名称 |
| --- |

### 枚举

| 名称 |
| --- |
