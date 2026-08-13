# ArrayReduceCallback

```TypeScript
type ArrayReduceCallback<AccType, ElementType, ArrayType> =
    (previousValue: AccType, currentValue: ElementType, currentIndex: number, array: ArrayType) => AccType
```

Defines the ArkTS Array reduction function, which is used by the 'reduceRight' API of the Array class.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-collections-type ArrayReduceCallback<AccType, ElementType, ArrayType> =    (previousValue: AccType, currentValue: ElementType, currentIndex: number, array: ArrayType) => AccType--><!--Device-collections-type ArrayReduceCallback<AccType, ElementType, ArrayType> =    (previousValue: AccType, currentValue: ElementType, currentIndex: number, array: ArrayType) => AccType-End-->

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
