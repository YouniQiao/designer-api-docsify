# TreeMapComparator

```TypeScript
export type TreeMapComparator<K> = (firstValue: K, secondValue: K) => double
```

TreeMap的比较器类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type TreeMapComparator<K> = (firstValue: K, secondValue: K) => double--><!--Device-unnamed-export type TreeMapComparator<K> = (firstValue: K, secondValue: K) => double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| firstValue | K | Yes | 第一个比较值。 |
| secondValue | K | Yes | 第二个比较值。 |

**Return value:**

| Type | Description |
| --- | --- |
| double | 比较结果。 |

