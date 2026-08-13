# TypedArrayPredicateFn

```TypeScript
type TypedArrayPredicateFn<ElementType, ArrayType> =
    (value: ElementType, index: number, array: ArrayType) => boolean
```

Describes the assertion function of the ArkTS typed array.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-collections-type TypedArrayPredicateFn<ElementType, ArrayType> =    (value: ElementType, index: number, array: ArrayType) => boolean--><!--Device-collections-type TypedArrayPredicateFn<ElementType, ArrayType> =    (value: ElementType, index: number, array: ArrayType) => boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | ElementType | Yes |
| index | number | Yes |
| array | ArrayType | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |
