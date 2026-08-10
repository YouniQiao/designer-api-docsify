# GridItem

网格容器中单项内容容器。

> **说明：**
>
> *
>
> * 仅支持作为[Grid]{@link ./grid}组件的子组件使用。
>
> * 当GridItem配合[LazyForEach](docroot://ui/rendering-control/arkts-rendering-control-lazyforeach.md)使用时，GridItem子组件在
> GridItem创建时创建。配合[if/else](docroot://ui/rendering-control/arkts-rendering-control-ifelse.md)、
> [ForEach](docroot://ui/rendering-control/arkts-rendering-control-foreach.md)使用时，或父组件为Grid时，GridItem子组件在GridItem布局时创
> 建。
>
> * 当Grid中存在大量GridItem时，使用[columnStart]{@link GridItemAttribute#columnStart}/
> [columnEnd]{@link GridItemAttribute#columnEnd}、[rowStart]{@link GridItemAttribute#rowStart}/
> [rowEnd]{@link GridItemAttribute#rowEnd}设置GridItem大小会导致在使用scrollToIndex滑动到指定Index时，依次遍历GridItem节点，耗时较长。建议使用
> [GridLayoutOptions]{@link GridLayoutOptions}布局，以提高查找GridItem位置的效率。最佳实践请参考
> [优化Grid组件加载慢丢帧问题](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve_grid_performance)。

## 子组件

可以包含单个子组件。

## GridItem

```TypeScript
GridItem(value?: GridItemOptions)
```

创建网格容器中单项内容容器。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GridItemInterface-(value?: GridItemOptions): GridItemAttribute--><!--Device-GridItemInterface-(value?: GridItemOptions): GridItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [GridItemOptions](arkts-arkui-griditemoptions-i.md) | No | 为GridItem提供可选参数，该对象内包含[GridItemStyle]{@link GridItemStyle}枚举类型的style参数。不传入时使用默认样 式，即GridItemStyle.NONE。<br/> |

## Summary

- [GridItemOptions](arkts-arkui-griditem-griditemoptions-i.md)
- [GridItemStyle](arkts-arkui-griditem-griditemstyle-e.md)
