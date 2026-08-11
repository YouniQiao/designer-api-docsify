# ArrayListComparatorFn

```TypeScript
export type ArrayListComparatorFn<T> = (firstValue: T, secondValue: T) => double
```

This type specifies the comparator of sort in comparation.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type ArrayListComparatorFn<T> = (firstValue: T, secondValue: T) => double--><!--Device-unnamed-export type ArrayListComparatorFn<T> = (firstValue: T, secondValue: T) => double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| firstValue | T | Yes | firstValue (required) previous element. |
| secondValue | T | Yes | secondValue (required) next element. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | the number type |

