# ArrayPredicateFn

```TypeScript
type ArrayPredicateFn<ElementType, ArrayType> =
    (value: ElementType, index: number, array: ArrayType) => boolean
```

Defines the ArkTS Array reduction function, which is used by the 'some' and 'every'APIs of the Array class to determine whether array elements meet certain test conditions.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-collections-type ArrayPredicateFn<ElementType, ArrayType> =    (value: ElementType, index: number, array: ArrayType) => boolean--><!--Device-collections-type ArrayPredicateFn<ElementType, ArrayType> =    (value: ElementType, index: number, array: ArrayType) => boolean-End-->

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
