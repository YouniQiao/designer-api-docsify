# TypedArrayForEachCallback

```TypeScript
type TypedArrayForEachCallback<ElementType, ArrayType> =
    (value: ElementType, index: number, array: ArrayType) => void
```

Describes the traversal function of the ArkTS typed array.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-collections-type TypedArrayForEachCallback<ElementType, ArrayType> =    (value: ElementType, index: number, array: ArrayType) => void--><!--Device-collections-type TypedArrayForEachCallback<ElementType, ArrayType> =    (value: ElementType, index: number, array: ArrayType) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | ElementType | Yes |
| index | number | Yes |
| array | ArrayType | Yes |
