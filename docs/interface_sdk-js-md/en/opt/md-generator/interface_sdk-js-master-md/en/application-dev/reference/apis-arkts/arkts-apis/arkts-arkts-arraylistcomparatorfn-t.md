# ArrayListComparatorFn

```TypeScript
export type ArrayListComparatorFn<T> = (firstValue: T, secondValue: T) => number
```

This type specifies the comparator of sort in comparation.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type ArrayListComparatorFn<T> = (firstValue: T, secondValue: T) => double--><!--Device-unnamed-export type ArrayListComparatorFn<T> = (firstValue: T, secondValue: T) => double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| firstValue | T | Yes |
| secondValue | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |
