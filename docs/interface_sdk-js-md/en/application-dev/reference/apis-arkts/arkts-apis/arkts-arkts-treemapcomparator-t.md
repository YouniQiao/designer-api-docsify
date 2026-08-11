# TreeMapComparator

```TypeScript
export type TreeMapComparator<K> = (firstValue: K, secondValue: K) => double
```

The type of TreeMap comparator.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type TreeMapComparator<K> = (firstValue: K, secondValue: K) => double--><!--Device-unnamed-export type TreeMapComparator<K> = (firstValue: K, secondValue: K) => double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| firstValue | K | Yes | The first value compared |
| secondValue | K | Yes | The second value compared |

**Return value:**

| Type | Description |
| --- | --- |
| double | Comparison results |

