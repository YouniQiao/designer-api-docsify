# VirtualScrollOptions

配置懒加载模式下期望加载的数据项总数、复用能力、数据精准懒加载能力。

## 默认懒加载说明

当Repeat属性`.virtualScroll()`缺省时：&lt;br&gt;1）ArkTS-Dyn中，默认渲染方式为全量加载，若要开启懒加载，需要设置`.virtualScroll()`属性。&lt;br&gt;2）ArkTS-Sta中，默认渲染方式为懒加载。若要关闭懒加载，需要设置`.virtualScroll({ disableVirtualScroll: true })`。

> **说明：**
> 
> 关闭懒加载后，Repeat仅有`.each()`和`.key()`属性生效，其他懒加载特有的功能（如template、totalCount、onLazyLoading等）不生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface VirtualScrollOptions--><!--Device-unnamed-export interface VirtualScrollOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onLazyLoading

```TypeScript
onLazyLoading?: OnLazyLoadingFunc
```

Data lazy loading。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VirtualScrollOptions-onLazyLoading?: OnLazyLoadingFunc--><!--Device-VirtualScrollOptions-onLazyLoading?: OnLazyLoadingFunc-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTotalCount

```TypeScript
onTotalCount?: OnTotalCountFunc
```

计算期望加载的数据项总数。需要开发者给定计算方法，其返回值可以不等于数据源长度（实际传入Repeat的数组的长度）。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VirtualScrollOptions-onTotalCount?: OnTotalCountFunc--><!--Device-VirtualScrollOptions-onTotalCount?: OnTotalCountFunc-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disableVirtualScroll

```TypeScript
disableVirtualScroll?: boolean
```

是否关闭懒加载模式。true：关闭懒加载模式，列表节点全部加载。false：使用懒加载模式。默认值：false该接口仅适用于ArkTS-Sta。

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VirtualScrollOptions-disableVirtualScroll?: boolean--><!--Device-VirtualScrollOptions-disableVirtualScroll?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## memoryOptimizationStrategy

```TypeScript
memoryOptimizationStrategy?: RepeatMemOptStrategy
```

Repeat的内存优化策略。

**Type:** [RepeatMemOptStrategy](arkts-arkui-repeat-repeatmemoptstrategy-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VirtualScrollOptions-memoryOptimizationStrategy?: RepeatMemOptStrategy--><!--Device-VirtualScrollOptions-memoryOptimizationStrategy?: RepeatMemOptStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reusable

```TypeScript
reusable?: boolean
```

是否开启复用功能。true：开启复用。false：关闭复用。默认值：true。

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VirtualScrollOptions-reusable?: boolean--><!--Device-VirtualScrollOptions-reusable?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## totalCount

```TypeScript
totalCount?: int
```

期望加载的数据项总数，可以不等于数据源长度（实际传入Repeat的数组的长度）。取值范围：自然数。totalCount缺省或超出取值范围时，totalCount取值为数据源长度，列表正常滚动。totalCount = 0时，不加载数据。0 < totalCount &lt;= 数据源长度时，界面中只渲染区间[0, totalCount - 1]范围内的数据。totalCount &gt; 数据源长度时，Repeat将渲染区间[0, totalCount - 1]范围内的数据，容器组件滚动条样式根据totalCount值变化。在容器组件滚动过程中，应用需要保证在列表即将滑动到数据源末尾时请求后续数据。开发者需要对数据请求的错误场景（如网络延迟）进行保护操作，直到数据源全部加载完成，否则列表滑动过程中会出现滚动效果异常。建议配合使用[onLazyLoading](arkts-arkui-onlazyloadingfunc-t.md)实现数据懒加载。除totalCount属性外，开发者也可以通过[onTotalCount](arkts-arkui-ontotalcountfunc-t.md)方法设置自定义方法，计算期望加载的数据项总数。取值限定为整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VirtualScrollOptions-totalCount?: int--><!--Device-VirtualScrollOptions-totalCount?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

