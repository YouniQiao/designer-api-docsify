# TypedArrayMapCallback

```TypeScript
type TypedArrayMapCallback<ElementType, ArrayType> =
    (value: ElementType, index: number, array: ArrayType) => ElementType
```

Describes the conversion mapping function of the ArkTS typed array.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-collections-type TypedArrayMapCallback<ElementType, ArrayType> =    (value: ElementType, index: number, array: ArrayType) => ElementType--><!--Device-collections-type TypedArrayMapCallback<ElementType, ArrayType> =    (value: ElementType, index: number, array: ArrayType) => ElementType-End-->

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
| ElementType |
