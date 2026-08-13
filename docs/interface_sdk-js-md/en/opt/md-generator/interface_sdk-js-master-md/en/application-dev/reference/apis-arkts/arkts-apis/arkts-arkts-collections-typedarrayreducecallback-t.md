# TypedArrayReduceCallback

```TypeScript
type TypedArrayReduceCallback<AccType, ElementType, ArrayType> =
    (previousValue: AccType, currentValue: ElementType, currentIndex: number, array: ArrayType) => AccType
```

Describes the reduce function of the ArkTS typed array.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-collections-type TypedArrayReduceCallback<AccType, ElementType, ArrayType> =    (previousValue: AccType, currentValue: ElementType, currentIndex: number, array: ArrayType) => AccType--><!--Device-collections-type TypedArrayReduceCallback<AccType, ElementType, ArrayType> =    (previousValue: AccType, currentValue: ElementType, currentIndex: number, array: ArrayType) => AccType-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| previousValue | AccType | Yes |
| [currentValue](../../apis-notification-kit/arkts-apis/arkts-notification-notificationcontent-notificationprogress-i.md) | ElementType | Yes |
| currentIndex | number | Yes |
| array | ArrayType | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| AccType |
