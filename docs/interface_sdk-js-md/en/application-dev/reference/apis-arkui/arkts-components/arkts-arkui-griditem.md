# GridItem

The **GridItem** component provides a single item in a grid.
> **NOTE**>> *>> * This component can be used only as a child of Grid.>> * When this component is used with> [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md), its child components are> created when it is created. When this component is used with> [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md) or> [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md), or when the parent component is> **Grid**, its child components are created when it is laid out.>> * If a **Grid** component contains a large number of **GridItem** components, using> [columnStart](arkts-arkui-griditem-attribute.md#columnstart)/[columnEnd](arkts-arkui-griditem-attribute.md#columnend) or> [rowStart](arkts-arkui-griditem-attribute.md#rowstart)/[rowEnd](arkts-arkui-griditem-attribute.md#rowend) to set the size of> **GridItem** components can lead to performance issues, especially when **scrollToIndex** is used to scroll to a> specific index. This is because **Grid** will traverse all **GridItem** nodes sequentially to find the specified> index, which can be time-consuming. To address this issue, it is recommended that you use> GridLayoutOptions for layout, which significantly improves the efficiency of finding the> position of **GridItem** components. For best practices, see> [Optimizing Frame Loss for Grid Component Loading](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-improve_grid_performance).

## Child Components

This component can contain a single child component.

## GridItem

```TypeScript
GridItem(value?: GridItemOptions)
```

Creates a **GridItem** component.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [GridItemOptions](arkts-arkui-griditemoptions-i.md) | No |

## Summary

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
