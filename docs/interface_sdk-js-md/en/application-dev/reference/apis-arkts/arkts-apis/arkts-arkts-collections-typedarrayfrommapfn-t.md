# TypedArrayFromMapFn

```TypeScript
type TypedArrayFromMapFn<FromElementType, ToElementType> = (value: FromElementType, index: number) => ToElementType
```

ArkTS TypedArray映射函数类型。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-collections-type TypedArrayFromMapFn<FromElementType, ToElementType> = (value: FromElementType, index: number) => ToElementType--><!--Device-collections-type TypedArrayFromMapFn<FromElementType, ToElementType> = (value: FromElementType, index: number) => ToElementType-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | FromElementType | Yes | 当前遍历的用于构造ArkTS TypedArray的元素。 |
| index | number | Yes | 当前遍历的用于构造ArkTS TypedArray的元素索引，从0开始。 |

**Return value:**

| Type | Description |
| --- | --- |
| ToElementType | 转换后的元素值。 |

