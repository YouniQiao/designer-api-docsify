# TreeSetComparator

```TypeScript
export type TreeSetComparator<T> = (firstValue: T, secondValue: T) => double
```

The type of TreeSet comparator.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type TreeSetComparator<T> = (firstValue: T, secondValue: T) => double--><!--Device-unnamed-export type TreeSetComparator<T> = (firstValue: T, secondValue: T) => double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| firstValue | T | Yes | The first value compared |
| secondValue | T | Yes | The second value compared |

**Return value:**

| Type | Description |
| --- | --- |
| double | Comparison results |

