# TypedArrayForEachCallback

```TypeScript
type TypedArrayForEachCallback<ElementType, ArrayType> =
    (value: ElementType, index: number, array: ArrayType) => void
```

ArkTS TypedArray遍历函数类型。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-collections-type TypedArrayForEachCallback<ElementType, ArrayType> =    (value: ElementType, index: number, array: ArrayType) => void--><!--Device-collections-type TypedArrayForEachCallback<ElementType, ArrayType> =    (value: ElementType, index: number, array: ArrayType) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ElementType | Yes | 当前遍历的ArkTS TypedArray元素。 |
| index | number | Yes | 当前遍历的ArkTS TypedArray元素索引，从0开始。 |
| array | ArrayType | Yes | 当前遍历的ArkTS TypedArray实例。 |

